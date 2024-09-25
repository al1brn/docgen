"""
Created on Tue Sep 10 07:44:18 2024

@author: alain


$ DOC START

$ DOC NOT transparent


Python object info

Documentation is based on structure information on objects to document

created : 2024 09 14

"""

import inspect
from pathlib import Path

import re
import sys
import os

folder = str(Path(os.getcwd()).parents[0])
if not folder in sys.path:
    sys.path.append(folder)
assert(folder in sys.path)

from docgen.parser import del_margin, extract_lists
from docgen.documentation import Section, Documentation, under_to_md

# =============================================================================================================================
# Lists in comment

# -----------------------------------------------------------------------------------------------------------------------------
# List item in CommentList

EMPTY  ='_EMPTY'
            
class ListItem:
    
    def __init__(self, name, type=None, default=EMPTY, description=None, **kwargs):
        """ An information line into a list
        
        This class is used to information displayed in a single lines.
        
        The line is intended to be displayed as `name (type = default) : description`.
        
        Properties
        ----------
        - name (str) : name attribute
        - type (str)  : type attribute
        - default (str) : default attribute
        - description (str) : description
        """
        self.name        = name
        self.type        = type
        self.default     = default
        self.description = description
        
        for k, v in kwargs.items():
            setattr(self, k, v)
            
            
    def __str__(self):
        s = f"- {self.name}"
        if self.has_type or self.has_default:
            s += " ("
            if self.has_type:
                s += self.type
            if self.has_default:
                s += f" = {self.default}"
            s += ")"
        
        if self.description is not None:
            s += f" : {self.description}"
            
        return s
    
    @classmethod
    def FromOther(cls, other):
        """ Create from another ListItem or from a dict
        
        Arguments
        ---------
        - other (ListItem or dict) : the source
        
        Returns
        -------
        - ListItem
        """
        
        if isinstance(other, dict):
            item = cls(name=other['name'])
            for k, v in other.items():                
                setattr(item, k, v)
                
        else:
            item = cls(name=other.name)
            for k in dir(other):
                if k not in dir(ListItem):
                    setattr(item, k, getattr(other, k))
                
        return item
    
    @classmethod
    def FromParameter(cls, param, description=None):
        """ Create an instance from the python paramer description.
        
        Returns
        -------
        - ListItem
        """
        name    = param.name
        type    = None  if param.annotation == param.empty else param.annotation
        default = EMPTY if param.default == param.empty else param.default
        
        return cls(name, type=type, default=default, description=None)
    
    def get_prop(self, attribute, default=None):
        """ Get a custom attribute value
        
        Arguments
        ---------
        - attribute (str) : attribute name
        - default : value to return if the attribute doesn't exist
        
        Returns
        -------
        - Any : attribute value or default if it doesn't exist
        """
        if attribute in dir(self):
            return getattr(self, attribute)
        else:
            return default
            
    @property
    def has_type(self):
        """ Check if <#type> is not None
        
        Returns
        -------
        - bool
        """
        return self.type is not None
    
    @property
    def has_default(self):
        """ Check if <#default> is different from <#EMPTY>
        
        Returns
        -------
        - bool
        """
        return self.default != EMPTY
    
    @property
    def has_description(self):
        """ Check if <#description> is not None
        
        Returns
        -------
        - bool
        """
        return self.description is not None
    
    def complete_with(self, other:'ListItem'):
        """ Complete with another list item.
        
        Replace empty attributes by values coming from the other ListItem.
        """
        
        if isinstance(other, dict):
            other = ListItem(**other)
        
        if not self.has_type:
            self.type = other.type
        if not self.has_default:
            self.default = other.default
        if not self.has_description:
            self.decrption = other.description
            
        for k in dir(other):
            if not k in dir(self):
                setattr(self, getattr(other, k))
                
    @property
    def markdown(self):
        s = f"- **{self.name}**"
        if self.has_type or self.has_default:
            s += " ("
            if self.has_type:
                s += f"_{self.type}_"
            if self.has_default:
                s += f" = {self.default}"
            s += ")"
            
        if self.has_description:
            s += f" : {self.description}"
            
        return s + "\n"
        
        
# -----------------------------------------------------------------------------------------------------------------------------
# Comment list

class DescriptionList(list):
    """ Description list made
    
    A description list is a list of Listtem
    
    A description is coming from the following syntax in a comment:
    
    ```
    title
    -----
    - name (type = default) : description
    - name (type = default) : description
    ```
    
    Only `name` is mandatory.
    
    > [!NOTE]
    > A description list for the arguments is built from the signature of a function
    > and can be enriched by a 'Arguments' list in a comment. See <#complete_with>.
    """
    
    @classmethod
    def FromList(cls, list_):
        dl = cls()
        if list_ is None:
            return dl
        
        for item in list_:
            dl.append(ListItem.FromOther(item))
            
        return dl
        
    
    def get(self, name):
        """ Get a list item by its name
        
        Argument
        --------
        - name (str) : item name
        
        Returns
        -------
        - ListItem : None if not found
        """
        for item in self:
            if item.name == name:
                return item
        return None
        
    
    def complete_with(self, other_list):
        """ Complete a list with another list
        
        If a list item doesn't exist, it is created
        If it already exists, empty fields (<!ListItem#type>, <!ListItem#default >and <!ListItem#description>)
        are set with values coming from other.
        
        This feature is used to build arguments list. 
            
        ``` python
        def foo(arg1, arg2:int, arg3='value', arg4:float=3.14):
        ```
        
        Will generate the following argument list:

        ````
        Arguments
        ---------
        - arg1
        - arg2 (int)
        - arg3 (='value')
        - arg4 (float = 3.14)
        ```
        
        This list can be enriched with the following list written in the function comment:
        
        
        ````
        Arguments
        ---------
        - arg1 (int) : first argument
        - arg3 (str) : third argument        
        ```
        
        Which will produce the final enriched list:

        ````
        Arguments
        ---------
        - arg1(int) : first argument
        - arg2 (int)
        - arg3 (str='value') : third argument 
        - arg4 (float = 3.14)
        ```
        
        Arguments
        ---------
        - other_list : DescriptionList
        """
        
        if other_list is None:
            return
        
        for other_item in other_list:
            
            if isinstance(other_item, dict):
                name = other_item['name']
            else:
                name = other_item.name
                
            item = self.get(name)
            
            if item is None:
                self.append(ListItem.FromOther(other_item))
                
            else:
                item.complete_with(other_item)

    # ====================================================================================================
    # Markdwon
    
    def markdown(self, title):
        return f"\n\n#### {title}:\n" + "".join([item.markdown for item in self]) + '\n'                
    
# =============================================================================================================================
# Base information

class ObjectSection(Section):
    
    SEP = '.'
    DOT = None
    
    def __init__(self, name, comment=None, tag=None, **parameters):
        """ Root class for informations on python objects
        
        The minimum information is <#name> and <#comment> can be completed
        by sub classes.
        
        Properties
        ----------
        - name (str) : module name, class name, property name...
        
        Arguments
        ---------
        - name (str) : object name
        - comment (str = None) : comment
        - tag (str = None) : section tag
        - parameters : parameter initial values
        """
        
        super().__init__(name, comment=comment, tag=tag, in_toc=True, toc_sort=True, toc_flat=True, **parameters)
        self.name = name
        
        # ----- Let's extract lists from comment

        self.user_lists = {}
        
        self.comment, lists = extract_lists(self.comment, 'arguments', 'raises', 'returns', 'properties')
        for list_name, list_ in lists.items():
            self.user_lists[list_name] = list_

    def __str__(self):
        return f"<{type(self).__name__} {self.name}>"
    
    @staticmethod
    def get_doc(py_object):
        """ Utitliy static method
        """
        
        doc = getattr(py_object, '__doc__', None)
        
        if doc is None:
            return None
        
        doc = doc.strip()
        if doc == "":
            return None
        else:
            return doc

    @staticmethod
    def get_function_class(func):
        
        names = func.__qualname__.split('.')
        if len(names) == 1:
            return None
        
        return '.'.join(names[:-1])

    @staticmethod
    def get_property_class(prop):
        
        names = prop.__qualname__.split('.')
        if len(names) == 1:
            return None
        
        return '.'.join(names[:-1])

    def regroup(self):
        return
        
# =============================================================================================================================
# Property Info
            
class PropertySection(ObjectSection):
    
    def __init__(self, name, comment=None, tag=None, **parameters):
        """ Information on property
        
        A property can be defined:
        - in a user list such as name (type = default) : description
        - from a fget method
        
        In case both exist, user list description is ignored if the
        fget provides a comment.
        
        Properties
        ----------
        - type (str) : type of the property
        - default (str) : default value
        - fget (Function_) : getter <!Function_>
        - fset (Function_) : setter <!Function_>
        
        Arguments
        ---------
        - name (str) : object name
        - comment (str = None) : comment
        - tag (str = None) : section tag
        - parameters : parameter initial values
        """

        self.type        = None
        self.default     = EMPTY
        self.fget        = None
        self.fset        = None
        
        super().__init__(name, comment=comment, tag=tag, **parameters)
        self.set_tag('Properties')
        
        if self.fget is not None:
            if self.type is None:
                self.type = self.fget.return_type
            if self.comment is None:
                self.comment = self.fget.comment
            
    def before_comment(self):
        
        stype = '?' if self.type is None else self.type
        
        use_table = False
        
        if use_table:
            yield "\n<table><tbody>\n"
            yield f"<tr><td>type</td><td><b>{stype}</b></td></tr>\n"
            if self.default != EMPTY:
                yield f"<tr><td>default</td><td><b>{self.default}</b</td></tr>\n"
            yield "</tbody></table>\n\n"
            
        else:
            yield f"> _type_: **{stype}**"
            if self.default != EMPTY:
                yield f"<br> _default_: **{self.default}**"
            yield "\n>\n"
        
    @classmethod
    def FromDict(cls, item):
        """ Create a property from a dict
        
        Arguments
        ---------
        - item (dict) : information on the property to create

        Returns
        -------
        - PropertySection
        """
        return cls(item['name'], comment=item.get('description'), type=item.get('type'), default=item.get('default', EMPTY))

    @classmethod
    def FromListItem(cls, item):
        """ Create a property from a list item
        
        Arguments
        ---------
        - item (ListItem) : information on the property to create

        Returns
        -------
        - PropertySection
        """
        return cls(item.name, comment=item.description, type=item.type, default=item.default)
        
        
    @classmethod
    def FromInspect(cls, name, property_object):
        """ Create a PropertySection by inspect a property
        
        > [!NOTE]
        > If name is None, the name is read from fget
        
        Arguments
        ---------
        - name (str) : name
        - property_object (property) : the object the scan
        
        Returns
        -------
        - PropertySection
        """
        fget = FunctionSection.FromInspect('fget', property_object.fget)
        fset = FunctionSection.FromInspect('fset', property_object.fset)
        
        return cls(name, cls.get_doc(property_object), fget=fget, fset=fset)
    
    @classmethod
    def FromStatic(cls, name, property_object):
        """ Creare a Property_ instance from a static property in a module or a class
        
        Arguments
        ---------
        - name (str = None)
        - property_object
        
        Returns
        -------
        - Property_
        """
        stype = type(property_object).__name__
        try:
            sdef = str(property_object)
        except:
            sdef = '???'
            
        if len(sdef) > 30:
            sdef = sdef[:30] + '...'
            
        return cls(name, type=stype, default=sdef)
    
    def complete_with(self, other, override=False):
        """ Enrich the description with another one
        
        A Property_ can be created either in properties list in a comment
        or by scaning object.
        This function allows to merge information coming from these two sources
        
        Arguments
        ---------
        - other (Property) : contains complementary description
        """
        
        if override:
            if other.comment is not None:
                self.comment = other.comment
            if other.type is not None:
                self.type = other.type
            if other.default != EMPTY:
                self.default = other.default
            if other.fget is not None:
                self.fget = other.fget
            if other.fset is not None:
                self.fset = other.fset
            
        else:
            if self.comment is None:
                self.comment = other.comment
            if self.type is None:
                self.type = other.type
            if self.default == EMPTY:
                self.default = other.default
            if self.fget is None:
                self.fget = other.fget
            if self.fset is None:
                self.fset = other.fset
         
# =============================================================================================================================
# Function info
        
class FunctionSection(ObjectSection):
    
    def __init__(self, name, comment=None, tag=None, **parameters):
        """ Function section

        Properties
        ----------
        - ftype (str) : function type (function, static, class, ...)
        - signature (str) : function signature
        - raises (DescriptionList = None) : list of raised exceptions
        - arguments (DescriptionList = []) : argument descriptions
        
        Arguments
        ---------
        - name (str) : object name
        - comment (str = None) : comment
        - tag (str = None) : section tag
        - parameters : parameter initial values
        """

        self.ftype = 'function'        
        self.signature = "()"
        super().__init__(name, comment=comment, tag=tag, top_bar='-', navigation=True, display_title=name + "()", **parameters)
        self.set_tag("Functions", "Methods")
        
        # ----- List extracted from comment
        
        self.raises    = DescriptionList.FromList(self.user_lists.get('raises'))
        self.arguments = DescriptionList.FromList(self.user_lists.get('arguments'))
        self.returns   = DescriptionList.FromList(self.user_lists.get('returns'))

            
    def __str__(self):
        return f"<Function {self.name}() returns: {[str(item) for item in self.returns]}>"
    
    @staticmethod
    def inspect_type(func):
        
        if '.' not in func.__qualname__ or not hasattr(func, '__module__'):
            return 'function'
            
        else:
            # __qualname__: 'className.functioNname'
            cls_name = func.__qualname__.rsplit('.', 1)[0]
            
            # Get the class by name
            cls = getattr(sys.modules[func.__module__], cls_name)
            
            # cls.__dict__[func.__name__] should return like <class 'staticmethod'>
            ftype = cls.__dict__[func.__name__].__class__.__name__
            
            if ftype == 'function':
                return 'method'
            else:
                return ftype
        
        
    @classmethod
    def FromInspect(cls, name, function_object):
        """ Create a FunctionSection by inspecting a function object
        
        Arguments
        ---------
        - name (str = None) : name of the function
        - object (function) : the object to inspec
        """        
        
        if function_object is None:
            return None
        
        try:
            sig = inspect.signature(function_object)    
        except:
            sig = "()"
            
        # ----- Create the function
        
        ftype = cls.inspect_type(function_object)
        
        function_ = cls(name, cls.get_doc(function_object), ftype=ftype, signature=str(sig))
        
        # ----- Arguments list if we have a signature
        
        if not isinstance(sig, str):
            
            old = function_.arguments
            function_.arguments = DescriptionList()

            for i_param, param in enumerate(sig.parameters.values()):
                if i_param == 0 and param.name in ['self', 'cls']:
                    continue
                
                old_arg = old.get(param.name)
                arg = ListItem.FromParameter(param)
                if old_arg is not None:
                    if arg.type is None:
                        arg.type = old_arg.type
                    if arg.default == EMPTY:
                        arg.default = old_arg.default
                    arg.description = old_arg.description
                    
                function_.arguments.append(arg)
                
        return function_
    
    # =============================================================================================================================
    # What the function returns
    
    @property
    def return_type(self):
        if self.returns is None or len(self.returns) == 0:
            return None
        
        return self.returns[0].name
    
    @property
    def return_type_descr(self):
        if self.returns is None or len(self.returns) == 0:
            return None
        
        ret = self.returns[0]
        
        s = str(ret)[len('- ' + ret.name):].strip()
        
        if s == ':':
            return None
        else:
            return s.replace(':', ',')
                    
    # =============================================================================================================================
    # Document
    
    def before_comment(self):

        yield f"> {self.ftype}\n\n"
        
        if self.signature is None:
            return

        sig = self.signature[1:].strip()
        for sc in ('self', 'cls'):
            if sig.startswith(sc):
                sig  = sig[len(sc):].strip()
                if sig.startswith(','):
                    sig  = sig[1:].strip()
                break
        sig = '(' + sig
        
        yield "``` python\n"
        yield f"{self.name}{sig}\n"
        yield "```\n\n"
        
        
    def after_comment(self):
        
        if len(self.raises):
            yield self.raises.markdown('Raises')
            
        if len(self.arguments):
            yield self.arguments.markdown('Arguments')
            
        if len(self.returns):
            yield self.returns.markdown('Returns')
    
# =============================================================================================================================
# Class Info
        
class ClassSection(ObjectSection):
    
    def __init__(self, name, comment=None, tag=None, **parameters):
        """ Class section
        
        Properties
        ----------
        - bases (list = []) : list of base classes
        - inherited (dict = {}) : inherited methods
        - _init (FunctionSection) : <!FunctionSection> description for __init__ function if it exists 
        
        Arguments
        ---------
        - name (str) : object name
        - comment (str = None) : comment
        - tag (str = None) : section tag
        - parameters : parameter initial values
        """
        
        self.bases     = []
        self._init     = None
        self.inherited = {}
        
        super().__init__(name, comment=comment, _rupture=Section.PAGE, tag=tag, toc=True, **parameters)
        self.set_tag("Classes")
        
        if self.comment is None and self._init is not None:
            self.comment    = self._init.comment
            self.user_lists = self._init.user_lists
        
        # ----- Properties described in a list of properties
        
        for item in self.user_lists.get('properties', []):
            self.add(item['name'], PropertySection.FromDict(item))
            
            
    def add_property(self, property_, override=False):
        
        current = self.get(property_.name)
        
        if current is None:
            self.add(property_.name, property_)
            
        else:
            if not isinstance(current, PropertySection):
                print(f"CAUTION: property name '{property_.name}' exists already as '{current.obj_type}' in {self.obj_type} '{self.name}'")
            
            current.complete_with(property_, override=override)
            
    @classmethod
    def FromInspect(cls, name, class_object):
        """ Create a FunctionSection by inspecting a class object
        
        > [!NOTE]
        > All dunder methods are ignored in this version
        
        Arguments
        ---------
        - name (str) : class name
        - class_object (class) : the class to inspect
        """
        
        assert(inspect.isclass(class_object))
        
        # Get the init method
        
        class_init = None
        init = getattr(class_object, '__init__')
        if init is not None:
            class_init = FunctionSection.FromInspect('__init__', init)
        
        class_ = cls(name, cls.get_doc(class_object), bases=[b.__name__ for b in class_object.__bases__], _init=class_init)
        
        # ----------------------------------------------------------------------------------------------------
        # Loop on the members
        
        def TEST():
            f = class_.find('get_function_class', first=True)
            if f is not None:
                assert(f.comment is None)

        for member_name, member in inspect.getmembers(class_object):
            
            TEST()
            
            if member_name in ['__init__', '__doc__', '__class__', '__dict__', '__name__', '__hash__', '__module__', '__weakref__']:
                continue
            
            if inspect.isclass(member):
                continue
            
            elif inspect.isfunction(member) or inspect.ismethod(member):
                
                # ----- Inherited
                
                func_class = cls.get_function_class(member)
                if func_class != name:
                    class_.inherited[member_name] = func_class
                    continue
                
                # ----- __func__ is inherited
                
                func = getattr(member, '__func__', None)
                if func is not None:
                    func_class = cls.get_function_class(func)
                    if func_class != name:
                        class_.inherited[member_name] = func_class
                        continue
                
                class_.add(member_name, FunctionSection.FromInspect(member_name, member))
            
            else:
                objclass = getattr(member, '__objclass__', None)
                
                if objclass is None:
                    
                    if type(member).__name__ in ['method_descriptor', 'builtin_function_or_method', 'wrapper_descriptor']:
                        continue
                    
                    if isinstance(member, property):
                        

                        func_class = cls.get_function_class(member.fget)
                        if func_class != name:
                            class_.inherited[member_name] = func_class
                            continue

                        class_.add_property(PropertySection.FromInspect(member_name, member))
                        
                    else:
                        class_.add_property(PropertySection.FromStatic(member_name, member))

                else:
                    if objclass is not object:
                        class_.inherited[member_name] = objclass.__name__

        return class_
    
    # =============================================================================================================================
    # Inheritance
    
    def complete_inheritance(self):
        
        for base in self.bases:
            base_class = self.top.find(base, tag="Classes", first=True)
            if base_class is None:
                continue
            
            base_class.complete_inheritance()
            
            for member in base_class.values():
                if member.title in self.keys() or member.title in self.inherited.keys():
                    continue
                self.inherited[member.title] = base_class.title
                
            for inh_name, inh_class in base_class.inherited.items():
                if inh_name in self.keys() or inh_name in self.inherited.keys():
                    continue
                self.inherited[inh_name] = inh_class
                
            
    # =============================================================================================================================
    # Document
    
    def before_comment(self):
        
        # Base classes
        
        sepa = None
        for base in self.bases:
            section = self.top.find(base, is_page=True, first=True)
            if section is not None:
                if sepa is None:
                    yield "> Bases classes: "
                    sepa = " :black_small_square: "
                else:
                    yield sepa
                yield section.link_to('!')
        if sepa is not None:
            yield '\n\n'

        # Signature
        
        if self._init is not None and self._init.signature is not None:
            sig = self._init.signature[1:].strip()
            if sig.startswith('self'):
                sig  = sig[4:].strip()
                if sig.startswith(','):
                    sig  = sig[1:].strip()
            sig = '(' + sig
            
            yield "``` python\n"
            yield f"{self.name}{sig}\n"
            yield "```\n\n"
            
    def after_comment(self):
        
        init = self._init
        if init is not None:
            for line in init.after_comment():
                yield line
            
        # Loop on inheritance
        
        if len(self.inherited):
            yield '### Inherited\n\n'
            
            # ----- Sorted inheritance
            
            sorted_keys = sorted(list(self.inherited.keys()), key=lambda s: s.replace('_', '').lower())
            for meth_name in sorted_keys:
                class_name = self.inherited[meth_name]
                section = self.top.find(class_name, is_page=True, first=True)
                if section is None:
                    pass
                    #yield class_name + '.' + under_to_md(meth_name)
                else:
                    yield section.link_to('#' + meth_name) + ' :black_small_square: '
            yield '\n\n'
            
    # =============================================================================================================================
    # Regroup
    
    def regroup(self):
        
        for section in self.values():
            section.regroup()
            
        self.new_tag_group("Properties",  sort_sections=True, in_toc=False, navigation=True)
        self.new_tag_group("Methods",     sort_sections=True, in_toc=False, navigation=True)


# =============================================================================================================================
# Class Info

class ModuleSection(ObjectSection):

    def __init__(self, name, comment=None, tag=None, **parameters):
        """ Modulesection
        
        Properties
        ----------
        - package (str) : module package
        - _init (ModuleSection) : <!ModuleSection> __init__ file if exists
        
        Arguments
        ---------
        - name (str) : object name
        - comment (str = None) : comment
        - tag (str = None) : section tag
        - parameters : parameter initial values
        """
        self.package = None
        self._init   = None
        
        super().__init__(name, comment, tag=tag, _rupture=Section.CHAPTER, toc=True, **parameters)
        self.set_tag("Modules")
        
    @classmethod
    def FromInspect(cls, name, module_object):
        """ Create a ModuleSection by inspecting a module object
        
        Arguments
        ---------
        - name (str) : module name
        - module_object (module) : the module to scan
        """
        
        assert(inspect.ismodule(module_object))
        
        package = module_object.__package__
        
        if package is None:
            print(f"Module {module_object} has no package, ignored...")
            return None
        
        module_ = cls(name, comment=cls.get_doc(module_object), package=package)

        # ----------------------------------------------------------------------------------------------------
        # Loop on members
        
        for member_name, member in inspect.getmembers(module_object):
            
            # ----- Ignore

            if member_name.startswith('__'):
                continue

            # ----- A module
            
            if inspect.ismodule(member):
                if member.__name__ != package + '.' + member_name:
                    continue
                
                module_.add(member_name, ModuleSection.FromInspect(member_name, member))
                
            # ----- A class
            
            elif inspect.isclass(member):
                if member.__module__ != module_object.__name__:
                    continue
                    
                module_.add(member_name, ClassSection.FromInspect(member_name, member))
                
            # ----- A function
            
            elif inspect.isfunction(member):
                if member.__module__ != module_object.__name__:
                    continue

                module_.add(member_name, FunctionSection.FromInspect(member_name, member))
                
            # ----- Global vars
                
            else:
                new_prop = PropertySection.FromStatic(member_name, member)
                
                prop = module_.get(member_name)
                if prop is None:
                    module_.add(member_name, new_prop)
                else:
                    prop.complete_with(new_prop)

        return module_

    # =============================================================================================================================
    # Regroup
    
    def regroup(self):
        
        for section in self.values():
            section.regroup()
            
        self.new_tag_group("Modules",          sort_sections=True, in_toc=False, navigation=True)
        self.new_tag_group("Global variables", sort_sections=True, in_toc=False, navigation=True)
        self.new_tag_group("Classes",          sort_sections=True, in_toc=False, navigation=True)
        self.new_tag_group("Functions",        sort_sections=True, in_toc=False, navigation=True)
    
    
    # =============================================================================================================================
    # Load this module
    
    @classmethod
    def LoadMe(cls):
        
        return cls.FromInspect('docgen', sys.modules['docgen'])
    
    @classmethod
    def LoadNumpy(cls):
        import numpy
        
        return cls.FromInspect('numpy', module_object=numpy)

    # =============================================================================================================================
    # Document
    
    def to_doc(self, doc):
        
        # ----- Create the section document in doc
        
        if self.is_top:
            chapter = doc
            doc.comment = self.comment
            doc.parse_comment()
        else:
            chapter = doc.new_chapter(self.name, self.comment, tag="Modules")
            
        if True:

            # ----- Members to doc
            
            for obj_ in self.values():
                obj_.to_doc(chapter)
                
                
            # ----- Group by tags
            # Note that if a module is set to transparent, its members will be
            # grouped in the proper section
            
            chapter.new_tag_group("Modules",          sort_sections=True, in_toc=False, navigation=True)
            chapter.new_tag_group("Global variables", sort_sections=True, in_toc=False, navigation=True)
            chapter.new_tag_group("Classes",          sort_sections=True, in_toc=False, navigation=True)
            chapter.new_tag_group("Functions",        sort_sections=True, in_toc=False, navigation=True)
            
        else:
            # Loop on the members
            
            prop_section  = chapter.new("Global variables", sort_sections=True, ignore_if_empty=True, in_toc=False, navigation=True)
            mod_section   = chapter.new("Modules",          sort_sections=True, ignore_if_empty=True, in_toc=False, navigation=True)
            class_section = chapter.new("Classes",          sort_sections=True, ignore_if_empty=True, in_toc=False, navigation=True)
            func_section  = chapter.new("Functions",        sort_sections=True, ignore_if_empty=True, in_toc=False, navigation=True)
    
            for member in self.values():
                if member.obj_type == 'property':
                    member.to_doc(prop_section)
                    
                elif member.obj_type == 'module':
                    member.to_doc(mod_section)
                    
                elif member.obj_type == 'class':
                    member.to_doc(class_section)
                    
                else:
                    member.to_doc(func_section)
            
        return chapter
    
    
# =============================================================================================================================
# Package documentation

class PackageDoc(Documentation):
    
    def __init__(self, package):
        super().__init__(ModuleSection.FromInspect(package.__name__, package))
        
    def cook(self):
        
        if self._cooked:
            return
        
        for cl in self.top_section.all_values():
            if cl.tag == "Classes":
                cl.complete_inheritance()
        
        self.top_section.regroup()
        
        super().cook()


# =============================================================================================================================
# Class : capture inheritance from another class

def capture_inheritance(class_, base_, remove=True):
    """ Capture properties et methods from another class
    
    Allow to document class items as it were not inherited.
    
    > [!Note]
    > if the name of the base class is in the inherits list, it is removed from it
    
    Arguments
    ---------
    - class_ (dict) : the class to enrich
    - base_ (dict) : the class to capture properties and methods from
    - remove (bool = True) : remove base name from inheritance list
    """
    
    for sub in base_['subs'].values():
        
        # Sub is overloaded or is __init__
        
        if sub['name'] in list(class_['subs'].keys()) + ['__init__']:
            continue

        # Let's capture it
        
        class_['subs'][sub['name']] = sub
        
    # Let's suppress the entrance in inherit
    
    if remove and class_.get('inherits') is not None:
        if base_['name'] in class_['inherits']:
            class_['inherits'].remove(base_['name'])
            
    return class_

def capture_inheritances(class_, files_, include=None, exclude=[], verbose=False):
    """ Capture inheritances
    
    Allow to document class items as it were not inherited.
    
    > [!Note]
    > if the name of the base class is in the inherits list, it is removed from it
    
    Arguments
    ---------
    - class_ (dict) : the class to enrich
    - files_ (dict) : the hierarchy containing base classes to capture from
    - include (list = None) : limit capture to the given list
    - exclude (list = []) : exclude classes in the given list
    """
    
    if class_.get('inherits') is None:
        return class_
    
    to_capture = class_['inherits'] if include is None else include
    captured = []
    
    for base_name in to_capture:
        
        if base_name in exclude:
            continue
        
        base_ = struct_search(files_, obj='class', name=base_name)
        if base_ is None:
            continue
        
        if verbose:
            print(f"Capture inheritance {class_['name']} <- {base_name}")
        
        capture_inheritance(class_, base_, remove=False)
        captured.append(base_name)
        
    for base_name in captured:
        if base_name in class_['inherits']:
            class_['inherits'].remove(base_name)
            
    return class_

# =============================================================================================================================
# Tests

if False:

    import sys
    from importlib import import_module
    
    import treedict
    
    module_ = Module_.FromInspect('treedict', treedict)
    
    doc = Doc('treedict sample', "/Users/alain/Documents/blender/scripts/modules/docgen/doc")
    module_.to_doc(doc)
    
    doc.cook()
    doc.get_documentation()
    
if True:
    #module_ = ModuleSection.LoadMe()
    doc = PackageDoc(sys.modules['docgen'])
    files = doc.create_documentation("/Users/alain/Documents/blender/scripts/modules/docgen/doc")





        
        
    




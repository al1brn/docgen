"""
Created on Tue Sep 10 07:44:18 2024

@author: alain


$ DOC START

Python object info

Documentation is based on structure information on objects to document

$ DOC END

created : 2024 09 14

"""

import inspect
from pathlib import Path

import re
import sys
import os

#sys.path.append(Path(__file__).parents[0])

#sys.path.append(os.getcwd())

from docgen.parser import parse_meta_comment, del_margin, extract_lists
from docgen.mddoc import Doc, under_to_md
from docgen.tree import TreeDict

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
    
    ````
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

class Object_(TreeDict):
    
    SEP = '.'
    DOT = None
    
    obj_type = None
    
    def __init__(self, name, comment=None, **kwargs):
        """ Root class for informations on python objects
        
        The minimum information is <#name> and <#comment> can be completed
        by sub classes.
        
        Properties
        ----------
        - name (str) : module name, class name, property name...
        - comment (str) : comment in __doc__
        - obj_type (str) : (read only) name of the object type
        - meta_props (dict) : dictionary of options set by meta instruction $ SET
        - meta_lists (ditc) : dictionary of <!DescriptionList> extracted in the comment
        
        Arguments
        ---------
        - name (str) : object name
        - comment (str = None) : comment
        - kwargs : additional properties
        """
        
        super().__init__()
        
        self.name    = name
        self.comment = del_margin(comment)
        self.hidden  = False
        
        self.meta_props = {}
        self.meta_lists = {}
        
        for k, v in kwargs.items():
            setattr(self, k, v)
            
        # ----- Parse the cmment
        
        self.parse_comment()
        

    def __str__(self):
        return f"<{type(self).__name__} {self.name}>"
    
    @property
    def key(self):
        return self.name
            
    def get_prop(self, prop_name, default=None):
        """ Get an optional property
        
        Arguments
        ---------
        - prop_name (str) : name of the property to read
        - default (any = None) : default value if the property doesn't exist
        
        Returns
        -------
        - any : the property or None if it doesn't exist
        """

        if hasattr(self, prop_name):
            return getattr(self, prop_name)
        else:
            return default
        
    def meta(self, meta_name, default=None):
        """ Get a meta property
        
        A meta property can be set in the comment with the syntax
        ```
         $ SET meta_name = value
        ```
        
        Arguments
        ---------
        - meta_name (str) : name of the meta property to read
        - default (any = None) : default value if the property doesn't exist
        
        Returns
        -------
        - any : the meta property value or None if it doesn't exist
        """
        return self.meta_props.get(meta_name, default)
        
    # ====================================================================================================
    # Parse the comment

    def parse_comment(self):
        """ Collect extra information from the comment
        
        #### Inline commands
        - $ DOC START : ignore lines above
        - $ DO END : ignore lines after
        - $ SET prop = 123 : pass properties to the doc generator
        
        In addition, special lists are extracted to create <!DescriptionList>
        
        #### Extracted lists
        - raises
        - arguments
        - returns
        - properties
        """
        
        if self.comment is None:
            return
        
        # ----------------------------------------------------------------------------------------------------
        # Extract meta commands
        
        #comment, props = parse_meta_comment(self.comment)
        #for k, v in props.items():
        #    self.meta_props[k] = v

        # ----------------------------------------------------------------------------------------------------
        # Extract the lists from the comment
        
        comment, lists = extract_lists(self.comment, 'arguments', 'raises', 'returns', 'properties')
        for k, v in lists.items():
            self.meta_lists[k] = v

        # ----------------------------------------------------------------------------------------------------
        # Done
                
        self.comment = comment

    # =============================================================================================================================
    # Write documentation
    
    def document(self, doc):
        return None
    

# =============================================================================================================================
# Property Info
            
class Property_(Object_):
    
    obj_type = 'property'
    
    def __init__(self, name, comment=None, **kwargs):
        """ Information on property
        
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
        - type (str = None) : type of the property
        - type_descr (str = None) : type description
        - default (str = EMPTY) : default value
        - fget (Function_ = None) : getter <!Function_>
        - fset (Function_ = None) : setter <!Function_>        
        """

        self.type       = None
        self.type_descr = None
        self.default    = EMPTY
        self.fget       = None
        self.fset       = None

        super().__init__(name, comment, **kwargs)
        
        
        if self.fget is not None:
            if self.type is None:
                self.type = self.fget.return_type
            if self.type_descr is None:
                self.type_descr = self.fget.return_type_descr
        
    @classmethod
    def FromDict(self, item):
        """ Create a property from a dict
        
        Arguments
        ---------
        - item (dict) : information on the property to create

        Returns
        -------
        - Property_        
        """
        return Property_(item['name'], comment=item.get('description'), type=item.get('type'), default=item.get('default'))

    @classmethod
    def FromListItem(self, item):
        """ Create a property from a list item
        
        Arguments
        ---------
        - item (ListItem) : information on the property to create

        Returns
        -------
        - Property_        
        """
        return Property_(item.name, comment=item.description, type=item.type, default=item.default)
        
        
    @classmethod
    def FromInspect(cls, name, property_object, verbose=False):
        """ Create a Property_ instance from a property
        
        > [!NOTE]
        > If name is None, the name is read from fget
        
        Arguments
        ---------
        - property_object (property) : the object the scan
        - name (str = None) : name
        
        Returns
        -------
        - Property_
        """            
        fget, fset = None, None
        try:
            fget = None if property_object.fget is None else Function_.FromInspect('fget', property_object.fget)
        except:
            pass

        try:
            fset = None if property_object.fset is None else Function_.FromInspect('fset', property_object.fset)
        except:
            pass
        
        if verbose:
            print("Read property", name)
            
        return cls(name, inspect.getdoc(property_object), fget=fget, fset=fset)
    
    @classmethod
    def FromStatic(cls, property_object, name=None):
        """ Creare a Property_ instance from a static property in a module or a class
        
        Arguments
        ---------
        - property_object
        - name (str = None)
        
        Returns
        -------
        - Property_
        """        
        stype = property_object.__name__ if hasattr(property_object, '__name__') else type(property_object).__name__
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
    # Document
    
    def document(self, doc):
        
        section = doc.new(self.name, in_toc=True)
        
        section.write(f"> TYPE: **{'?' if self.type is None else self.type}**{'' if self.type_descr is None else ' ' + self.type_descr}")
        if self.default != EMPTY:
            section.write(f"<br> DEFAULT: **{self.default}**")
        section.write("\n\n")
        
        section.write(self.comment)
        
        return section
    
# =============================================================================================================================
# Class / Function root

class ClassFunc_(Object_):
    def __init__(self, name, comment=None, signature=None, **kwargs):
        """ Classes and function root description
        
        Classes and functions have arguments and raises lists

        Properties
        ----------
        - signature (str) : function signature
        - raises (DescriptionList = None) : list of raised exceptions
        - arguments (DescriptionList = []) : argument descriptions
        
        Arguments
        ---------
        - name (str) : object name
        - comment (str = None) : comment
        - signature (str = None) : function signature
        - kwargs : custom parameters
        """
        super().__init__(name, comment, signature=signature, **kwargs)
        
        self.raises    = DescriptionList.FromList(self.meta_lists.get('raises'))
        self.arguments = DescriptionList.FromList(self.meta_lists.get('arguments'))
            
            
    def add_property(self, property_, override=False):
        current = self.get(property_.name)
        if current is None:
            self.add(property_.name, property_)
        else:
            if not isinstance(current, Property_):
                print(f"CAUTION: property name '{property_.name}' exists already as '{current.obj_type}' in {self.obj_type} '{self.name}'")
            current.complete_with(property_, override=override)
    
# =============================================================================================================================
# Function info
        
class Function_(ClassFunc_):
    
    obj_type = 'function'
    
    def __init__(self, name, comment=None, signature=None, **kwargs):
        """ Description of a function

        Properties
        ----------
        - raises (DescriptionList = None) : list of raises exceptions
        - arguments (DescriptionList = None) : arguments description
        - returns (list) : list of <!ListItem>
        
        Arguments
        ---------
        - name (str) : object name
        - comment (str = None) : comment
        
        - signature (str = None) : function signature
        - arguments (list = None) : list of <!ListItem>
        - raises (list = None) : list of <!ListItem>
        - returns (list = None) : list of <!ListItem>
        """
        
        super().__init__(name, comment, signature=signature, **kwargs)
        
        # ----- List extracted from comment
        
        self.returns = DescriptionList.FromList(self.meta_lists.get('returns'))

            
    def __str__(self):
        return f"<Function_ {self.name}() returns: {[str(item) for item in self.returns]}>"
        
        
    @classmethod
    def FromInspect(cls, name, function_object, verbose=False):
        """ Create a Function_ instance from a function
        
        > [!NOTE]
        > If **name** argument is none, `object.__name__` is taken.
        
        Arguments
        ---------
        - object (function) : the object to scan
        - name (str = None) : name of the object
        """        
        if verbose:
            print("Read function", name)
            
        try:
            sig = inspect.signature(function_object)    
        except:
            sig = '()'
            
        # ----- Create the function
        
        function_ = cls(name, inspect.getdoc(function_object), signature=str(sig))

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
    
    def document(self, doc):
        
        section = doc.new(self.name, in_toc=True, top_bar='-', navigation=True)
        
        if self.signature is not None:

            sig = self.signature[1:].strip()
            for sc in ('self', 'cls'):
                if sig.startswith(sc):
                    sig  = sig[len(sc):].strip()
                    if sig.startswith(','):
                        sig  = sig[1:].strip()
                    break
            sig = '(' + sig
            
            section.write_source(self.name + sig)
            
        section.write(self.comment)
        
        section.parse_comment()
        
        if len(self.raises):
            section.write(self.raises.markdown('Raises'))
            
        if len(self.arguments):
            section.write(self.arguments.markdown('Arguments'))
            
        if len(self.returns):
            section.write(self.returns.markdown('Returns'))
        
        return section
    
# =============================================================================================================================
# Class Info
        
class Class_(ClassFunc_):
    
    obj_type = 'class'
    
    def __init__(self, name, comment=None, bases=None, **kwargs):
        """ Information on a class
        
        Properties
        ----------
        - bases (list) : list of base classes
        - _init (Function_) : <!Function_> description for __init__ function if it exists 
        
        Arguments
        ---------
        - name (str) : class name
        - comment (str) : comment
        - bases (list) : list of base classes
        - kwargs : complementary information
        """
        
        super().__init__(name, comment, **kwargs)
        self.bases = [] if bases is None else bases
        self._init = None
        self.inherited = {}
        
        # ----- Properties described in a list of properties
        
        props = self.meta_lists.get('properties')
        if props is not None:
            for item in props:
                self.add_property(Property_.FromDict(item))
        
    @classmethod
    def FromInspect(cls, class_name, class_object, verbose=False):
        """ Create an Class_ instance from a python class

        > [!NOTE]
        > If **name** argument is none, `object.__name__` is taken.
        
        The method `__init__` is not stored in the <#members> dictionary but in <#_init> property.
        
        > [!CAUTION]
        > All dunder methods are ignored in this version
        
        Arguments
        ---------
        - name (str) : class name
        - class_object (class) : the object to scan
        """
        
        assert(inspect.isclass(class_object))
        
        class_ = cls(class_name, inspect.getdoc(class_object), [b.__name__ for b in class_object.__bases__])
        
        # ----------------------------------------------------------------------------------------------------
        # Loop on the members

        for name, member in inspect.getmembers(class_object):
            
            if name in ['__doc__', '__class__', '__dict__', '__name__', '__hash__', '__module__', '__weakref__']:
                continue
            
            is_init = name == '__init__'
            if is_init:                
                class_._init = Function_.FromInspect('__init__', member)
                
                if class_.comment is None:
                    class_.comment = inspect.getdoc(member)
                    class_.parse_comment()
                    
                class_.signature = class_._init.signature
                class_.arguments = class_._init.arguments
                class_.raises    = class_._init.raises
                
                class_._init.comment
                    
            else:
                if inspect.isclass(member):
                    continue
                
                elif inspect.isfunction(member) or inspect.ismethod(member):
                    doc = inspect.getdoc(member)
                    if doc is None or doc.strip() == "":
                        continue
                    
                    f_ = class_.add(name, Function_.FromInspect(name, member))
                
                else:
                    objclass = getattr(member, '__objclass__', None)
                    if objclass is None:
                        
                        if type(member).__name__ in ['method_descriptor', 'builtin_function_or_method', 'wrapper_descriptor']:
                            continue
                        
                        if isinstance(member, property):
                            class_.add_property(Property_.FromInspect(name, member))
                            
                        else:
                            new_prop = Property_.FromStatic(member, name=name)
                            
                            prop = class_.get(name)
                            if prop is None:
                                class_.add(name, new_prop)
                            else:
                                prop.complete_with(new_prop)

                    else:
                        if objclass is not object:
                            class_.inherited[name] = objclass.__name__

        return class_
            
            
    # =============================================================================================================================
    # Document
    
    def document(self, doc):
        
        page = doc.new_page(self.name, sort_sections=False, toc_sort=True)
        
        if self.signature is not None:
            sig = self.signature[1:].strip()
            if sig.startswith('self'):
                sig  = sig[4:].strip()
                if sig.startswith(','):
                    sig  = sig[1:].strip()
            sig = '(' + sig
            page.write_source(self.name + sig)
            
        page.write(self.comment)
        
        if len(self.raises):
            page.write(self.raises.markdown('Raises'))
            
        if len(self.arguments):
            page.write(self.arguments.markdown('Arguments'))
            
        # Loop on the members
        
        if len(self.inherited):
            page.write('\n\n### Inherited\n\n')
            for k, v in self.inherited.items():
                page.write(v + '.' + under_to_md(k) + ' :black_small_square: ')
        
        prop_section = page.new("Properties", sort_sections=True, ignore_if_empty=True, in_toc=False, navigation=True)
        meth_section = page.new("Methods",    sort_sections=True, ignore_if_empty=True, in_toc=False)
        
        for member in self.values():
            if member.obj_type == 'property':
                member.document(prop_section)
            else:
                member.document(meth_section)
            
        return page
            

# =============================================================================================================================
# Class Info

class Module_(Object_):
    
    obj_type = 'module'
    
    def __init__(self, name, comment=None, **kwargs):
        """ Information on a module
        
        Arguments
        ---------
        - name (str) : class name
        - comment (str) : comment
        - package (str) : package
        - kwargs : complementary information        
        """

        super().__init__(name, comment, **kwargs)
        
    @classmethod
    def FromInspect(cls, module_name, module_object, verbose=False):
        """ Create an Module_ instance from a python module

        Arguments
        ---------
        - module_object (module) : the module to scan
        """
        
        assert(inspect.ismodule(module_object))
        
        package = module_object.__package__
        
        if package is None:
            print(f"Module {module_object} has no package, ignored...")
            return None
        
        module_ = cls(module_name, inspect.getdoc(module_object))
        
        if verbose:
            print(f"Read module '{module_.name}', package '{package}'...")

        # ----------------------------------------------------------------------------------------------------
        # Loop on members
        
        for name, member in inspect.getmembers(module_object):
            
            # ----- Ignore

            if name.startswith('__'):
                continue

            # ----- A module
            
            if inspect.ismodule(member):
                if member.__name__ != package + '.' + name:
                    continue
                
                module_.add(name, Module_.FromInspect(name, member, verbose=verbose))
                
            # ----- A class
            
            elif inspect.isclass(member):
                if member.__module__ != module_object.__name__:
                    continue
                    
                module_.add(name, Class_.FromInspect(name, member, verbose=verbose))
                
            # ----- A function
            
            elif inspect.isfunction(member):
                if member.__module__ != module_object.__name__:
                    continue

                module_.add(name, Function_.FromInspect(name, member, verbose=verbose))
                
            # ----- Global vars
                
            else:
                new_prop = Property_.FromStatic(member, name=name)
                
                prop = module_.get(name)
                if prop is None:
                    module_.add(name, new_prop)
                else:
                    prop.complete_with(new_prop)

            
        return module_
    
    # =============================================================================================================================
    # Load this module
    
    @classmethod
    def LoadMe(cls):
        
        return cls.FromInspect('docgen', sys.modules['docgen'])
    
    @classmethod
    def LoadNumpy(cls):
        import numpy
        
        return cls.FromInspect('numpy', module_object=numpy, verbose=False)


    # =============================================================================================================================
    # Document
    
    def document(self, doc):
        
        if self.is_top:
            chapter = doc
            doc.comment = self.comment
            doc.parse_comment()
        else:
            chapter = doc.new_chapter(self.name, self.comment)
            
        # Loop on the members
        
        prop_section  = chapter.new("Global variables", sort_sections=True, ignore_if_empty=True, in_toc=False, navigation=True)
        mod_section   = chapter.new("Modules",          sort_sections=True, ignore_if_empty=True, in_toc=False, navigation=True)
        class_section = chapter.new("Classes",          sort_sections=True, ignore_if_empty=True, in_toc=False, navigation=True)
        func_section  = chapter.new("Functions",        sort_sections=True, ignore_if_empty=True, in_toc=False, navigation=True)
        
        for member in self.values():
            if member.obj_type == 'property':
                member.document(prop_section)
                
            elif member.obj_type == 'module':
                member.document(mod_section)
                
            elif member.obj_type == 'class':
                member.document(class_section)
                
            else:
                member.document(func_section)
            
        return chapter
 


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
    module_.document(doc)
    
    doc.cook()
    doc.get_documentation()
    
module_  = Module_.LoadMe()

doc = Doc('treedict sample', "/Users/alain/Documents/blender/scripts/modules/docgen/doc")
module_.document(doc)

doc.cook()
doc.get_documentation()






        
        
    




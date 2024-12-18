"""
Created on Tue Sep 10 07:44:18 2024

@author: alain


$ DOC START

$ DOC NOT transparent


Python object info

Documentation is based on structure information on objects to document

created : 2024 09 14

"""

from typing import Any, Optional, Union, List, Tuple, Dict, Iterator, ForwardRef

import inspect
from pathlib import Path

import sys
import os

folder = str(Path(os.getcwd()).parents[0])
if not folder in sys.path:
    sys.path.append(folder)
assert(folder in sys.path)

from docgen.parser import extract_lists
from docgen.documentation import Section, Documentation

EMPTY  ='_EMPTY'

# =============================================================================================================================
# Format annotation

def format_type(atype: type) -> str:
    
    if atype is None:
        return None
    
    elif isinstance(atype, str):
        return atype

    elif isinstance(atype, ForwardRef):
        return atype.__forward_arg__
    
    elif hasattr(atype, '__module__') and atype.__module__ == 'typing':

        name = getattr(atype, '__name__', None)
        if name is None:
            return str(atype)
        
        args = atype.__args__ if hasattr(atype, '__args__') else []
    
        if name in ['Union', 'Optional']:            
            return " | ".join([format_type(arg) for arg in args])
        
        elif name == 'List':
            return f"list of {format_type(args[0])}" if len(args) else 'list'
        
        elif name == 'Tuple':
            return f"tuple ({', '.join([format_type(arg) for arg in args])})"
        
        elif name == 'Dict':
            return f"dict[{format_type(args[0])}]: {format_type(args[1])}" if len(args) == 2 else 'dict'
        
        elif name == 'Iterator':
            return f"iterator: {format_type(args[0])}" if len(args) else 'iterator'

        return name
    
    elif hasattr(atype, '__name__'):
        name = atype.__name__
        if name == 'NoneType':
            name = 'None'
        return name
    
    else:
        return str(atype)

# =============================================================================================================================
# Lists in comment

# -----------------------------------------------------------------------------------------------------------------------------
# List item in CommentList

class ListItem:
    
    def __init__(self, name: str, type: Optional[type] = None, default: Any = EMPTY, description: Optional[str] = None, **kwargs):
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
        self.type        = format_type(type)
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
    def FromOther(cls, other: 'ListItem') -> 'ListItem':
        """ Create from another ListItem or from a dict
        
        Arguments
        ---------
        - other (ListItem or dict) : the source
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
    def FromParameter(cls, param: object, description: Optional[str] = None) -> 'ListItem':
        """ Create an instance from the python paramer description.
        """
        name    = param.name
        atype   = None  if param.annotation == param.empty else param.annotation
        default = EMPTY if param.default == param.empty else param.default

        return cls(name, type=atype, default=default, description=None)
    
    def get_prop(self, attribute: str, default: Any = None) -> Any:
        """ Get a custom attribute value
        
        Arguments
        ---------
        - attribute (str) : attribute name
        - default : value to return if the attribute doesn't exist
        """
        if attribute in dir(self):
            return getattr(self, attribute)
        else:
            return default
            
    @property
    def has_type(self) -> bool:
        """ Check if <#type> is not None
        """
        return self.type is not None
    
    @property
    def has_default(self) -> bool:
        """ Check if <#default> is different from <#EMPTY>
        """
        return self.default != EMPTY
    
    @property
    def has_description(self) -> bool:
        """ Check if <#description> is not None
        """
        return self.description is not None
    
    def complete_with(self, other:'ListItem') -> None:
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
    def markdown(self) -> str:
        """ Markdown text

        List item is formatted in : "- name (type) : description"
        Items are omitted when they don't exist 
        """
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
    def FromList(cls, list_: list) -> 'DescriptionList':
        """ Initialize from a list
        """
        dl = cls()
        if list_ is None:
            return dl
        
        for item in list_:
            dl.append(ListItem.FromOther(item))
            
        return dl
        
    
    def get(self, name: str) -> Optional[ListItem]:
        """ Get a list item by its name
        
        Argument
        --------
        - name (str) : item name
        """
        for item in self:
            if item.name == name:
                return item
        return None
    
    def complete_with(self, other_list: 'DescriptionList') -> None:
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
    
    def markdown(self, title: str) -> str:
        """ Markdown text of the list

        The mardown includes a title wich is underlined followed by the list
        of markdown for the items

        Arguments
        ---------
        - title : list title
        """
        return f"\n\n#### {title}:\n" + "".join([item.markdown for item in self]) + '\n'                
    
# =============================================================================================================================
# Base information

class ObjectSection(Section):
    
    SEP = '.'
    DOT = None
    
    def __init__(self, name: str, comment: Optional[str] = None, tag: Optional[str] = None, **parameters):
        """ Root class for informations on python objects
        
        The minimum information is <#name> and <#comment> can be completed
        by sub classes.
        
        Properties
        ----------
        - name (str) : module name, class name, property name...
        
        Arguments
        ---------
        - name  : object name
        - comment : comment
        - tag : section tag
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
    
    def clone(self) -> 'ObjectSection':
        """ Clone
        """
        clone = type(self)(self.name)

        for name in dir(self):
            if name.startswith('__') or name == 'name':
                continue
            
            value = getattr(self, name)
            if inspect.ismethod(value) or inspect.isfunction(value):
                continue
            
            try:
                setattr(clone, name, value)
            except:
                pass

        return clone
    
    @staticmethod
    def get_doc(py_object: object) -> str:
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
    def get_function_class(func: object) -> Optional[str]:
        """ Get the class name of a function
        """
        names = func.__qualname__.split('.')
        if len(names) == 1:
            return None
        
        return '.'.join(names[:-1])

    @staticmethod
    def get_property_class(prop: str) -> Optional[str]:
        """ The the class name of a property
        """
        names = prop.__qualname__.split('.')
        if len(names) == 1:
            return None
        
        return '.'.join(names[:-1])

    def regroup(self):
        return
        
# =============================================================================================================================
# Property Info
            
class PropertySection(ObjectSection):
    
    def __init__(self, name: str, comment: Optional[str] = None, tag: Optional[str] = None, **parameters):
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
        - name : object name
        - comment : comment
        - tag : section tag
        - parameters : parameter initial values
        """

        self.type        = None
        self.default     = EMPTY
        self.fget        = None
        self.fset        = None
        
        super().__init__(name, comment=comment, tag=tag, navigation=True, **parameters)
        self.set_tag('Properties')
        
        if self.fget is not None:
            if self.type is None:
                self.type = self.fget.return_type
            if self.comment is None:
                self.comment = self.fget.comment
            
    def before_comment(self) -> Iterator[str]:
        """ Yield the lines before the comment section
        """
        
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
    def FromDict(cls, item: dict) -> 'PropertySection':
        """ Create a property from a dict
        
        Arguments
        ---------
        - item : information on the property to create
        """
        return cls(item['name'], comment=item.get('description'), type=item.get('type'), default=item.get('default', EMPTY))

    @classmethod
    def FromListItem(cls, item: ListItem) -> 'PropertySection':
        """ Create a property from a list item
        
        Arguments
        ---------
        - item : information on the property to create
        """
        return cls(item.name, comment=item.description, type=item.type, default=item.default)
        
        
    @classmethod
    def FromInspect(cls, name: str, property_object: property) -> 'PropertySection':
        """ Create a PropertySection by inspect a property
        
        > [!NOTE]
        > If name is None, the name is read from fget
        
        Arguments
        ---------
        - name : name
        - property_object : the object the scan
        """
        fget = FunctionSection.FromInspect('fget', property_object.fget)
        fset = FunctionSection.FromInspect('fset', property_object.fset)
        
        return cls(name, cls.get_doc(property_object), fget=fget, fset=fset)
    
    @classmethod
    def FromStatic(cls, name, property_object: property) -> 'PropertySection':
        """ Creare a Property_ instance from a static property in a module or a class
        
        Arguments
        ---------
        - name : name
        - property_object : property
        """
        stype = type(property_object).__name__
        try:
            sdef = str(property_object)
        except:
            sdef = '???'
            
        if len(sdef) > 30:
            sdef = sdef[:30] + '...'
            
        return cls(name, type=stype, default=sdef)
    
    def complete_with(self, other: 'PropertySection', override: bool = False) -> None:
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
    
    def __init__(self, name: str, comment: Optional[str] = None, tag: Optional[str] = None, **parameters):
        """ Function section

        Properties
        ----------
        - ftype (str) : function type (function, static, class, ...)
        - signature (str) : function signature
        - raises (DescriptionList = None) : list of raised exceptions
        - arguments (DescriptionList = []) : argument descriptions
        
        Arguments
        ---------
        - name : object name
        - comment : comment
        - tag : section tag
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
    def inspect_type(func: object) -> str:
        """ Get the function type name
        """
        
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
    def FromInspect(cls, name: str, function_object: object) -> 'FunctionSection':
        """ Create a FunctionSection by inspecting a function object
        
        Arguments
        ---------
        - name : name of the function
        - object : the object to inspect
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

        # ----- Return type

        if hasattr(function_object, '__annotations__'):
            ret_type = function_object.__annotations__.get('return', 'NONE')
            if ret_type != 'NONE':
                if len(function_.returns):
                    function_.returns[0].name = format_type(ret_type)
                else:
                    function_.returns.append(ListItem(format_type(ret_type)))
        
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
    def return_type(self) -> Optional[str]:
        """ Type returned by the function
        """
        if self.returns is None or len(self.returns) == 0:
            return None
        
        return self.returns[0].name
    
    @property
    def return_type_descr(self) -> Optional[str]:
        """ Description of function return
        """                                            
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
    
    def before_comment(self) -> Iterator[str]:

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
        
        
    def after_comment(self) -> Iterator[str]:
        
        if len(self.raises):
            yield self.raises.markdown('Raises')
            
        if len(self.arguments):
            yield self.arguments.markdown('Arguments')
            
        if len(self.returns):
            yield self.returns.markdown('Returns')
    
# =============================================================================================================================
# Class Info
        
class ClassSection(ObjectSection):
    
    def __init__(self, name: str, comment: str | None = None, tag: Optional[str] = None, **parameters):
        """ Class section
        
        Properties
        ----------
        - bases (list = []) : list of base classes
        - inherited (dict = {}) : inherited methods
        - no_init (bool = False) : ignore init documentation
        - _init (FunctionSection) : <!FunctionSection> description for __init__ function if it exists 
        
        Arguments
        ---------
        - name  : object name
        - comment : comment
        - tag : section tag
        - parameters : parameter initial values
        """
        
        self.bases     = []
        self._init     = None
        self.no_init   = False
        self.inherited = {}
        
        super().__init__(name, comment=comment, _rupture=Section.PAGE, tag=tag, toc=True, **parameters)
        self.set_tag("Classes")
        if self.no_init:
            self._init = None
        
        if self.comment is None and self._init is not None:
            if self.comment is None:
                self.comment = self._init.comment
            self.user_lists = self._init.user_lists
        
        # ----- Properties described in a list of properties
        
        for item in self.user_lists.get('properties', []):
            self.add(item['name'], PropertySection.FromDict(item))
            
            
    def add_property(self, property_: object, override: bool = False) -> None:
        """ Add a property
        """
        current = self.get(property_.name)
        
        if current is None:
            self.add(property_.name, property_)
            
        else:
            if not isinstance(current, PropertySection):
                print(f"CAUTION: property name '{property_.name}' exists already as '{current.obj_type}' in {self.obj_type} '{self.name}'")
            
            current.complete_with(property_, override=override)
            
    @classmethod
    def FromInspect(cls, name: str, class_object: object) -> 'ClassSection':
        """ Create a FunctionSection by inspecting a class object
        
        > [!NOTE]
        > All dunder methods are ignored in this version
        
        Arguments
        ---------
        - name: class name
        - class_object : the class to inspect
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
        
        for member_name, member in inspect.getmembers(class_object):
            
            if member_name in ['__weakref__']:
                continue
            
            elif inspect.ismodule(member) or inspect.ismethodwrapper(member):
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
                
            elif isinstance(member, property):
                
                func_class = cls.get_function_class(member.fget)
                if func_class != name:
                    class_.inherited[member_name] = func_class
                    continue

                class_.add_property(PropertySection.FromInspect(member_name, member))
                
                
            else:
                if name.startswith('__') and name.endswith('__'):
                    continue
                    
                if type(member).__name__ in ['method_descriptor', 'builtin_function_or_method', 'wrapper_descriptor']:
                    continue
                
                objclass = getattr(member, '__objclass__', None)
                
                if objclass is None:
                    
                    class_.add_property(PropertySection.FromStatic(member_name, member))

                elif objclass is not object:
                        class_.inherited[member_name] = objclass.__name__   
                        
                else:
                    pass

        return class_
    
    # =============================================================================================================================
    # Inheritance
    
    def complete_inheritance(self) -> None:
        """ Complete inheritance list from the base classes
        
        By inspecting classes, we don't have instance properties.
        These properties are declared in the comment section of classes.
        
        This method fill the <#inherited> dictionary of inherited members
        """
        
        for base in self.bases:
            base_class = self.top.find(base, tag="Classes")
            if base_class is None:
                continue
            
            # ----- Make sure the base class is completed
            
            base_class.complete_inheritance()
            
            # ----- Loop on the base class direct members
            
            for member in base_class.values():
                if member.title in self.keys() or member.title in self.inherited.keys():
                    continue
                self.inherited[member.title] = base_class.title
                
            # ----- Loop on the base class inherited methods
                
            for inh_name, inh_class in base_class.inherited.items():
                if inh_name in self.keys() or inh_name in self.inherited.keys():
                    continue
                self.inherited[inh_name] = inh_class
                
    def hide_inheritance(self, hidden_classes: List['ClassSection']) -> None:
        """ Hide inheritance from hidden classes
        
        Intermediary classes can be hidden from the documentation. When it is the case:
        - methods and properties are cloned in the descending classes
        - inherited methods and properties becomes direct inheritance from the
          descending classes
          
         > [!IMPORTANT]
         > The classes provided in the hidden classes must have already hidden their hidden
         > base classes
          
        Arguments
        ---------
        - hidden_classes (list of ClassSection) : list of hidden classes
        """
        
        for hidden_class in hidden_classes:
            if hidden_class is self:
                continue
            
            if hidden_class.title not in self.bases:
                continue
            
            # ----- Hide from the base class list
            # and add the one from hidden class
            
            del self.bases[self.bases.index(hidden_class.title)]
            for name in hidden_class.bases:
                if name not in self.bases:
                    self.bases.append(name)
                    
            # ----- Clone the members of the hidden class when they
            # are inherited. When they are not, thery are supposed
            # to be overriden
            
            to_remove = []
            
            for member in hidden_class.values():
                
                # Is the member inherited ?
                
                if not member.title in self.inherited.keys():
                    assert(member.title not in self.values())
                    continue
                
                # Member could be inherited from another class
                
                if self.inherited[member.title] != hidden_class.title:
                    continue
                
                # It is inhited:
                # - we remove from inheritance
                # - and we clone the member
                
                to_remove.append(member.title)
                self.add(member.title, member.clone())
                        
            for name in to_remove:
                del self.inherited[name]
                
            
    # =============================================================================================================================
    # Document
    
    def before_comment(self) -> Iterator[str]:
        
        # Base classes
        
        sepa = None
        for base in self.bases:
            section = self.top.find(base, tag="Classes")
            if section is not None:
                if sepa is None:
                    yield "> Bases classes: "
                    sepa = " :black_small_square: "
                else:
                    yield sepa
                yield section.link()
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
            
    def after_comment(self) -> Iterator[str]:
        
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
                section = self.top.find(class_name, tag="Classes")
                if section is None:
                    pass
                    #yield class_name + '.' + under_to_md(meth_name)
                else:
                    yield section.link_to(meth_name) + ' :black_small_square: '
            yield '\n\n'
            
    # =============================================================================================================================
    # Regroup
    
    def regroup(self) -> None:
        
        for section in self.values():
            if section.is_hidden:
                continue
            
            if isinstance(section, ObjectSection):
                section.regroup()
            
        self.new_tag_group("Properties",    sort_sections=True, in_toc=False)
        self.new_tag_group("Methods",       sort_sections=True, in_toc=False)


# =============================================================================================================================
# Class Info

class ModuleSection(ObjectSection):

    def __init__(self, name: str, comment: Optional[str] = None, tag: Optional[str] = None, **parameters):
        """ Modulesection
        
        Properties
        ----------
        - package (str) : module package
        - _init (ModuleSection) : <!ModuleSection> __init__ file if exists
        
        Arguments
        ---------
        - name : object name
        - comment : comment
        - tag : section tag
        - parameters : parameter initial values
        """
        self.package   = None
        self._init     = None
        self.is_folder = None
        
        super().__init__(name, comment, tag=tag, _rupture=Section.CHAPTER, toc=True, **parameters)
        self.set_tag("Modules")
        
    @classmethod
    def FromInspect(cls, name: str, module_object: object) -> 'ModuleSection':
        """ Create a ModuleSection by inspecting a module object
        
        Arguments
        ---------
        - name : module name
        - module_object : the module to scan
        """
        
        assert(inspect.ismodule(module_object))
        
        package = module_object.__package__
        
        if package is None:
            print(f"Module {module_object} has no package, ignored...")
            return None
        
        is_folder = module_object.__name__ == module_object.__package__
        
        module_ = cls(name, comment=cls.get_doc(module_object), package=package, is_folder=is_folder)

        # ----------------------------------------------------------------------------------------------------
        # Loop on members
        
        for member_name, member in inspect.getmembers(module_object):
            
            # ----- By name
            
            if member_name in ['__weakref__']:
                continue
            
            # ----- A module

            elif inspect.ismodule(member):
                
                if member.__name__ != module_object.__name__ + '.' + member_name:
                    continue
                
                
                #if not member.__name__.startswith(module_object.__name__):
                #    continue   
                
                module_.add(member_name, ModuleSection.FromInspect(member_name, member))
                
            # ----- A class
            
            elif inspect.isclass(member):
                
                if member.__module__ != module_object.__name__:
                    continue
                
                module_.add(member_name, ClassSection.FromInspect(member_name, member))
                
            # ----- A Function
            
            elif inspect.isfunction(member):

                if member.__module__ != module_object.__name__:
                    continue
                    
                module_.add(member_name, FunctionSection.FromInspect(member_name, member))
                
            # ----- Global vars
            
            else:
                if member_name.startswith('__') and member_name.endswith('__'):
                    continue
                
                new_prop = PropertySection.FromStatic(member_name, member)
                
                prop = module_.get(member_name)
                if prop is None:
                    module_.add(member_name, new_prop)
                else:
                    prop.complete_with(new_prop)

        return module_

    # =============================================================================================================================
    # Regroup
    
    def regroup(self) -> None:
        
        for section in self.values():
            if section.is_hidden:
                continue

            if isinstance(section, ObjectSection):
                section.regroup()

            if section.tag != ["Modules", "Global variables", "Classes", "Functions"]:
                section.tag = "Miscellaneous"
            
        self.new_tag_group("Modules",          sort_sections=True, in_toc=False, navigation=True)
        self.new_tag_group("Global variables", sort_sections=True, in_toc=False, navigation=False)
        self.new_tag_group("Classes",          sort_sections=True, in_toc=False, navigation=True)
        self.new_tag_group("Functions",        sort_sections=True, in_toc=False, navigation=False)
        self.new_tag_group("Miscellaneous",    sort_sections=True, in_toc=False, navigation=False)
    
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
# Package documentation

class PackageDoc(Documentation):
    
    def __init__(self, package: object):
        """ Package documentation
        """
        
        # ----- Load the documentation
        
        super().__init__(ModuleSection.FromInspect(package.__name__, package))
        self.top_section.SEP = '.'
        self.top_section.DOT = None
        
        # ----- Modules and class names in modules
        
        self.modules = {}
        package_name = package.__package__
        
        for name, member in inspect.getmembers(package):
            
            if inspect.ismodule(member):
                if not member.__package__.startswith(package_name):
                    continue
                
                module_name = member.__package__[len(package_name)+1:]

                if module_name in self.modules:
                    continue
                
                self.modules[module_name] = []
                
            elif inspect.isclass(member):
                if not member.__module__.startswith(package_name):
                    continue
                
                module_name = member.__module__[len(package_name)+1:]
                
                if not module_name in self.modules:
                    self.modules[module_name] = []
                
                self.modules[module_name].append(name)
                
        # ------ All the exposed classes
        
        self.classes = {}
        for module_path, classes in self.modules.items():
            for class_name in classes:
                self.classes[class_name] = self.top_section[module_path + '.' + class_name]

        # ------ Let's hide non exposed classes
        
        all_classes = {c.name: c for c in self.top_section.find(tag="Classes", first=False)}
        for class_name, class_ in all_classes.items():
            if class_name not in self.classes:
                class_.hidden = True
                
        hidden_classes = {class_name: class_ for class_name, class_ in all_classes.items() if class_.hidden}
        
        # ------ We hide inheritance inside the hidden classes
        
        hidden_complete = []
        
        again = True
        wd   = 0
        while again: # Normally should work
            again = False
            completed  = []
            wd += 1
            for class_name, class_ in hidden_classes.items():
                
                class_.hide_inheritance(hidden_complete)
                
                complete = True
                for other_ in hidden_classes:
                    if other_.title in class_.bases:
                        complete = False
                        break
                        
                if complete:
                    completed.append(class_)
                else:
                    again = True
                
            for class_ in completed:
                hidden_complete.append(class_)
                del hidden_classes[class_.title]
                
            if wd > 100:
                print("COMPLETE", [class_.title for class_ in hidden_complete])
                print("NOT     ", [class_.title for class_ in hidden_classes])
                raise Exception("Algo error")
                
        # ----- Hide inheritance of exposed classes
        
        for class_ in self.classes.values():
            class_.hide_inheritance(hidden_complete)
            
    # ====================================================================================================
    # cook
    
    def cook(self) -> None:
        
        if self._cooked:
            return
        
        for cl in self.top_section.all_values():
            if cl.tag == "Classes":
                cl.complete_inheritance()
        
        self.top_section.regroup()
        
        super().cook()

class TestClass:
    def __init__(self, a: str, b: int =123, c: Optional[float] = None):
        """ Test class

        Just to test documentaton options

        """
        pass

    @classmethod
    def constructor(cls) -> 'TestClass':
        """ Test return TestClass
        """
        pass

    def test_func(self, a: Union[list, tuple, str]='Test', b: Optional[Union[List, Tuple, str]]='Test', c:int = 1) -> Any:
        """ Test method

        Arguments
        ---------
        - a : arg a description
        - b : arg b description
        - c (int) : arg c desciption
        """
        pass

    def test_func2(self) -> Any:
        """ Test method

        Returns
        -------
        - list : return comment
        """
        pass

# =============================================================================================================================
# Demo

def auto_gen(folder):

    # -----------------------------------------------------------------------------------------------------------------------------
    # Load the package

    print("Load package...")

    doc = PackageDoc(docgen)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Create documentation

    print("Create documentation files...")
    doc.create_documentation(folder)

    print("Done")





        
        
    




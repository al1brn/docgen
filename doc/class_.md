# Class_

Tree interface based on a dict

This class inherits from <!Tree> and dict. Direct children are managed from dict inheritance.

This implementation can be chosen when direct child keys must be unique and when there is no
particular need in controlling the order of the children.Tree interface based on a dict

This class inherits from <!Tree> and dict. Direct children are managed from dict inheritance.

This implementation can be chosen when direct child keys must be unique and when there is no
particular need in controlling the order of the children.

## Content


- A : [add](#add) :black_small_square: [all_count](#all_count) :black_small_square: [all_items](#all_items) :black_small_square: [all_paths](#all_paths) :black_small_square: [all_values](#all_values)
- C : [clear](#clear) :black_small_square: [copy](#copy) :black_small_square: [count](#count)
- D : [depth](#depth)
- F : [FromFile](#fromfile) :black_small_square: [FromInspect](#frominspect) :black_small_square: [find_key](#find_key) :black_small_square: [fromkeys](#fromkeys)
- G : [get](#get) :black_small_square: [get_child](#get_child) :black_small_square: [get_prop](#get_prop)
- I : [is_top](#is_top) :black_small_square: [items](#items)
- J : [join_keys](#join_keys)
- K : [key](#key) :black_small_square: [key_separator](#key_separator) :black_small_square: [keys](#keys)
- M : [meta](#meta)
- N : [new](#new)
- O : [obj_type](#obj_type)
- P : [parse_comment](#parse_comment) :black_small_square: [path](#path) :black_small_square: [pop](#pop) :black_small_square: [popitem](#popitem)
- S : [set_child](#set_child) :black_small_square: [setdefault](#setdefault) :black_small_square: [solve_path](#solve_path)
- T : [test](#test) :black_small_square: [top](#top)
- U : [update](#update)
- V : [values](#values)
- _ : [__class_getitem__](#__class_getitem__) :black_small_square: [__contains__](#__contains__) :black_small_square: [__delattr__](#__delattr__) :black_small_square: [__delitem__](#__delitem__) :black_small_square: [__dict__](#__dict__) :black_small_square: [__dir__](#__dir__) :black_small_square: [__doc__](#__doc__) :black_small_square: [__eq__](#__eq__) :black_small_square: [__format__](#__format__) :black_small_square: [__ge__](#__ge__) :black_small_square: [__getattribute__](#__getattribute__) :black_small_square: [__getstate__](#__getstate__) :black_small_square: [__gt__](#__gt__) :black_small_square: [__hash__](#__hash__) :black_small_square: [__init_subclass__](#__init_subclass__) :black_small_square: [__ior__](#__ior__) :black_small_square: [__le__](#__le__) :black_small_square: [__len__](#__len__) :black_small_square: [__lt__](#__lt__) :black_small_square: [__module__](#__module__) :black_small_square: [__ne__](#__ne__) :black_small_square: [__new__](#__new__) :black_small_square: [__or__](#__or__) :black_small_square: [__reduce__](#__reduce__) :black_small_square: [__reduce_ex__](#__reduce_ex__) :black_small_square: [__repr__](#__repr__) :black_small_square: [__reversed__](#__reversed__) :black_small_square: [__ror__](#__ror__) :black_small_square: [__setattr__](#__setattr__) :black_small_square: [__sizeof__](#__sizeof__) :black_small_square: [__str__](#__str__) :black_small_square: [__subclasshook__](#__subclasshook__) :black_small_square: [__weakref__](#__weakref__)



## Properties

### __class_getitem__


> type __class_getitem__ ( = <built-in method __class_getit...)



### __contains__


> type __contains__ ( = <method '__contains__' of 'dic...)



### __delattr__


> type __delattr__ ( = <slot wrapper '__delattr__' of...)



### __delitem__


> type __delitem__ ( = <slot wrapper '__delitem__' of...)



### __dict__


> type mappingproxy ( = {'__module__': '__main__', 'ob...)



### __dir__


> type __dir__ ( = <method '__dir__' of 'object' ...)



### __doc__


> type NoneType ( = None)



### __eq__


> type __eq__ ( = <slot wrapper '__eq__' of 'dic...)



### __format__


> type __format__ ( = <method '__format__' of 'objec...)



### __ge__


> type __ge__ ( = <slot wrapper '__ge__' of 'dic...)



### __getattribute__


> type __getattribute__ ( = <slot wrapper '__getattribute_...)



### __getstate__


> type __getstate__ ( = <method '__getstate__' of 'obj...)



### __gt__


> type __gt__ ( = <slot wrapper '__gt__' of 'dic...)



### __hash__


> type NoneType ( = None)



### __init_subclass__


> type __init_subclass__ ( = <built-in method __init_subcla...)



### __ior__


> type __ior__ ( = <slot wrapper '__ior__' of 'di...)



### __le__


> type __le__ ( = <slot wrapper '__le__' of 'dic...)



### __len__


> type __len__ ( = <slot wrapper '__len__' of 'di...)



### __lt__


> type __lt__ ( = <slot wrapper '__lt__' of 'dic...)



### __module__


> type str ( = __main__)



### __ne__


> type __ne__ ( = <slot wrapper '__ne__' of 'dic...)



### __new__


> type __new__ ( = <built-in method __new__ of ty...)



### __or__


> type __or__ ( = <slot wrapper '__or__' of 'dic...)



### __reduce__


> type __reduce__ ( = <method '__reduce__' of 'objec...)



### __reduce_ex__


> type __reduce_ex__ ( = <method '__reduce_ex__' of 'ob...)



### __repr__


> type __repr__ ( = <slot wrapper '__repr__' of 'd...)



### __reversed__


> type __reversed__ ( = <method '__reversed__' of 'dic...)



### __ror__


> type __ror__ ( = <slot wrapper '__ror__' of 'di...)



### __setattr__


> type __setattr__ ( = <slot wrapper '__setattr__' of...)



### __sizeof__


> type __sizeof__ ( = <method '__sizeof__' of 'dict'...)



### __subclasshook__


> type __subclasshook__ ( = <built-in method __subclasshoo...)



### __weakref__


> type __weakref__ ( = <attribute '__weakref__' of 'T...)



### all_count


> type property ( = <property object at 0x141878cc...)



### clear


> type clear ( = <method 'clear' of 'dict' obje...)



### copy


> type copy ( = <method 'copy' of 'dict' objec...)



### count


> type property ( = <property object at 0x14187b9c...)



### depth


> type property ( = <property object at 0x1418784a...)



### fromkeys


> type fromkeys ( = <built-in method fromkeys of t...)



### is_top


> type property ( = <property object at 0x1418799e...)



### items


> type items ( = <method 'items' of 'dict' obje...)



### key


> type property ( = <property object at 0x1418938d...)



### key_separator


> type property ( = <property object at 0x14187b51...)



### keys


> type keys ( = <method 'keys' of 'dict' objec...)



### obj_type


> type str ( = class)



### path


> type property ( = <property object at 0x14187a84...)



### pop


> type pop ( = <method 'pop' of 'dict' object...)



### popitem


> type popitem ( = <method 'popitem' of 'dict' ob...)



### setdefault


> type setdefault ( = <method 'setdefault' of 'dict'...)



### top


> type property ( = <property object at 0x141878e0...)



### update


> type update ( = <method 'update' of 'dict' obj...)



### values


> type values ( = <method 'values' of 'dict' obj...)



## Methods

### FromFile

----------



``` python
FromFile(folder, pattern='*.*', ignore=('.*', '_*'))
```

Read the content of a drive

This methods shows how to use method <#add> to recursively load folder files and sub folders.

Arguments:
- **folder** (_str_)
- **pattern** (_str or tuple of strs_ = *.*)
- **ignore** (_str or tuple of strs_ = ('.*', '_*'))



Returns:
- **Tree** : 



### FromInspect

----------



``` python
FromInspect(class_object, verbose=False)
```

Create an Class_ instance from a python class

> [!NOTE]
> If **name** argument is none, `object.__name__` is taken.

The method `__init__` is not stored in the <#members> dictionary but in <#_init> property.

> [!CAUTION]
> All dunder methods are ignored in this version

Arguments:
- **class_object** (_class_)
- **verbose** ( = False)



### __str__

----------



``` python
__str__(self)
```

Return str(self).

Arguments:
- **self**



### add

----------



``` python
add(self, path, node)
```

Add a new node at the path

This method calls <#set_child>.

Arguments:
- **self**
- **path** (_str_)
- **node** (_Tree_)



Returns:
- **Tree** : the node argument



### all_items

----------



``` python
all_items(self)
```

All items iterator

Iterate on all items in the folder and sub folders.

Arguments:
- **self**



Returns:
- **iterator** : 



### all_paths

----------



``` python
all_paths(self)
```

All paths iterator

Iterate on all paths in the folder and sub folders.

Arguments:
- **self**



Returns:
- **iterator** : 



### all_values

----------



``` python
all_values(self)
```

All values iterator

Iterate on all values in the folder and sub folders.

Arguments:
- **self**



Returns:
- **iterator** : 



### find_key

----------



``` python
find_key(self, *keys, first=False)
```

Find one or more keys in the tree.

Arguments:
- **self**
- **keys** (_list of strs_)
- **first** (_boolean_ = False)



Returns:
- **Tree** : on single tree if first is Trur



### get

----------



``` python
get(self, path, default=None)
```

Get the node at path

Arguments:
- **self**
- **path** (_str_)
- **default** (_Tree_ = None)



Returns:
- **Tree** : 



### get_child

----------



``` python
get_child(self, key)
```

Get a direct child by its key

Arguments:
- **self**
- **key**



### get_prop

----------



``` python
get_prop(self, prop_name, default=None)
```

Get an optional property

Arguments:
- **self**
- **prop_name** (_str_)
- **default** (_any_ = None)



Returns:
- **any** : the property or None if it doesn't exist



### join_keys

----------



``` python
join_keys(self, *keys)
```

Join keys to form a path

Joins the keys with the key separator avoiding double separators: `join_keys("AAA", "BBB")`
and `join_keys("AAA/", "BBB")` will both give `"AAA/BBB"`.

Arguments:
- **self**
- **keys**



Returns:
- **str** : key joined by key separator



### meta

----------



``` python
meta(self, meta_name, default=None)
```

Get a meta property

A meta property can be set in the comment with the syntax
```
 $ SET meta_name = value
```

Arguments:
- **self**
- **meta_name** (_str_)
- **default** (_any_ = None)



Returns:
- **any** : the meta property value or None if it doesn't exist



### new

----------



``` python
new(self, path, **kwargs)
```

Create a new node at the given path

The default implementation create a new node by calling the defaut constructors:
    
``` python
new_node = type(self)(**kwargs)
``` 

For a different behavior, either use `<#add>` method of overload this method.

Arguments:
- **self**
- **path** (_str_)
- **kwargs**



Returns:
- **Tree** : the created node



### parse_comment

----------



``` python
parse_comment(self)
```

Collect extra information from the comment

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

Arguments:
- **self**



### set_child

----------



``` python
set_child(self, key, child)
```

set a direct child by its key

Arguments:
- **self**
- **key**
- **child**



### solve_path

----------



``` python
solve_path(self, path)
```

Solve a path

Solve a path while possible.

Raises an error if more than one key remain unsolved after the last node.

Returns the last node which can be solved and the remaining key.

Raises:
- **KeyError** : 



Arguments:
- **self**
- **path** (_str_)



Returns:
- **couple** : not None Tree, remaining key or None if fully solved



### test

----------



``` python
test()
```

Perform basic tests
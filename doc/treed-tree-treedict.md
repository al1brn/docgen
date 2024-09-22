#TreeDict

Tree interface based on a dict

This class inherits from [Tree](treed-tree-treedict.md#tree) and dict. Direct children are managed from dict inheritance.

This implementation can be chosen when direct child keys must be unique and when there is no
particular need in controlling the order of the children.Tree interface based on a dict

This class inherits from [Tree](treed-tree-treedict.md#tree) and dict. Direct children are managed from dict inheritance.

This implementation can be chosen when direct child keys must be unique and when there is no
particular need in controlling the order of the children.

##Content

- [DOT](treed-tree-treedict.md#dot)
- [SEP](treed-tree-treedict.md#sep)
- [__class_getitem__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_)
- [__contains__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_\_)
- [__delattr__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_)
- [__delitem__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_)
- [__dict__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_)
- [__dir__](treed-tree-treedict.md#\_\_\_\_\_\_\_)
- [__doc__](treed-tree-treedict.md#\_\_\_\_\_\_\_)
- [__eq__](treed-tree-treedict.md#\_\_\_\_\_\_)
- [__format__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_)
- [__ge__](treed-tree-treedict.md#\_\_\_\_\_\_)
- [__getattribute__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_)
- [__getstate__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_\_)
- [__gt__](treed-tree-treedict.md#\_\_\_\_\_\_)
- [__hash__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_)
- [__init_subclass__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_)
- [__ior__](treed-tree-treedict.md#\_\_\_\_\_\_\_)
- [__le__](treed-tree-treedict.md#\_\_\_\_\_\_)
- [__len__](treed-tree-treedict.md#\_\_\_\_\_\_\_)
- [__lt__](treed-tree-treedict.md#\_\_\_\_\_\_)
- [__module__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_)
- [__ne__](treed-tree-treedict.md#\_\_\_\_\_\_)
- [__new__](treed-tree-treedict.md#\_\_\_\_\_\_\_)
- [__or__](treed-tree-treedict.md#\_\_\_\_\_\_)
- [__reduce__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_)
- [__reduce_ex__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_\_\_)
- [__repr__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_)
- [__reversed__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_\_)
- [__ror__](treed-tree-treedict.md#\_\_\_\_\_\_\_)
- [__setattr__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_)
- [__sizeof__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_)
- [__subclasshook__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_)
- [__weakref__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_)
- [all_count](treed-tree-treedict.md#all_count)
- [clear](treed-tree-treedict.md#clear)
- [copy](treed-tree-treedict.md#copy)
- [count](treed-tree-treedict.md#count)
- [depth](treed-tree-treedict.md#depth)
- [fromkeys](treed-tree-treedict.md#fromkeys)
- [is_top](treed-tree-treedict.md#is_top)
- [items](treed-tree-treedict.md#items)
- [key](treed-tree-treedict.md#key)
- [keys](treed-tree-treedict.md#keys)
- [path](treed-tree-treedict.md#path)
- [pop](treed-tree-treedict.md#pop)
- [popitem](treed-tree-treedict.md#popitem)
- [setdefault](treed-tree-treedict.md#setdefault)
- [top](treed-tree-treedict.md#top)
- [update](treed-tree-treedict.md#update)
- [values](treed-tree-treedict.md#values)
- [FromFile](treed-tree-treedict.md#fromfile)
- [FromInspect](treed-tree-treedict.md#frominspect)
- [Test](treed-tree-treedict.md#test)
- [__str__](treed-tree-treedict.md#\_\_\_\_\_\_\_)
- [add](treed-tree-treedict.md#add)
- [all_items](treed-tree-treedict.md#all_items)
- [all_paths](treed-tree-treedict.md#all_paths)
- [all_values](treed-tree-treedict.md#all_values)
- [create_path](treed-tree-treedict.md#create_path)
- [find](treed-tree-treedict.md#find)
- [get](treed-tree-treedict.md#get)
- [get_child](treed-tree-treedict.md#get_child)
- [join_keys](treed-tree-treedict.md#join_keys)
- [new](treed-tree-treedict.md#new)
- [new_paths](treed-tree-treedict.md#new_paths)
- [set_child](treed-tree-treedict.md#set_child)
- [solve_path](treed-tree-treedict.md#solve_path)
- [solve_to_missing](treed-tree-treedict.md#solve_to_missing)
- [test](treed-tree-treedict.md#test)


##Properties

###Content

- [DOT](treed-tree-treedict.md#dot)
- [SEP](treed-tree-treedict.md#sep)
- [__class_getitem__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_)
- [__contains__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_\_)
- [__delattr__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_)
- [__delitem__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_)
- [__dict__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_)
- [__dir__](treed-tree-treedict.md#\_\_\_\_\_\_\_)
- [__doc__](treed-tree-treedict.md#\_\_\_\_\_\_\_)
- [__eq__](treed-tree-treedict.md#\_\_\_\_\_\_)
- [__format__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_)
- [__ge__](treed-tree-treedict.md#\_\_\_\_\_\_)
- [__getattribute__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_)
- [__getstate__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_\_)
- [__gt__](treed-tree-treedict.md#\_\_\_\_\_\_)
- [__hash__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_)
- [__init_subclass__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_)
- [__ior__](treed-tree-treedict.md#\_\_\_\_\_\_\_)
- [__le__](treed-tree-treedict.md#\_\_\_\_\_\_)
- [__len__](treed-tree-treedict.md#\_\_\_\_\_\_\_)
- [__lt__](treed-tree-treedict.md#\_\_\_\_\_\_)
- [__module__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_)
- [__ne__](treed-tree-treedict.md#\_\_\_\_\_\_)
- [__new__](treed-tree-treedict.md#\_\_\_\_\_\_\_)
- [__or__](treed-tree-treedict.md#\_\_\_\_\_\_)
- [__reduce__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_)
- [__reduce_ex__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_\_\_)
- [__repr__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_)
- [__reversed__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_\_)
- [__ror__](treed-tree-treedict.md#\_\_\_\_\_\_\_)
- [__setattr__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_)
- [__sizeof__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_)
- [__subclasshook__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_)
- [__weakref__](treed-tree-treedict.md#\_\_\_\_\_\_\_\_\_\_\_)
- [all_count](treed-tree-treedict.md#all_count)
- [clear](treed-tree-treedict.md#clear)
- [copy](treed-tree-treedict.md#copy)
- [count](treed-tree-treedict.md#count)
- [depth](treed-tree-treedict.md#depth)
- [fromkeys](treed-tree-treedict.md#fromkeys)
- [is_top](treed-tree-treedict.md#is_top)
- [items](treed-tree-treedict.md#items)
- [key](treed-tree-treedict.md#key)
- [keys](treed-tree-treedict.md#keys)
- [path](treed-tree-treedict.md#path)
- [pop](treed-tree-treedict.md#pop)
- [popitem](treed-tree-treedict.md#popitem)
- [setdefault](treed-tree-treedict.md#setdefault)
- [top](treed-tree-treedict.md#top)
- [update](treed-tree-treedict.md#update)
- [values](treed-tree-treedict.md#values)


###DOT


> type str ( = .)



###SEP


> type str ( = /)



###\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_


> type __class_getitem__ ( = <built-in method __class_getit...)



###\_\_\_\_\_\_\_\_\_\_\_\_


> type __contains__ ( = <method '__contains__' of 'dic...)



###\_\_\_\_\_\_\_\_\_\_\_


> type __delattr__ ( = <slot wrapper '__delattr__' of...)



###\_\_\_\_\_\_\_\_\_\_\_


> type __delitem__ ( = <slot wrapper '__delitem__' of...)



###\_\_\_\_\_\_\_\_


> type mappingproxy ( = {'__module__': 'treedict.tree'...)



###\_\_\_\_\_\_\_


> type __dir__ ( = <method '__dir__' of 'object' ...)



###\_\_\_\_\_\_\_


> type str ( =  Tree interface based on a dic...)



###\_\_\_\_\_\_


> type __eq__ ( = <slot wrapper '__eq__' of 'dic...)



###\_\_\_\_\_\_\_\_\_\_


> type __format__ ( = <method '__format__' of 'objec...)



###\_\_\_\_\_\_


> type __ge__ ( = <slot wrapper '__ge__' of 'dic...)



###\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_


> type __getattribute__ ( = <slot wrapper '__getattribute_...)



###\_\_\_\_\_\_\_\_\_\_\_\_


> type __getstate__ ( = <method '__getstate__' of 'obj...)



###\_\_\_\_\_\_


> type __gt__ ( = <slot wrapper '__gt__' of 'dic...)



###\_\_\_\_\_\_\_\_


> type NoneType ( = None)



###\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_


> type __init_subclass__ ( = <built-in method __init_subcla...)



###\_\_\_\_\_\_\_


> type __ior__ ( = <slot wrapper '__ior__' of 'di...)



###\_\_\_\_\_\_


> type __le__ ( = <slot wrapper '__le__' of 'dic...)



###\_\_\_\_\_\_\_


> type __len__ ( = <slot wrapper '__len__' of 'di...)



###\_\_\_\_\_\_


> type __lt__ ( = <slot wrapper '__lt__' of 'dic...)



###\_\_\_\_\_\_\_\_\_\_


> type str ( = treedict.tree)



###\_\_\_\_\_\_


> type __ne__ ( = <slot wrapper '__ne__' of 'dic...)



###\_\_\_\_\_\_\_


> type __new__ ( = <built-in method __new__ of ty...)



###\_\_\_\_\_\_


> type __or__ ( = <slot wrapper '__or__' of 'dic...)



###\_\_\_\_\_\_\_\_\_\_


> type __reduce__ ( = <method '__reduce__' of 'objec...)



###\_\_\_\_\_\_\_\_\_\_\_\_\_


> type __reduce_ex__ ( = <method '__reduce_ex__' of 'ob...)



###\_\_\_\_\_\_\_\_


> type __repr__ ( = <slot wrapper '__repr__' of 'd...)



###\_\_\_\_\_\_\_\_\_\_\_\_


> type __reversed__ ( = <method '__reversed__' of 'dic...)



###\_\_\_\_\_\_\_


> type __ror__ ( = <slot wrapper '__ror__' of 'di...)



###\_\_\_\_\_\_\_\_\_\_\_


> type __setattr__ ( = <slot wrapper '__setattr__' of...)



###\_\_\_\_\_\_\_\_\_\_


> type __sizeof__ ( = <method '__sizeof__' of 'dict'...)



###\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_


> type __subclasshook__ ( = <built-in method __subclasshoo...)



###\_\_\_\_\_\_\_\_\_\_\_


> type __weakref__ ( = <attribute '__weakref__' of 'T...)



###all_count


> type property ( = <property object at 0x1786da07...)



###clear


> type clear ( = <method 'clear' of 'dict' obje...)



###copy


> type copy ( = <method 'copy' of 'dict' objec...)



###count


> type property ( = <property object at 0x1786dbe7...)



###depth


> type property ( = <property object at 0x1786db0b...)



###fromkeys


> type fromkeys ( = <built-in method fromkeys of t...)



###is_top


> type property ( = <property object at 0x1786d9fd...)



###items


> type items ( = <method 'items' of 'dict' obje...)



###key


> type property ( = <property object at 0x1786da3e...)



###keys


> type keys ( = <method 'keys' of 'dict' objec...)



###path


> type property ( = <property object at 0x1786da16...)



###pop


> type pop ( = <method 'pop' of 'dict' object...)



###popitem


> type popitem ( = <method 'popitem' of 'dict' ob...)



###setdefault


> type setdefault ( = <method 'setdefault' of 'dict'...)



###top


> type property ( = <property object at 0x1786dbbf...)



###update


> type update ( = <method 'update' of 'dict' obj...)



###values


> type values ( = <method 'values' of 'dict' obj...)



##Methods

###Content

- [FromFile](treed-tree-treedict.md#fromfile)
- [FromInspect](treed-tree-treedict.md#frominspect)
- [Test](treed-tree-treedict.md#test)
- [__str__](treed-tree-treedict.md#\_\_\_\_\_\_\_)
- [add](treed-tree-treedict.md#add)
- [all_items](treed-tree-treedict.md#all_items)
- [all_paths](treed-tree-treedict.md#all_paths)
- [all_values](treed-tree-treedict.md#all_values)
- [create_path](treed-tree-treedict.md#create_path)
- [find](treed-tree-treedict.md#find)
- [get](treed-tree-treedict.md#get)
- [get_child](treed-tree-treedict.md#get_child)
- [join_keys](treed-tree-treedict.md#join_keys)
- [new](treed-tree-treedict.md#new)
- [new_paths](treed-tree-treedict.md#new_paths)
- [set_child](treed-tree-treedict.md#set_child)
- [solve_path](treed-tree-treedict.md#solve_path)
- [solve_to_missing](treed-tree-treedict.md#solve_to_missing)
- [test](treed-tree-treedict.md#test)


###FromFile

----------



``` python
FromFile(folder, pattern='*.*', ignore=('.*', '_*'))
```

Read the content of a drive

This methods shows how to use method [add](#add) to recursively load folder files and sub folders.

Arguments:
- **folder** (_str_)
- **pattern** (_str or tuple of strs_ = *.*)
- **ignore** (_str or tuple of strs_ = ('.*', '_*'))



Returns:
- **Tree** : 



###FromInspect

----------



``` python
FromInspect(obj)
```

Load python module

Load module and module members using inspect

Arguments:
- **obj** (_any_)



Returns:
- **Tree** : 



###Test

----------



``` python
Test(**kwargs)
```

A tree for test

Arguments:
- **kwargs**



###\_\_\_\_\_\_\_

----------



``` python
__str__(self)
```

Return str(self).

Arguments:
- **self**



###add

----------



``` python
add(self, path, node, complete_path=False)
```

Add a new node at the path

This method calls [set_child](#set_child).

Arguments:
- **self**
- **path** (_str_)
- **node** (_Tree_)
- **complete_path** ( = False)



Returns:
- **Tree** : the node argument



###all_items

----------



``` python
all_items(self, include_self=False)
```

All items iterator

Iterate on all items in the folder and sub folders.

Arguments:
- **self**
- **include_self** ( = False)



Returns:
- **iterator** : 



###all_paths

----------



``` python
all_paths(self, include_self=False)
```

All paths iterator

Iterate on all paths in the folder and sub folders.

Arguments:
- **self**
- **include_self** ( = False)



Returns:
- **iterator** : 



###all_values

----------



``` python
all_values(self, include_self=False)
```

All values iterator

Iterate on all values in the folder and sub folders.

Arguments:
- **self**
- **include_self** ( = False)



Returns:
- **iterator** : 



###create_path

----------



``` python
create_path(self, *keys)
```

Create nodes in a path

Nodes are create by calling [new](#new) method.

Arguments:
- **self**
- **keys** (_list of strs_)



Returns:
- **Tree** : last created node



###find

----------



``` python
find(self, *keys, first=False, **criteria)
```

Find one or more keys in the tree.

Arguments:
- **self**
- **keys** (_list of strs_)
- **first** (_boolean_ = False)
- **criteria**



Returns:
- **Tree** : on single tree if first is Trur



###get

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



###get_child

----------



``` python
get_child(self, key)
```

Get a direct child by its key

Arguments:
- **self**
- **key**



###join_keys

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



###new

----------



``` python
new(self, path, complete_path=False, **kwargs)
```

Create a new node at the given path

The default implementation create a new node by calling the defaut constructor
and adding it by calling [add](#add):
    
``` python
return self.add(path, type(self)(**kwargs), complete_path=complete_path)
```

Raises:
- **PathError** : if nodes are missing in the path



Arguments:
- **self**
- **path** (_str_)
- **complete_path** (_set_ = False)
- **kwargs**



Returns:
- **Tree** : the created node



###new_paths

----------



``` python
new_paths(self, *paths, complete_path=False, **kwargs)
```

Create several nodes defined by their path

Basically, this method call [new](#new) for each provided path.

The following rules apply:            
- paths starting by '/' are created at top level
- paths starting by '.' are created at the *last created node* level
- paths starting by '..' are created at parent level of *last created node* level
- otherwise, nodes are created at at the node level

``` python
node = tree.new("MyNode")
node.new_paths("AAA", "BBB", "./under BBB", "../after 'under BBB'", "/After MyNode")
# - MyNode
#   - AAA
#   - BBB
#     - under BBB
#     - after 'under BBB'
# - After MyNode
```

Arguments:
- **self**
- **paths** (_list of str_)
- **complete_path** (_bool_ = False)
- **kwargs**



Returns:
- **Tree** : the created child



###set_child

----------



``` python
set_child(self, key, child, index=None)
```

set a direct child by its key

Arguments:
- **self**
- **key**
- **child**
- **index** ( = None)



###solve_path

----------



``` python
solve_path(self, path, complete_path=False)
```

Solve a path

Returns the node corresponding to the path.

If it doesn't exist, two cases are possible:
- only the last key in the path is missing: the methods return the parent
  and the missing key
- an intermediary node is missing: the methods raises an error or creates
  the missing nodes depending on the arguments **complete_path**.
  
> [!NOTE]
> Missing nodes in the path are created with method [create_path](#create_path)

Raises:
- **PathError** : if the path can't be solved up to the last, or last but one



Arguments:
- **self**
- **path** (_str_)
- **complete_path** (_bool_ = False)



Returns:
- **Tree** : (found node, None) or (parent node, missing key)



###solve_to_missing

----------



``` python
solve_to_missing(self, path)
```

Solve a path to missing keys

Solve a path, return the existing node and the list of non existing keys.

Raises:
- **PathError** : if path is incorrect



Arguments:
- **self**
- **path** (_str_)



Returns:
- **node** : last existing node, list of missing keys



###test

----------



``` python
test()
```

Perform basic tests
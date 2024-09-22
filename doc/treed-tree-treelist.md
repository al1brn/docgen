#TreeList

Tree interface based on a list

This class inherits from [Tree](treed-tree-treelist.md#tree) and list. Direct children are store in the list.

Several children can share the same key.

This implementation can be chosen when direct children can share a same key and / or when there is
a need to control the order of the childrenTree interface based on a list

This class inherits from [Tree](treed-tree-treelist.md#tree) and list. Direct children are store in the list.

Several children can share the same key.

This implementation can be chosen when direct children can share a same key and / or when there is
a need to control the order of the children

##Content

- [DOT](treed-tree-treelist.md#dot)
- [SEP](treed-tree-treelist.md#sep)
- [__add__](treed-tree-treelist.md#\__add__)
- [__class_getitem__](treed-tree-treelist.md#\__class_getitem__)
- [__contains__](treed-tree-treelist.md#\__contains__)
- [__delattr__](treed-tree-treelist.md#\__delattr__)
- [__delitem__](treed-tree-treelist.md#\__delitem__)
- [__dict__](treed-tree-treelist.md#\__dict__)
- [__dir__](treed-tree-treelist.md#\__dir__)
- [__doc__](treed-tree-treelist.md#\__doc__)
- [__eq__](treed-tree-treelist.md#\__eq__)
- [__format__](treed-tree-treelist.md#\__format__)
- [__ge__](treed-tree-treelist.md#\__ge__)
- [__getattribute__](treed-tree-treelist.md#\__getattribute__)
- [__getstate__](treed-tree-treelist.md#\__getstate__)
- [__gt__](treed-tree-treelist.md#\__gt__)
- [__hash__](treed-tree-treelist.md#\__hash__)
- [__iadd__](treed-tree-treelist.md#\__iadd__)
- [__imul__](treed-tree-treelist.md#\__imul__)
- [__init_subclass__](treed-tree-treelist.md#\__init_subclass__)
- [__le__](treed-tree-treelist.md#\__le__)
- [__len__](treed-tree-treelist.md#\__len__)
- [__lt__](treed-tree-treelist.md#\__lt__)
- [__module__](treed-tree-treelist.md#\__module__)
- [__mul__](treed-tree-treelist.md#\__mul__)
- [__ne__](treed-tree-treelist.md#\__ne__)
- [__new__](treed-tree-treelist.md#\__new__)
- [__reduce__](treed-tree-treelist.md#\__reduce__)
- [__reduce_ex__](treed-tree-treelist.md#\__reduce_ex__)
- [__repr__](treed-tree-treelist.md#\__repr__)
- [__reversed__](treed-tree-treelist.md#\__reversed__)
- [__rmul__](treed-tree-treelist.md#\__rmul__)
- [__setattr__](treed-tree-treelist.md#\__setattr__)
- [__sizeof__](treed-tree-treelist.md#\__sizeof__)
- [__subclasshook__](treed-tree-treelist.md#\__subclasshook__)
- [__weakref__](treed-tree-treelist.md#\__weakref__)
- [all_count](treed-tree-treelist.md#all_count)
- [append](treed-tree-treelist.md#append)
- [clear](treed-tree-treelist.md#clear)
- [copy](treed-tree-treelist.md#copy)
- [count](treed-tree-treelist.md#count)
- [depth](treed-tree-treelist.md#depth)
- [extend](treed-tree-treelist.md#extend)
- [index](treed-tree-treelist.md#index)
- [insert](treed-tree-treelist.md#insert)
- [is_top](treed-tree-treelist.md#is_top)
- [path](treed-tree-treelist.md#path)
- [pop](treed-tree-treelist.md#pop)
- [remove](treed-tree-treelist.md#remove)
- [reverse](treed-tree-treelist.md#reverse)
- [sort](treed-tree-treelist.md#sort)
- [top](treed-tree-treelist.md#top)
- [FromFile](treed-tree-treelist.md#fromfile)
- [FromInspect](treed-tree-treelist.md#frominspect)
- [Test](treed-tree-treelist.md#test)
- [__str__](treed-tree-treelist.md#\__str__)
- [add](treed-tree-treelist.md#add)
- [all_items](treed-tree-treelist.md#all_items)
- [all_paths](treed-tree-treelist.md#all_paths)
- [all_values](treed-tree-treelist.md#all_values)
- [create_path](treed-tree-treelist.md#create_path)
- [find](treed-tree-treelist.md#find)
- [get](treed-tree-treelist.md#get)
- [get_child](treed-tree-treelist.md#get_child)
- [items](treed-tree-treelist.md#items)
- [join_keys](treed-tree-treelist.md#join_keys)
- [keys](treed-tree-treelist.md#keys)
- [new](treed-tree-treelist.md#new)
- [new_paths](treed-tree-treelist.md#new_paths)
- [set_child](treed-tree-treelist.md#set_child)
- [solve_path](treed-tree-treelist.md#solve_path)
- [solve_to_missing](treed-tree-treelist.md#solve_to_missing)
- [test](treed-tree-treelist.md#test)
- [values](treed-tree-treelist.md#values)


##Properties

###Content

- [DOT](treed-tree-treelist.md#dot)
- [SEP](treed-tree-treelist.md#sep)
- [__add__](treed-tree-treelist.md#\__add__)
- [__class_getitem__](treed-tree-treelist.md#\__class_getitem__)
- [__contains__](treed-tree-treelist.md#\__contains__)
- [__delattr__](treed-tree-treelist.md#\__delattr__)
- [__delitem__](treed-tree-treelist.md#\__delitem__)
- [__dict__](treed-tree-treelist.md#\__dict__)
- [__dir__](treed-tree-treelist.md#\__dir__)
- [__doc__](treed-tree-treelist.md#\__doc__)
- [__eq__](treed-tree-treelist.md#\__eq__)
- [__format__](treed-tree-treelist.md#\__format__)
- [__ge__](treed-tree-treelist.md#\__ge__)
- [__getattribute__](treed-tree-treelist.md#\__getattribute__)
- [__getstate__](treed-tree-treelist.md#\__getstate__)
- [__gt__](treed-tree-treelist.md#\__gt__)
- [__hash__](treed-tree-treelist.md#\__hash__)
- [__iadd__](treed-tree-treelist.md#\__iadd__)
- [__imul__](treed-tree-treelist.md#\__imul__)
- [__init_subclass__](treed-tree-treelist.md#\__init_subclass__)
- [__le__](treed-tree-treelist.md#\__le__)
- [__len__](treed-tree-treelist.md#\__len__)
- [__lt__](treed-tree-treelist.md#\__lt__)
- [__module__](treed-tree-treelist.md#\__module__)
- [__mul__](treed-tree-treelist.md#\__mul__)
- [__ne__](treed-tree-treelist.md#\__ne__)
- [__new__](treed-tree-treelist.md#\__new__)
- [__reduce__](treed-tree-treelist.md#\__reduce__)
- [__reduce_ex__](treed-tree-treelist.md#\__reduce_ex__)
- [__repr__](treed-tree-treelist.md#\__repr__)
- [__reversed__](treed-tree-treelist.md#\__reversed__)
- [__rmul__](treed-tree-treelist.md#\__rmul__)
- [__setattr__](treed-tree-treelist.md#\__setattr__)
- [__sizeof__](treed-tree-treelist.md#\__sizeof__)
- [__subclasshook__](treed-tree-treelist.md#\__subclasshook__)
- [__weakref__](treed-tree-treelist.md#\__weakref__)
- [all_count](treed-tree-treelist.md#all_count)
- [append](treed-tree-treelist.md#append)
- [clear](treed-tree-treelist.md#clear)
- [copy](treed-tree-treelist.md#copy)
- [count](treed-tree-treelist.md#count)
- [depth](treed-tree-treelist.md#depth)
- [extend](treed-tree-treelist.md#extend)
- [index](treed-tree-treelist.md#index)
- [insert](treed-tree-treelist.md#insert)
- [is_top](treed-tree-treelist.md#is_top)
- [path](treed-tree-treelist.md#path)
- [pop](treed-tree-treelist.md#pop)
- [remove](treed-tree-treelist.md#remove)
- [reverse](treed-tree-treelist.md#reverse)
- [sort](treed-tree-treelist.md#sort)
- [top](treed-tree-treelist.md#top)


###DOT


> type str ( = .)



###SEP


> type str ( = /)



###\__add__


> type __add__ ( = <slot wrapper '__add__' of 'li...)



###\__class_getitem__


> type __class_getitem__ ( = <built-in method __class_getit...)



###\__contains__


> type __contains__ ( = <slot wrapper '__contains__' o...)



###\__delattr__


> type __delattr__ ( = <slot wrapper '__delattr__' of...)



###\__delitem__


> type __delitem__ ( = <slot wrapper '__delitem__' of...)



###\__dict__


> type mappingproxy ( = {'__module__': 'treedict.tree'...)



###\__dir__


> type __dir__ ( = <method '__dir__' of 'object' ...)



###\__doc__


> type str ( =  Tree interface based on a lis...)



###\__eq__


> type __eq__ ( = <slot wrapper '__eq__' of 'lis...)



###\__format__


> type __format__ ( = <method '__format__' of 'objec...)



###\__ge__


> type __ge__ ( = <slot wrapper '__ge__' of 'lis...)



###\__getattribute__


> type __getattribute__ ( = <slot wrapper '__getattribute_...)



###\__getstate__


> type __getstate__ ( = <method '__getstate__' of 'obj...)



###\__gt__


> type __gt__ ( = <slot wrapper '__gt__' of 'lis...)



###\__hash__


> type NoneType ( = None)



###\__iadd__


> type __iadd__ ( = <slot wrapper '__iadd__' of 'l...)



###\__imul__


> type __imul__ ( = <slot wrapper '__imul__' of 'l...)



###\__init_subclass__


> type __init_subclass__ ( = <built-in method __init_subcla...)



###\__le__


> type __le__ ( = <slot wrapper '__le__' of 'lis...)



###\__len__


> type __len__ ( = <slot wrapper '__len__' of 'li...)



###\__lt__


> type __lt__ ( = <slot wrapper '__lt__' of 'lis...)



###\__module__


> type str ( = treedict.tree)



###\__mul__


> type __mul__ ( = <slot wrapper '__mul__' of 'li...)



###\__ne__


> type __ne__ ( = <slot wrapper '__ne__' of 'lis...)



###\__new__


> type __new__ ( = <built-in method __new__ of ty...)



###\__reduce__


> type __reduce__ ( = <method '__reduce__' of 'objec...)



###\__reduce_ex__


> type __reduce_ex__ ( = <method '__reduce_ex__' of 'ob...)



###\__repr__


> type __repr__ ( = <slot wrapper '__repr__' of 'l...)



###\__reversed__


> type __reversed__ ( = <method '__reversed__' of 'lis...)



###\__rmul__


> type __rmul__ ( = <slot wrapper '__rmul__' of 'l...)



###\__setattr__


> type __setattr__ ( = <slot wrapper '__setattr__' of...)



###\__sizeof__


> type __sizeof__ ( = <method '__sizeof__' of 'list'...)



###\__subclasshook__


> type __subclasshook__ ( = <built-in method __subclasshoo...)



###\__weakref__


> type __weakref__ ( = <attribute '__weakref__' of 'T...)



###all_count


> type property ( = <property object at 0x17853aa7...)



###append


> type append ( = <method 'append' of 'list' obj...)



###clear


> type clear ( = <method 'clear' of 'list' obje...)



###copy


> type copy ( = <method 'copy' of 'list' objec...)



###count


> type property ( = <property object at 0x17853962...)



###depth


> type property ( = <property object at 0x17853903...)



###extend


> type extend ( = <method 'extend' of 'list' obj...)



###index


> type index ( = <method 'index' of 'list' obje...)



###insert


> type insert ( = <method 'insert' of 'list' obj...)



###is_top


> type property ( = <property object at 0x17853bd8...)



###path


> type property ( = <property object at 0x17853ac5...)



###pop


> type pop ( = <method 'pop' of 'list' object...)



###remove


> type remove ( = <method 'remove' of 'list' obj...)



###reverse


> type reverse ( = <method 'reverse' of 'list' ob...)



###sort


> type sort ( = <method 'sort' of 'list' objec...)



###top


> type property ( = <property object at 0x178538ae...)



##Methods

###Content

- [FromFile](treed-tree-treelist.md#fromfile)
- [FromInspect](treed-tree-treelist.md#frominspect)
- [Test](treed-tree-treelist.md#test)
- [__str__](treed-tree-treelist.md#\__str__)
- [add](treed-tree-treelist.md#add)
- [all_items](treed-tree-treelist.md#all_items)
- [all_paths](treed-tree-treelist.md#all_paths)
- [all_values](treed-tree-treelist.md#all_values)
- [create_path](treed-tree-treelist.md#create_path)
- [find](treed-tree-treelist.md#find)
- [get](treed-tree-treelist.md#get)
- [get_child](treed-tree-treelist.md#get_child)
- [items](treed-tree-treelist.md#items)
- [join_keys](treed-tree-treelist.md#join_keys)
- [keys](treed-tree-treelist.md#keys)
- [new](treed-tree-treelist.md#new)
- [new_paths](treed-tree-treelist.md#new_paths)
- [set_child](treed-tree-treelist.md#set_child)
- [solve_path](treed-tree-treelist.md#solve_path)
- [solve_to_missing](treed-tree-treelist.md#solve_to_missing)
- [test](treed-tree-treelist.md#test)
- [values](treed-tree-treelist.md#values)


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



###\__str__

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



###items

----------



``` python
items(self)
```

Iterate on (key, value) pais

Arguments:
- **self**



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



###keys

----------



``` python
keys(self)
```

Iterate on keys

Arguments:
- **self**



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

###values

----------



``` python
values(self)
```

Iterate on childs

Arguments:
- **self**


# TreeList

Tree interface based on a list

This class inherits from [Tree](treed-tree-treelist.md#tree) and list. Direct children are store in the list.

Several children can share the same key.

This implementation can be chosen when direct children can share a same key and / or when there is
a need to control the order of the childrenTree interface based on a list

This class inherits from [Tree](treed-tree-treelist.md#tree) and list. Direct children are store in the list.

Several children can share the same key.

This implementation can be chosen when direct children can share a same key and / or when there is
a need to control the order of the children

### Inherited

list.__add__ :white_medium_small_square: list.__contains__ :white_medium_small_square: list.__delitem__ :white_medium_small_square: list.__eq__ :white_medium_small_square: list.__ge__ :white_medium_small_square: list.__getattribute__ :white_medium_small_square: list.__gt__ :white_medium_small_square: list.__iadd__ :white_medium_small_square: list.__imul__ :white_medium_small_square: list.__le__ :white_medium_small_square: list.__len__ :white_medium_small_square: list.__lt__ :white_medium_small_square: list.__mul__ :white_medium_small_square: list.__ne__ :white_medium_small_square: list.__repr__ :white_medium_small_square: list.__reversed__ :white_medium_small_square: list.__rmul__ :white_medium_small_square: list.__sizeof__ :white_medium_small_square: TreeList.__weakref__ :white_medium_small_square: list.append :white_medium_small_square: list.clear :white_medium_small_square: list.copy :white_medium_small_square: list.extend :white_medium_small_square: list.index :white_medium_small_square: list.insert :white_medium_small_square: list.pop :white_medium_small_square: list.remove :white_medium_small_square: list.reverse :white_medium_small_square: list.sort :white_medium_small_square: 

## Content

- [DOT](treed-tree-treelist.md#dot)
- [SEP](treed-tree-treelist.md#sep)
- [\_\_class_getitem__](treed-tree-treelist.md#__class_getitem__)
- [\_\_dict__](treed-tree-treelist.md#__dict__)
- [\_\_doc__](treed-tree-treelist.md#__doc__)
- [\_\_hash__](treed-tree-treelist.md#__hash__)
- [\_\_init_subclass__](treed-tree-treelist.md#__init_subclass__)
- [\_\_module__](treed-tree-treelist.md#__module__)
- [\_\_new__](treed-tree-treelist.md#__new__)
- [\_\_subclasshook__](treed-tree-treelist.md#__subclasshook__)
- [all_count](treed-tree-treelist.md#all_count)
- [count](treed-tree-treelist.md#count)
- [depth](treed-tree-treelist.md#depth)
- [is_top](treed-tree-treelist.md#is_top)
- [path](treed-tree-treelist.md#path)
- [top](treed-tree-treelist.md#top)
- [FromFile](treed-tree-treelist.md#fromfile)
- [FromInspect](treed-tree-treelist.md#frominspect)
- [Test](treed-tree-treelist.md#test)
- [\_\_str__](treed-tree-treelist.md#__str__)
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


## Properties

### Content

- [DOT](treed-tree-treelist.md#dot)
- [SEP](treed-tree-treelist.md#sep)
- [\_\_class_getitem__](treed-tree-treelist.md#__class_getitem__)
- [\_\_dict__](treed-tree-treelist.md#__dict__)
- [\_\_doc__](treed-tree-treelist.md#__doc__)
- [\_\_hash__](treed-tree-treelist.md#__hash__)
- [\_\_init_subclass__](treed-tree-treelist.md#__init_subclass__)
- [\_\_module__](treed-tree-treelist.md#__module__)
- [\_\_new__](treed-tree-treelist.md#__new__)
- [\_\_subclasshook__](treed-tree-treelist.md#__subclasshook__)
- [all_count](treed-tree-treelist.md#all_count)
- [count](treed-tree-treelist.md#count)
- [depth](treed-tree-treelist.md#depth)
- [is_top](treed-tree-treelist.md#is_top)
- [path](treed-tree-treelist.md#path)
- [top](treed-tree-treelist.md#top)


### DOT


> type str ( = .)



### SEP


> type str ( = /)



### \_\_class_getitem__


> type __class_getitem__ ( = <built-in method __class_getit...)



### \_\_dict__


> type mappingproxy ( = {'__module__': 'treedict.tree'...)



### \_\_doc__


> type str ( =  Tree interface based on a lis...)



### \_\_hash__


> type NoneType ( = None)



### \_\_init_subclass__


> type __init_subclass__ ( = <built-in method __init_subcla...)



### \_\_module__


> type str ( = treedict.tree)



### \_\_new__


> type __new__ ( = <built-in method __new__ of ty...)



### \_\_subclasshook__


> type __subclasshook__ ( = <built-in method __subclasshoo...)



### all_count


> type property ( = <property object at 0x178e99df...)



### count


> type property ( = <property object at 0x178e9b5b...)



### depth


> type property ( = <property object at 0x178e995d...)



### is_top


> type property ( = <property object at 0x178e99ee...)



### path


> type property ( = <property object at 0x178e9b06...)



### top


> type property ( = <property object at 0x178e998a...)



## Methods

### Content

- [FromFile](treed-tree-treelist.md#fromfile)
- [FromInspect](treed-tree-treelist.md#frominspect)
- [Test](treed-tree-treelist.md#test)
- [\_\_str__](treed-tree-treelist.md#__str__)
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


----------
### FromFile



``` python
FromFile(folder, pattern='*.*', ignore=('.*', '_*'))
```

Read the content of a drive

This methods shows how to use method [add](#add) to recursively load folder files and sub folders.

#### Arguments:
- **folder** (_str_)
- **pattern** (_str or tuple of strs_ = *.*)
- **ignore** (_str or tuple of strs_ = ('.*', '_*'))



#### Returns:
- **Tree** : 



----------
### FromInspect



``` python
FromInspect(obj)
```

Load python module

Load module and module members using inspect

#### Arguments:
- **obj** (_any_)



#### Returns:
- **Tree** : 



----------
### Test



``` python
Test(**kwargs)
```

A tree for test

#### Arguments:
- **kwargs**



----------
### \_\_str__



``` python
__str__(self)
```

Return str(self).

#### Arguments:
- **self**



----------
### add



``` python
add(self, path, node, complete_path=False)
```

Add a new node at the path

This method calls [set_child](#set_child).

#### Arguments:
- **self**
- **path** (_str_)
- **node** (_Tree_)
- **complete_path** ( = False)



#### Returns:
- **Tree** : the node argument



----------
### all_items



``` python
all_items(self, include_self=False)
```

All items iterator

Iterate on all items in the folder and sub folders.

#### Arguments:
- **self**
- **include_self** ( = False)



#### Returns:
- **iterator** : 



----------
### all_paths



``` python
all_paths(self, include_self=False)
```

All paths iterator

Iterate on all paths in the folder and sub folders.

#### Arguments:
- **self**
- **include_self** ( = False)



#### Returns:
- **iterator** : 



----------
### all_values



``` python
all_values(self, include_self=False)
```

All values iterator

Iterate on all values in the folder and sub folders.

#### Arguments:
- **self**
- **include_self** ( = False)



#### Returns:
- **iterator** : 



----------
### create_path



``` python
create_path(self, *keys)
```

Create nodes in a path

Nodes are create by calling [new](#new) method.

#### Arguments:
- **self**
- **keys** (_list of strs_)



#### Returns:
- **Tree** : last created node



----------
### find



``` python
find(self, *keys, first=False, **criteria)
```

Find one or more keys in the tree.

#### Arguments:
- **self**
- **keys** (_list of strs_)
- **first** (_boolean_ = False)
- **criteria**



#### Returns:
- **Tree** : on single tree if first is Trur



----------
### get



``` python
get(self, path, default=None)
```

Get the node at path

#### Arguments:
- **self**
- **path** (_str_)
- **default** (_Tree_ = None)



#### Returns:
- **Tree** : 



----------
### get_child



``` python
get_child(self, key)
```

Get a direct child by its key

#### Arguments:
- **self**
- **key**



----------
### items



``` python
items(self)
```

Iterate on (key, value) pais

#### Arguments:
- **self**



----------
### join_keys



``` python
join_keys(self, *keys)
```

Join keys to form a path

Joins the keys with the key separator avoiding double separators: `join_keys("AAA", "BBB")`
and `join_keys("AAA/", "BBB")` will both give `"AAA/BBB"`.

#### Arguments:
- **self**
- **keys**



#### Returns:
- **str** : key joined by key separator



----------
### keys



``` python
keys(self)
```

Iterate on keys

#### Arguments:
- **self**



----------
### new



``` python
new(self, path, complete_path=False, **kwargs)
```

Create a new node at the given path

The default implementation create a new node by calling the defaut constructor
and adding it by calling [add](#add):
    
``` python
return self.add(path, type(self)(**kwargs), complete_path=complete_path)
```

#### Raises:
- **PathError** : if nodes are missing in the path



#### Arguments:
- **self**
- **path** (_str_)
- **complete_path** (_set_ = False)
- **kwargs**



#### Returns:
- **Tree** : the created node



----------
### new_paths



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

#### Arguments:
- **self**
- **paths** (_list of str_)
- **complete_path** (_bool_ = False)
- **kwargs**



#### Returns:
- **Tree** : the created child



----------
### set_child



``` python
set_child(self, key, child, index=None)
```

set a direct child by its key

#### Arguments:
- **self**
- **key**
- **child**
- **index** ( = None)



----------
### solve_path



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

#### Raises:
- **PathError** : if the path can't be solved up to the last, or last but one



#### Arguments:
- **self**
- **path** (_str_)
- **complete_path** (_bool_ = False)



#### Returns:
- **Tree** : (found node, None) or (parent node, missing key)



----------
### solve_to_missing



``` python
solve_to_missing(self, path)
```

Solve a path to missing keys

Solve a path, return the existing node and the list of non existing keys.

#### Raises:
- **PathError** : if path is incorrect



#### Arguments:
- **self**
- **path** (_str_)



#### Returns:
- **node** : last existing node, list of missing keys



----------
### test



``` python
test()
```

Perform basic tests

----------
### values



``` python
values(self)
```

Iterate on childs

#### Arguments:
- **self**


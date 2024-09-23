# TreeDict



``` python
TreeDict()
```

Tree interface based on a dict

This class inherits from [Tree](treed-tree-treedict.md#tree) and dict. Direct children are managed from dict inheritance.

This implementation can be chosen when direct child keys must be unique and when there is no
particular need in controlling the order of the children.

#### Arguments:
- **self**



### Inherited

dict.\_\_contains__ :black_small_square: dict.\_\_delitem__ :black_small_square: dict.\_\_eq__ :black_small_square: dict.\_\_ge__ :black_small_square: dict.\_\_getattribute__ :black_small_square: dict.\_\_gt__ :black_small_square: dict.\_\_ior__ :black_small_square: dict.\_\_le__ :black_small_square: dict.\_\_len__ :black_small_square: dict.\_\_lt__ :black_small_square: dict.\_\_ne__ :black_small_square: dict.\_\_or__ :black_small_square: dict.\_\_repr__ :black_small_square: dict.\_\_reversed__ :black_small_square: dict.\_\_ror__ :black_small_square: dict.\_\_sizeof__ :black_small_square: dict.clear :black_small_square: dict.copy :black_small_square: dict.items :black_small_square: dict.keys :black_small_square: dict.pop :black_small_square: dict.popitem :black_small_square: dict.setdefault :black_small_square: dict.update :black_small_square: dict.values :black_small_square: 

## Content

- **A** : [add](treed-tree-treedict.md#add) :white_medium_small_square: [all_count](treed-tree-treedict.md#all_count) :white_medium_small_square: [all_items](treed-tree-treedict.md#all_items) :white_medium_small_square: [all_paths](treed-tree-treedict.md#all_paths) :white_medium_small_square: [all_values](treed-tree-treedict.md#all_values)
- **C** : [count](treed-tree-treedict.md#count) :white_medium_small_square: [create_path](treed-tree-treedict.md#create_path)
- **D** : [depth](treed-tree-treedict.md#depth) :white_medium_small_square: [DOT](treed-tree-treedict.md#dot)
- **F** : [find](treed-tree-treedict.md#find) :white_medium_small_square: [FromFile](treed-tree-treedict.md#fromfile) :white_medium_small_square: [FromInspect](treed-tree-treedict.md#frominspect)
- **G** : [get](treed-tree-treedict.md#get) :white_medium_small_square: [get_child](treed-tree-treedict.md#get_child)
- **I** : [is_top](treed-tree-treedict.md#is_top)
- **J** : [join_keys](treed-tree-treedict.md#join_keys)
- **K** : [key](treed-tree-treedict.md#key)
- **N** : [new](treed-tree-treedict.md#new) :white_medium_small_square: [new_paths](treed-tree-treedict.md#new_paths)
- **P** : [path](treed-tree-treedict.md#path)
- **S** : [SEP](treed-tree-treedict.md#sep) :white_medium_small_square: [set_child](treed-tree-treedict.md#set_child) :white_medium_small_square: [solve_path](treed-tree-treedict.md#solve_path) :white_medium_small_square: [solve_to_missing](treed-tree-treedict.md#solve_to_missing)
- **T** : [top](treed-tree-treedict.md#top)



## Properties

### all_count

> TYPE: **int**

Total number of children

### count

> TYPE: **int**

Number of direct children, equivalent to `len(self)`

### depth

> TYPE: **int**

Distance to the top (0 for top section)

### DOT

> TYPE: **str**<br> DEFAULT: **.**



### is_top

> TYPE: **bool**

True if owner is None

### key

> TYPE: **str** , None for top node

Get the key

In a **TreeDict**, the **key** is known by the parent. A node can retrieve it
by searching for itself in the direct children of its parent.

To make this process more efficient, **key** is cached by default in
hidden property **_key**.

### path

> TYPE: **str**

Node path up to the top node

### SEP

> TYPE: **str**<br> DEFAULT: **/**



### top

> TYPE: **Section**

Get the topmost section

## Methods

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


# TreeList



``` python
TreeList()
```

Tree interface based on a list

This class inherits from [Tree](treed-tree-tree.md) and list. Direct children are store in the list.

Several children can share the same key.

This implementation can be chosen when direct children can share a same key and / or when there is
a need to control the order of the children

### Inherited

list.\_\_add__ :black_small_square: list.\_\_contains__ :black_small_square: list.\_\_delitem__ :black_small_square: list.\_\_eq__ :black_small_square: list.\_\_ge__ :black_small_square: list.\_\_getattribute__ :black_small_square: list.\_\_gt__ :black_small_square: list.\_\_iadd__ :black_small_square: list.\_\_imul__ :black_small_square: list.\_\_le__ :black_small_square: list.\_\_len__ :black_small_square: list.\_\_lt__ :black_small_square: list.\_\_mul__ :black_small_square: list.\_\_ne__ :black_small_square: list.\_\_repr__ :black_small_square: list.\_\_reversed__ :black_small_square: list.\_\_rmul__ :black_small_square: list.\_\_sizeof__ :black_small_square: list.append :black_small_square: list.clear :black_small_square: list.copy :black_small_square: list.extend :black_small_square: list.index :black_small_square: list.insert :black_small_square: list.pop :black_small_square: list.remove :black_small_square: list.reverse :black_small_square: list.sort :black_small_square: 

## Content

- **A** : [add](treed-tree-treelist.md#add) :black_small_square: [all_count](treed-tree-treelist.md#all_count) :black_small_square: [all_items](treed-tree-treelist.md#all_items) :black_small_square: [all_paths](treed-tree-treelist.md#all_paths) :black_small_square: [all_values](treed-tree-treelist.md#all_values)
- **C** : [count](treed-tree-treelist.md#count) :black_small_square: [create_path](treed-tree-treelist.md#create_path)
- **D** : [depth](treed-tree-treelist.md#depth) :black_small_square: [DOT](treed-tree-treelist.md#dot)
- **F** : [find](treed-tree-treelist.md#find) :black_small_square: [FromFile](treed-tree-treelist.md#fromfile) :black_small_square: [FromInspect](treed-tree-treelist.md#frominspect)
- **G** : [get](treed-tree-treelist.md#get) :black_small_square: [get_child](treed-tree-treelist.md#get_child)
- **I** : [is_top](treed-tree-treelist.md#is_top) :black_small_square: [items](treed-tree-treelist.md#items)
- **J** : [join_keys](treed-tree-treelist.md#join_keys)
- **K** : [keys](treed-tree-treelist.md#keys)
- **N** : [new](treed-tree-treelist.md#new) :black_small_square: [new_paths](treed-tree-treelist.md#new_paths)
- **P** : [path](treed-tree-treelist.md#path)
- **S** : [SEP](treed-tree-treelist.md#sep) :black_small_square: [set_child](treed-tree-treelist.md#set_child) :black_small_square: [solve_path](treed-tree-treelist.md#solve_path) :black_small_square: [solve_to_missing](treed-tree-treelist.md#solve_to_missing)
- **T** : [top](treed-tree-treelist.md#top)
- **V** : [values](treed-tree-treelist.md#values)



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

### path

> TYPE: **str**

Node path up to the top node

### SEP

> TYPE: **str**<br> DEFAULT: **/**



### top

> TYPE: **Section**

Get the topmost section

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [TreeList](#treelist)</sub>



## Methods

----------
### add



``` python
add(path, node, complete_path=False)
```

Add a new node at the path

This method calls [set_child](#set_child).


#### Arguments:
- **path** (_str_)
- **node** (_Tree_)
- **complete_path** ( = False)



#### Returns:
- **Tree** : the node argument



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### all_items



``` python
all_items(include_self=False)
```

All items iterator

Iterate on all items in the folder and sub folders.


#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### all_paths



``` python
all_paths(include_self=False)
```

All paths iterator

Iterate on all paths in the folder and sub folders.


#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### all_values



``` python
all_values(include_self=False)
```

All values iterator

Iterate on all values in the folder and sub folders.


#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### create_path



``` python
create_path(*keys)
```

Create nodes in a path

Nodes are create by calling [new](#new) method.


#### Arguments:
- **keys** (_list of strs_)



#### Returns:
- **Tree** : last created node



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### find



``` python
find(*keys, first=False, **criteria)
```

Find one or more keys in the tree.


#### Arguments:
- **keys** (_list of strs_)
- **first** (_boolean_ = False)
- **criteria**



#### Returns:
- **Tree** : on single tree if first is Trur



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### get



``` python
get(path, default=None)
```

Get the node at path


#### Arguments:
- **path** (_str_)
- **default** (_Tree_ = None)



#### Returns:
- **Tree** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### get_child



``` python
get_child(key)
```

Get a direct child by its key


#### Arguments:
- **key**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### items



``` python
items()
```

Iterate on (key, value) pais


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### join_keys



``` python
join_keys(*keys)
```

Join keys to form a path

Joins the keys with the key separator avoiding double separators: `join_keys("AAA", "BBB")`
and `join_keys("AAA/", "BBB")` will both give `"AAA/BBB"`.


#### Arguments:
- **keys**



#### Returns:
- **str** : key joined by key separator



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### keys



``` python
keys()
```

Iterate on keys


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### new



``` python
new(path, complete_path=False, **kwargs)
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
- **path** (_str_)
- **complete_path** (_set_ = False)
- **kwargs**



#### Returns:
- **Tree** : the created node



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### new_paths



``` python
new_paths(*paths, complete_path=False, **kwargs)
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
- **paths** (_list of str_)
- **complete_path** (_bool_ = False)
- **kwargs**



#### Returns:
- **Tree** : the created child



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### set_child



``` python
set_child(key, child, index=None)
```

set a direct child by its key


#### Arguments:
- **key**
- **child**
- **index** ( = None)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### solve_path



``` python
solve_path(path, complete_path=False)
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
- **path** (_str_)
- **complete_path** (_bool_ = False)



#### Returns:
- **Tree** : (found node, None) or (parent node, missing key)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### solve_to_missing



``` python
solve_to_missing(path)
```

Solve a path to missing keys

Solve a path, return the existing node and the list of non existing keys.


#### Raises:
- **PathError** : if path is incorrect



#### Arguments:
- **path** (_str_)



#### Returns:
- **node** : last existing node, list of missing keys



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### values



``` python
values()
```

Iterate on childs


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>


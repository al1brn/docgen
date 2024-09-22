# TreeChain

Tree interface whith chained nodes

This class implements directly the [Tree](treed-tree-treechain.md#tree) interface by chaining the nodes with [child](treed-tree-treechain.md#child) and [next](treed-tree-treechain.md#next)
properties:
- **child** : first child, the node has no children if Node
- **next** : next child in the collection of parent children, last child if NoneTree interface whith chained nodes

This class implements directly the [Tree](treed-tree-treechain.md#tree) interface by chaining the nodes with [child](treed-tree-treechain.md#child) and [next](treed-tree-treechain.md#next)
properties:
- **child** : first child, the node has no children if Node
- **next** : next child in the collection of parent children, last child if None

### Inherited

Tree.\_\_weakref__ :black_small_square: 

## Content

- **A** :arrow_right: [add](treed-tree-treechain.md#add) :white_medium_small_square: [all_count](treed-tree-treechain.md#all_count) :white_medium_small_square: [all_items](treed-tree-treechain.md#all_items) :white_medium_small_square: [all_paths](treed-tree-treechain.md#all_paths) :white_medium_small_square: [all_values](treed-tree-treechain.md#all_values)
- **C** :arrow_right: [child](treed-tree-treechain.md#child) :white_medium_small_square: [count](treed-tree-treechain.md#count) :white_medium_small_square: [create_path](treed-tree-treechain.md#create_path)
- **D** :arrow_right: [depth](treed-tree-treechain.md#depth) :white_medium_small_square: [DOT](treed-tree-treechain.md#dot)
- **F** :arrow_right: [find](treed-tree-treechain.md#find) :white_medium_small_square: [FromFile](treed-tree-treechain.md#fromfile) :white_medium_small_square: [FromInspect](treed-tree-treechain.md#frominspect)
- **G** :arrow_right: [get](treed-tree-treechain.md#get) :white_medium_small_square: [get_child](treed-tree-treechain.md#get_child)
- **I** :arrow_right: [is_top](treed-tree-treechain.md#is_top) :white_medium_small_square: [items](treed-tree-treechain.md#items)
- **J** :arrow_right: [join_keys](treed-tree-treechain.md#join_keys)
- **K** :arrow_right: [keys](treed-tree-treechain.md#keys)
- **L** :arrow_right: [last_child](treed-tree-treechain.md#last_child)
- **N** :arrow_right: [new](treed-tree-treechain.md#new) :white_medium_small_square: [new_paths](treed-tree-treechain.md#new_paths) :white_medium_small_square: [next](treed-tree-treechain.md#next)
- **P** :arrow_right: [path](treed-tree-treechain.md#path)
- **S** :arrow_right: [SEP](treed-tree-treechain.md#sep) :white_medium_small_square: [set_child](treed-tree-treechain.md#set_child) :white_medium_small_square: [solve_path](treed-tree-treechain.md#solve_path) :white_medium_small_square: [solve_to_missing](treed-tree-treechain.md#solve_to_missing) :white_medium_small_square: [sort](treed-tree-treechain.md#sort) :white_medium_small_square: [\_\_str__](treed-tree-treechain.md#__str__)
- **T** :arrow_right: [Test](treed-tree-treechain.md#test) :white_medium_small_square: [test](treed-tree-treechain.md#test) :white_medium_small_square: [top](treed-tree-treechain.md#top)
- **V** :arrow_right: [values](treed-tree-treechain.md#values)


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
### sort



``` python
sort(self, key=None, reverse=False)
```

Sort the direct children

#### Arguments:
- **self**
- **key** (_function_ = None)
- **reverse** (_bool_ = False)



----------
### \_\_str__



``` python
__str__(self)
```

str
$ DOC SET hidden

#### Arguments:
- **self**



----------
### Test



``` python
Test(**kwargs)
```

A tree for test

#### Arguments:
- **kwargs**



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



## Properties

### all_count


> type ?



### child


> type TreeChain ( = None)

the first child of the direct children. None if the node has node child

### count


> type ?



### depth


> type ?

Distance to the top

### DOT


> type str ( = .)



### is_top


> type ?

Is top section

### last_child


> type ?



### next


> type TreeChain ( = None)

the next next in the parent children series. None if it is the last one

### path


> type ?

Node path up to the top node

### SEP


> type str ( = /)



### top


> type ?

Get the topmost section
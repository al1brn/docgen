# Tree

``` python
Tree()
```

Tree interface

This abstract class exposes an interface for a tree.

Each node in a tree has a single parent and can have children. The top node in the tree
has no parent.

Each node, but the top one, has a key. A node can be considered as a dictionary of children keyed
by their key.

Keys can be composed with a key separator to form a path. A patch extends the scope of the "keys"
accepted by a node:
    
``` python
# default key separator is '/'

child = node['AAA']      # returns the child keyed by 'AAA'
child = node ['AAA/BBB'] # return child 'BBB' of child 'AAA'
````

### Abstract methods

Actual implementation of a Tree requires the following properties and methods:

- key (str property) : the key of the node
- get_child (method) : get a direct child by its key
- set_child (method) : insert a child in the collection of direct children
- values (method) : returns an iterator on the direct children
- keys (method) : returns an iterator on the keys of the direct children
- items (method) : returns an iterator on the (key, child) pairs of the direct children


### Creating a whole tree

A tree can be created using the [add](tree-tree.md#add) method with the following pseudo code:
    
``` python
class MyTree(TreeDict): # of TreeList or TreeChain or your own implementation
    def __init__(self, source):
        # Initialize self from source content
        ...
        
        # Loop on source children
        for key, child in source:
            self.add(key, MyTree(child))
``` 

The constructor ['#FromFile' not found]() gives an actual implementation to load the arborescence
of a disk folder:
    
<$ Tree.FromFolder>

### path

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

Node path up to the top node

----------
### remove_from_parent

``` python
remove_from_parent()
```

Remove the section from its parent list of children

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Methods](tree-tree.md#methods)</sub>

----------
### set_child

``` python
set_child(key, child, index=None)
```

Set a direct child by its key

#### Arguments:
- **key**
- **child**
- **index** ( = None)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Methods](tree-tree.md#methods)</sub>

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
> Missing nodes in the path are created with method [create_path](tree-tree.md#create_path)

#### Raises:
- **PathError** : if the path can't be solved up to the last, or last but one



#### Arguments:
- **path** (_str_) : the path to solve
- **complete_path** (_bool_ = False) : create missing nodes (but the last one) if necessary



#### Returns:
- **Tree** : (found node, None) or (parent node, missing key)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Methods](tree-tree.md#methods)</sub>

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
- **path** (_str_) : path to solve



#### Returns:
- **node** : last existing node, list of missing keys

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Methods](tree-tree.md#methods)</sub>

### top

<table><tbody>
<tr><td>type</td><td><b>Section</b></td></tr>
</tbody></table>

Get the topmost section

## Properties



### all_count

<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>

Total number of children

### count

<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>

Number of direct children, equivalent to `len(self)`

### depth

<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>

Distance to the top (0 for top section)

### is_top

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

True if owner is None

### key

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

node key

### parent

<table><tbody>
<tr><td>type</td><td><b>Tree</b></td></tr>
</tbody></table>

parent node, None if it is the top most node in the tree

### path

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

Node path up to the top node

### top

<table><tbody>
<tr><td>type</td><td><b>Section</b></td></tr>
</tbody></table>

Get the topmost section

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Tree](tree-tree.md)</sub>

## Methods



----------
### add

``` python
add(path, node, complete_path=False)
```

Add a new node at the path

This method calls [set_child](tree-tree.md#set_child).

#### Arguments:
- **path** (_str_) : the path where to locate the node
- **node** (_Tree_) : the node to set at the path
- **complete_path** ( = False)



#### Returns:
- **Tree** : the node argument

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Methods](tree-tree.md#methods)</sub>

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Methods](tree-tree.md#methods)</sub>

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Methods](tree-tree.md#methods)</sub>

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Methods](tree-tree.md#methods)</sub>

----------
### create_path

``` python
create_path(*keys)
```

Create nodes in a path

Nodes are create by calling [new](tree-tree.md#new) method.

#### Arguments:
- **keys** (_list of strs_) : key forming the path to create



#### Returns:
- **Tree** : last created node

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Methods](tree-tree.md#methods)</sub>

----------
### detach

``` python
detach()
```

Detach the section from its parent children

> [!IMPORANT]
> This method calls the abstract method [remove_from_parent](tree-tree.md#remove_from_parent) which must perform
> the actual removal from the parent's list of children.

#### Returns:
- **Tree** : self

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Methods](tree-tree.md#methods)</sub>

----------
### find

``` python
find(*keys, first=False, **criteria)
```

Find one or more keys in the tree.

#### Arguments:
- **keys** (_list of strs_) : the keys to look for
- **first** (_boolean_ = False) : stop on the first match an return the found node
- **criteria** : search the node with attributes match keyword arguments



#### Returns:
- **Tree** : on single tree if first is Trur

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Methods](tree-tree.md#methods)</sub>

----------
### get

``` python
get(path, default=None)
```

Get the node at path

#### Arguments:
- **path** (_str_) : the node path
- **default** (_Tree_ = None) : the node to return if the path is not solved



#### Returns:
- **Tree** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Methods](tree-tree.md#methods)</sub>

----------
### get_child

``` python
get_child(key)
```

Get a direct child by its key

#### Arguments:
- **key**

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Methods](tree-tree.md#methods)</sub>

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Methods](tree-tree.md#methods)</sub>

----------
### move_to_parent

``` python
move_to_parent(new_parent, new_key=None)
```

Change the position of a node from one parent to another

This methods basically calls [detach](tree-tree.md#detach) and then [add](tree-tree.md#add).


Returns
- Tree : self

#### Arguments:
- **new_parent** (_Tree_) : where to locate the node
- **new_key** (_str_ = None) : new key, uses the current key is None

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Methods](tree-tree.md#methods)</sub>

----------
### new

``` python
new(path, complete_path=False, **kwargs)
```

Create a new node at the given path

The default implementation create a new node by calling the defaut constructor
and adding it by calling [add](tree-tree.md#add):
    
``` python
return self.add(path, type(self)(**kwargs), complete_path=complete_path)
```

#### Raises:
- **PathError** : if nodes are missing in the path



#### Arguments:
- **path** (_str_) : the path where to create a new node
- **complete_path** (_set_ = False) : create the path if hole exist
- **kwargs** : default constructor arguments



#### Returns:
- **Tree** : the created node

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Methods](tree-tree.md#methods)</sub>

----------
### new_paths

``` python
new_paths(*paths, complete_path=False, **kwargs)
```

Create several nodes defined by their path

Basically, this method call [new](tree-tree.md#new) for each provided path.

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
- **paths** (_list of str_) : the paths of the nodes to create
- **complete_path** (_bool_ = False) : create intermediary nodes in paths
- **kwargs** : default constructor arguments when creating intermediary is required



#### Returns:
- **Tree** : the created child

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Methods](tree-tree.md#methods)</sub>

----------
### remove_from_parent

``` python
remove_from_parent()
```

Remove the section from its parent list of children

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Methods](tree-tree.md#methods)</sub>

----------
### set_child

``` python
set_child(key, child, index=None)
```

Set a direct child by its key

#### Arguments:
- **key**
- **child**
- **index** ( = None)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Methods](tree-tree.md#methods)</sub>

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
> Missing nodes in the path are created with method [create_path](tree-tree.md#create_path)

#### Raises:
- **PathError** : if the path can't be solved up to the last, or last but one



#### Arguments:
- **path** (_str_) : the path to solve
- **complete_path** (_bool_ = False) : create missing nodes (but the last one) if necessary



#### Returns:
- **Tree** : (found node, None) or (parent node, missing key)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Methods](tree-tree.md#methods)</sub>

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
- **path** (_str_) : path to solve



#### Returns:
- **node** : last existing node, list of missing keys

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Methods](tree-tree.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#tree) :black_small_square:  :black_small_square: [Tree](tree-tree.md)</sub>
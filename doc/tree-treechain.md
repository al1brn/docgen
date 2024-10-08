# TreeChain

``` python
TreeChain(d=None)
```

Tree interface whith chained nodes

This class implements directly the [Tree](tree-tree.md#tree) interface by chaining the nodes with [child](tree-treechain.md#child) and [next](tree-treechain.md#next)
properties:
- **child** : first child, the node has no children if Node
- **next** : next child in the collection of parent children, last child if None

#### Arguments:
- **d** ( = None)

## Content

- **A** : [add](tree-treechain.md#add) :black_small_square: [all_count](tree-treechain.md#all_count) :black_small_square: [all_items](tree-treechain.md#all_items) :black_small_square: [all_paths](tree-treechain.md#all_paths) :black_small_square: [all_values](tree-treechain.md#all_values)
- **C** : [child](tree-treechain.md#child) :black_small_square: [count](tree-treechain.md#count) :black_small_square: [create_path](tree-treechain.md#create_path)
- **D** : [depth](tree-treechain.md#depth) :black_small_square: [detach](tree-treechain.md#detach)
- **F** : [find](tree-treechain.md#find) :black_small_square: [FromFile](tree-treechain.md#fromfile) :black_small_square: [FromInspect](tree-treechain.md#frominspect)
- **G** : [get](tree-treechain.md#get) :black_small_square: [get_child](tree-treechain.md#get_child)
- **I** : [is_top](tree-treechain.md#is_top) :black_small_square: [items](tree-treechain.md#items)
- **J** : [join_keys](tree-treechain.md#join_keys)
- **K** : [keys](tree-treechain.md#keys)
- **M** : [move_to_parent](tree-treechain.md#move_to_parent)
- **N** : [new](tree-treechain.md#new) :black_small_square: [new_paths](tree-treechain.md#new_paths) :black_small_square: [next](tree-treechain.md#next)
- **P** : [path](tree-treechain.md#path)
- **R** : [remove_from_parent](tree-treechain.md#remove_from_parent)
- **S** : [set_child](tree-treechain.md#set_child) :black_small_square: [solve_path](tree-treechain.md#solve_path) :black_small_square: [solve_to_missing](tree-treechain.md#solve_to_missing) :black_small_square: [sort](tree-treechain.md#sort)
- **T** : [top](tree-treechain.md#top)
- **V** : [values](tree-treechain.md#values)

## Properties



### all_count

> _type_: **int**
>

Total number of children

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Properties](tree-treechain.md#properties)</sub>

### child

> _type_: **TreeChain**
>

the first child of the direct children. None if the node has node child

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Properties](tree-treechain.md#properties)</sub>

### count

> _type_: **int**
>

Number of direct children, equivalent to `len(self)`

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Properties](tree-treechain.md#properties)</sub>

### depth

> _type_: **int**
>

Distance to the top (0 for top section)

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Properties](tree-treechain.md#properties)</sub>

### is_top

> _type_: **bool**
>

True if owner is None

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Properties](tree-treechain.md#properties)</sub>

### next

> _type_: **TreeChain**
>

the next next in the parent children series. None if it is the last one

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Properties](tree-treechain.md#properties)</sub>

### path

> _type_: **str**
>

Node path up to the top node

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Properties](tree-treechain.md#properties)</sub>

### top

> _type_: **Section**
>

Get the topmost section

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Properties](tree-treechain.md#properties)</sub>

## Methods



----------
### add()

> method

``` python
add(path, node, complete_path=False)
```

Add a new node at the path

This method calls [set_child](tree-treechain.md#set_child).

#### Arguments:
- **path** (_str_) : the path where to locate the node
- **node** (_Tree_) : the node to set at the path
- **complete_path** ( = False)



#### Returns:
- **Tree** : the node argument

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### all_items()

> method

``` python
all_items(include_self=False)
```

All items iterator

Iterate on all items in the folder and sub folders.

#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** :

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### all_paths()

> method

``` python
all_paths(include_self=False)
```

All paths iterator

Iterate on all paths in the folder and sub folders.

#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** :

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### all_values()

> method

``` python
all_values(include_self=False)
```

All values iterator

Iterate on all values in the folder and sub folders.

#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** :

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### create_path()

> method

``` python
create_path(*keys)
```

Create nodes in a path

Nodes are create by calling [new](tree-treechain.md#new) method.

#### Arguments:
- **keys** (_list of strs_) : key forming the path to create



#### Returns:
- **Tree** : last created node

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### detach()

> method

``` python
detach()
```

Detach the section from its parent children

> [!IMPORANT]
> This method calls the abstract method [remove_from_parent](tree-treechain.md#remove_from_parent) which must perform
> the actual removal from the parent's list of children.

#### Returns:
- **Tree** : self

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### find()

> method

``` python
find(*keys, first=True, **criteria)
```

Find one or more keys in the tree.

#### Arguments:
- **keys** (_list of strs_) : the keys to look for
- **first** (_boolean_ = True) : stop on the first match an return the found node
- **criteria** : search the node with attributes match keyword arguments



#### Returns:
- **Tree** : on single tree if first is Trur

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### FromFile()

> classmethod

``` python
FromFile(folder, pattern='*.*', ignore=('.*', '_*'))
```

Read the content of a drive

This methods shows how to use method [add](tree-treechain.md#add) to recursively load folder files and sub folders.

#### Arguments:
- **folder** (_str_) : folder to load
- **pattern** (_str or tuple of strs_ = *.*) : file selection
- **ignore** (_str or tuple of strs_ = ('.*', '_*')) : files starting by one of the characters in the string are ignored



#### Returns:
- **Tree** :

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### FromInspect()

> classmethod

``` python
FromInspect(obj)
```

Load python module

Load module and module members using inspect

#### Arguments:
- **obj** (_any_) : object to inspect



#### Returns:
- **Tree** :

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### get()

> method

``` python
get(path, default=None)
```

Get the node at path

#### Arguments:
- **path** (_str_) : the node path
- **default** (_Tree_ = None) : the node to return if the path is not solved



#### Returns:
- **Tree** :

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### get_child()

> method

``` python
get_child(key)
```

Get a direct child by its key

#### Arguments:
- **key**

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### items()

> method

``` python
items()
```

Iterate on (key, value) pais

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### join_keys()

> method

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

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### keys()

> method

``` python
keys()
```

Iterate on keys

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### move_to_parent()

> method

``` python
move_to_parent(new_parent, new_key=None)
```

Change the position of a node from one parent to another

This methods basically calls [detach](tree-treechain.md#detach) and then [add](tree-treechain.md#add).


Returns
- Tree : self

#### Arguments:
- **new_parent** (_Tree_) : where to locate the node
- **new_key** (_str_ = None) : new key, uses the current key is None

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### new()

> method

``` python
new(path, complete_path=False, **kwargs)
```

Create a new node at the given path

The default implementation create a new node by calling the defaut constructor
and adding it by calling [add](tree-treechain.md#add):
    
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

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### new_paths()

> method

``` python
new_paths(*paths, complete_path=False, **kwargs)
```

Create several nodes defined by their path

Basically, this method call [new](tree-treechain.md#new) for each provided path.

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

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### remove_from_parent()

> method

``` python
remove_from_parent()
```

Remove the section from its parent list of children

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### set_child()

> method

``` python
set_child(key, child, index=None)
```

set a direct child by its key

#### Arguments:
- **key**
- **child**
- **index** ( = None)

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### solve_path()

> method

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
> Missing nodes in the path are created with method [create_path](tree-treechain.md#create_path)

#### Raises:
- **PathError** : if the path can't be solved up to the last, or last but one



#### Arguments:
- **path** (_str_) : the path to solve
- **complete_path** (_bool_ = False) : create missing nodes (but the last one) if necessary



#### Returns:
- **Tree** : (found node, None) or (parent node, missing key)

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### solve_to_missing()

> method

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

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### sort()

> method

``` python
sort(key=None, reverse=False)
```

Sort the direct children

#### Arguments:
- **key** (_function_ = None) : function to use to sort the children
- **reverse** (_bool_ = False) : sort in rerverse order

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### values()

> method

``` python
values()
```

Iterate on childs

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeChain](tree-treechain.md#treechain) :black_small_square: [Content](tree-treechain.md#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>
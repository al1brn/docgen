# TreeChain

``` python
TreeChain(d=None)
```

Tree interface whith chained nodes

This class implements directly the [Tree](tree-tree.md) interface by chaining the nodes with [child](tree-treechain.md#child) and [next](tree-treechain.md#next)
properties:
- **child** : first child, the node has no children if Node
- **next** : next child in the collection of parent children, last child if None

#### Arguments:
- **d** ( = None)

## Content

- [all_count](tree-treechain.md#all_count)
- [child](tree-treechain.md#child)
- [count](tree-treechain.md#count)
- [depth](tree-treechain.md#depth)
- [is_top](tree-treechain.md#is_top)
- [next](tree-treechain.md#next)
- [path](tree-treechain.md#path)
- [top](tree-treechain.md#top)
- [add](tree-treechain.md#add)
- [all_items](tree-treechain.md#all_items)
- [all_paths](tree-treechain.md#all_paths)
- [all_values](tree-treechain.md#all_values)
- [create_path](tree-treechain.md#create_path)
- [detach](tree-treechain.md#detach)
- [find](tree-treechain.md#find)
- [FromFile](tree-treechain.md#fromfile)
- [FromInspect](tree-treechain.md#frominspect)
- [get](tree-treechain.md#get)
- [get_child](tree-treechain.md#get_child)
- [items](tree-treechain.md#items)
- [join_keys](tree-treechain.md#join_keys)
- [keys](tree-treechain.md#keys)
- [move_to_parent](tree-treechain.md#move_to_parent)
- [new](tree-treechain.md#new)
- [new_paths](tree-treechain.md#new_paths)
- [remove_from_parent](tree-treechain.md#remove_from_parent)
- [set_child](tree-treechain.md#set_child)
- [solve_path](tree-treechain.md#solve_path)
- [solve_to_missing](tree-treechain.md#solve_to_missing)
- [sort](tree-treechain.md#sort)
- [values](tree-treechain.md#values)

## Properties



### all_count

> _type_: **int**
>

Total number of children

### child

> _type_: **TreeChain**
>

the first child of the direct children. None if the node has node child

### count

> _type_: **int**
>

Number of direct children, equivalent to `len(self)`

### depth

> _type_: **int**
>

Distance to the top (0 for top section)

### is_top

> _type_: **bool**
>

True if owner is None

### next

> _type_: **TreeChain**
>

the next next in the parent children series. None if it is the last one

### path

> _type_: **str**
>

Node path up to the top node

### top

> _type_: **Section**
>

Get the topmost section

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [TreeChain](tree-treechain.md)</sub>

## Methods



----------
### add

``` python
add(path, node, complete_path=False)
```


 > type : method

Add a new node at the path

This method calls [set_child](tree-treechain.md#set_child).

#### Arguments:
- **path** (_str_) : the path where to locate the node
- **node** (_Tree_) : the node to set at the path
- **complete_path** ( = False)



#### Returns:
- **Tree** : the node argument

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### all_items

``` python
all_items(include_self=False)
```


 > type : method

All items iterator

Iterate on all items in the folder and sub folders.

#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### all_paths

``` python
all_paths(include_self=False)
```


 > type : method

All paths iterator

Iterate on all paths in the folder and sub folders.

#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### all_values

``` python
all_values(include_self=False)
```


 > type : method

All values iterator

Iterate on all values in the folder and sub folders.

#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### create_path

``` python
create_path(*keys)
```


 > type : method

Create nodes in a path

Nodes are create by calling [new](tree-treechain.md#new) method.

#### Arguments:
- **keys** (_list of strs_) : key forming the path to create



#### Returns:
- **Tree** : last created node

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### detach

``` python
detach()
```


 > type : method

Detach the section from its parent children

> [!IMPORANT]
> This method calls the abstract method [remove_from_parent](tree-treechain.md#remove_from_parent) which must perform
> the actual removal from the parent's list of children.

#### Returns:
- **Tree** : self

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### find

``` python
find(*keys, first=False, **criteria)
```


 > type : method

Find one or more keys in the tree.

#### Arguments:
- **keys** (_list of strs_) : the keys to look for
- **first** (_boolean_ = False) : stop on the first match an return the found node
- **criteria** : search the node with attributes match keyword arguments



#### Returns:
- **Tree** : on single tree if first is Trur

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### FromFile

``` python
FromFile(folder, pattern='*.*', ignore=('.*', '_*'))
```


 > type : classmethod

Read the content of a drive

This methods shows how to use method [add](tree-treechain.md#add) to recursively load folder files and sub folders.

#### Arguments:
- **folder** (_str_) : folder to load
- **pattern** (_str or tuple of strs_ = *.*) : file selection
- **ignore** (_str or tuple of strs_ = ('.*', '_*')) : files starting by one of the characters in the string are ignored



#### Returns:
- **Tree** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### FromInspect

``` python
FromInspect(obj)
```


 > type : classmethod

Load python module

Load module and module members using inspect

#### Arguments:
- **obj** (_any_) : object to inspect



#### Returns:
- **Tree** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### get

``` python
get(path, default=None)
```


 > type : method

Get the node at path

#### Arguments:
- **path** (_str_) : the node path
- **default** (_Tree_ = None) : the node to return if the path is not solved



#### Returns:
- **Tree** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### get_child

``` python
get_child(key)
```


 > type : method

Get a direct child by its key

#### Arguments:
- **key**

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### items

``` python
items()
```


 > type : method

Iterate on (key, value) pais

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### join_keys

``` python
join_keys(*keys)
```


 > type : method

Join keys to form a path

Joins the keys with the key separator avoiding double separators: `join_keys("AAA", "BBB")`
and `join_keys("AAA/", "BBB")` will both give `"AAA/BBB"`.

#### Arguments:
- **keys**



#### Returns:
- **str** : key joined by key separator

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### keys

``` python
keys()
```


 > type : method

Iterate on keys

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### move_to_parent

``` python
move_to_parent(new_parent, new_key=None)
```


 > type : method

Change the position of a node from one parent to another

This methods basically calls [detach](tree-treechain.md#detach) and then [add](tree-treechain.md#add).


Returns
- Tree : self

#### Arguments:
- **new_parent** (_Tree_) : where to locate the node
- **new_key** (_str_ = None) : new key, uses the current key is None

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### new

``` python
new(path, complete_path=False, **kwargs)
```


 > type : method

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### new_paths

``` python
new_paths(*paths, complete_path=False, **kwargs)
```


 > type : method

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### remove_from_parent

``` python
remove_from_parent()
```


 > type : method

Remove the section from its parent list of children

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### set_child

``` python
set_child(key, child, index=None)
```


 > type : method

set a direct child by its key

#### Arguments:
- **key**
- **child**
- **index** ( = None)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### solve_path

``` python
solve_path(path, complete_path=False)
```


 > type : method

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### solve_to_missing

``` python
solve_to_missing(path)
```


 > type : method

Solve a path to missing keys

Solve a path, return the existing node and the list of non existing keys.

#### Raises:
- **PathError** : if path is incorrect



#### Arguments:
- **path** (_str_) : path to solve



#### Returns:
- **node** : last existing node, list of missing keys

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### sort

``` python
sort(key=None, reverse=False)
```


 > type : method

Sort the direct children

#### Arguments:
- **key** (_function_ = None) : function to use to sort the children
- **reverse** (_bool_ = False) : sort in rerverse order

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### values

``` python
values()
```


 > type : method

Iterate on childs

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [TreeChain](tree-treechain.md)</sub>
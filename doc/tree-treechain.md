# TreeChain

> Bases classes: [Tree](tree-tree.md)

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

### Inherited

[FromFile](tree-tree.md#fromfile) :black_small_square: [FromInspect](tree-tree.md#frominspect) :black_small_square: [Test](docum-section.md#test) :black_small_square: [\_\_getitem__](tree-tree.md#__getitem__) :black_small_square: [\_\_iter__](tree-tree.md#__iter__) :black_small_square: [\_\_setitem__](tree-tree.md#__setitem__) :black_small_square: [\_\_str__](docum-documentation.md#__str__) :black_small_square: [add](tree-tree.md#add) :black_small_square: [all_items](tree-tree.md#all_items) :black_small_square: [all_paths](tree-tree.md#all_paths) :black_small_square: [all_values](tree-tree.md#all_values) :black_small_square: [create_path](tree-tree.md#create_path) :black_small_square: [detach](tree-tree.md#detach) :black_small_square: [dump](tree-tree.md#dump) :black_small_square: [find](tree-tree.md#find) :black_small_square: [get](tree-tree.md#get) :black_small_square: [join_keys](tree-tree.md#join_keys) :black_small_square: [move_to_parent](tree-tree.md#move_to_parent) :black_small_square: [new](tree-tree.md#new) :black_small_square: [new_paths](tree-tree.md#new_paths) :black_small_square: [solve_path](tree-tree.md#solve_path) :black_small_square: [solve_to_missing](tree-tree.md#solve_to_missing) :black_small_square: [test](parse---parser.md#test) :black_small_square: [test_numpy](tree-tree.md#test_numpy) :black_small_square:

## Content

- **A** : [all_count](tree-treechain.md#all_count)
- **C** : [child](tree-treechain.md#child) :black_small_square: [count](tree-treechain.md#count)
- **D** : [depth](tree-treechain.md#depth)
- **G** : [get_child](tree-treechain.md#get_child)
- **I** : [is_top](tree-treechain.md#is_top) :black_small_square: [items](tree-treechain.md#items)
- **K** : [keys](tree-treechain.md#keys)
- **N** : [next](tree-treechain.md#next)
- **P** : [path](tree-treechain.md#path)
- **R** : [remove_from_parent](tree-treechain.md#remove_from_parent)
- **S** : [set_child](tree-treechain.md#set_child) :black_small_square: [sort](tree-treechain.md#sort)
- **T** : [top](tree-treechain.md#top)
- **V** : [values](tree-treechain.md#values)

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
### get_child()

> method

``` python
get_child(key)
```

Get a direct child by its key

#### Arguments:
- **key**

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### items()

> method

``` python
items()
```

Iterate on (key, value) pais

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### keys()

> method

``` python
keys()
```

Iterate on keys

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### remove_from_parent()

> method

``` python
remove_from_parent()
```

Remove the section from its parent list of children

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

----------
### values()

> method

``` python
values()
```

Iterate on childs

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treechain.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [TreeChain](tree-treechain.md)</sub>
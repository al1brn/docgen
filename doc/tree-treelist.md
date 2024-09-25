# TreeList

``` python
TreeList()
```

Tree interface based on a list

This class inherits from [Tree](tree-tree.md) and list. Direct children are store in the list.

Several children can share the same key.

This implementation can be chosen when direct children can share a same key and / or when there is
a need to control the order of the children### Inherited

[FromFile](tree-tree.md#fromfile) :black_small_square: [FromInspect](tree-tree.md#frominspect) :black_small_square: [Test](docum-section.md#test) :black_small_square:  :black_small_square:  :black_small_square:  :black_small_square:  :black_small_square:  :black_small_square:  :black_small_square: [__getitem__](tree-tree.md#__getitem__) :black_small_square:  :black_small_square:  :black_small_square:  :black_small_square: [__iter__](tree-tree.md#__iter__) :black_small_square:  :black_small_square:  :black_small_square:  :black_small_square:  :black_small_square:  :black_small_square:  :black_small_square:  :black_small_square:  :black_small_square: [__setitem__](tree-tree.md#__setitem__) :black_small_square:  :black_small_square: [__str__](docum-documentation.md#__str__) :black_small_square: [add](tree-tree.md#add) :black_small_square: [all_items](tree-tree.md#all_items) :black_small_square: [all_paths](tree-tree.md#all_paths) :black_small_square: [all_values](tree-tree.md#all_values) :black_small_square:  :black_small_square:  :black_small_square:  :black_small_square: [create_path](tree-tree.md#create_path) :black_small_square: [detach](tree-tree.md#detach) :black_small_square: [dump](tree-tree.md#dump) :black_small_square:  :black_small_square: [find](tree-tree.md#find) :black_small_square: [get](tree-tree.md#get) :black_small_square:  :black_small_square:  :black_small_square: [join_keys](tree-tree.md#join_keys) :black_small_square: [move_to_parent](tree-tree.md#move_to_parent) :black_small_square: [new](tree-tree.md#new) :black_small_square: [new_paths](tree-tree.md#new_paths) :black_small_square:  :black_small_square:  :black_small_square:  :black_small_square: [solve_path](tree-tree.md#solve_path) :black_small_square: [solve_to_missing](tree-tree.md#solve_to_missing) :black_small_square:  :black_small_square: [test](parse---parser.md#test) :black_small_square: [test_numpy](tree-tree.md#test_numpy) :black_small_square:

## Content

- **A** : [all_count](tree-treelist.md#all_count)
- **C** : [count](tree-treelist.md#count)
- **D** : [depth](tree-treelist.md#depth)
- **G** : [get_child](tree-treelist.md#get_child)
- **I** : [is_top](tree-treelist.md#is_top) :black_small_square: [items](tree-treelist.md#items)
- **K** : [keys](tree-treelist.md#keys)
- **P** : [path](tree-treelist.md#path)
- **R** : [remove_from_parent](tree-treelist.md#remove_from_parent)
- **S** : [set_child](tree-treelist.md#set_child)
- **T** : [top](tree-treelist.md#top)
- **V** : [values](tree-treelist.md#values)

## Properties



### all_count

> _type_: **int**
>

Total number of children

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

### path

> _type_: **str**
>

Node path up to the top node

### top

> _type_: **Section**
>

Get the topmost section

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [TreeList](tree-treelist.md)</sub>

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### items()

> method

``` python
items()
```

Iterate on (key, value) pais

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### keys()

> method

``` python
keys()
```

Iterate on keys

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### remove_from_parent()

> method

``` python
remove_from_parent()
```

Remove the section from its parent list of children

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### values()

> method

``` python
values()
```

Iterate on childs

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [TreeList](tree-treelist.md)</sub>
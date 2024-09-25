# TreeDict

> Bases classes: [Tree](tree-tree.md)

``` python
TreeDict()
```

Tree interface based on a dict

This class inherits from [Tree](tree-tree.md) and dict. Direct children are managed from dict inheritance.

This implementation can be chosen when direct child keys must be unique and when there is no
particular need in controlling the order of the children.### Inherited

[\_\_getitem__](tree-tree.md#__getitem__) :black_small_square: [\_\_iter__](tree-tree.md#__iter__) :black_small_square: [\_\_setitem__](tree-tree.md#__setitem__) :black_small_square: [\_\_str__](docum-documentation.md#__str__) :black_small_square: [add](tree-tree.md#add) :black_small_square: [all_items](tree-tree.md#all_items) :black_small_square: [all_paths](tree-tree.md#all_paths) :black_small_square: [all_values](tree-tree.md#all_values) :black_small_square: [create_path](tree-tree.md#create_path) :black_small_square: [detach](tree-tree.md#detach) :black_small_square: [dump](tree-tree.md#dump) :black_small_square: [find](tree-tree.md#find) :black_small_square: [FromFile](tree-tree.md#fromfile) :black_small_square: [FromInspect](tree-tree.md#frominspect) :black_small_square: [get](tree-tree.md#get) :black_small_square: [join_keys](tree-tree.md#join_keys) :black_small_square: [move_to_parent](tree-tree.md#move_to_parent) :black_small_square: [new](tree-tree.md#new) :black_small_square: [new_paths](tree-tree.md#new_paths) :black_small_square: [solve_path](tree-tree.md#solve_path) :black_small_square: [solve_to_missing](tree-tree.md#solve_to_missing) :black_small_square: [Test](docum-section.md#test) :black_small_square: [test](parse---parser.md#test) :black_small_square: [test_numpy](tree-tree.md#test_numpy) :black_small_square:

## Content

- [all_count](tree-treedict.md#all_count)
- [count](tree-treedict.md#count)
- [depth](tree-treedict.md#depth)
- [get_child](tree-treedict.md#get_child)
- [is_top](tree-treedict.md#is_top)
- [key](tree-treedict.md#key)
- [path](tree-treedict.md#path)
- [remove_from_parent](tree-treedict.md#remove_from_parent)
- [set_child](tree-treedict.md#set_child)
- [top](tree-treedict.md#top)

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

### key

> _type_: **str**
>

Get the key

In a **TreeDict**, the **key** is known by the parent. A node can retrieve it
by searching for itself in the direct children of its parent.

To make this process more efficient, **key** is cached by default in
hidden property **_key**.

### path

> _type_: **str**
>

Node path up to the top node

### top

> _type_: **Section**
>

Get the topmost section

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treedict) :black_small_square: [Content](#content) :black_small_square: [TreeDict](tree-treedict.md)</sub>

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treedict) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treedict.md#methods)</sub>

----------
### remove_from_parent()

> method

``` python
remove_from_parent()
```

Remove the section from its parent list of children

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treedict) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treedict.md#methods)</sub>

----------
### set_child()

> method

``` python
set_child(key, child, index=None)
```

Set a direct child by its key

#### Arguments:
- **key**
- **child**
- **index** ( = None)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treedict) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treedict.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treedict) :black_small_square: [Content](#content) :black_small_square: [TreeDict](tree-treedict.md)</sub>
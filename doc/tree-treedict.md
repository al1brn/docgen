# TreeDict

> Bases classes: [Tree](tree-tree.md#tree)

``` python
TreeDict()
```

Tree interface based on a dict

This class inherits from [Tree](tree-tree.md#tree) and dict. Direct children are managed from dict inheritance.

This implementation can be chosen when direct child keys must be unique and when there is no
particular need in controlling the order of the children.### Inherited

[add](tree-tree.md#add) :black_small_square: [all_count](tree-tree.md#all_count) :black_small_square: [all_items](tree-tree.md#all_items) :black_small_square: [all_paths](tree-tree.md#all_paths) :black_small_square: [all_values](tree-tree.md#all_values) :black_small_square: [count](tree-tree.md#count) :black_small_square: [create_path](tree-tree.md#create_path) :black_small_square: [depth](tree-tree.md#depth) :black_small_square: [detach](tree-tree.md#detach) :black_small_square: [dump](tree-tree.md#dump) :black_small_square: [find](tree-tree.md#find) :black_small_square: [FromFile](tree-tree.md#fromfile) :black_small_square: [FromInspect](tree-tree.md#frominspect) :black_small_square: [get](tree-tree.md#get) :black_small_square: [\_\_getitem__](tree-tree.md#__getitem__) :black_small_square: [is_top](tree-tree.md#is_top) :black_small_square: [\_\_iter__](tree-tree.md#__iter__) :black_small_square: [join_keys](tree-tree.md#join_keys) :black_small_square: [move_to_parent](tree-tree.md#move_to_parent) :black_small_square: [new](tree-tree.md#new) :black_small_square: [new_paths](tree-tree.md#new_paths) :black_small_square: [parent](tree-tree.md#parent) :black_small_square: [path](tree-tree.md#path) :black_small_square: [\_\_setitem__](tree-tree.md#__setitem__) :black_small_square: [solve_path](tree-tree.md#solve_path) :black_small_square: [solve_to_missing](tree-tree.md#solve_to_missing) :black_small_square: [\_\_str__](docum-documentation.md#__str__) :black_small_square: [Test](docum-section.md#test) :black_small_square: [test](parse---parser.md#test) :black_small_square: [test_numpy](tree-tree.md#test_numpy) :black_small_square: [top](tree-tree.md#top) :black_small_square:

## Content

- [get_child](tree-treedict.md#get_child)
- [key](tree-treedict.md#key)
- [remove_from_parent](tree-treedict.md#remove_from_parent)
- [set_child](tree-treedict.md#set_child)

## Properties



### key

> _type_: **str**
>

Get the key

In a **TreeDict**, the **key** is known by the parent. A node can retrieve it
by searching for itself in the direct children of its parent.

To make this process more efficient, **key** is cached by default in
hidden property **_key**.

<sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeDict](tree-treedict.md#treedict) :black_small_square: [Content](tree-treedict.md#content) :black_small_square: [TreeDict](tree-treedict.md#treedict)</sub>

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

<sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeDict](tree-treedict.md#treedict) :black_small_square: [Content](tree-treedict.md#content) :black_small_square: [Methods](tree-treedict.md#methods)</sub>

----------
### remove_from_parent()

> method

``` python
remove_from_parent()
```

Remove the section from its parent list of children

<sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeDict](tree-treedict.md#treedict) :black_small_square: [Content](tree-treedict.md#content) :black_small_square: [Methods](tree-treedict.md#methods)</sub>

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

<sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeDict](tree-treedict.md#treedict) :black_small_square: [Content](tree-treedict.md#content) :black_small_square: [Methods](tree-treedict.md#methods)</sub>

<sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [TreeDict](tree-treedict.md#treedict) :black_small_square: [Content](tree-treedict.md#content) :black_small_square: [TreeDict](tree-treedict.md#treedict)</sub>
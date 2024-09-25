# TreeDict

``` python
TreeDict()
```

Tree interface based on a dict

This class inherits from [Tree](tree-tree.md) and dict. Direct children are managed from dict inheritance.

This implementation can be chosen when direct child keys must be unique and when there is no
particular need in controlling the order of the children.### Inherited

T.r.e.e.FromFileT.r.e.e.FromInspectT.r.e.e.Testdict.\_\_contains__dict.\_\_delitem__dict.\_\_eq__dict.\_\_ge__dict.\_\_getattribute__T.r.e.e.\_\_getitem__dict.\_\_gt__dict.\_\_ior__T.r.e.e.\_\_iter__dict.\_\_le__dict.\_\_len__dict.\_\_lt__dict.\_\_ne__dict.\_\_or__dict.\_\_repr__dict.\_\_reversed__dict.\_\_ror__T.r.e.e.\_\_setitem__dict.\_\_sizeof__T.r.e.e.\_\_str__T.r.e.e.addT.r.e.e.all_itemsT.r.e.e.all_pathsT.r.e.e.all_valuesdict.cleardict.copyT.r.e.e.create_pathT.r.e.e.detachT.r.e.e.dumpT.r.e.e.findT.r.e.e.getdict.itemsT.r.e.e.join_keysdict.keysT.r.e.e.move_to_parentT.r.e.e.newT.r.e.e.new_pathsdict.popdict.popitemdict.setdefaultT.r.e.e.solve_pathT.r.e.e.solve_to_missingT.r.e.e.testT.r.e.e.test_numpydict.updatedict.values

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
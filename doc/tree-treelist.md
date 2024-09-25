# TreeList

``` python
TreeList()
```

Tree interface based on a list

This class inherits from [Tree](tree-tree.md) and list. Direct children are store in the list.

Several children can share the same key.

This implementation can be chosen when direct children can share a same key and / or when there is
a need to control the order of the children### Inherited

T.r.e.e.FromFileT.r.e.e.FromInspectT.r.e.e.Testlist.\_\_add__list.\_\_contains__list.\_\_delitem__list.\_\_eq__list.\_\_ge__list.\_\_getattribute__T.r.e.e.\_\_getitem__list.\_\_gt__list.\_\_iadd__list.\_\_imul__T.r.e.e.\_\_iter__list.\_\_le__list.\_\_len__list.\_\_lt__list.\_\_mul__list.\_\_ne__list.\_\_repr__list.\_\_reversed__list.\_\_rmul__T.r.e.e.\_\_setitem__list.\_\_sizeof__T.r.e.e.\_\_str__T.r.e.e.addT.r.e.e.all_itemsT.r.e.e.all_pathsT.r.e.e.all_valueslist.appendlist.clearlist.copyT.r.e.e.create_pathT.r.e.e.detachT.r.e.e.dumplist.extendT.r.e.e.findT.r.e.e.getlist.indexlist.insertT.r.e.e.join_keysT.r.e.e.move_to_parentT.r.e.e.newT.r.e.e.new_pathslist.poplist.removelist.reverseT.r.e.e.solve_pathT.r.e.e.solve_to_missinglist.sortT.r.e.e.testT.r.e.e.test_numpy

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
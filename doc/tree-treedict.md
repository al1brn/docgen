# TreeDict

``` python
TreeDict()
```

Tree interface based on a dict

This class inherits from [Tree](tree-tree.md) and dict. Direct children are managed from dict inheritance.

This implementation can be chosen when direct child keys must be unique and when there is no
particular need in controlling the order of the children.### Inherited

Tree.FromFile :black_small_square: Tree.FromInspect :black_small_square: Tree.Test :black_small_square: dict.\_\_contains__ :black_small_square: dict.\_\_delitem__ :black_small_square: dict.\_\_eq__ :black_small_square: dict.\_\_ge__ :black_small_square: dict.\_\_getattribute__ :black_small_square: Tree.\_\_getitem__ :black_small_square: dict.\_\_gt__ :black_small_square: dict.\_\_ior__ :black_small_square: Tree.\_\_iter__ :black_small_square: dict.\_\_le__ :black_small_square: dict.\_\_len__ :black_small_square: dict.\_\_lt__ :black_small_square: dict.\_\_ne__ :black_small_square: dict.\_\_or__ :black_small_square: dict.\_\_repr__ :black_small_square: dict.\_\_reversed__ :black_small_square: dict.\_\_ror__ :black_small_square: Tree.\_\_setitem__ :black_small_square: dict.\_\_sizeof__ :black_small_square: Tree.\_\_str__ :black_small_square: Tree.add :black_small_square: Tree.all_items :black_small_square: Tree.all_paths :black_small_square: Tree.all_values :black_small_square: dict.clear :black_small_square: dict.copy :black_small_square: Tree.create_path :black_small_square: Tree.detach :black_small_square: Tree.dump :black_small_square: Tree.find :black_small_square: Tree.get :black_small_square: dict.items :black_small_square: Tree.join_keys :black_small_square: dict.keys :black_small_square: Tree.move_to_parent :black_small_square: Tree.new :black_small_square: Tree.new_paths :black_small_square: dict.pop :black_small_square: dict.popitem :black_small_square: dict.setdefault :black_small_square: Tree.solve_path :black_small_square: Tree.solve_to_missing :black_small_square: Tree.test :black_small_square: Tree.test_numpy :black_small_square: dict.update :black_small_square: dict.values :black_small_square:

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
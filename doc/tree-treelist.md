# TreeList

``` python
TreeList()
```

Tree interface based on a list

This class inherits from [Tree](tree-tree.md) and list. Direct children are store in the list.

Several children can share the same key.

This implementation can be chosen when direct children can share a same key and / or when there is
a need to control the order of the children### Inherited

Tree.FromFile :black_small_square: Tree.FromInspect :black_small_square: Tree.Test :black_small_square: list.\_\_add__ :black_small_square: list.\_\_contains__ :black_small_square: list.\_\_delitem__ :black_small_square: list.\_\_eq__ :black_small_square: list.\_\_ge__ :black_small_square: list.\_\_getattribute__ :black_small_square: Tree.\_\_getitem__ :black_small_square: list.\_\_gt__ :black_small_square: list.\_\_iadd__ :black_small_square: list.\_\_imul__ :black_small_square: Tree.\_\_iter__ :black_small_square: list.\_\_le__ :black_small_square: list.\_\_len__ :black_small_square: list.\_\_lt__ :black_small_square: list.\_\_mul__ :black_small_square: list.\_\_ne__ :black_small_square: list.\_\_repr__ :black_small_square: list.\_\_reversed__ :black_small_square: list.\_\_rmul__ :black_small_square: Tree.\_\_setitem__ :black_small_square: list.\_\_sizeof__ :black_small_square: Tree.\_\_str__ :black_small_square: Tree.add :black_small_square: Tree.all_items :black_small_square: Tree.all_paths :black_small_square: Tree.all_values :black_small_square: list.append :black_small_square: list.clear :black_small_square: list.copy :black_small_square: Tree.create_path :black_small_square: Tree.detach :black_small_square: Tree.dump :black_small_square: list.extend :black_small_square: Tree.find :black_small_square: Tree.get :black_small_square: list.index :black_small_square: list.insert :black_small_square: Tree.join_keys :black_small_square: Tree.move_to_parent :black_small_square: Tree.new :black_small_square: Tree.new_paths :black_small_square: list.pop :black_small_square: list.remove :black_small_square: list.reverse :black_small_square: Tree.solve_path :black_small_square: Tree.solve_to_missing :black_small_square: list.sort :black_small_square: Tree.test :black_small_square: Tree.test_numpy :black_small_square:

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
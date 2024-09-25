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

### Inherited

Tree.FromFile :black_small_square: Tree.FromInspect :black_small_square: Tree.Test :black_small_square: Tree.\_\_getitem__ :black_small_square: Tree.\_\_iter__ :black_small_square: Tree.\_\_setitem__ :black_small_square: Tree.\_\_str__ :black_small_square: Tree.add :black_small_square: Tree.all_items :black_small_square: Tree.all_paths :black_small_square: Tree.all_values :black_small_square: Tree.create_path :black_small_square: Tree.detach :black_small_square: Tree.dump :black_small_square: Tree.find :black_small_square: Tree.get :black_small_square: Tree.join_keys :black_small_square: Tree.move_to_parent :black_small_square: Tree.new :black_small_square: Tree.new_paths :black_small_square: Tree.solve_path :black_small_square: Tree.solve_to_missing :black_small_square: Tree.test :black_small_square: Tree.test_numpy :black_small_square:

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
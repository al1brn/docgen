# TreeIterator

``` python
TreeIterator(tree, include_self=False, values=True, paths=True)
```

Iterator of a Tree

This iterator iterates recursively on all the nodes in the [Tree](tree-tree.md) in the order:
- node
- children

The node on which the iterator is called is not yield.

The example below illustrates the yielding order:
    
```
- Top
  - AAA
    - a
    - b
  - BBB
    - c
    - d
    
Iteration on 'top'' gives the nodes in the following order which doesn't
include the top node istself:
    
> AAA, a, b, BBB, c, d
```

The iteration can be partially cut with method [no_child](tree-treeiterator.md#no_child) which prevents
to explore the children and the followers of a node

#### Arguments:
- **tree** (_Tree_) : the tree to iterate
- **include_self** (_bool_ = False) : include the tree itself
- **values** (_bool_ = True) : return values
- **paths** (_bool_ = True) : return paths



#### Returns:
- **paths** : depending on **values** and **paths** arguments

## Content

- [__iter__](tree-treeiterator.md#__iter__)
- [__next__](tree-treeiterator.md#__next__)
- [no_child](tree-treeiterator.md#no_child)

## Methods



----------
### \_\_iter__()

> method

``` python
__iter__()
```

The stack contains the current node and an iterator on its direct children

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treeiterator) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treeiterator.md#methods)</sub>

----------
### \_\_next__()

> method

``` python
__next__()
```

Next

The algorithm is the following:

```
while stack is not empty:
    - pop from the stack the current node and child itertor
    - get the next child
    - if got one:
        - restore the stack
        - push the child on the stack
        - return the child
    - else
        continue to pop the stack
```

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treeiterator) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treeiterator.md#methods)</sub>

----------
### no_child()

> method

``` python
no_child(up=0)
```

Iteration partial break

This partial break commands the iterator not to iterate on the children.

In addtion, the **up** argument controls how many level to go up in the chain
of parents:
- up = 0 -> ignore children, continue with next node
- up = 1 -> continue with parent's next node
- up = 2 -> continue with grand parent's next node
- ...

#### Arguments:
- **up** (_int_ = 0) : number of levels to move up for the next node (0 = ignore children et continue on next node)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treeiterator) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treeiterator.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treeiterator) :black_small_square: [Content](#content) :black_small_square: [TreeIterator](tree-treeiterator.md)</sub>
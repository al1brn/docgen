# TreeIterator

Iterator of a Tree

This iterator iterates recursively on all the nodes in the [Tree](treed-tree-treeiterator.md#tree) in the order:
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

The iteration can be partially cut with method [no_child](#no_child) which prevents
to explore the children and the followers of a nodeIterator of a Tree

This iterator iterates recursively on all the nodes in the [Tree](treed-tree-treeiterator.md#tree) in the order:
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

The iteration can be partially cut with method [no_child](#no_child) which prevents
to explore the children and the followers of a node

### Inherited

TreeIterator.\_\_weakref__ :black_small_square: 

## Content

- [\_\_module__](treed-tree-treeiterator.md#__module__)
- [\_\_iter__](treed-tree-treeiterator.md#__iter__)
- [\_\_next__](treed-tree-treeiterator.md#__next__)
- [no_child](treed-tree-treeiterator.md#no_child)


## Properties

### Content

- [\_\_module__](treed-tree-treeiterator.md#__module__)

### \_\_module__


> type str ( = treedict.tree)



## Methods

### Content

- [\_\_iter__](treed-tree-treeiterator.md#__iter__)
- [\_\_next__](treed-tree-treeiterator.md#__next__)
- [no_child](treed-tree-treeiterator.md#no_child)


----------
### \_\_iter__



``` python
__iter__(self)
```

The stack contains the current node and an iterator on its direct children

#### Arguments:
- **self**



----------
### \_\_next__



``` python
__next__(self)
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

#### Arguments:
- **self**



----------
### no_child



``` python
no_child(self, up=0)
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
- **self**
- **up** (_int_ = 0)


# TreeIterator



``` python
TreeIterator(tree, include_tree=False, values=True, paths=True)
```

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
to explore the children and the followers of a node

#### Arguments:
- **self**
- **tree** (_Tree_)
- **include_tree** (_bool_ = False)
- **values** (_bool_ = True)
- **paths** (_bool_ = True)



## Content

- [__iter__](treed-tree-treeiterator.md#__iter__)
- [__next__](treed-tree-treeiterator.md#__next__)
- [no_child](treed-tree-treeiterator.md#no_child)



## Methods

----------
### \_\_iter__



``` python
__iter__()
```

The stack contains the current node and an iterator on its direct children


#### Arguments:
- **self**



<sub>[{title}](index.md) :black_small_square: [{title}](#{self.page.anchor}) :black_small_square: [Content](#content) :black_small_square: [{title}](#{self.page.anchor})</sub>



----------
### \_\_next__



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


#### Arguments:
- **self**



<sub>[{title}](index.md) :black_small_square: [{title}](#{self.page.anchor}) :black_small_square: [Content](#content) :black_small_square: [{title}](#{self.page.anchor})</sub>



----------
### no_child



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
- **self**
- **up** (_int_ = 0)



<sub>[{title}](index.md) :black_small_square: [{title}](#{self.page.anchor}) :black_small_square: [Content](#content) :black_small_square: [{title}](#{self.page.anchor})</sub>


#TreeIterator

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

##Content

- [__delattr__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_\_)
- [__dict__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_)
- [__dir__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_)
- [__doc__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_)
- [__eq__](treed-tree-treeiterator.md#\_\_\_\_\_\_)
- [__format__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_)
- [__ge__](treed-tree-treeiterator.md#\_\_\_\_\_\_)
- [__getattribute__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_)
- [__getstate__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_\_\_)
- [__gt__](treed-tree-treeiterator.md#\_\_\_\_\_\_)
- [__hash__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_)
- [__init_subclass__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_)
- [__le__](treed-tree-treeiterator.md#\_\_\_\_\_\_)
- [__lt__](treed-tree-treeiterator.md#\_\_\_\_\_\_)
- [__module__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_)
- [__ne__](treed-tree-treeiterator.md#\_\_\_\_\_\_)
- [__new__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_)
- [__reduce__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_)
- [__reduce_ex__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_\_\_\_)
- [__repr__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_)
- [__setattr__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_\_)
- [__sizeof__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_)
- [__str__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_)
- [__subclasshook__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_)
- [__weakref__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_\_)
- [__iter__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_)
- [__next__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_)
- [no_child](treed-tree-treeiterator.md#no_child)


##Properties

###Content

- [__delattr__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_\_)
- [__dict__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_)
- [__dir__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_)
- [__doc__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_)
- [__eq__](treed-tree-treeiterator.md#\_\_\_\_\_\_)
- [__format__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_)
- [__ge__](treed-tree-treeiterator.md#\_\_\_\_\_\_)
- [__getattribute__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_)
- [__getstate__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_\_\_)
- [__gt__](treed-tree-treeiterator.md#\_\_\_\_\_\_)
- [__hash__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_)
- [__init_subclass__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_)
- [__le__](treed-tree-treeiterator.md#\_\_\_\_\_\_)
- [__lt__](treed-tree-treeiterator.md#\_\_\_\_\_\_)
- [__module__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_)
- [__ne__](treed-tree-treeiterator.md#\_\_\_\_\_\_)
- [__new__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_)
- [__reduce__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_)
- [__reduce_ex__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_\_\_\_)
- [__repr__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_)
- [__setattr__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_\_)
- [__sizeof__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_)
- [__str__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_)
- [__subclasshook__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_)
- [__weakref__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_\_\_\_)


###\_\_\_\_\_\_\_\_\_\_\_


> type __delattr__ ( = <slot wrapper '__delattr__' of...)



###\_\_\_\_\_\_\_\_


> type mappingproxy ( = {'__module__': 'treedict.tree'...)



###\_\_\_\_\_\_\_


> type __dir__ ( = <method '__dir__' of 'object' ...)



###\_\_\_\_\_\_\_


> type NoneType ( = None)



###\_\_\_\_\_\_


> type __eq__ ( = <slot wrapper '__eq__' of 'obj...)



###\_\_\_\_\_\_\_\_\_\_


> type __format__ ( = <method '__format__' of 'objec...)



###\_\_\_\_\_\_


> type __ge__ ( = <slot wrapper '__ge__' of 'obj...)



###\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_


> type __getattribute__ ( = <slot wrapper '__getattribute_...)



###\_\_\_\_\_\_\_\_\_\_\_\_


> type __getstate__ ( = <method '__getstate__' of 'obj...)



###\_\_\_\_\_\_


> type __gt__ ( = <slot wrapper '__gt__' of 'obj...)



###\_\_\_\_\_\_\_\_


> type __hash__ ( = <slot wrapper '__hash__' of 'o...)



###\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_


> type __init_subclass__ ( = <built-in method __init_subcla...)



###\_\_\_\_\_\_


> type __le__ ( = <slot wrapper '__le__' of 'obj...)



###\_\_\_\_\_\_


> type __lt__ ( = <slot wrapper '__lt__' of 'obj...)



###\_\_\_\_\_\_\_\_\_\_


> type str ( = treedict.tree)



###\_\_\_\_\_\_


> type __ne__ ( = <slot wrapper '__ne__' of 'obj...)



###\_\_\_\_\_\_\_


> type __new__ ( = <built-in method __new__ of ty...)



###\_\_\_\_\_\_\_\_\_\_


> type __reduce__ ( = <method '__reduce__' of 'objec...)



###\_\_\_\_\_\_\_\_\_\_\_\_\_


> type __reduce_ex__ ( = <method '__reduce_ex__' of 'ob...)



###\_\_\_\_\_\_\_\_


> type __repr__ ( = <slot wrapper '__repr__' of 'o...)



###\_\_\_\_\_\_\_\_\_\_\_


> type __setattr__ ( = <slot wrapper '__setattr__' of...)



###\_\_\_\_\_\_\_\_\_\_


> type __sizeof__ ( = <method '__sizeof__' of 'objec...)



###\_\_\_\_\_\_\_


> type __str__ ( = <slot wrapper '__str__' of 'ob...)



###\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_


> type __subclasshook__ ( = <built-in method __subclasshoo...)



###\_\_\_\_\_\_\_\_\_\_\_


> type __weakref__ ( = <attribute '__weakref__' of 'T...)



##Methods

###Content

- [__iter__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_)
- [__next__](treed-tree-treeiterator.md#\_\_\_\_\_\_\_\_)
- [no_child](treed-tree-treeiterator.md#no_child)


###\_\_\_\_\_\_\_\_

----------



``` python
__iter__(self)
```

The stack contains the current node and an iterator on its direct children

Arguments:
- **self**



###\_\_\_\_\_\_\_\_

----------



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

Arguments:
- **self**



###no_child

----------



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

Arguments:
- **self**
- **up** (_int_ = 0)


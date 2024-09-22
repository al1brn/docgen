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

## Content

- [\_\_delattr__](treed-tree-treeiterator.md#__delattr__)
- [\_\_dict__](treed-tree-treeiterator.md#__dict__)
- [\_\_dir__](treed-tree-treeiterator.md#__dir__)
- [\_\_doc__](treed-tree-treeiterator.md#__doc__)
- [\_\_eq__](treed-tree-treeiterator.md#__eq__)
- [\_\_format__](treed-tree-treeiterator.md#__format__)
- [\_\_ge__](treed-tree-treeiterator.md#__ge__)
- [\_\_getattribute__](treed-tree-treeiterator.md#__getattribute__)
- [\_\_getstate__](treed-tree-treeiterator.md#__getstate__)
- [\_\_gt__](treed-tree-treeiterator.md#__gt__)
- [\_\_hash__](treed-tree-treeiterator.md#__hash__)
- [\_\_init_subclass__](treed-tree-treeiterator.md#__init_subclass__)
- [\_\_le__](treed-tree-treeiterator.md#__le__)
- [\_\_lt__](treed-tree-treeiterator.md#__lt__)
- [\_\_module__](treed-tree-treeiterator.md#__module__)
- [\_\_ne__](treed-tree-treeiterator.md#__ne__)
- [\_\_new__](treed-tree-treeiterator.md#__new__)
- [\_\_reduce__](treed-tree-treeiterator.md#__reduce__)
- [\_\_reduce_ex__](treed-tree-treeiterator.md#__reduce_ex__)
- [\_\_repr__](treed-tree-treeiterator.md#__repr__)
- [\_\_setattr__](treed-tree-treeiterator.md#__setattr__)
- [\_\_sizeof__](treed-tree-treeiterator.md#__sizeof__)
- [\_\_str__](treed-tree-treeiterator.md#__str__)
- [\_\_subclasshook__](treed-tree-treeiterator.md#__subclasshook__)
- [\_\_weakref__](treed-tree-treeiterator.md#__weakref__)
- [\_\_iter__](treed-tree-treeiterator.md#__iter__)
- [\_\_next__](treed-tree-treeiterator.md#__next__)
- [no_child](treed-tree-treeiterator.md#no_child)


## Properties

### Content

- [\_\_delattr__](treed-tree-treeiterator.md#__delattr__)
- [\_\_dict__](treed-tree-treeiterator.md#__dict__)
- [\_\_dir__](treed-tree-treeiterator.md#__dir__)
- [\_\_doc__](treed-tree-treeiterator.md#__doc__)
- [\_\_eq__](treed-tree-treeiterator.md#__eq__)
- [\_\_format__](treed-tree-treeiterator.md#__format__)
- [\_\_ge__](treed-tree-treeiterator.md#__ge__)
- [\_\_getattribute__](treed-tree-treeiterator.md#__getattribute__)
- [\_\_getstate__](treed-tree-treeiterator.md#__getstate__)
- [\_\_gt__](treed-tree-treeiterator.md#__gt__)
- [\_\_hash__](treed-tree-treeiterator.md#__hash__)
- [\_\_init_subclass__](treed-tree-treeiterator.md#__init_subclass__)
- [\_\_le__](treed-tree-treeiterator.md#__le__)
- [\_\_lt__](treed-tree-treeiterator.md#__lt__)
- [\_\_module__](treed-tree-treeiterator.md#__module__)
- [\_\_ne__](treed-tree-treeiterator.md#__ne__)
- [\_\_new__](treed-tree-treeiterator.md#__new__)
- [\_\_reduce__](treed-tree-treeiterator.md#__reduce__)
- [\_\_reduce_ex__](treed-tree-treeiterator.md#__reduce_ex__)
- [\_\_repr__](treed-tree-treeiterator.md#__repr__)
- [\_\_setattr__](treed-tree-treeiterator.md#__setattr__)
- [\_\_sizeof__](treed-tree-treeiterator.md#__sizeof__)
- [\_\_str__](treed-tree-treeiterator.md#__str__)
- [\_\_subclasshook__](treed-tree-treeiterator.md#__subclasshook__)
- [\_\_weakref__](treed-tree-treeiterator.md#__weakref__)


### \_\_delattr__


> type __delattr__ ( = <slot wrapper '__delattr__' of...)



### \_\_dict__


> type mappingproxy ( = {'__module__': 'treedict.tree'...)



### \_\_dir__


> type __dir__ ( = <method '__dir__' of 'object' ...)



### \_\_doc__


> type NoneType ( = None)



### \_\_eq__


> type __eq__ ( = <slot wrapper '__eq__' of 'obj...)



### \_\_format__


> type __format__ ( = <method '__format__' of 'objec...)



### \_\_ge__


> type __ge__ ( = <slot wrapper '__ge__' of 'obj...)



### \_\_getattribute__


> type __getattribute__ ( = <slot wrapper '__getattribute_...)



### \_\_getstate__


> type __getstate__ ( = <method '__getstate__' of 'obj...)



### \_\_gt__


> type __gt__ ( = <slot wrapper '__gt__' of 'obj...)



### \_\_hash__


> type __hash__ ( = <slot wrapper '__hash__' of 'o...)



### \_\_init_subclass__


> type __init_subclass__ ( = <built-in method __init_subcla...)



### \_\_le__


> type __le__ ( = <slot wrapper '__le__' of 'obj...)



### \_\_lt__


> type __lt__ ( = <slot wrapper '__lt__' of 'obj...)



### \_\_module__


> type str ( = treedict.tree)



### \_\_ne__


> type __ne__ ( = <slot wrapper '__ne__' of 'obj...)



### \_\_new__


> type __new__ ( = <built-in method __new__ of ty...)



### \_\_reduce__


> type __reduce__ ( = <method '__reduce__' of 'objec...)



### \_\_reduce_ex__


> type __reduce_ex__ ( = <method '__reduce_ex__' of 'ob...)



### \_\_repr__


> type __repr__ ( = <slot wrapper '__repr__' of 'o...)



### \_\_setattr__


> type __setattr__ ( = <slot wrapper '__setattr__' of...)



### \_\_sizeof__


> type __sizeof__ ( = <method '__sizeof__' of 'objec...)



### \_\_str__


> type __str__ ( = <slot wrapper '__str__' of 'ob...)



### \_\_subclasshook__


> type __subclasshook__ ( = <built-in method __subclasshoo...)



### \_\_weakref__


> type __weakref__ ( = <attribute '__weakref__' of 'T...)



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

Arguments:
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

Arguments:
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

Arguments:
- **self**
- **up** (_int_ = 0)


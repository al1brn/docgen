# treedict


This module contains interface classes to implement tree hierarchy.

If comes with the root abstract interface [Tree](#tree) and 3 useable child classes [TreeDict](#treedict), [TreeList](#treelist) and [TreeChain](#treechain)
implementing the abstract methods respectively with a dict, a list and [LINK ERROR: section 'child' not found](treed-tree-treechain.md)  [LINK ERROR: section 'next' not found](treed-tree-treechain.md) chaining
between nodes.


Each node in a tree has a single parent and can have children. The top node in the tree
has no parent.

Each node, but the top one, has a key. A node can be considered as a dictionary of children keyed
by their key.

Keys can be composed with a key separator to form a path. A patch extends the scope of the "keys"
accepted by a node:
    
``` python
# default key separator is '/'

child = node['AAA']      # returns the child keyed by 'AAA'
child = node ['AAA/BBB'] # return child 'BBB' of child 'AAA'
````

### Tree methods

#### Getting child

A child can be addressed via a path relativelly to the caller:
    
```python
child = node['AAA/BBB']  # child BBB of child AAA
child = node['/AAA/BBB'] # same but starting from the top of the tree
```

A child, or a list of children can be found with [find](#find) method:
    
```python
child = node.find('AAA', 'BBB', first=False) # Find all children whose key is either 'AAA' or 'BBB'
child = node.find('AAA', 'BBB', first=False] # Find the first node with a key eqaul to 'AAA' or 'BBB'
```

#### Iterating on the children

One can iterate either on the direct children or on all the children in the hierarchy.
As for a dictionary, the iterators can return the node, the key or both in pair.

We have then 6 possible iterators:
- values() : direct children
- keys() : direct keys
- items() : direct (key, child) pairs
- all_values() : all children
- all_paths() : all paths
- all_items() : all (path, child) pairs

#### Abstract methods

Actual implementation of a Tree requires the following properties and methods:

- key (str property) : the key of the node
- get_child (method) : get a direct child by its key
- set_child (method) : add a child in the collection of direct children
- create_child (method) : create a new child
- values (method) : returns an iterator on the direct children
- keys (method) : returns an iterator on the keys of the direct children
- items (method) : returns an iterator on the (key, child) pairs of the direct children

### Implementation

#### With a dict

[TreeDict](#treedict) inherits from [Tree](#tree) and dict. Direct children are managed from dict inheritance.

This implementation can be chosen when direct child keys must be unique and when there is no
particular need in controlling the order of the children.

#### With a list

[TreeList](#treelist) inherits from [Tree](#tree) and list. Direct children are store in the list.

Several children can share the same key.

This implementation can be chosen when direct children can share a same key and / or when there is
a need to control the order of the children

#### Chaining implementation

[TreeChain](#treechain) implements directly the interface by chaining the nodes with [LINK ERROR: section 'child' not found](treed-tree-treechain.md) and [LINK ERROR: section 'next' not found](treed-tree-treechain.md)
properties:
- **child** : first child, the node has no children if Node
- **next** : next child in the collection of parent children, last child if None

Not sure if this implementation is better than one of the two above!

#### Testing

Testing can be made with [test](treed-tree-tree.md#test) method which provides basic testing.

One can also call [LINK ERROR: section 'FromFolder' not found](treed-tree-tree.md) and [LINK ERROR: section 'FromModule' not found](treed-tree-tree.md) which respectively create
a full tree from a disk folder and from python module.



## Content

- [__builtins__](treed---treedict.md#builtins)
- [__cached__](treed---treedict.md#cached)
- [__doc__](treed---treedict.md#doc)
- [__file__](treed---treedict.md#file)
- [__loader__](treed---treedict.md#loader)
- [__name__](treed---treedict.md#name)
- [__package__](treed---treedict.md#package)
- [__path__](treed---treedict.md#path)
- [__spec__](treed---treedict.md#spec)
- [tree](treed-tree---tree.md#tree)
  - [__builtins__](treed-tree---tree.md#builtins)
  - [__cached__](treed-tree---tree.md#cached)
  - [__doc__](treed-tree---tree.md#doc)
  - [__file__](treed-tree---tree.md#file)
  - [__loader__](treed-tree---tree.md#loader)
  - [__name__](treed-tree---tree.md#name)
  - [__package__](treed-tree---tree.md#package)
  - [__spec__](treed-tree---tree.md#spec)
  - [PathError](treed-tree-patherror.md#patherror)
    - [__cause__](treed-tree-patherror.md#cause)
    - [__context__](treed-tree-patherror.md#context)
    - [__delattr__](treed-tree-patherror.md#delattr)
    - [__dict__](treed-tree-patherror.md#dict)
    - [__dir__](treed-tree-patherror.md#dir)
    - [__doc__](treed-tree-patherror.md#doc)
    - [__eq__](treed-tree-patherror.md#eq)
    - [__format__](treed-tree-patherror.md#format)
    - [__ge__](treed-tree-patherror.md#ge)
    - [__getattribute__](treed-tree-patherror.md#getattribute)
    - [__getstate__](treed-tree-patherror.md#getstate)
    - [__gt__](treed-tree-patherror.md#gt)
    - [__hash__](treed-tree-patherror.md#hash)
    - [__init_subclass__](treed-tree-patherror.md#init_subclass)
    - [__le__](treed-tree-patherror.md#le)
    - [__lt__](treed-tree-patherror.md#lt)
    - [__module__](treed-tree-patherror.md#module)
    - [__ne__](treed-tree-patherror.md#ne)
    - [__new__](treed-tree-patherror.md#new)
    - [__reduce__](treed-tree-patherror.md#reduce)
    - [__reduce_ex__](treed-tree-patherror.md#reduce_ex)
    - [__repr__](treed-tree-patherror.md#repr)
    - [__setattr__](treed-tree-patherror.md#setattr)
    - [__setstate__](treed-tree-patherror.md#setstate)
    - [__sizeof__](treed-tree-patherror.md#sizeof)
    - [__str__](treed-tree-patherror.md#str)
    - [__subclasshook__](treed-tree-patherror.md#subclasshook)
    - [__suppress_context__](treed-tree-patherror.md#suppress_context)
    - [__traceback__](treed-tree-patherror.md#traceback)
    - [__weakref__](treed-tree-patherror.md#weakref)
    - [add_note](treed-tree-patherror.md#add_note)
    - [args](treed-tree-patherror.md#args)
    - [with_traceback](treed-tree-patherror.md#with_traceback)
  - [Tree](treed-tree-tree.md#tree)
    - [DOT](treed-tree-tree.md#dot)
    - [SEP](treed-tree-tree.md#sep)
    - [__delattr__](treed-tree-tree.md#delattr)
    - [__dict__](treed-tree-tree.md#dict)
    - [__dir__](treed-tree-tree.md#dir)
    - [__doc__](treed-tree-tree.md#doc)
    - [__eq__](treed-tree-tree.md#eq)
    - [__format__](treed-tree-tree.md#format)
    - [__ge__](treed-tree-tree.md#ge)
    - [__getattribute__](treed-tree-tree.md#getattribute)
    - [__getstate__](treed-tree-tree.md#getstate)
    - [__gt__](treed-tree-tree.md#gt)
    - [__hash__](treed-tree-tree.md#hash)
    - [__init_subclass__](treed-tree-tree.md#init_subclass)
    - [__le__](treed-tree-tree.md#le)
    - [__lt__](treed-tree-tree.md#lt)
    - [__module__](treed-tree-tree.md#module)
    - [__ne__](treed-tree-tree.md#ne)
    - [__new__](treed-tree-tree.md#new)
    - [__reduce__](treed-tree-tree.md#reduce)
    - [__reduce_ex__](treed-tree-tree.md#reduce_ex)
    - [__repr__](treed-tree-tree.md#repr)
    - [__setattr__](treed-tree-tree.md#setattr)
    - [__sizeof__](treed-tree-tree.md#sizeof)
    - [__subclasshook__](treed-tree-tree.md#subclasshook)
    - [__weakref__](treed-tree-tree.md#weakref)
    - [all_count](treed-tree-tree.md#all_count)
    - [count](treed-tree-tree.md#count)
    - [depth](treed-tree-tree.md#depth)
    - [is_top](treed-tree-tree.md#is_top)
    - [path](treed-tree-tree.md#path)
    - [top](treed-tree-tree.md#top)
    - [FromFile](treed-tree-tree.md#fromfile)
    - [FromInspect](treed-tree-tree.md#frominspect)
    - [Test](treed-tree-tree.md#test)
    - [__str__](treed-tree-tree.md#str)
    - [add](treed-tree-tree.md#add)
    - [all_items](treed-tree-tree.md#all_items)
    - [all_paths](treed-tree-tree.md#all_paths)
    - [all_values](treed-tree-tree.md#all_values)
    - [create_path](treed-tree-tree.md#create_path)
    - [find](treed-tree-tree.md#find)
    - [get](treed-tree-tree.md#get)
    - [get_child](treed-tree-tree.md#get_child)
    - [join_keys](treed-tree-tree.md#join_keys)
    - [new](treed-tree-tree.md#new)
    - [new_paths](treed-tree-tree.md#new_paths)
    - [set_child](treed-tree-tree.md#set_child)
    - [solve_path](treed-tree-tree.md#solve_path)
    - [solve_to_missing](treed-tree-tree.md#solve_to_missing)
    - [test](treed-tree-tree.md#test)
  - [TreeChain](treed-tree-treechain.md#treechain)
    - [DOT](treed-tree-treechain.md#dot)
    - [SEP](treed-tree-treechain.md#sep)
    - [__delattr__](treed-tree-treechain.md#delattr)
    - [__dict__](treed-tree-treechain.md#dict)
    - [__dir__](treed-tree-treechain.md#dir)
    - [__doc__](treed-tree-treechain.md#doc)
    - [__eq__](treed-tree-treechain.md#eq)
    - [__format__](treed-tree-treechain.md#format)
    - [__ge__](treed-tree-treechain.md#ge)
    - [__getattribute__](treed-tree-treechain.md#getattribute)
    - [__getstate__](treed-tree-treechain.md#getstate)
    - [__gt__](treed-tree-treechain.md#gt)
    - [__hash__](treed-tree-treechain.md#hash)
    - [__init_subclass__](treed-tree-treechain.md#init_subclass)
    - [__le__](treed-tree-treechain.md#le)
    - [__lt__](treed-tree-treechain.md#lt)
    - [__module__](treed-tree-treechain.md#module)
    - [__ne__](treed-tree-treechain.md#ne)
    - [__new__](treed-tree-treechain.md#new)
    - [__reduce__](treed-tree-treechain.md#reduce)
    - [__reduce_ex__](treed-tree-treechain.md#reduce_ex)
    - [__repr__](treed-tree-treechain.md#repr)
    - [__setattr__](treed-tree-treechain.md#setattr)
    - [__sizeof__](treed-tree-treechain.md#sizeof)
    - [__subclasshook__](treed-tree-treechain.md#subclasshook)
    - [__weakref__](treed-tree-treechain.md#weakref)
    - [all_count](treed-tree-treechain.md#all_count)
    - [count](treed-tree-treechain.md#count)
    - [depth](treed-tree-treechain.md#depth)
    - [is_top](treed-tree-treechain.md#is_top)
    - [last_child](treed-tree-treechain.md#last_child)
    - [path](treed-tree-treechain.md#path)
    - [top](treed-tree-treechain.md#top)
    - [FromFile](treed-tree-treechain.md#fromfile)
    - [FromInspect](treed-tree-treechain.md#frominspect)
    - [Test](treed-tree-treechain.md#test)
    - [__str__](treed-tree-treechain.md#str)
    - [add](treed-tree-treechain.md#add)
    - [all_items](treed-tree-treechain.md#all_items)
    - [all_paths](treed-tree-treechain.md#all_paths)
    - [all_values](treed-tree-treechain.md#all_values)
    - [create_path](treed-tree-treechain.md#create_path)
    - [find](treed-tree-treechain.md#find)
    - [get](treed-tree-treechain.md#get)
    - [get_child](treed-tree-treechain.md#get_child)
    - [items](treed-tree-treechain.md#items)
    - [join_keys](treed-tree-treechain.md#join_keys)
    - [keys](treed-tree-treechain.md#keys)
    - [new](treed-tree-treechain.md#new)
    - [new_paths](treed-tree-treechain.md#new_paths)
    - [set_child](treed-tree-treechain.md#set_child)
    - [solve_path](treed-tree-treechain.md#solve_path)
    - [solve_to_missing](treed-tree-treechain.md#solve_to_missing)
    - [sort](treed-tree-treechain.md#sort)
    - [test](treed-tree-treechain.md#test)
    - [values](treed-tree-treechain.md#values)
  - [TreeDict](treed-tree-treedict.md#treedict)
    - [DOT](treed-tree-treedict.md#dot)
    - [SEP](treed-tree-treedict.md#sep)
    - [__class_getitem__](treed-tree-treedict.md#class_getitem)
    - [__contains__](treed-tree-treedict.md#contains)
    - [__delattr__](treed-tree-treedict.md#delattr)
    - [__delitem__](treed-tree-treedict.md#delitem)
    - [__dict__](treed-tree-treedict.md#dict)
    - [__dir__](treed-tree-treedict.md#dir)
    - [__doc__](treed-tree-treedict.md#doc)
    - [__eq__](treed-tree-treedict.md#eq)
    - [__format__](treed-tree-treedict.md#format)
    - [__ge__](treed-tree-treedict.md#ge)
    - [__getattribute__](treed-tree-treedict.md#getattribute)
    - [__getstate__](treed-tree-treedict.md#getstate)
    - [__gt__](treed-tree-treedict.md#gt)
    - [__hash__](treed-tree-treedict.md#hash)
    - [__init_subclass__](treed-tree-treedict.md#init_subclass)
    - [__ior__](treed-tree-treedict.md#ior)
    - [__le__](treed-tree-treedict.md#le)
    - [__len__](treed-tree-treedict.md#len)
    - [__lt__](treed-tree-treedict.md#lt)
    - [__module__](treed-tree-treedict.md#module)
    - [__ne__](treed-tree-treedict.md#ne)
    - [__new__](treed-tree-treedict.md#new)
    - [__or__](treed-tree-treedict.md#or)
    - [__reduce__](treed-tree-treedict.md#reduce)
    - [__reduce_ex__](treed-tree-treedict.md#reduce_ex)
    - [__repr__](treed-tree-treedict.md#repr)
    - [__reversed__](treed-tree-treedict.md#reversed)
    - [__ror__](treed-tree-treedict.md#ror)
    - [__setattr__](treed-tree-treedict.md#setattr)
    - [__sizeof__](treed-tree-treedict.md#sizeof)
    - [__subclasshook__](treed-tree-treedict.md#subclasshook)
    - [__weakref__](treed-tree-treedict.md#weakref)
    - [all_count](treed-tree-treedict.md#all_count)
    - [clear](treed-tree-treedict.md#clear)
    - [copy](treed-tree-treedict.md#copy)
    - [count](treed-tree-treedict.md#count)
    - [depth](treed-tree-treedict.md#depth)
    - [fromkeys](treed-tree-treedict.md#fromkeys)
    - [is_top](treed-tree-treedict.md#is_top)
    - [items](treed-tree-treedict.md#items)
    - [key](treed-tree-treedict.md#key)
    - [keys](treed-tree-treedict.md#keys)
    - [path](treed-tree-treedict.md#path)
    - [pop](treed-tree-treedict.md#pop)
    - [popitem](treed-tree-treedict.md#popitem)
    - [setdefault](treed-tree-treedict.md#setdefault)
    - [top](treed-tree-treedict.md#top)
    - [update](treed-tree-treedict.md#update)
    - [values](treed-tree-treedict.md#values)
    - [FromFile](treed-tree-treedict.md#fromfile)
    - [FromInspect](treed-tree-treedict.md#frominspect)
    - [Test](treed-tree-treedict.md#test)
    - [__str__](treed-tree-treedict.md#str)
    - [add](treed-tree-treedict.md#add)
    - [all_items](treed-tree-treedict.md#all_items)
    - [all_paths](treed-tree-treedict.md#all_paths)
    - [all_values](treed-tree-treedict.md#all_values)
    - [create_path](treed-tree-treedict.md#create_path)
    - [find](treed-tree-treedict.md#find)
    - [get](treed-tree-treedict.md#get)
    - [get_child](treed-tree-treedict.md#get_child)
    - [join_keys](treed-tree-treedict.md#join_keys)
    - [new](treed-tree-treedict.md#new)
    - [new_paths](treed-tree-treedict.md#new_paths)
    - [set_child](treed-tree-treedict.md#set_child)
    - [solve_path](treed-tree-treedict.md#solve_path)
    - [solve_to_missing](treed-tree-treedict.md#solve_to_missing)
    - [test](treed-tree-treedict.md#test)
  - [TreeIterator](treed-tree-treeiterator.md#treeiterator)
    - [__delattr__](treed-tree-treeiterator.md#delattr)
    - [__dict__](treed-tree-treeiterator.md#dict)
    - [__dir__](treed-tree-treeiterator.md#dir)
    - [__doc__](treed-tree-treeiterator.md#doc)
    - [__eq__](treed-tree-treeiterator.md#eq)
    - [__format__](treed-tree-treeiterator.md#format)
    - [__ge__](treed-tree-treeiterator.md#ge)
    - [__getattribute__](treed-tree-treeiterator.md#getattribute)
    - [__getstate__](treed-tree-treeiterator.md#getstate)
    - [__gt__](treed-tree-treeiterator.md#gt)
    - [__hash__](treed-tree-treeiterator.md#hash)
    - [__init_subclass__](treed-tree-treeiterator.md#init_subclass)
    - [__le__](treed-tree-treeiterator.md#le)
    - [__lt__](treed-tree-treeiterator.md#lt)
    - [__module__](treed-tree-treeiterator.md#module)
    - [__ne__](treed-tree-treeiterator.md#ne)
    - [__new__](treed-tree-treeiterator.md#new)
    - [__reduce__](treed-tree-treeiterator.md#reduce)
    - [__reduce_ex__](treed-tree-treeiterator.md#reduce_ex)
    - [__repr__](treed-tree-treeiterator.md#repr)
    - [__setattr__](treed-tree-treeiterator.md#setattr)
    - [__sizeof__](treed-tree-treeiterator.md#sizeof)
    - [__str__](treed-tree-treeiterator.md#str)
    - [__subclasshook__](treed-tree-treeiterator.md#subclasshook)
    - [__weakref__](treed-tree-treeiterator.md#weakref)
    - [__iter__](treed-tree-treeiterator.md#iter)
    - [__next__](treed-tree-treeiterator.md#next)
    - [no_child](treed-tree-treeiterator.md#no_child)
  - [TreeList](treed-tree-treelist.md#treelist)
    - [DOT](treed-tree-treelist.md#dot)
    - [SEP](treed-tree-treelist.md#sep)
    - [__add__](treed-tree-treelist.md#add)
    - [__class_getitem__](treed-tree-treelist.md#class_getitem)
    - [__contains__](treed-tree-treelist.md#contains)
    - [__delattr__](treed-tree-treelist.md#delattr)
    - [__delitem__](treed-tree-treelist.md#delitem)
    - [__dict__](treed-tree-treelist.md#dict)
    - [__dir__](treed-tree-treelist.md#dir)
    - [__doc__](treed-tree-treelist.md#doc)
    - [__eq__](treed-tree-treelist.md#eq)
    - [__format__](treed-tree-treelist.md#format)
    - [__ge__](treed-tree-treelist.md#ge)
    - [__getattribute__](treed-tree-treelist.md#getattribute)
    - [__getstate__](treed-tree-treelist.md#getstate)
    - [__gt__](treed-tree-treelist.md#gt)
    - [__hash__](treed-tree-treelist.md#hash)
    - [__iadd__](treed-tree-treelist.md#iadd)
    - [__imul__](treed-tree-treelist.md#imul)
    - [__init_subclass__](treed-tree-treelist.md#init_subclass)
    - [__le__](treed-tree-treelist.md#le)
    - [__len__](treed-tree-treelist.md#len)
    - [__lt__](treed-tree-treelist.md#lt)
    - [__module__](treed-tree-treelist.md#module)
    - [__mul__](treed-tree-treelist.md#mul)
    - [__ne__](treed-tree-treelist.md#ne)
    - [__new__](treed-tree-treelist.md#new)
    - [__reduce__](treed-tree-treelist.md#reduce)
    - [__reduce_ex__](treed-tree-treelist.md#reduce_ex)
    - [__repr__](treed-tree-treelist.md#repr)
    - [__reversed__](treed-tree-treelist.md#reversed)
    - [__rmul__](treed-tree-treelist.md#rmul)
    - [__setattr__](treed-tree-treelist.md#setattr)
    - [__sizeof__](treed-tree-treelist.md#sizeof)
    - [__subclasshook__](treed-tree-treelist.md#subclasshook)
    - [__weakref__](treed-tree-treelist.md#weakref)
    - [all_count](treed-tree-treelist.md#all_count)
    - [append](treed-tree-treelist.md#append)
    - [clear](treed-tree-treelist.md#clear)
    - [copy](treed-tree-treelist.md#copy)
    - [count](treed-tree-treelist.md#count)
    - [depth](treed-tree-treelist.md#depth)
    - [extend](treed-tree-treelist.md#extend)
    - [index](treed-tree-treelist.md#index)
    - [insert](treed-tree-treelist.md#insert)
    - [is_top](treed-tree-treelist.md#is_top)
    - [path](treed-tree-treelist.md#path)
    - [pop](treed-tree-treelist.md#pop)
    - [remove](treed-tree-treelist.md#remove)
    - [reverse](treed-tree-treelist.md#reverse)
    - [sort](treed-tree-treelist.md#sort)
    - [top](treed-tree-treelist.md#top)
    - [FromFile](treed-tree-treelist.md#fromfile)
    - [FromInspect](treed-tree-treelist.md#frominspect)
    - [Test](treed-tree-treelist.md#test)
    - [__str__](treed-tree-treelist.md#str)
    - [add](treed-tree-treelist.md#add)
    - [all_items](treed-tree-treelist.md#all_items)
    - [all_paths](treed-tree-treelist.md#all_paths)
    - [all_values](treed-tree-treelist.md#all_values)
    - [create_path](treed-tree-treelist.md#create_path)
    - [find](treed-tree-treelist.md#find)
    - [get](treed-tree-treelist.md#get)
    - [get_child](treed-tree-treelist.md#get_child)
    - [items](treed-tree-treelist.md#items)
    - [join_keys](treed-tree-treelist.md#join_keys)
    - [keys](treed-tree-treelist.md#keys)
    - [new](treed-tree-treelist.md#new)
    - [new_paths](treed-tree-treelist.md#new_paths)
    - [set_child](treed-tree-treelist.md#set_child)
    - [solve_path](treed-tree-treelist.md#solve_path)
    - [solve_to_missing](treed-tree-treelist.md#solve_to_missing)
    - [test](treed-tree-treelist.md#test)
    - [values](treed-tree-treelist.md#values)
  - [demo_no_child](treed-tree---tree.md#demo_no_child)
  - [pprint](treed-tree---tree.md#pprint)


## Global variables

### Content

- [__builtins__](treed---treedict.md#builtins)
- [__cached__](treed---treedict.md#cached)
- [__doc__](treed---treedict.md#doc)
- [__file__](treed---treedict.md#file)
- [__loader__](treed---treedict.md#loader)
- [__name__](treed---treedict.md#name)
- [__package__](treed---treedict.md#package)
- [__path__](treed---treedict.md#path)
- [__spec__](treed---treedict.md#spec)


### __builtins__


> type dict ( = {'__name__': 'builtins', '__do...)



### __cached__


> type str ( = /Users/alain/Documents/blender...)



### __doc__


> type str ( = 
Created on Mon Sep 16 12:22:4...)



### __file__


> type str ( = /Users/alain/Documents/blender...)



### __loader__


> type SourceFileLoader ( = <_frozen_importlib_external.So...)



### __name__


> type str ( = treedict)



### __package__


> type str ( = treedict)



### __path__


> type list ( = ['/Users/alain/Documents/blend...)



### __spec__


> type ModuleSpec ( = ModuleSpec(name='treedict', lo...)



## Functions

### Content

- [tree](treed-tree---tree.md#tree)
- [__builtins__](treed-tree---tree.md#builtins)
- [__cached__](treed-tree---tree.md#cached)
- [__doc__](treed-tree---tree.md#doc)
- [__file__](treed-tree---tree.md#file)
- [__loader__](treed-tree---tree.md#loader)
- [__name__](treed-tree---tree.md#name)
- [__package__](treed-tree---tree.md#package)
- [__spec__](treed-tree---tree.md#spec)
- [PathError](treed-tree-patherror.md#patherror)
  - [__cause__](treed-tree-patherror.md#cause)
  - [__context__](treed-tree-patherror.md#context)
  - [__delattr__](treed-tree-patherror.md#delattr)
  - [__dict__](treed-tree-patherror.md#dict)
  - [__dir__](treed-tree-patherror.md#dir)
  - [__doc__](treed-tree-patherror.md#doc)
  - [__eq__](treed-tree-patherror.md#eq)
  - [__format__](treed-tree-patherror.md#format)
  - [__ge__](treed-tree-patherror.md#ge)
  - [__getattribute__](treed-tree-patherror.md#getattribute)
  - [__getstate__](treed-tree-patherror.md#getstate)
  - [__gt__](treed-tree-patherror.md#gt)
  - [__hash__](treed-tree-patherror.md#hash)
  - [__init_subclass__](treed-tree-patherror.md#init_subclass)
  - [__le__](treed-tree-patherror.md#le)
  - [__lt__](treed-tree-patherror.md#lt)
  - [__module__](treed-tree-patherror.md#module)
  - [__ne__](treed-tree-patherror.md#ne)
  - [__new__](treed-tree-patherror.md#new)
  - [__reduce__](treed-tree-patherror.md#reduce)
  - [__reduce_ex__](treed-tree-patherror.md#reduce_ex)
  - [__repr__](treed-tree-patherror.md#repr)
  - [__setattr__](treed-tree-patherror.md#setattr)
  - [__setstate__](treed-tree-patherror.md#setstate)
  - [__sizeof__](treed-tree-patherror.md#sizeof)
  - [__str__](treed-tree-patherror.md#str)
  - [__subclasshook__](treed-tree-patherror.md#subclasshook)
  - [__suppress_context__](treed-tree-patherror.md#suppress_context)
  - [__traceback__](treed-tree-patherror.md#traceback)
  - [__weakref__](treed-tree-patherror.md#weakref)
  - [add_note](treed-tree-patherror.md#add_note)
  - [args](treed-tree-patherror.md#args)
  - [with_traceback](treed-tree-patherror.md#with_traceback)
- [Tree](treed-tree-tree.md#tree)
  - [DOT](treed-tree-tree.md#dot)
  - [SEP](treed-tree-tree.md#sep)
  - [__delattr__](treed-tree-tree.md#delattr)
  - [__dict__](treed-tree-tree.md#dict)
  - [__dir__](treed-tree-tree.md#dir)
  - [__doc__](treed-tree-tree.md#doc)
  - [__eq__](treed-tree-tree.md#eq)
  - [__format__](treed-tree-tree.md#format)
  - [__ge__](treed-tree-tree.md#ge)
  - [__getattribute__](treed-tree-tree.md#getattribute)
  - [__getstate__](treed-tree-tree.md#getstate)
  - [__gt__](treed-tree-tree.md#gt)
  - [__hash__](treed-tree-tree.md#hash)
  - [__init_subclass__](treed-tree-tree.md#init_subclass)
  - [__le__](treed-tree-tree.md#le)
  - [__lt__](treed-tree-tree.md#lt)
  - [__module__](treed-tree-tree.md#module)
  - [__ne__](treed-tree-tree.md#ne)
  - [__new__](treed-tree-tree.md#new)
  - [__reduce__](treed-tree-tree.md#reduce)
  - [__reduce_ex__](treed-tree-tree.md#reduce_ex)
  - [__repr__](treed-tree-tree.md#repr)
  - [__setattr__](treed-tree-tree.md#setattr)
  - [__sizeof__](treed-tree-tree.md#sizeof)
  - [__subclasshook__](treed-tree-tree.md#subclasshook)
  - [__weakref__](treed-tree-tree.md#weakref)
  - [all_count](treed-tree-tree.md#all_count)
  - [count](treed-tree-tree.md#count)
  - [depth](treed-tree-tree.md#depth)
  - [is_top](treed-tree-tree.md#is_top)
  - [path](treed-tree-tree.md#path)
  - [top](treed-tree-tree.md#top)
  - [FromFile](treed-tree-tree.md#fromfile)
  - [FromInspect](treed-tree-tree.md#frominspect)
  - [Test](treed-tree-tree.md#test)
  - [__str__](treed-tree-tree.md#str)
  - [add](treed-tree-tree.md#add)
  - [all_items](treed-tree-tree.md#all_items)
  - [all_paths](treed-tree-tree.md#all_paths)
  - [all_values](treed-tree-tree.md#all_values)
  - [create_path](treed-tree-tree.md#create_path)
  - [find](treed-tree-tree.md#find)
  - [get](treed-tree-tree.md#get)
  - [get_child](treed-tree-tree.md#get_child)
  - [join_keys](treed-tree-tree.md#join_keys)
  - [new](treed-tree-tree.md#new)
  - [new_paths](treed-tree-tree.md#new_paths)
  - [set_child](treed-tree-tree.md#set_child)
  - [solve_path](treed-tree-tree.md#solve_path)
  - [solve_to_missing](treed-tree-tree.md#solve_to_missing)
  - [test](treed-tree-tree.md#test)
- [TreeChain](treed-tree-treechain.md#treechain)
  - [DOT](treed-tree-treechain.md#dot)
  - [SEP](treed-tree-treechain.md#sep)
  - [__delattr__](treed-tree-treechain.md#delattr)
  - [__dict__](treed-tree-treechain.md#dict)
  - [__dir__](treed-tree-treechain.md#dir)
  - [__doc__](treed-tree-treechain.md#doc)
  - [__eq__](treed-tree-treechain.md#eq)
  - [__format__](treed-tree-treechain.md#format)
  - [__ge__](treed-tree-treechain.md#ge)
  - [__getattribute__](treed-tree-treechain.md#getattribute)
  - [__getstate__](treed-tree-treechain.md#getstate)
  - [__gt__](treed-tree-treechain.md#gt)
  - [__hash__](treed-tree-treechain.md#hash)
  - [__init_subclass__](treed-tree-treechain.md#init_subclass)
  - [__le__](treed-tree-treechain.md#le)
  - [__lt__](treed-tree-treechain.md#lt)
  - [__module__](treed-tree-treechain.md#module)
  - [__ne__](treed-tree-treechain.md#ne)
  - [__new__](treed-tree-treechain.md#new)
  - [__reduce__](treed-tree-treechain.md#reduce)
  - [__reduce_ex__](treed-tree-treechain.md#reduce_ex)
  - [__repr__](treed-tree-treechain.md#repr)
  - [__setattr__](treed-tree-treechain.md#setattr)
  - [__sizeof__](treed-tree-treechain.md#sizeof)
  - [__subclasshook__](treed-tree-treechain.md#subclasshook)
  - [__weakref__](treed-tree-treechain.md#weakref)
  - [all_count](treed-tree-treechain.md#all_count)
  - [count](treed-tree-treechain.md#count)
  - [depth](treed-tree-treechain.md#depth)
  - [is_top](treed-tree-treechain.md#is_top)
  - [last_child](treed-tree-treechain.md#last_child)
  - [path](treed-tree-treechain.md#path)
  - [top](treed-tree-treechain.md#top)
  - [FromFile](treed-tree-treechain.md#fromfile)
  - [FromInspect](treed-tree-treechain.md#frominspect)
  - [Test](treed-tree-treechain.md#test)
  - [__str__](treed-tree-treechain.md#str)
  - [add](treed-tree-treechain.md#add)
  - [all_items](treed-tree-treechain.md#all_items)
  - [all_paths](treed-tree-treechain.md#all_paths)
  - [all_values](treed-tree-treechain.md#all_values)
  - [create_path](treed-tree-treechain.md#create_path)
  - [find](treed-tree-treechain.md#find)
  - [get](treed-tree-treechain.md#get)
  - [get_child](treed-tree-treechain.md#get_child)
  - [items](treed-tree-treechain.md#items)
  - [join_keys](treed-tree-treechain.md#join_keys)
  - [keys](treed-tree-treechain.md#keys)
  - [new](treed-tree-treechain.md#new)
  - [new_paths](treed-tree-treechain.md#new_paths)
  - [set_child](treed-tree-treechain.md#set_child)
  - [solve_path](treed-tree-treechain.md#solve_path)
  - [solve_to_missing](treed-tree-treechain.md#solve_to_missing)
  - [sort](treed-tree-treechain.md#sort)
  - [test](treed-tree-treechain.md#test)
  - [values](treed-tree-treechain.md#values)
- [TreeDict](treed-tree-treedict.md#treedict)
  - [DOT](treed-tree-treedict.md#dot)
  - [SEP](treed-tree-treedict.md#sep)
  - [__class_getitem__](treed-tree-treedict.md#class_getitem)
  - [__contains__](treed-tree-treedict.md#contains)
  - [__delattr__](treed-tree-treedict.md#delattr)
  - [__delitem__](treed-tree-treedict.md#delitem)
  - [__dict__](treed-tree-treedict.md#dict)
  - [__dir__](treed-tree-treedict.md#dir)
  - [__doc__](treed-tree-treedict.md#doc)
  - [__eq__](treed-tree-treedict.md#eq)
  - [__format__](treed-tree-treedict.md#format)
  - [__ge__](treed-tree-treedict.md#ge)
  - [__getattribute__](treed-tree-treedict.md#getattribute)
  - [__getstate__](treed-tree-treedict.md#getstate)
  - [__gt__](treed-tree-treedict.md#gt)
  - [__hash__](treed-tree-treedict.md#hash)
  - [__init_subclass__](treed-tree-treedict.md#init_subclass)
  - [__ior__](treed-tree-treedict.md#ior)
  - [__le__](treed-tree-treedict.md#le)
  - [__len__](treed-tree-treedict.md#len)
  - [__lt__](treed-tree-treedict.md#lt)
  - [__module__](treed-tree-treedict.md#module)
  - [__ne__](treed-tree-treedict.md#ne)
  - [__new__](treed-tree-treedict.md#new)
  - [__or__](treed-tree-treedict.md#or)
  - [__reduce__](treed-tree-treedict.md#reduce)
  - [__reduce_ex__](treed-tree-treedict.md#reduce_ex)
  - [__repr__](treed-tree-treedict.md#repr)
  - [__reversed__](treed-tree-treedict.md#reversed)
  - [__ror__](treed-tree-treedict.md#ror)
  - [__setattr__](treed-tree-treedict.md#setattr)
  - [__sizeof__](treed-tree-treedict.md#sizeof)
  - [__subclasshook__](treed-tree-treedict.md#subclasshook)
  - [__weakref__](treed-tree-treedict.md#weakref)
  - [all_count](treed-tree-treedict.md#all_count)
  - [clear](treed-tree-treedict.md#clear)
  - [copy](treed-tree-treedict.md#copy)
  - [count](treed-tree-treedict.md#count)
  - [depth](treed-tree-treedict.md#depth)
  - [fromkeys](treed-tree-treedict.md#fromkeys)
  - [is_top](treed-tree-treedict.md#is_top)
  - [items](treed-tree-treedict.md#items)
  - [key](treed-tree-treedict.md#key)
  - [keys](treed-tree-treedict.md#keys)
  - [path](treed-tree-treedict.md#path)
  - [pop](treed-tree-treedict.md#pop)
  - [popitem](treed-tree-treedict.md#popitem)
  - [setdefault](treed-tree-treedict.md#setdefault)
  - [top](treed-tree-treedict.md#top)
  - [update](treed-tree-treedict.md#update)
  - [values](treed-tree-treedict.md#values)
  - [FromFile](treed-tree-treedict.md#fromfile)
  - [FromInspect](treed-tree-treedict.md#frominspect)
  - [Test](treed-tree-treedict.md#test)
  - [__str__](treed-tree-treedict.md#str)
  - [add](treed-tree-treedict.md#add)
  - [all_items](treed-tree-treedict.md#all_items)
  - [all_paths](treed-tree-treedict.md#all_paths)
  - [all_values](treed-tree-treedict.md#all_values)
  - [create_path](treed-tree-treedict.md#create_path)
  - [find](treed-tree-treedict.md#find)
  - [get](treed-tree-treedict.md#get)
  - [get_child](treed-tree-treedict.md#get_child)
  - [join_keys](treed-tree-treedict.md#join_keys)
  - [new](treed-tree-treedict.md#new)
  - [new_paths](treed-tree-treedict.md#new_paths)
  - [set_child](treed-tree-treedict.md#set_child)
  - [solve_path](treed-tree-treedict.md#solve_path)
  - [solve_to_missing](treed-tree-treedict.md#solve_to_missing)
  - [test](treed-tree-treedict.md#test)
- [TreeIterator](treed-tree-treeiterator.md#treeiterator)
  - [__delattr__](treed-tree-treeiterator.md#delattr)
  - [__dict__](treed-tree-treeiterator.md#dict)
  - [__dir__](treed-tree-treeiterator.md#dir)
  - [__doc__](treed-tree-treeiterator.md#doc)
  - [__eq__](treed-tree-treeiterator.md#eq)
  - [__format__](treed-tree-treeiterator.md#format)
  - [__ge__](treed-tree-treeiterator.md#ge)
  - [__getattribute__](treed-tree-treeiterator.md#getattribute)
  - [__getstate__](treed-tree-treeiterator.md#getstate)
  - [__gt__](treed-tree-treeiterator.md#gt)
  - [__hash__](treed-tree-treeiterator.md#hash)
  - [__init_subclass__](treed-tree-treeiterator.md#init_subclass)
  - [__le__](treed-tree-treeiterator.md#le)
  - [__lt__](treed-tree-treeiterator.md#lt)
  - [__module__](treed-tree-treeiterator.md#module)
  - [__ne__](treed-tree-treeiterator.md#ne)
  - [__new__](treed-tree-treeiterator.md#new)
  - [__reduce__](treed-tree-treeiterator.md#reduce)
  - [__reduce_ex__](treed-tree-treeiterator.md#reduce_ex)
  - [__repr__](treed-tree-treeiterator.md#repr)
  - [__setattr__](treed-tree-treeiterator.md#setattr)
  - [__sizeof__](treed-tree-treeiterator.md#sizeof)
  - [__str__](treed-tree-treeiterator.md#str)
  - [__subclasshook__](treed-tree-treeiterator.md#subclasshook)
  - [__weakref__](treed-tree-treeiterator.md#weakref)
  - [__iter__](treed-tree-treeiterator.md#iter)
  - [__next__](treed-tree-treeiterator.md#next)
  - [no_child](treed-tree-treeiterator.md#no_child)
- [TreeList](treed-tree-treelist.md#treelist)
  - [DOT](treed-tree-treelist.md#dot)
  - [SEP](treed-tree-treelist.md#sep)
  - [__add__](treed-tree-treelist.md#add)
  - [__class_getitem__](treed-tree-treelist.md#class_getitem)
  - [__contains__](treed-tree-treelist.md#contains)
  - [__delattr__](treed-tree-treelist.md#delattr)
  - [__delitem__](treed-tree-treelist.md#delitem)
  - [__dict__](treed-tree-treelist.md#dict)
  - [__dir__](treed-tree-treelist.md#dir)
  - [__doc__](treed-tree-treelist.md#doc)
  - [__eq__](treed-tree-treelist.md#eq)
  - [__format__](treed-tree-treelist.md#format)
  - [__ge__](treed-tree-treelist.md#ge)
  - [__getattribute__](treed-tree-treelist.md#getattribute)
  - [__getstate__](treed-tree-treelist.md#getstate)
  - [__gt__](treed-tree-treelist.md#gt)
  - [__hash__](treed-tree-treelist.md#hash)
  - [__iadd__](treed-tree-treelist.md#iadd)
  - [__imul__](treed-tree-treelist.md#imul)
  - [__init_subclass__](treed-tree-treelist.md#init_subclass)
  - [__le__](treed-tree-treelist.md#le)
  - [__len__](treed-tree-treelist.md#len)
  - [__lt__](treed-tree-treelist.md#lt)
  - [__module__](treed-tree-treelist.md#module)
  - [__mul__](treed-tree-treelist.md#mul)
  - [__ne__](treed-tree-treelist.md#ne)
  - [__new__](treed-tree-treelist.md#new)
  - [__reduce__](treed-tree-treelist.md#reduce)
  - [__reduce_ex__](treed-tree-treelist.md#reduce_ex)
  - [__repr__](treed-tree-treelist.md#repr)
  - [__reversed__](treed-tree-treelist.md#reversed)
  - [__rmul__](treed-tree-treelist.md#rmul)
  - [__setattr__](treed-tree-treelist.md#setattr)
  - [__sizeof__](treed-tree-treelist.md#sizeof)
  - [__subclasshook__](treed-tree-treelist.md#subclasshook)
  - [__weakref__](treed-tree-treelist.md#weakref)
  - [all_count](treed-tree-treelist.md#all_count)
  - [append](treed-tree-treelist.md#append)
  - [clear](treed-tree-treelist.md#clear)
  - [copy](treed-tree-treelist.md#copy)
  - [count](treed-tree-treelist.md#count)
  - [depth](treed-tree-treelist.md#depth)
  - [extend](treed-tree-treelist.md#extend)
  - [index](treed-tree-treelist.md#index)
  - [insert](treed-tree-treelist.md#insert)
  - [is_top](treed-tree-treelist.md#is_top)
  - [path](treed-tree-treelist.md#path)
  - [pop](treed-tree-treelist.md#pop)
  - [remove](treed-tree-treelist.md#remove)
  - [reverse](treed-tree-treelist.md#reverse)
  - [sort](treed-tree-treelist.md#sort)
  - [top](treed-tree-treelist.md#top)
  - [FromFile](treed-tree-treelist.md#fromfile)
  - [FromInspect](treed-tree-treelist.md#frominspect)
  - [Test](treed-tree-treelist.md#test)
  - [__str__](treed-tree-treelist.md#str)
  - [add](treed-tree-treelist.md#add)
  - [all_items](treed-tree-treelist.md#all_items)
  - [all_paths](treed-tree-treelist.md#all_paths)
  - [all_values](treed-tree-treelist.md#all_values)
  - [create_path](treed-tree-treelist.md#create_path)
  - [find](treed-tree-treelist.md#find)
  - [get](treed-tree-treelist.md#get)
  - [get_child](treed-tree-treelist.md#get_child)
  - [items](treed-tree-treelist.md#items)
  - [join_keys](treed-tree-treelist.md#join_keys)
  - [keys](treed-tree-treelist.md#keys)
  - [new](treed-tree-treelist.md#new)
  - [new_paths](treed-tree-treelist.md#new_paths)
  - [set_child](treed-tree-treelist.md#set_child)
  - [solve_path](treed-tree-treelist.md#solve_path)
  - [solve_to_missing](treed-tree-treelist.md#solve_to_missing)
  - [test](treed-tree-treelist.md#test)
  - [values](treed-tree-treelist.md#values)
- [demo_no_child](treed-tree---tree.md#demo_no_child)
- [pprint](treed-tree---tree.md#pprint)

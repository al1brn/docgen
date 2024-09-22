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

- [tree](treed-tree---tree.md#tree)
- [PathError](treed-tree-patherror.md#patherror)
- [Tree](treed-tree-tree.md#tree)
  - [DOT](treed-tree-tree.md#dot)
  - [SEP](treed-tree-tree.md#sep)
  - [FromFile](treed-tree-tree.md#fromfile)
  - [FromInspect](treed-tree-tree.md#frominspect)
  - [Test](treed-tree-tree.md#test)
  - [\_\_str__](treed-tree-tree.md#__str__)
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
  - [FromFile](treed-tree-treechain.md#fromfile)
  - [FromInspect](treed-tree-treechain.md#frominspect)
  - [Test](treed-tree-treechain.md#test)
  - [\_\_str__](treed-tree-treechain.md#__str__)
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
  - [FromFile](treed-tree-treedict.md#fromfile)
  - [FromInspect](treed-tree-treedict.md#frominspect)
  - [Test](treed-tree-treedict.md#test)
  - [\_\_str__](treed-tree-treedict.md#__str__)
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
  - [\_\_iter__](treed-tree-treeiterator.md#__iter__)
  - [\_\_next__](treed-tree-treeiterator.md#__next__)
  - [no_child](treed-tree-treeiterator.md#no_child)
- [TreeList](treed-tree-treelist.md#treelist)
  - [DOT](treed-tree-treelist.md#dot)
  - [SEP](treed-tree-treelist.md#sep)
  - [FromFile](treed-tree-treelist.md#fromfile)
  - [FromInspect](treed-tree-treelist.md#frominspect)
  - [Test](treed-tree-treelist.md#test)
  - [\_\_str__](treed-tree-treelist.md#__str__)
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


## Functions

### Content

- [tree](treed-tree---tree.md#tree)
- [PathError](treed-tree-patherror.md#patherror)
- [Tree](treed-tree-tree.md#tree)
  - [DOT](treed-tree-tree.md#dot)
  - [SEP](treed-tree-tree.md#sep)
  - [FromFile](treed-tree-tree.md#fromfile)
  - [FromInspect](treed-tree-tree.md#frominspect)
  - [Test](treed-tree-tree.md#test)
  - [\_\_str__](treed-tree-tree.md#__str__)
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
  - [FromFile](treed-tree-treechain.md#fromfile)
  - [FromInspect](treed-tree-treechain.md#frominspect)
  - [Test](treed-tree-treechain.md#test)
  - [\_\_str__](treed-tree-treechain.md#__str__)
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
  - [FromFile](treed-tree-treedict.md#fromfile)
  - [FromInspect](treed-tree-treedict.md#frominspect)
  - [Test](treed-tree-treedict.md#test)
  - [\_\_str__](treed-tree-treedict.md#__str__)
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
  - [\_\_iter__](treed-tree-treeiterator.md#__iter__)
  - [\_\_next__](treed-tree-treeiterator.md#__next__)
  - [no_child](treed-tree-treeiterator.md#no_child)
- [TreeList](treed-tree-treelist.md#treelist)
  - [DOT](treed-tree-treelist.md#dot)
  - [SEP](treed-tree-treelist.md#sep)
  - [FromFile](treed-tree-treelist.md#fromfile)
  - [FromInspect](treed-tree-treelist.md#frominspect)
  - [Test](treed-tree-treelist.md#test)
  - [\_\_str__](treed-tree-treelist.md#__str__)
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

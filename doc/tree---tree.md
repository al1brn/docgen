# tree

This module contains interface classes to implement tree hierarchy.

If comes with the root abstract interface [Tree](tree-tree.md) and 3 useable child classes [TreeDict](tree-treedict.md), [TreeList](tree-treelist.md) and [TreeChain](tree-treechain.md)
implementing the abstract methods respectively with a dict, a list and [child](tree-treechain.md#child)  [next](tree-treechain.md#next) chaining
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

A child, or a list of children can be found with [find](tree-tree.md#find) method:
    
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
- remove_from_parent(method) : remove the section from its parent list of children
- create_child (method) : create a new child
- values (method) : returns an iterator on the direct children
- keys (method) : returns an iterator on the keys of the direct children
- items (method) : returns an iterator on the (key, child) pairs of the direct children

### Implementation

#### With a dict

[TreeDict](tree-treedict.md) inherits from [Tree](tree-tree.md) and dict. Direct children are managed from dict inheritance.

This implementation can be chosen when direct child keys must be unique and when there is no
particular need in controlling the order of the children.

#### With a list

[TreeList](tree-treelist.md) inherits from [Tree](tree-tree.md) and list. Direct children are store in the list.

Several children can share the same key.

This implementation can be chosen when direct children can share a same key and / or when there is
a need to control the order of the children

#### Chaining implementation

[TreeChain](tree-treechain.md) implements directly the interface by chaining the nodes with [child](tree-treechain.md#child) and [next](tree-treechain.md#next)
properties:
- **child** : first child, the node has no children if Node
- **next** : next child in the collection of parent children, last child if None

Not sure if this implementation is better than one of the two above!

#### Testing

Testing can be made with [impossible to find the section 'test' in page 'Tree'](tree-tree.md) method which provides basic testing.

One can also call [impossible to find the section 'FromFolder' in page 'Tree'](tree-tree.md) and [impossible to find the section 'FromModule' in page 'Tree'](tree-tree.md) which respectively create
a full tree from a disk folder and from python module.

## Content

- [PathError](tree-patherror.md)
- [Tree](tree-tree.md)
  - [all_count](tree-tree.md#all_count)
  - [count](tree-tree.md#count)
  - [depth](tree-tree.md#depth)
  - [is_top](tree-tree.md#is_top)
  - [key](tree-tree.md#key)
  - [parent](tree-tree.md#parent)
  - [path](tree-tree.md#path)
  - [top](tree-tree.md#top)
  - [add](tree-tree.md#add)
  - [all_items](tree-tree.md#all_items)
  - [all_paths](tree-tree.md#all_paths)
  - [all_values](tree-tree.md#all_values)
  - [create_path](tree-tree.md#create_path)
  - [detach](tree-tree.md#detach)
  - [find](tree-tree.md#find)
  - [FromFile](tree-tree.md#fromfile)
  - [FromInspect](tree-tree.md#frominspect)
  - [get](tree-tree.md#get)
  - [get_child](tree-tree.md#get_child)
  - [join_keys](tree-tree.md#join_keys)
  - [move_to_parent](tree-tree.md#move_to_parent)
  - [new](tree-tree.md#new)
  - [new_paths](tree-tree.md#new_paths)
  - [remove_from_parent](tree-tree.md#remove_from_parent)
  - [set_child](tree-tree.md#set_child)
  - [solve_path](tree-tree.md#solve_path)
  - [solve_to_missing](tree-tree.md#solve_to_missing)
- [TreeChain](tree-treechain.md)
  - [all_count](tree-treechain.md#all_count)
  - [child](tree-treechain.md#child)
  - [count](tree-treechain.md#count)
  - [depth](tree-treechain.md#depth)
  - [is_top](tree-treechain.md#is_top)
  - [next](tree-treechain.md#next)
  - [path](tree-treechain.md#path)
  - [top](tree-treechain.md#top)
  - [add](tree-treechain.md#add)
  - [all_items](tree-treechain.md#all_items)
  - [all_paths](tree-treechain.md#all_paths)
  - [all_values](tree-treechain.md#all_values)
  - [create_path](tree-treechain.md#create_path)
  - [detach](tree-treechain.md#detach)
  - [find](tree-treechain.md#find)
  - [FromFile](tree-treechain.md#fromfile)
  - [FromInspect](tree-treechain.md#frominspect)
  - [get](tree-treechain.md#get)
  - [get_child](tree-treechain.md#get_child)
  - [items](tree-treechain.md#items)
  - [join_keys](tree-treechain.md#join_keys)
  - [keys](tree-treechain.md#keys)
  - [move_to_parent](tree-treechain.md#move_to_parent)
  - [new](tree-treechain.md#new)
  - [new_paths](tree-treechain.md#new_paths)
  - [remove_from_parent](tree-treechain.md#remove_from_parent)
  - [set_child](tree-treechain.md#set_child)
  - [solve_path](tree-treechain.md#solve_path)
  - [solve_to_missing](tree-treechain.md#solve_to_missing)
  - [sort](tree-treechain.md#sort)
  - [values](tree-treechain.md#values)
- [TreeDict](tree-treedict.md)
  - [key](tree-treedict.md#key)
  - [get_child](tree-treedict.md#get_child)
  - [remove_from_parent](tree-treedict.md#remove_from_parent)
  - [set_child](tree-treedict.md#set_child)
- [TreeIterator](tree-treeiterator.md)
  - [\_\_iter__](tree-treeiterator.md#__iter__)
  - [\_\_next__](tree-treeiterator.md#__next__)
  - [no_child](tree-treeiterator.md#no_child)
- [TreeList](tree-treelist.md)
  - [get_child](tree-treelist.md#get_child)
  - [items](tree-treelist.md#items)
  - [keys](tree-treelist.md#keys)
  - [remove_from_parent](tree-treelist.md#remove_from_parent)
  - [set_child](tree-treelist.md#set_child)
  - [values](tree-treelist.md#values)

## Classes



- [PathError](tree-patherror.md)
- [Tree](tree-tree.md)
- [TreeChain](tree-treechain.md)
- [TreeDict](tree-treedict.md)
- [TreeIterator](tree-treeiterator.md)
- [TreeList](tree-treelist.md)

<sub>:arrow_right: [docgen](index.md) :black_small_square: [tree](tree---tree.md) :black_small_square: [Content](tree---tree.md#content) :black_small_square: [tree](tree---tree.md)</sub>
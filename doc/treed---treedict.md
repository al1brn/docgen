# treedict


This module contains interface classes to implement tree hierarchy.

If comes with the root abstract interface <!Tree> and 3 useable child classes <!TreeDict>, <!TreeList> and <!TreeChain>
implementing the abstract methods respectively with a dict, a list and <!TreeChain#child>  <!TreeChain#next> chaining
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

A child, or a list of children can be found with <#find> method:
    
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

<!TreeDict> inherits from <!Tree> and dict. Direct children are managed from dict inheritance.

This implementation can be chosen when direct child keys must be unique and when there is no
particular need in controlling the order of the children.

#### With a list

<!TreeList> inherits from <!Tree> and list. Direct children are store in the list.

Several children can share the same key.

This implementation can be chosen when direct children can share a same key and / or when there is
a need to control the order of the children

#### Chaining implementation

<!TreeChain> implements directly the interface by chaining the nodes with <!TreeChain#child> and <!TreeChain#next>
properties:
- **child** : first child, the node has no children if Node
- **next** : next child in the collection of parent children, last child if None

Not sure if this implementation is better than one of the two above!

#### Testing

Testing can be made with <!Tree#test> method which provides basic testing.

One can also call <!Tree#FromFolder> and <!Tree#FromModule> which respectively create
a full tree from a disk folder and from python module.



## Global variables

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


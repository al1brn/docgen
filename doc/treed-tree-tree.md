#Tree

Tree interface

This abstract class exposes an interface for a tree.

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

### Abstract methods

Actual implementation of a Tree requires the following properties and methods:

- key (str property) : the key of the node
- get_child (method) : get a direct child by its key
- set_child (method) : insert a child in the collection of direct children
- values (method) : returns an iterator on the direct children
- keys (method) : returns an iterator on the keys of the direct children
- items (method) : returns an iterator on the (key, child) pairs of the direct children


### Creating a whole tree

A tree can be created using the [add](#add) method with the following pseudo code:
    
``` python
class MyTree(TreeDict): # of TreeList or TreeChain or your own implementation
    def __init__(self, source):
        # Initialize self from source content
        ...
        
        # Loop on source children
        for key, child in source:
            self.add(key, MyTree(child))
``` 

The constructor [FromFile](#fromfile) gives an actual implementation to load the arborescence
of a disk folder:
    
<$ Tree.FromFolder>Tree interface

This abstract class exposes an interface for a tree.

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

### Abstract methods

Actual implementation of a Tree requires the following properties and methods:

- key (str property) : the key of the node
- get_child (method) : get a direct child by its key
- set_child (method) : insert a child in the collection of direct children
- values (method) : returns an iterator on the direct children
- keys (method) : returns an iterator on the keys of the direct children
- items (method) : returns an iterator on the (key, child) pairs of the direct children


### Creating a whole tree

A tree can be created using the [add](#add) method with the following pseudo code:
    
``` python
class MyTree(TreeDict): # of TreeList or TreeChain or your own implementation
    def __init__(self, source):
        # Initialize self from source content
        ...
        
        # Loop on source children
        for key, child in source:
            self.add(key, MyTree(child))
``` 

The constructor [FromFile](#fromfile) gives an actual implementation to load the arborescence
of a disk folder:
    
<$ Tree.FromFolder>

##Content

- [DOT](treed-tree-tree.md#dot)
- [SEP](treed-tree-tree.md#sep)
- [__delattr__](treed-tree-tree.md#\__delattr__)
- [__dict__](treed-tree-tree.md#\__dict__)
- [__dir__](treed-tree-tree.md#\__dir__)
- [__doc__](treed-tree-tree.md#\__doc__)
- [__eq__](treed-tree-tree.md#\__eq__)
- [__format__](treed-tree-tree.md#\__format__)
- [__ge__](treed-tree-tree.md#\__ge__)
- [__getattribute__](treed-tree-tree.md#\__getattribute__)
- [__getstate__](treed-tree-tree.md#\__getstate__)
- [__gt__](treed-tree-tree.md#\__gt__)
- [__hash__](treed-tree-tree.md#\__hash__)
- [__init_subclass__](treed-tree-tree.md#\__init_subclass__)
- [__le__](treed-tree-tree.md#\__le__)
- [__lt__](treed-tree-tree.md#\__lt__)
- [__module__](treed-tree-tree.md#\__module__)
- [__ne__](treed-tree-tree.md#\__ne__)
- [__new__](treed-tree-tree.md#\__new__)
- [__reduce__](treed-tree-tree.md#\__reduce__)
- [__reduce_ex__](treed-tree-tree.md#\__reduce_ex__)
- [__repr__](treed-tree-tree.md#\__repr__)
- [__setattr__](treed-tree-tree.md#\__setattr__)
- [__sizeof__](treed-tree-tree.md#\__sizeof__)
- [__subclasshook__](treed-tree-tree.md#\__subclasshook__)
- [__weakref__](treed-tree-tree.md#\__weakref__)
- [all_count](treed-tree-tree.md#all_count)
- [count](treed-tree-tree.md#count)
- [depth](treed-tree-tree.md#depth)
- [is_top](treed-tree-tree.md#is_top)
- [path](treed-tree-tree.md#path)
- [top](treed-tree-tree.md#top)
- [FromFile](treed-tree-tree.md#fromfile)
- [FromInspect](treed-tree-tree.md#frominspect)
- [Test](treed-tree-tree.md#test)
- [__str__](treed-tree-tree.md#\__str__)
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


##Properties

###Content

- [DOT](treed-tree-tree.md#dot)
- [SEP](treed-tree-tree.md#sep)
- [__delattr__](treed-tree-tree.md#\__delattr__)
- [__dict__](treed-tree-tree.md#\__dict__)
- [__dir__](treed-tree-tree.md#\__dir__)
- [__doc__](treed-tree-tree.md#\__doc__)
- [__eq__](treed-tree-tree.md#\__eq__)
- [__format__](treed-tree-tree.md#\__format__)
- [__ge__](treed-tree-tree.md#\__ge__)
- [__getattribute__](treed-tree-tree.md#\__getattribute__)
- [__getstate__](treed-tree-tree.md#\__getstate__)
- [__gt__](treed-tree-tree.md#\__gt__)
- [__hash__](treed-tree-tree.md#\__hash__)
- [__init_subclass__](treed-tree-tree.md#\__init_subclass__)
- [__le__](treed-tree-tree.md#\__le__)
- [__lt__](treed-tree-tree.md#\__lt__)
- [__module__](treed-tree-tree.md#\__module__)
- [__ne__](treed-tree-tree.md#\__ne__)
- [__new__](treed-tree-tree.md#\__new__)
- [__reduce__](treed-tree-tree.md#\__reduce__)
- [__reduce_ex__](treed-tree-tree.md#\__reduce_ex__)
- [__repr__](treed-tree-tree.md#\__repr__)
- [__setattr__](treed-tree-tree.md#\__setattr__)
- [__sizeof__](treed-tree-tree.md#\__sizeof__)
- [__subclasshook__](treed-tree-tree.md#\__subclasshook__)
- [__weakref__](treed-tree-tree.md#\__weakref__)
- [all_count](treed-tree-tree.md#all_count)
- [count](treed-tree-tree.md#count)
- [depth](treed-tree-tree.md#depth)
- [is_top](treed-tree-tree.md#is_top)
- [path](treed-tree-tree.md#path)
- [top](treed-tree-tree.md#top)


###DOT


> type str ( = .)



###SEP


> type str ( = /)



###\__delattr__


> type __delattr__ ( = <slot wrapper '__delattr__' of...)



###\__dict__


> type mappingproxy ( = {'__module__': 'treedict.tree'...)



###\__dir__


> type __dir__ ( = <method '__dir__' of 'object' ...)



###\__doc__


> type NoneType ( = None)



###\__eq__


> type __eq__ ( = <slot wrapper '__eq__' of 'obj...)



###\__format__


> type __format__ ( = <method '__format__' of 'objec...)



###\__ge__


> type __ge__ ( = <slot wrapper '__ge__' of 'obj...)



###\__getattribute__


> type __getattribute__ ( = <slot wrapper '__getattribute_...)



###\__getstate__


> type __getstate__ ( = <method '__getstate__' of 'obj...)



###\__gt__


> type __gt__ ( = <slot wrapper '__gt__' of 'obj...)



###\__hash__


> type __hash__ ( = <slot wrapper '__hash__' of 'o...)



###\__init_subclass__


> type __init_subclass__ ( = <built-in method __init_subcla...)



###\__le__


> type __le__ ( = <slot wrapper '__le__' of 'obj...)



###\__lt__


> type __lt__ ( = <slot wrapper '__lt__' of 'obj...)



###\__module__


> type str ( = treedict.tree)



###\__ne__


> type __ne__ ( = <slot wrapper '__ne__' of 'obj...)



###\__new__


> type __new__ ( = <built-in method __new__ of ty...)



###\__reduce__


> type __reduce__ ( = <method '__reduce__' of 'objec...)



###\__reduce_ex__


> type __reduce_ex__ ( = <method '__reduce_ex__' of 'ob...)



###\__repr__


> type __repr__ ( = <slot wrapper '__repr__' of 'o...)



###\__setattr__


> type __setattr__ ( = <slot wrapper '__setattr__' of...)



###\__sizeof__


> type __sizeof__ ( = <method '__sizeof__' of 'objec...)



###\__subclasshook__


> type __subclasshook__ ( = <built-in method __subclasshoo...)



###\__weakref__


> type __weakref__ ( = <attribute '__weakref__' of 'T...)



###all_count


> type property ( = <property object at 0x17853aa7...)



###count


> type property ( = <property object at 0x17853962...)



###depth


> type property ( = <property object at 0x17853903...)



###is_top


> type property ( = <property object at 0x17853bd8...)



###path


> type property ( = <property object at 0x17853ac5...)



###top


> type property ( = <property object at 0x178538ae...)



##Methods

###Content

- [FromFile](treed-tree-tree.md#fromfile)
- [FromInspect](treed-tree-tree.md#frominspect)
- [Test](treed-tree-tree.md#test)
- [__str__](treed-tree-tree.md#\__str__)
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


###FromFile

----------



``` python
FromFile(folder, pattern='*.*', ignore=('.*', '_*'))
```

Read the content of a drive

This methods shows how to use method [add](#add) to recursively load folder files and sub folders.

Arguments:
- **folder** (_str_)
- **pattern** (_str or tuple of strs_ = *.*)
- **ignore** (_str or tuple of strs_ = ('.*', '_*'))



Returns:
- **Tree** : 



###FromInspect

----------



``` python
FromInspect(obj)
```

Load python module

Load module and module members using inspect

Arguments:
- **obj** (_any_)



Returns:
- **Tree** : 



###Test

----------



``` python
Test(**kwargs)
```

A tree for test

Arguments:
- **kwargs**



###\__str__

----------



``` python
__str__(self)
```

Return str(self).

Arguments:
- **self**



###add

----------



``` python
add(self, path, node, complete_path=False)
```

Add a new node at the path

This method calls [set_child](#set_child).

Arguments:
- **self**
- **path** (_str_)
- **node** (_Tree_)
- **complete_path** ( = False)



Returns:
- **Tree** : the node argument



###all_items

----------



``` python
all_items(self, include_self=False)
```

All items iterator

Iterate on all items in the folder and sub folders.

Arguments:
- **self**
- **include_self** ( = False)



Returns:
- **iterator** : 



###all_paths

----------



``` python
all_paths(self, include_self=False)
```

All paths iterator

Iterate on all paths in the folder and sub folders.

Arguments:
- **self**
- **include_self** ( = False)



Returns:
- **iterator** : 



###all_values

----------



``` python
all_values(self, include_self=False)
```

All values iterator

Iterate on all values in the folder and sub folders.

Arguments:
- **self**
- **include_self** ( = False)



Returns:
- **iterator** : 



###create_path

----------



``` python
create_path(self, *keys)
```

Create nodes in a path

Nodes are create by calling [new](#new) method.

Arguments:
- **self**
- **keys** (_list of strs_)



Returns:
- **Tree** : last created node



###find

----------



``` python
find(self, *keys, first=False, **criteria)
```

Find one or more keys in the tree.

Arguments:
- **self**
- **keys** (_list of strs_)
- **first** (_boolean_ = False)
- **criteria**



Returns:
- **Tree** : on single tree if first is Trur



###get

----------



``` python
get(self, path, default=None)
```

Get the node at path

Arguments:
- **self**
- **path** (_str_)
- **default** (_Tree_ = None)



Returns:
- **Tree** : 



###get_child

----------



``` python
get_child(self, key)
```

Get a direct child by its key

Arguments:
- **self**
- **key**



###join_keys

----------



``` python
join_keys(self, *keys)
```

Join keys to form a path

Joins the keys with the key separator avoiding double separators: `join_keys("AAA", "BBB")`
and `join_keys("AAA/", "BBB")` will both give `"AAA/BBB"`.

Arguments:
- **self**
- **keys**



Returns:
- **str** : key joined by key separator



###new

----------



``` python
new(self, path, complete_path=False, **kwargs)
```

Create a new node at the given path

The default implementation create a new node by calling the defaut constructor
and adding it by calling [add](#add):
    
``` python
return self.add(path, type(self)(**kwargs), complete_path=complete_path)
```

Raises:
- **PathError** : if nodes are missing in the path



Arguments:
- **self**
- **path** (_str_)
- **complete_path** (_set_ = False)
- **kwargs**



Returns:
- **Tree** : the created node



###new_paths

----------



``` python
new_paths(self, *paths, complete_path=False, **kwargs)
```

Create several nodes defined by their path

Basically, this method call [new](#new) for each provided path.

The following rules apply:            
- paths starting by '/' are created at top level
- paths starting by '.' are created at the *last created node* level
- paths starting by '..' are created at parent level of *last created node* level
- otherwise, nodes are created at at the node level

``` python
node = tree.new("MyNode")
node.new_paths("AAA", "BBB", "./under BBB", "../after 'under BBB'", "/After MyNode")
# - MyNode
#   - AAA
#   - BBB
#     - under BBB
#     - after 'under BBB'
# - After MyNode
```

Arguments:
- **self**
- **paths** (_list of str_)
- **complete_path** (_bool_ = False)
- **kwargs**



Returns:
- **Tree** : the created child



###set_child

----------



``` python
set_child(self, key, child, index=None)
```

set a direct child by its key

Arguments:
- **self**
- **key**
- **child**
- **index** ( = None)



###solve_path

----------



``` python
solve_path(self, path, complete_path=False)
```

Solve a path

Returns the node corresponding to the path.

If it doesn't exist, two cases are possible:
- only the last key in the path is missing: the methods return the parent
  and the missing key
- an intermediary node is missing: the methods raises an error or creates
  the missing nodes depending on the arguments **complete_path**.
  
> [!NOTE]
> Missing nodes in the path are created with method [create_path](#create_path)

Raises:
- **PathError** : if the path can't be solved up to the last, or last but one



Arguments:
- **self**
- **path** (_str_)
- **complete_path** (_bool_ = False)



Returns:
- **Tree** : (found node, None) or (parent node, missing key)



###solve_to_missing

----------



``` python
solve_to_missing(self, path)
```

Solve a path to missing keys

Solve a path, return the existing node and the list of non existing keys.

Raises:
- **PathError** : if path is incorrect



Arguments:
- **self**
- **path** (_str_)



Returns:
- **node** : last existing node, list of missing keys



###test

----------



``` python
test()
```

Perform basic tests
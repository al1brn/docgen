# TreeChain



``` python
TreeChain(d=None)
```

Tree interface whith chained nodes

This class implements directly the [impossible to find a section with title '!Tree']() interface by chaining the nodes with [page not found in '!TreeChain#child']() and [page not found in '!TreeChain#next']()
properties:
- **child** : first child, the node has no children if Node
- **next** : next child in the collection of parent children, last child if None

#### Arguments:
- **self**
- **d** ( = None)



## Content

- **A** : [add](treed-tree-treechain.md#add) :black_small_square: [all_count](treed-tree-treechain.md#all_count) :black_small_square: [all_items](treed-tree-treechain.md#all_items) :black_small_square: [all_paths](treed-tree-treechain.md#all_paths) :black_small_square: [all_values](treed-tree-treechain.md#all_values)
- **C** : [child](treed-tree-treechain.md#child) :black_small_square: [count](treed-tree-treechain.md#count) :black_small_square: [create_path](treed-tree-treechain.md#create_path)
- **D** : [depth](treed-tree-treechain.md#depth) :black_small_square: [DOT](treed-tree-treechain.md#dot)
- **F** : [find](treed-tree-treechain.md#find) :black_small_square: [FromFile](treed-tree-treechain.md#fromfile) :black_small_square: [FromInspect](treed-tree-treechain.md#frominspect)
- **G** : [get](treed-tree-treechain.md#get) :black_small_square: [get_child](treed-tree-treechain.md#get_child)
- **I** : [is_top](treed-tree-treechain.md#is_top) :black_small_square: [items](treed-tree-treechain.md#items)
- **J** : [join_keys](treed-tree-treechain.md#join_keys)
- **K** : [keys](treed-tree-treechain.md#keys)
- **L** : [last_child](treed-tree-treechain.md#last_child)
- **N** : [new](treed-tree-treechain.md#new) :black_small_square: [new_paths](treed-tree-treechain.md#new_paths) :black_small_square: [next](treed-tree-treechain.md#next)
- **P** : [path](treed-tree-treechain.md#path)
- **S** : [SEP](treed-tree-treechain.md#sep) :black_small_square: [set_child](treed-tree-treechain.md#set_child) :black_small_square: [solve_path](treed-tree-treechain.md#solve_path) :black_small_square: [solve_to_missing](treed-tree-treechain.md#solve_to_missing) :black_small_square: [sort](treed-tree-treechain.md#sort)
- **T** : [top](treed-tree-treechain.md#top)
- **V** : [values](treed-tree-treechain.md#values)



## Properties

### all_count

> TYPE: **int**

Total number of children

### child

> TYPE: **TreeChain**<br> DEFAULT: **None**

the first child of the direct children. None if the node has node child

### count

> TYPE: **int**

Number of direct children, equivalent to `len(self)`

### depth

> TYPE: **int**

Distance to the top (0 for top section)

### DOT

> TYPE: **str**<br> DEFAULT: **.**



### is_top

> TYPE: **bool**

True if owner is None

### last_child

> TYPE: **?**



### next

> TYPE: **TreeChain**<br> DEFAULT: **None**

the next next in the parent children series. None if it is the last one

### path

> TYPE: **str**

Node path up to the top node

### SEP

> TYPE: **str**<br> DEFAULT: **/**



### top

> TYPE: **Section**

Get the topmost section

## Methods

----------
### add



``` python
add(path, node, complete_path=False)
```

Add a new node at the path

This method calls [set_child](#set_child).


#### Arguments:
- **self**
- **path** (_str_)
- **node** (_Tree_)
- **complete_path** ( = False)



#### Returns:
- **Tree** : the node argument



<sub>[index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [up](#methods)</sub>



----------
### all_items



``` python
all_items(include_self=False)
```

All items iterator

Iterate on all items in the folder and sub folders.


#### Arguments:
- **self**
- **include_self** ( = False)



#### Returns:
- **iterator** : 



<sub>[index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [up](#methods)</sub>



----------
### all_paths



``` python
all_paths(include_self=False)
```

All paths iterator

Iterate on all paths in the folder and sub folders.


#### Arguments:
- **self**
- **include_self** ( = False)



#### Returns:
- **iterator** : 



<sub>[index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [up](#methods)</sub>



----------
### all_values



``` python
all_values(include_self=False)
```

All values iterator

Iterate on all values in the folder and sub folders.


#### Arguments:
- **self**
- **include_self** ( = False)



#### Returns:
- **iterator** : 



<sub>[index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [up](#methods)</sub>



----------
### create_path



``` python
create_path(*keys)
```

Create nodes in a path

Nodes are create by calling [new](#new) method.


#### Arguments:
- **self**
- **keys** (_list of strs_)



#### Returns:
- **Tree** : last created node



<sub>[index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [up](#methods)</sub>



----------
### find



``` python
find(*keys, first=False, **criteria)
```

Find one or more keys in the tree.


#### Arguments:
- **self**
- **keys** (_list of strs_)
- **first** (_boolean_ = False)
- **criteria**



#### Returns:
- **Tree** : on single tree if first is Trur



<sub>[index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [up](#methods)</sub>



----------
### FromFile



``` python
FromFile(folder, pattern='*.*', ignore=('.*', '_*'))
```

Read the content of a drive

This methods shows how to use method [add](#add) to recursively load folder files and sub folders.


#### Arguments:
- **folder** (_str_)
- **pattern** (_str or tuple of strs_ = *.*)
- **ignore** (_str or tuple of strs_ = ('.*', '_*'))



#### Returns:
- **Tree** : 



<sub>[index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [up](#methods)</sub>



----------
### FromInspect



``` python
FromInspect(obj)
```

Load python module

Load module and module members using inspect


#### Arguments:
- **obj** (_any_)



#### Returns:
- **Tree** : 



<sub>[index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [up](#methods)</sub>



----------
### get



``` python
get(path, default=None)
```

Get the node at path


#### Arguments:
- **self**
- **path** (_str_)
- **default** (_Tree_ = None)



#### Returns:
- **Tree** : 



<sub>[index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [up](#methods)</sub>



----------
### get_child



``` python
get_child(key)
```

Get a direct child by its key


#### Arguments:
- **self**
- **key**



<sub>[index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [up](#methods)</sub>



----------
### items



``` python
items()
```

Iterate on (key, value) pais


#### Arguments:
- **self**



<sub>[index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [up](#methods)</sub>



----------
### join_keys



``` python
join_keys(*keys)
```

Join keys to form a path

Joins the keys with the key separator avoiding double separators: `join_keys("AAA", "BBB")`
and `join_keys("AAA/", "BBB")` will both give `"AAA/BBB"`.


#### Arguments:
- **self**
- **keys**



#### Returns:
- **str** : key joined by key separator



<sub>[index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [up](#methods)</sub>



----------
### keys



``` python
keys()
```

Iterate on keys


#### Arguments:
- **self**



<sub>[index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [up](#methods)</sub>



----------
### new



``` python
new(path, complete_path=False, **kwargs)
```

Create a new node at the given path

The default implementation create a new node by calling the defaut constructor
and adding it by calling [add](#add):
    
``` python
return self.add(path, type(self)(**kwargs), complete_path=complete_path)
```


#### Raises:
- **PathError** : if nodes are missing in the path



#### Arguments:
- **self**
- **path** (_str_)
- **complete_path** (_set_ = False)
- **kwargs**



#### Returns:
- **Tree** : the created node



<sub>[index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [up](#methods)</sub>



----------
### new_paths



``` python
new_paths(*paths, complete_path=False, **kwargs)
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


#### Arguments:
- **self**
- **paths** (_list of str_)
- **complete_path** (_bool_ = False)
- **kwargs**



#### Returns:
- **Tree** : the created child



<sub>[index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [up](#methods)</sub>



----------
### set_child



``` python
set_child(key, child, index=None)
```

set a direct child by its key


#### Arguments:
- **self**
- **key**
- **child**
- **index** ( = None)



<sub>[index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [up](#methods)</sub>



----------
### solve_path



``` python
solve_path(path, complete_path=False)
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


#### Raises:
- **PathError** : if the path can't be solved up to the last, or last but one



#### Arguments:
- **self**
- **path** (_str_)
- **complete_path** (_bool_ = False)



#### Returns:
- **Tree** : (found node, None) or (parent node, missing key)



<sub>[index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [up](#methods)</sub>



----------
### solve_to_missing



``` python
solve_to_missing(path)
```

Solve a path to missing keys

Solve a path, return the existing node and the list of non existing keys.


#### Raises:
- **PathError** : if path is incorrect



#### Arguments:
- **self**
- **path** (_str_)



#### Returns:
- **node** : last existing node, list of missing keys



<sub>[index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [up](#methods)</sub>



----------
### sort



``` python
sort(key=None, reverse=False)
```

Sort the direct children


#### Arguments:
- **self**
- **key** (_function_ = None)
- **reverse** (_bool_ = False)



<sub>[index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [up](#methods)</sub>



----------
### values



``` python
values()
```

Iterate on childs


#### Arguments:
- **self**



<sub>[index](index.md) :black_small_square: [top](#treechain) :black_small_square: [Content](#content) :black_small_square: [up](#methods)</sub>


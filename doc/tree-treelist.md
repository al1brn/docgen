# TreeList

``` python
TreeList()
```

Tree interface based on a list

This class inherits from [Tree](tree-tree.md) and list. Direct children are store in the list.

Several children can share the same key.

This implementation can be chosen when direct children can share a same key and / or when there is
a need to control the order of the children### Inherited

list.\_\_add__ :black_small_square: list.\_\_contains__ :black_small_square: list.\_\_delitem__ :black_small_square: list.\_\_eq__ :black_small_square: list.\_\_ge__ :black_small_square: list.\_\_getattribute__ :black_small_square: list.\_\_gt__ :black_small_square: list.\_\_iadd__ :black_small_square: list.\_\_imul__ :black_small_square: list.\_\_le__ :black_small_square: list.\_\_len__ :black_small_square: list.\_\_lt__ :black_small_square: list.\_\_mul__ :black_small_square: list.\_\_ne__ :black_small_square: list.\_\_repr__ :black_small_square: list.\_\_reversed__ :black_small_square: list.\_\_rmul__ :black_small_square: list.\_\_sizeof__ :black_small_square: list.append :black_small_square: list.clear :black_small_square: list.copy :black_small_square: list.extend :black_small_square: list.index :black_small_square: list.insert :black_small_square: list.pop :black_small_square: list.remove :black_small_square: list.reverse :black_small_square: list.sort :black_small_square:

## Content

- **A** : [add()](tree-treelist.md#add()) :black_small_square: [all_count](tree-treelist.md#all_count) :black_small_square: [all_items()](tree-treelist.md#all_items()) :black_small_square: [all_paths()](tree-treelist.md#all_paths()) :black_small_square: [all_values()](tree-treelist.md#all_values())
- **C** : [count](tree-treelist.md#count) :black_small_square: [create_path()](tree-treelist.md#create_path())
- **D** : [depth](tree-treelist.md#depth) :black_small_square: [detach()](tree-treelist.md#detach())
- **F** : [find()](tree-treelist.md#find()) :black_small_square: [FromFile()](tree-treelist.md#fromfile()) :black_small_square: [FromInspect()](tree-treelist.md#frominspect())
- **G** : [get()](tree-treelist.md#get()) :black_small_square: [get_child()](tree-treelist.md#get_child())
- **I** : [is_top](tree-treelist.md#is_top) :black_small_square: [items()](tree-treelist.md#items())
- **J** : [join_keys()](tree-treelist.md#join_keys())
- **K** : [keys()](tree-treelist.md#keys())
- **M** : [move_to_parent()](tree-treelist.md#move_to_parent())
- **N** : [new()](tree-treelist.md#new()) :black_small_square: [new_paths()](tree-treelist.md#new_paths())
- **P** : [path](tree-treelist.md#path)
- **R** : [remove_from_parent()](tree-treelist.md#remove_from_parent())
- **S** : [set_child()](tree-treelist.md#set_child()) :black_small_square: [solve_path()](tree-treelist.md#solve_path()) :black_small_square: [solve_to_missing()](tree-treelist.md#solve_to_missing())
- **T** : [top](tree-treelist.md#top)
- **V** : [values()](tree-treelist.md#values())

## Properties



### all_count

> _type_: **int**
>

Total number of children

### count

> _type_: **int**
>

Number of direct children, equivalent to `len(self)`

### depth

> _type_: **int**
>

Distance to the top (0 for top section)

### is_top

> _type_: **bool**
>

True if owner is None

### path

> _type_: **str**
>

Node path up to the top node

### top

> _type_: **Section**
>

Get the topmost section

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [TreeList](tree-treelist.md)</sub>

## Methods



----------
### add()

> method

``` python
add()(path, node, complete_path=False)
```

Add a new node at the path

This method calls ['#set_child' not found]().

#### Arguments:
- **path** (_str_) : the path where to locate the node
- **node** (_Tree_) : the node to set at the path
- **complete_path** ( = False)



#### Returns:
- **Tree** : the node argument

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### all_items()

> method

``` python
all_items()(include_self=False)
```

All items iterator

Iterate on all items in the folder and sub folders.

#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### all_paths()

> method

``` python
all_paths()(include_self=False)
```

All paths iterator

Iterate on all paths in the folder and sub folders.

#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### all_values()

> method

``` python
all_values()(include_self=False)
```

All values iterator

Iterate on all values in the folder and sub folders.

#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### create_path()

> method

``` python
create_path()(*keys)
```

Create nodes in a path

Nodes are create by calling ['#new' not found]() method.

#### Arguments:
- **keys** (_list of strs_) : key forming the path to create



#### Returns:
- **Tree** : last created node

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### detach()

> method

``` python
detach()()
```

Detach the section from its parent children

> [!IMPORANT]
> This method calls the abstract method ['#remove_from_parent' not found]() which must perform
> the actual removal from the parent's list of children.

#### Returns:
- **Tree** : self

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### find()

> method

``` python
find()(*keys, first=False, **criteria)
```

Find one or more keys in the tree.

#### Arguments:
- **keys** (_list of strs_) : the keys to look for
- **first** (_boolean_ = False) : stop on the first match an return the found node
- **criteria** : search the node with attributes match keyword arguments



#### Returns:
- **Tree** : on single tree if first is Trur

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### FromFile()

> classmethod

``` python
FromFile()(folder, pattern='*.*', ignore=('.*', '_*'))
```

Read the content of a drive

This methods shows how to use method ['#add' not found]() to recursively load folder files and sub folders.

#### Arguments:
- **folder** (_str_) : folder to load
- **pattern** (_str or tuple of strs_ = *.*) : file selection
- **ignore** (_str or tuple of strs_ = ('.*', '_*')) : files starting by one of the characters in the string are ignored



#### Returns:
- **Tree** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### FromInspect()

> classmethod

``` python
FromInspect()(obj)
```

Load python module

Load module and module members using inspect

#### Arguments:
- **obj** (_any_) : object to inspect



#### Returns:
- **Tree** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### get()

> method

``` python
get()(path, default=None)
```

Get the node at path

#### Arguments:
- **path** (_str_) : the node path
- **default** (_Tree_ = None) : the node to return if the path is not solved



#### Returns:
- **Tree** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### get_child()

> method

``` python
get_child()(key)
```

Get a direct child by its key

#### Arguments:
- **key**

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### items()

> method

``` python
items()()
```

Iterate on (key, value) pais

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### join_keys()

> method

``` python
join_keys()(*keys)
```

Join keys to form a path

Joins the keys with the key separator avoiding double separators: `join_keys("AAA", "BBB")`
and `join_keys("AAA/", "BBB")` will both give `"AAA/BBB"`.

#### Arguments:
- **keys**



#### Returns:
- **str** : key joined by key separator

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### keys()

> method

``` python
keys()()
```

Iterate on keys

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### move_to_parent()

> method

``` python
move_to_parent()(new_parent, new_key=None)
```

Change the position of a node from one parent to another

This methods basically calls ['#detach' not found]() and then ['#add' not found]().


Returns
- Tree : self

#### Arguments:
- **new_parent** (_Tree_) : where to locate the node
- **new_key** (_str_ = None) : new key, uses the current key is None

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### new()

> method

``` python
new()(path, complete_path=False, **kwargs)
```

Create a new node at the given path

The default implementation create a new node by calling the defaut constructor
and adding it by calling ['#add' not found]():
    
``` python
return self.add(path, type(self)(**kwargs), complete_path=complete_path)
```

#### Raises:
- **PathError** : if nodes are missing in the path



#### Arguments:
- **path** (_str_) : the path where to create a new node
- **complete_path** (_set_ = False) : create the path if hole exist
- **kwargs** : default constructor arguments



#### Returns:
- **Tree** : the created node

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### new_paths()

> method

``` python
new_paths()(*paths, complete_path=False, **kwargs)
```

Create several nodes defined by their path

Basically, this method call ['#new' not found]() for each provided path.

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
- **paths** (_list of str_) : the paths of the nodes to create
- **complete_path** (_bool_ = False) : create intermediary nodes in paths
- **kwargs** : default constructor arguments when creating intermediary is required



#### Returns:
- **Tree** : the created child

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### remove_from_parent()

> method

``` python
remove_from_parent()()
```

Remove the section from its parent list of children

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### set_child()

> method

``` python
set_child()(key, child, index=None)
```

set a direct child by its key

#### Arguments:
- **key**
- **child**
- **index** ( = None)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### solve_path()

> method

``` python
solve_path()(path, complete_path=False)
```

Solve a path

Returns the node corresponding to the path.

If it doesn't exist, two cases are possible:
- only the last key in the path is missing: the methods return the parent
  and the missing key
- an intermediary node is missing: the methods raises an error or creates
  the missing nodes depending on the arguments **complete_path**.
  
> [!NOTE]
> Missing nodes in the path are created with method ['#create_path' not found]()

#### Raises:
- **PathError** : if the path can't be solved up to the last, or last but one



#### Arguments:
- **path** (_str_) : the path to solve
- **complete_path** (_bool_ = False) : create missing nodes (but the last one) if necessary



#### Returns:
- **Tree** : (found node, None) or (parent node, missing key)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### solve_to_missing()

> method

``` python
solve_to_missing()(path)
```

Solve a path to missing keys

Solve a path, return the existing node and the list of non existing keys.

#### Raises:
- **PathError** : if path is incorrect



#### Arguments:
- **path** (_str_) : path to solve



#### Returns:
- **node** : last existing node, list of missing keys

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

----------
### values()

> method

``` python
values()()
```

Iterate on childs

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [Methods](tree-treelist.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#treelist) :black_small_square: [Content](#content) :black_small_square: [TreeList](tree-treelist.md)</sub>
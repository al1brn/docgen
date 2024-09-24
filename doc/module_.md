# Module_



``` python
Module_(name, comment=None, **kwargs)
```

Tree interface based on a dict

This class inherits from [Tree](tree-tree.md) and dict. Direct children are managed from dict inheritance.

This implementation can be chosen when direct child keys must be unique and when there is no
particular need in controlling the order of the children.

#### Arguments:
- **name** (_str_) : class name
- **comment** (_str_ = None) : comment
- **kwargs** : complementary information



### Inherited

dict.\_\_contains__ :black_small_square: dict.\_\_delitem__ :black_small_square: dict.\_\_eq__ :black_small_square: dict.\_\_ge__ :black_small_square: dict.\_\_getattribute__ :black_small_square: dict.\_\_gt__ :black_small_square: dict.\_\_ior__ :black_small_square: dict.\_\_le__ :black_small_square: dict.\_\_len__ :black_small_square: dict.\_\_lt__ :black_small_square: dict.\_\_ne__ :black_small_square: dict.\_\_or__ :black_small_square: dict.\_\_repr__ :black_small_square: dict.\_\_reversed__ :black_small_square: dict.\_\_ror__ :black_small_square: dict.\_\_sizeof__ :black_small_square: dict.clear :black_small_square: dict.copy :black_small_square: dict.items :black_small_square: dict.keys :black_small_square: dict.pop :black_small_square: dict.popitem :black_small_square: dict.setdefault :black_small_square: dict.update :black_small_square: dict.values :black_small_square: 

## Content

- **A** : [add](module_.md#add) :black_small_square: [all_count](module_.md#all_count) :black_small_square: [all_items](module_.md#all_items) :black_small_square: [all_paths](module_.md#all_paths) :black_small_square: [all_values](module_.md#all_values)
- **C** : [count](module_.md#count) :black_small_square: [create_path](module_.md#create_path)
- **D** : [depth](module_.md#depth) :black_small_square: [detach](module_.md#detach) :black_small_square: [DOT](module_.md#dot)
- **F** : [find](module_.md#find) :black_small_square: [FromFile](module_.md#fromfile) :black_small_square: [FromInspect](module_.md#frominspect)
- **G** : [get](module_.md#get) :black_small_square: [get_child](module_.md#get_child) :black_small_square: [get_prop](module_.md#get_prop)
- **I** : [is_top](module_.md#is_top)
- **J** : [join_keys](module_.md#join_keys)
- **K** : [key](module_.md#key)
- **M** : [meta](module_.md#meta) :black_small_square: [move_to_parent](module_.md#move_to_parent)
- **N** : [new](module_.md#new) :black_small_square: [new_paths](module_.md#new_paths)
- **O** : [obj_type](module_.md#obj_type)
- **P** : [parse_comment](module_.md#parse_comment) :black_small_square: [path](module_.md#path)
- **R** : [remove_from_parent](module_.md#remove_from_parent)
- **S** : [SEP](module_.md#sep) :black_small_square: [set_child](module_.md#set_child) :black_small_square: [solve_path](module_.md#solve_path) :black_small_square: [solve_to_missing](module_.md#solve_to_missing)
- **T** : [top](module_.md#top)



## Properties

### all_count


<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>

Total number of children

### count


<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>

Number of direct children, equivalent to `len(self)`

### depth


<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>

Distance to the top (0 for top section)

### DOT


<table><tbody>
<tr><td>type</td><td><b>NoneType</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>



### is_top


<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

True if owner is None

### key


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>

Get the key

In a **TreeDict**, the **key** is known by the parent. A node can retrieve it
by searching for itself in the direct children of its parent.

To make this process more efficient, **key** is cached by default in
hidden property **_key**.

### obj_type


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>module</b</td></tr>
</tbody></table>



### path


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

Node path up to the top node

### SEP


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>.</b</td></tr>
</tbody></table>



### top


<table><tbody>
<tr><td>type</td><td><b>Section</b></td></tr>
</tbody></table>

Get the topmost section

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Module_](#module_)</sub>



## Methods

----------
### add



``` python
add(path, node, complete_path=False)
```

Add a new node at the path

This method calls [set_child](#set_child).


#### Arguments:
- **path** (_str_) : the path where to locate the node
- **node** (_Tree_) : the node to set at the path
- **complete_path** ( = False)



#### Returns:
- **Tree** : the node argument



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### all_items



``` python
all_items(include_self=False)
```

All items iterator

Iterate on all items in the folder and sub folders.


#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### all_paths



``` python
all_paths(include_self=False)
```

All paths iterator

Iterate on all paths in the folder and sub folders.


#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### all_values



``` python
all_values(include_self=False)
```

All values iterator

Iterate on all values in the folder and sub folders.


#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### create_path



``` python
create_path(*keys)
```

Create nodes in a path

Nodes are create by calling [new](#new) method.


#### Arguments:
- **keys** (_list of strs_) : key forming the path to create



#### Returns:
- **Tree** : last created node



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### detach



``` python
detach()
```

Detach the section from its parent children

> [!IMPORANT]
> This method calls the abstract method [remove_from_parent](#remove_from_parent) which must perform
> the actual removal from the parent's list of children.


#### Returns:
- **Tree** : self



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### find



``` python
find(*keys, first=False, **criteria)
```

Find one or more keys in the tree.


#### Arguments:
- **keys** (_list of strs_) : the keys to look for
- **first** (_boolean_ = False) : stop on the first match an return the found node
- **criteria** : search the node with attributes match keyword arguments



#### Returns:
- **Tree** : on single tree if first is Trur



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### FromFile



``` python
FromFile(folder, pattern='*.*', ignore=('.*', '_*'))
```

Read the content of a drive

This methods shows how to use method [add](#add) to recursively load folder files and sub folders.


#### Arguments:
- **folder** (_str_) : folder to load
- **pattern** (_str or tuple of strs_ = *.*) : file selection
- **ignore** (_str or tuple of strs_ = ('.*', '_*')) : files starting by one of the characters in the string are ignored



#### Returns:
- **Tree** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### FromInspect



``` python
FromInspect(module_name, module_object, verbose=False)
```

Create an Module_ instance from a python module


#### Arguments:
- **module_name**
- **module_object** (_module_) : the module to scan
- **verbose** ( = False)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### get



``` python
get(path, default=None)
```

Get the node at path


#### Arguments:
- **path** (_str_) : the node path
- **default** (_Tree_ = None) : the node to return if the path is not solved



#### Returns:
- **Tree** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### get_child



``` python
get_child(key)
```

Get a direct child by its key


#### Arguments:
- **key**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### get_prop



``` python
get_prop(prop_name, default=None)
```

Get an optional property


#### Arguments:
- **prop_name** (_str_) : name of the property to read
- **default** (_any_ = None) : default value if the property doesn't exist



#### Returns:
- **any** : the property or None if it doesn't exist



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### join_keys



``` python
join_keys(*keys)
```

Join keys to form a path

Joins the keys with the key separator avoiding double separators: `join_keys("AAA", "BBB")`
and `join_keys("AAA/", "BBB")` will both give `"AAA/BBB"`.


#### Arguments:
- **keys**



#### Returns:
- **str** : key joined by key separator



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### meta



``` python
meta(meta_name, default=None)
```

Get a meta property

A meta property can be set in the comment with the syntax
```
 $ SET meta_name = value
```


#### Arguments:
- **meta_name** (_str_) : name of the meta property to read
- **default** (_any_ = None) : default value if the property doesn't exist



#### Returns:
- **any** : the meta property value or None if it doesn't exist



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### move_to_parent



``` python
move_to_parent(new_parent, new_key=None)
```

Change the position of a node from one parent to another

This methods basically calls [detach](#detach) and then [add](#add).


Returns
- Tree : self


#### Arguments:
- **new_parent** (_Tree_) : where to locate the node
- **new_key** (_str_ = None) : new key, uses the current key is None



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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
- **path** (_str_) : the path where to create a new node
- **complete_path** (_set_ = False) : create the path if hole exist
- **kwargs** : default constructor arguments



#### Returns:
- **Tree** : the created node



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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
- **paths** (_list of str_) : the paths of the nodes to create
- **complete_path** (_bool_ = False) : create intermediary nodes in paths
- **kwargs** : default constructor arguments when creating intermediary is required



#### Returns:
- **Tree** : the created child



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### parse_comment



``` python
parse_comment()
```

Collect extra information from the comment

#### Inline commands
- $ DOC START : ignore lines above
- $ DO END : ignore lines after
- $ SET prop = 123 : pass properties to the doc generator

In addition, special lists are extracted to create [DescriptionList](descriptionlist.md)

#### Extracted lists
- raises
- arguments
- returns
- properties


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### remove_from_parent



``` python
remove_from_parent()
```

Remove the section from its parent list of children


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### set_child



``` python
set_child(key, child, index=None)
```

Set a direct child by its key


#### Arguments:
- **key**
- **child**
- **index** ( = None)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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
- **path** (_str_) : the path to solve
- **complete_path** (_bool_ = False) : create missing nodes (but the last one) if necessary



#### Returns:
- **Tree** : (found node, None) or (parent node, missing key)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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
- **path** (_str_) : path to solve



#### Returns:
- **node** : last existing node, list of missing keys



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#module_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>


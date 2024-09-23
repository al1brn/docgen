# ClassFunc_



``` python
ClassFunc_(name, comment=None, signature=None, **kwargs)
```

Tree interface based on a dict

This class inherits from [Tree](tree3-tree.md) and dict. Direct children are managed from dict inheritance.

This implementation can be chosen when direct child keys must be unique and when there is no
particular need in controlling the order of the children.

#### Arguments:
- **name** (_str_) : object name
- **comment** (_str_ = None) : comment
- **signature** (_str_ = None) : function signature
- **kwargs** : custom parameters



### Inherited

dict.\_\_contains__ :black_small_square: dict.\_\_delitem__ :black_small_square: dict.\_\_eq__ :black_small_square: dict.\_\_ge__ :black_small_square: dict.\_\_getattribute__ :black_small_square: dict.\_\_gt__ :black_small_square: dict.\_\_ior__ :black_small_square: dict.\_\_le__ :black_small_square: dict.\_\_len__ :black_small_square: dict.\_\_lt__ :black_small_square: dict.\_\_ne__ :black_small_square: dict.\_\_or__ :black_small_square: dict.\_\_repr__ :black_small_square: dict.\_\_reversed__ :black_small_square: dict.\_\_ror__ :black_small_square: dict.\_\_sizeof__ :black_small_square: dict.clear :black_small_square: dict.copy :black_small_square: dict.items :black_small_square: dict.keys :black_small_square: dict.pop :black_small_square: dict.popitem :black_small_square: dict.setdefault :black_small_square: dict.update :black_small_square: dict.values :black_small_square: 

## Content

- **A** : [add](objin1-classfunc_.md#add) :black_small_square: [all_count](objin1-classfunc_.md#all_count) :black_small_square: [all_items](objin1-classfunc_.md#all_items) :black_small_square: [all_paths](objin1-classfunc_.md#all_paths) :black_small_square: [all_values](objin1-classfunc_.md#all_values)
- **C** : [count](objin1-classfunc_.md#count) :black_small_square: [create_path](objin1-classfunc_.md#create_path)
- **D** : [depth](objin1-classfunc_.md#depth) :black_small_square: [DOT](objin1-classfunc_.md#dot)
- **F** : [find](objin1-classfunc_.md#find) :black_small_square: [FromFile](objin1-classfunc_.md#fromfile) :black_small_square: [FromInspect](objin1-classfunc_.md#frominspect)
- **G** : [get](objin1-classfunc_.md#get) :black_small_square: [get_child](objin1-classfunc_.md#get_child) :black_small_square: [get_prop](objin1-classfunc_.md#get_prop)
- **I** : [is_top](objin1-classfunc_.md#is_top)
- **J** : [join_keys](objin1-classfunc_.md#join_keys)
- **K** : [key](objin1-classfunc_.md#key)
- **M** : [meta](objin1-classfunc_.md#meta)
- **N** : [new](objin1-classfunc_.md#new) :black_small_square: [new_paths](objin1-classfunc_.md#new_paths)
- **O** : [obj_type](objin1-classfunc_.md#obj_type)
- **P** : [parse_comment](objin1-classfunc_.md#parse_comment) :black_small_square: [path](objin1-classfunc_.md#path)
- **S** : [SEP](objin1-classfunc_.md#sep) :black_small_square: [set_child](objin1-classfunc_.md#set_child) :black_small_square: [solve_path](objin1-classfunc_.md#solve_path) :black_small_square: [solve_to_missing](objin1-classfunc_.md#solve_to_missing)
- **T** : [top](objin1-classfunc_.md#top)



## Properties

### all_count

> TYPE: **int**

Total number of children

### count

> TYPE: **int**

Number of direct children, equivalent to `len(self)`

### depth

> TYPE: **int**

Distance to the top (0 for top section)

### DOT

> TYPE: **NoneType**<br> DEFAULT: **None**



### is_top

> TYPE: **bool**

True if owner is None

### key

> TYPE: **?**

Get the key

In a **TreeDict**, the **key** is known by the parent. A node can retrieve it
by searching for itself in the direct children of its parent.

To make this process more efficient, **key** is cached by default in
hidden property **_key**.

### obj_type

> TYPE: **NoneType**<br> DEFAULT: **None**



### path

> TYPE: **str**

Node path up to the top node

### SEP

> TYPE: **str**<br> DEFAULT: **.**



### top

> TYPE: **Section**

Get the topmost section

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classfunc_) :black_small_square: [Content](#content) :black_small_square: [ClassFunc_](#classfunc_)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classfunc_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classfunc_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classfunc_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classfunc_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classfunc_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classfunc_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classfunc_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### FromInspect



``` python
FromInspect(obj)
```

Load python module

Load module and module members using inspect


#### Arguments:
- **obj** (_any_) : object to inspect



#### Returns:
- **Tree** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classfunc_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classfunc_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### get_child



``` python
get_child(key)
```

Get a direct child by its key


#### Arguments:
- **key**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classfunc_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classfunc_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classfunc_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classfunc_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classfunc_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classfunc_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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

In addition, special lists are extracted to create [DescriptionList](objin1-descriptionlist.md)

#### Extracted lists
- raises
- arguments
- returns
- properties


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classfunc_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### set_child



``` python
set_child(key, child, index=None)
```

set a direct child by its key


#### Arguments:
- **key**
- **child**
- **index** ( = None)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classfunc_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classfunc_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classfunc_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>


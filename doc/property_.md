# Property_



``` python
Property_(name, comment=None, **kwargs)
```

Information on property


#### Arguments:
- **name** (_str_) : object name
- **comment** (_str_ = None) : comment
- **kwargs**



### Inherited

dict.\_\_contains__ :black_small_square: dict.\_\_delitem__ :black_small_square: dict.\_\_eq__ :black_small_square: dict.\_\_ge__ :black_small_square: dict.\_\_getattribute__ :black_small_square: dict.\_\_gt__ :black_small_square: dict.\_\_ior__ :black_small_square: dict.\_\_le__ :black_small_square: dict.\_\_len__ :black_small_square: dict.\_\_lt__ :black_small_square: dict.\_\_ne__ :black_small_square: dict.\_\_or__ :black_small_square: dict.\_\_repr__ :black_small_square: dict.\_\_reversed__ :black_small_square: dict.\_\_ror__ :black_small_square: dict.\_\_sizeof__ :black_small_square: dict.clear :black_small_square: dict.copy :black_small_square: dict.items :black_small_square: dict.keys :black_small_square: dict.pop :black_small_square: dict.popitem :black_small_square: dict.setdefault :black_small_square: dict.update :black_small_square: dict.values :black_small_square: 

## Content

- **A** : [add](property_.md#add) :black_small_square: [all_count](property_.md#all_count) :black_small_square: [all_items](property_.md#all_items) :black_small_square: [all_paths](property_.md#all_paths) :black_small_square: [all_values](property_.md#all_values)
- **C** : [complete_with](property_.md#complete_with) :black_small_square: [count](property_.md#count) :black_small_square: [create_path](property_.md#create_path)
- **D** : [default](property_.md#default) :black_small_square: [depth](property_.md#depth) :black_small_square: [detach](property_.md#detach) :black_small_square: [DOT](property_.md#dot)
- **F** : [fget](property_.md#fget) :black_small_square: [find](property_.md#find) :black_small_square: [FromDict](property_.md#fromdict) :black_small_square: [FromFile](property_.md#fromfile) :black_small_square: [FromInspect](property_.md#frominspect) :black_small_square: [FromListItem](property_.md#fromlistitem) :black_small_square: [FromStatic](property_.md#fromstatic) :black_small_square: [fset](property_.md#fset)
- **G** : [get](property_.md#get) :black_small_square: [get_child](property_.md#get_child) :black_small_square: [get_prop](property_.md#get_prop)
- **I** : [is_top](property_.md#is_top)
- **J** : [join_keys](property_.md#join_keys)
- **K** : [key](property_.md#key)
- **M** : [meta](property_.md#meta) :black_small_square: [move_to_parent](property_.md#move_to_parent)
- **N** : [new](property_.md#new) :black_small_square: [new_paths](property_.md#new_paths)
- **O** : [obj_type](property_.md#obj_type)
- **P** : [parse_comment](property_.md#parse_comment) :black_small_square: [path](property_.md#path)
- **R** : [remove_from_parent](property_.md#remove_from_parent)
- **S** : [SEP](property_.md#sep) :black_small_square: [set_child](property_.md#set_child) :black_small_square: [solve_path](property_.md#solve_path) :black_small_square: [solve_to_missing](property_.md#solve_to_missing)
- **T** : [top](property_.md#top) :black_small_square: [type](property_.md#type)



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


### default


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>

default value


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




### fget


<table><tbody>
<tr><td>type</td><td><b>Function_</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>

getter [Function_](function_.md)


### fset


<table><tbody>
<tr><td>type</td><td><b>Function_</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>

setter [Function_](function_.md)


### is_top


<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

True if owner is None


### key


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




### obj_type


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>property</b</td></tr>
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


### type


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>

type of the property


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Property_](#property_)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### complete_with



``` python
complete_with(other, override=False)
```

Enrich the description with another one

A Property_ can be created either in properties list in a comment
or by scaning object.
This function allows to merge information coming from these two sources


#### Arguments:
- **other** (_Property_) : contains complementary description
- **override** ( = False)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### FromDict



``` python
FromDict(item)
```

Create a property from a dict


#### Arguments:
- **item** (_dict_) : information on the property to create



#### Returns:
- **Property_** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### FromInspect



``` python
FromInspect(name, property_object, verbose=False)
```

Create a Property_ instance from a property

> [!NOTE]
> If name is None, the name is read from fget


#### Arguments:
- **name** (_str_ = None) : name
- **property_object** (_property_) : the object the scan
- **verbose** ( = False)



#### Returns:
- **Property_** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### FromListItem



``` python
FromListItem(item)
```

Create a property from a list item


#### Arguments:
- **item** (_ListItem_) : information on the property to create



#### Returns:
- **Property_** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### FromStatic



``` python
FromStatic(property_object, name=None)
```

Creare a Property_ instance from a static property in a module or a class


#### Arguments:
- **property_object** : 
- **name** (_str_ = None)



#### Returns:
- **Property_** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### get_child



``` python
get_child(key)
```

Get a direct child by its key


#### Arguments:
- **key**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### remove_from_parent



``` python
remove_from_parent()
```

Remove the section from its parent list of children


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#property_) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>

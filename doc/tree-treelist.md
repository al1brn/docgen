# TreeList

``` python
f{self.name}{sig}
```



``` python
f{self.name}{sig}
```



Tree interface based on a list

This class inherits from [Tree](tree-tree.md) and list. Direct children are store in the list.

Several children can share the same key.

This implementation can be chosen when direct children can share a same key and / or when there is
a need to control the order of the children
### Inherited

list.\_\_add__ :black_small_square: list.\_\_contains__ :black_small_square: list.\_\_delitem__ :black_small_square: list.\_\_eq__ :black_small_square: list.\_\_ge__ :black_small_square: list.\_\_getattribute__ :black_small_square: list.\_\_gt__ :black_small_square: list.\_\_iadd__ :black_small_square: list.\_\_imul__ :black_small_square: list.\_\_le__ :black_small_square: list.\_\_len__ :black_small_square: list.\_\_lt__ :black_small_square: list.\_\_mul__ :black_small_square: list.\_\_ne__ :black_small_square: list.\_\_repr__ :black_small_square: list.\_\_reversed__ :black_small_square: list.\_\_rmul__ :black_small_square: list.\_\_sizeof__ :black_small_square: list.append :black_small_square: list.clear :black_small_square: list.copy :black_small_square: list.extend :black_small_square: list.index :black_small_square: list.insert :black_small_square: list.pop :black_small_square: list.remove :black_small_square: list.reverse :black_small_square: list.sort :black_small_square: 

### Inherited

list.\_\_add__ :black_small_square: list.\_\_contains__ :black_small_square: list.\_\_delitem__ :black_small_square: list.\_\_eq__ :black_small_square: list.\_\_ge__ :black_small_square: list.\_\_getattribute__ :black_small_square: list.\_\_gt__ :black_small_square: list.\_\_iadd__ :black_small_square: list.\_\_imul__ :black_small_square: list.\_\_le__ :black_small_square: list.\_\_len__ :black_small_square: list.\_\_lt__ :black_small_square: list.\_\_mul__ :black_small_square: list.\_\_ne__ :black_small_square: list.\_\_repr__ :black_small_square: list.\_\_reversed__ :black_small_square: list.\_\_rmul__ :black_small_square: list.\_\_sizeof__ :black_small_square: list.append :black_small_square: list.clear :black_small_square: list.copy :black_small_square: list.extend :black_small_square: list.index :black_small_square: list.insert :black_small_square: list.pop :black_small_square: list.remove :black_small_square: list.reverse :black_small_square: list.sort :black_small_square: 



## DOT


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>.</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>.</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>.</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>.</b</td></tr>
</tbody></table>



## FromFile

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Read the content of a drive

This methods shows how to use method [add](tree-treelist.md#add) to recursively load folder files and sub folders.

Arguments
---------
- folder (str) : folder to load
- pattern (str or tuple of strs) : file selection
- ignore (str or tuple of strs) : files starting by one of the characters in the string are ignored

Returns
-------
- Tree


#### Arguments:
- **folder** (_str_) : folder to load
- **pattern** (_str or tuple of strs_ = *.*) : file selection
- **ignore** (_str or tuple of strs_ = ('.*', '_*')) : files starting by one of the characters in the string are ignored



#### Returns:
- **Tree** : 



#### Arguments:
- **folder** (_str_) : folder to load
- **pattern** (_str or tuple of strs_ = *.*) : file selection
- **ignore** (_str or tuple of strs_ = ('.*', '_*')) : files starting by one of the characters in the string are ignored



#### Returns:
- **Tree** : 



#### Arguments:
- **folder** (_str_) : folder to load
- **pattern** (_str or tuple of strs_ = *.*) : file selection
- **ignore** (_str or tuple of strs_ = ('.*', '_*')) : files starting by one of the characters in the string are ignored



#### Returns:
- **Tree** : 



#### Arguments:
- **folder** (_str_) : folder to load
- **pattern** (_str or tuple of strs_ = *.*) : file selection
- **ignore** (_str or tuple of strs_ = ('.*', '_*')) : files starting by one of the characters in the string are ignored



#### Returns:
- **Tree** : 



## FromInspect

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Load python module

Load module and module members using inspect

Arguments
---------
- obj (any) : object to inspect

Returns
-------
- Tree


#### Arguments:
- **obj** (_any_) : object to inspect



#### Returns:
- **Tree** : 



#### Arguments:
- **obj** (_any_) : object to inspect



#### Returns:
- **Tree** : 



#### Arguments:
- **obj** (_any_) : object to inspect



#### Returns:
- **Tree** : 



#### Arguments:
- **obj** (_any_) : object to inspect



#### Returns:
- **Tree** : 



## SEP


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>/</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>/</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>/</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>/</b</td></tr>
</tbody></table>



## add

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Add a new node at the path

This method calls [set_child](tree-treelist.md#set_child).

Arguments
---------
- path (str) : the path where to locate the node
- node (Tree) : the node to set at the path

Returns
-------
- Tree : the node argument


#### Arguments:
- **path** (_str_) : the path where to locate the node
- **node** (_Tree_) : the node to set at the path
- **complete_path** ( = False)



#### Returns:
- **Tree** : the node argument



#### Arguments:
- **path** (_str_) : the path where to locate the node
- **node** (_Tree_) : the node to set at the path
- **complete_path** ( = False)



#### Returns:
- **Tree** : the node argument



#### Arguments:
- **path** (_str_) : the path where to locate the node
- **node** (_Tree_) : the node to set at the path
- **complete_path** ( = False)



#### Returns:
- **Tree** : the node argument



#### Arguments:
- **path** (_str_) : the path where to locate the node
- **node** (_Tree_) : the node to set at the path
- **complete_path** ( = False)



#### Returns:
- **Tree** : the node argument



## all_count


<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>



Total number of children

Returns
-------
- int


## all_items

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



All items iterator

Iterate on all items in the folder and sub folders.

Returns
-------
- iterator


#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** : 



#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** : 



#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** : 



#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** : 



## all_paths

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



All paths iterator

Iterate on all paths in the folder and sub folders.
Returns
-------
- iterator


#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** : 



#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** : 



#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** : 



#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** : 



## all_values

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



All values iterator

Iterate on all values in the folder and sub folders.

Returns
-------
- iterator


#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** : 



#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** : 



#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** : 



#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** : 



## count


<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>



Number of direct children, equivalent to `len(self)`

Returns
-------
- int


## create_path

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Create nodes in a path

Nodes are create by calling [new](tree-treelist.md#new) method.

Arguments
---------
- keys (list of strs) : key forming the path to create

Returns
-------
- Tree : last created node


#### Arguments:
- **keys** (_list of strs_) : key forming the path to create



#### Returns:
- **Tree** : last created node



#### Arguments:
- **keys** (_list of strs_) : key forming the path to create



#### Returns:
- **Tree** : last created node



#### Arguments:
- **keys** (_list of strs_) : key forming the path to create



#### Returns:
- **Tree** : last created node



#### Arguments:
- **keys** (_list of strs_) : key forming the path to create



#### Returns:
- **Tree** : last created node



## depth


<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>



Distance to the top (0 for top section)

Returns
-------
- int


## detach

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Detach the section from its parent children

> [!IMPORANT]
> This method calls the abstract method [remove_from_parent](tree-treelist.md#remove_from_parent) which must perform
> the actual removal from the parent's list of children.

Returns
-------
- Tree : self


#### Returns:
- **Tree** : self



#### Returns:
- **Tree** : self



#### Returns:
- **Tree** : self



#### Returns:
- **Tree** : self



## find

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Find one or more keys in the tree.

Arguments
---------
- keys (list of strs) : the keys to look for
- first (boolean) : stop on the first match an return the found node
- criteria : search the node with attributes match keyword arguments

Returns
-------
- Tree or list of Trees: on single tree if first is Trur


#### Arguments:
- **keys** (_list of strs_) : the keys to look for
- **first** (_boolean_ = False) : stop on the first match an return the found node
- **criteria** : search the node with attributes match keyword arguments



#### Returns:
- **Tree** : on single tree if first is Trur



#### Arguments:
- **keys** (_list of strs_) : the keys to look for
- **first** (_boolean_ = False) : stop on the first match an return the found node
- **criteria** : search the node with attributes match keyword arguments



#### Returns:
- **Tree** : on single tree if first is Trur



#### Arguments:
- **keys** (_list of strs_) : the keys to look for
- **first** (_boolean_ = False) : stop on the first match an return the found node
- **criteria** : search the node with attributes match keyword arguments



#### Returns:
- **Tree** : on single tree if first is Trur



#### Arguments:
- **keys** (_list of strs_) : the keys to look for
- **first** (_boolean_ = False) : stop on the first match an return the found node
- **criteria** : search the node with attributes match keyword arguments



#### Returns:
- **Tree** : on single tree if first is Trur



## get

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Get the node at path

Arguments
---------
- path (str) : the node path
- default (Tree) : the node to return if the path is not solved

Returns
-------
- Tree


#### Arguments:
- **path** (_str_) : the node path
- **default** (_Tree_ = None) : the node to return if the path is not solved



#### Returns:
- **Tree** : 



#### Arguments:
- **path** (_str_) : the node path
- **default** (_Tree_ = None) : the node to return if the path is not solved



#### Returns:
- **Tree** : 



#### Arguments:
- **path** (_str_) : the node path
- **default** (_Tree_ = None) : the node to return if the path is not solved



#### Returns:
- **Tree** : 



#### Arguments:
- **path** (_str_) : the node path
- **default** (_Tree_ = None) : the node to return if the path is not solved



#### Returns:
- **Tree** : 



## get_child

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Get a direct child by its key


#### Arguments:
- **key**



#### Arguments:
- **key**



#### Arguments:
- **key**



#### Arguments:
- **key**



## is_top


<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>



True if owner is None

Returns
-------
- bool


## items

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Iterate on (key, value) pais


## join_keys

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Join keys to form a path

Joins the keys with the key separator avoiding double separators: `join_keys("AAA", "BBB")`
and `join_keys("AAA/", "BBB")` will both give `"AAA/BBB"`.


Returns
-------
- str : key joined by key separator


#### Arguments:
- **keys**



#### Returns:
- **str** : key joined by key separator



#### Arguments:
- **keys**



#### Returns:
- **str** : key joined by key separator



#### Arguments:
- **keys**



#### Returns:
- **str** : key joined by key separator



#### Arguments:
- **keys**



#### Returns:
- **str** : key joined by key separator



## keys

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Iterate on keys


## move_to_parent

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Change the position of a node from one parent to another

This methods basically calls [detach](tree-treelist.md#detach) and then [add](tree-treelist.md#add).

Arguments
---------
- new_parent (Tree) : where to locate the node
- new_key (str = None) : new key, uses the current key is None

Returns
- Tree : self


#### Arguments:
- **new_parent** (_Tree_) : where to locate the node
- **new_key** (_str_ = None) : new key, uses the current key is None



#### Arguments:
- **new_parent** (_Tree_) : where to locate the node
- **new_key** (_str_ = None) : new key, uses the current key is None



#### Arguments:
- **new_parent** (_Tree_) : where to locate the node
- **new_key** (_str_ = None) : new key, uses the current key is None



#### Arguments:
- **new_parent** (_Tree_) : where to locate the node
- **new_key** (_str_ = None) : new key, uses the current key is None



## new

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Create a new node at the given path

The default implementation create a new node by calling the defaut constructor
and adding it by calling [add](tree-treelist.md#add):
    
``` python
return self.add(path, type(self)(**kwargs), complete_path=complete_path)
``` 

Raises
------
- PathError : if nodes are missing in the path

Arguments
---------
- path (str) : the path where to create a new node
- complete_path (set = None) : create the path if hole exist
- kwargs : default constructor arguments

Returns
-------
- Tree : the created node


#### Raises:
- **PathError** : if nodes are missing in the path



#### Arguments:
- **path** (_str_) : the path where to create a new node
- **complete_path** (_set_ = False) : create the path if hole exist
- **kwargs** : default constructor arguments



#### Returns:
- **Tree** : the created node



#### Raises:
- **PathError** : if nodes are missing in the path



#### Arguments:
- **path** (_str_) : the path where to create a new node
- **complete_path** (_set_ = False) : create the path if hole exist
- **kwargs** : default constructor arguments



#### Returns:
- **Tree** : the created node



#### Raises:
- **PathError** : if nodes are missing in the path



#### Arguments:
- **path** (_str_) : the path where to create a new node
- **complete_path** (_set_ = False) : create the path if hole exist
- **kwargs** : default constructor arguments



#### Returns:
- **Tree** : the created node



#### Raises:
- **PathError** : if nodes are missing in the path



#### Arguments:
- **path** (_str_) : the path where to create a new node
- **complete_path** (_set_ = False) : create the path if hole exist
- **kwargs** : default constructor arguments



#### Returns:
- **Tree** : the created node



## new_paths

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Create several nodes defined by their path

Basically, this method call [new](tree-treelist.md#new) for each provided path.

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

Arguments
---------
- paths (list of str) : the paths of the nodes to create
- complete_path (bool = False) : create intermediary nodes in paths
- kwargs : default constructor arguments when creating intermediary is required

Returns
-------
- Tree : the created child


#### Arguments:
- **paths** (_list of str_) : the paths of the nodes to create
- **complete_path** (_bool_ = False) : create intermediary nodes in paths
- **kwargs** : default constructor arguments when creating intermediary is required



#### Returns:
- **Tree** : the created child



#### Arguments:
- **paths** (_list of str_) : the paths of the nodes to create
- **complete_path** (_bool_ = False) : create intermediary nodes in paths
- **kwargs** : default constructor arguments when creating intermediary is required



#### Returns:
- **Tree** : the created child



#### Arguments:
- **paths** (_list of str_) : the paths of the nodes to create
- **complete_path** (_bool_ = False) : create intermediary nodes in paths
- **kwargs** : default constructor arguments when creating intermediary is required



#### Returns:
- **Tree** : the created child



#### Arguments:
- **paths** (_list of str_) : the paths of the nodes to create
- **complete_path** (_bool_ = False) : create intermediary nodes in paths
- **kwargs** : default constructor arguments when creating intermediary is required



#### Returns:
- **Tree** : the created child



## path


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>



Node path up to the top node

Returns
-------
- str


## remove_from_parent

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Remove the section from its parent list of children


## set_child

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



set a direct child by its key


#### Arguments:
- **key**
- **child**
- **index** ( = None)



#### Arguments:
- **key**
- **child**
- **index** ( = None)



#### Arguments:
- **key**
- **child**
- **index** ( = None)



#### Arguments:
- **key**
- **child**
- **index** ( = None)



## solve_path

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Solve a path

Returns the node corresponding to the path.

If it doesn't exist, two cases are possible:
- only the last key in the path is missing: the methods return the parent
  and the missing key
- an intermediary node is missing: the methods raises an error or creates
  the missing nodes depending on the arguments **complete_path**.
  
> [!NOTE]
> Missing nodes in the path are created with method [create_path](tree-treelist.md#create_path)
 
Raises
------
- PathError : if the path can't be solved up to the last, or last but one

Arguments
---------
- path (str) : the path to solve
- complete_path (bool) : create missing nodes (but the last one) if necessary

Returns
-------
- Tree, str : (found node, None) or (parent node, missing key)


#### Raises:
- **PathError** : if the path can't be solved up to the last, or last but one



#### Arguments:
- **path** (_str_) : the path to solve
- **complete_path** (_bool_ = False) : create missing nodes (but the last one) if necessary



#### Returns:
- **Tree** : (found node, None) or (parent node, missing key)



#### Raises:
- **PathError** : if the path can't be solved up to the last, or last but one



#### Arguments:
- **path** (_str_) : the path to solve
- **complete_path** (_bool_ = False) : create missing nodes (but the last one) if necessary



#### Returns:
- **Tree** : (found node, None) or (parent node, missing key)



#### Raises:
- **PathError** : if the path can't be solved up to the last, or last but one



#### Arguments:
- **path** (_str_) : the path to solve
- **complete_path** (_bool_ = False) : create missing nodes (but the last one) if necessary



#### Returns:
- **Tree** : (found node, None) or (parent node, missing key)



#### Raises:
- **PathError** : if the path can't be solved up to the last, or last but one



#### Arguments:
- **path** (_str_) : the path to solve
- **complete_path** (_bool_ = False) : create missing nodes (but the last one) if necessary



#### Returns:
- **Tree** : (found node, None) or (parent node, missing key)



## solve_to_missing

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Solve a path to missing keys

Solve a path, return the existing node and the list of non existing keys.

Raises
------
- PathError : if path is incorrect


Arguments
---------
- path (str) : path to solve

Returns
-------
- node, list : last existing node, list of missing keys


#### Raises:
- **PathError** : if path is incorrect



#### Arguments:
- **path** (_str_) : path to solve



#### Returns:
- **node** : last existing node, list of missing keys



#### Raises:
- **PathError** : if path is incorrect



#### Arguments:
- **path** (_str_) : path to solve



#### Returns:
- **node** : last existing node, list of missing keys



#### Raises:
- **PathError** : if path is incorrect



#### Arguments:
- **path** (_str_) : path to solve



#### Returns:
- **node** : last existing node, list of missing keys



#### Raises:
- **PathError** : if path is incorrect



#### Arguments:
- **path** (_str_) : path to solve



#### Returns:
- **node** : last existing node, list of missing keys



## top


<table><tbody>
<tr><td>type</td><td><b>Section</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>Section</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>Section</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>Section</b></td></tr>
</tbody></table>



Get the topmost section

Returns
-------
- Section


## values

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Iterate on childs

# ModuleSection

``` python
f{self.name}{sig}
```



``` python
f{self.name}{sig}
```



Modulesection

Properties
----------
- package (str) : module package
- _init (ModuleSection) : [ModuleSection](pydoc-modulesection.md) __init__ file if exists

Arguments
---------
- name (str) : object name
- comment (str = None) : comment
- tag (str = None) : section tag
- parameters : parameter initial values


#### Arguments:
- **name** (_str_) : object name
- **comment** (_str_ = None) : comment
- **tag** (_str_ = None) : section tag
- **parameters** : parameter initial values

### Inherited

list.\_\_add__ :black_small_square: list.\_\_contains__ :black_small_square: list.\_\_delitem__ :black_small_square: list.\_\_eq__ :black_small_square: list.\_\_ge__ :black_small_square: list.\_\_getattribute__ :black_small_square: list.\_\_gt__ :black_small_square: list.\_\_iadd__ :black_small_square: list.\_\_imul__ :black_small_square: list.\_\_le__ :black_small_square: list.\_\_len__ :black_small_square: list.\_\_lt__ :black_small_square: list.\_\_mul__ :black_small_square: list.\_\_ne__ :black_small_square: list.\_\_repr__ :black_small_square: list.\_\_reversed__ :black_small_square: list.\_\_rmul__ :black_small_square: list.\_\_sizeof__ :black_small_square: list.append :black_small_square: list.clear :black_small_square: list.copy :black_small_square: list.extend :black_small_square: list.index :black_small_square: list.insert :black_small_square: list.pop :black_small_square: list.remove :black_small_square: list.reverse :black_small_square: list.sort :black_small_square: 



#### Arguments:
- **name** (_str_) : object name
- **comment** (_str_ = None) : comment
- **tag** (_str_ = None) : section tag
- **parameters** : parameter initial values

### Inherited

list.\_\_add__ :black_small_square: list.\_\_contains__ :black_small_square: list.\_\_delitem__ :black_small_square: list.\_\_eq__ :black_small_square: list.\_\_ge__ :black_small_square: list.\_\_getattribute__ :black_small_square: list.\_\_gt__ :black_small_square: list.\_\_iadd__ :black_small_square: list.\_\_imul__ :black_small_square: list.\_\_le__ :black_small_square: list.\_\_len__ :black_small_square: list.\_\_lt__ :black_small_square: list.\_\_mul__ :black_small_square: list.\_\_ne__ :black_small_square: list.\_\_repr__ :black_small_square: list.\_\_reversed__ :black_small_square: list.\_\_rmul__ :black_small_square: list.\_\_sizeof__ :black_small_square: list.append :black_small_square: list.clear :black_small_square: list.copy :black_small_square: list.extend :black_small_square: list.index :black_small_square: list.insert :black_small_square: list.pop :black_small_square: list.remove :black_small_square: list.reverse :black_small_square: list.sort :black_small_square: 



## CHAPTER


<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
<tr><td>default</td><td><b>2</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
<tr><td>default</td><td><b>2</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
<tr><td>default</td><td><b>2</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
<tr><td>default</td><td><b>2</b</td></tr>
</tbody></table>



## DOT


<table><tbody>
<tr><td>type</td><td><b>NoneType</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>NoneType</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>NoneType</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>NoneType</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
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

This methods shows how to use method [add](pydoc-modulesection.md#add) to recursively load folder files and sub folders.

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



Create a ModuleSection by inspecting a module object

Arguments
---------
- name (str) : module name
- module_object (module) : the module to scan


#### Arguments:
- **name** (_str_) : module name
- **module_object** (_module_) : the module to scan



#### Arguments:
- **name** (_str_) : module name
- **module_object** (_module_) : the module to scan



#### Arguments:
- **name** (_str_) : module name
- **module_object** (_module_) : the module to scan



#### Arguments:
- **name** (_str_) : module name
- **module_object** (_module_) : the module to scan



## PAGE


<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
<tr><td>default</td><td><b>1</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
<tr><td>default</td><td><b>1</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
<tr><td>default</td><td><b>1</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
<tr><td>default</td><td><b>1</b</td></tr>
</tbody></table>



## SEP


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



## TEXT


<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
<tr><td>default</td><td><b>0</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
<tr><td>default</td><td><b>0</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
<tr><td>default</td><td><b>0</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
<tr><td>default</td><td><b>0</b</td></tr>
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

This method calls [set_child](pydoc-modulesection.md#set_child).

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



## anchor


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



The anchor of this section within the page

Returns
-------
- str : section anchor


## chapter


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



Get the chapter this section belongs to

> [!CAUTION]
> Since a chapter returns self, a misuse could lead to infinite recurrence loop

Returns
-------
- Section : chapter this section belongs to


## chapter_prefix


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



Get the prefix to use in the file names of pages in this chapter

To avoid to long names, prefix uses the 5 first chars plus a number
if collision

Returns
-------
- str : chapter path with - char as separator


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

Nodes are create by calling [new](pydoc-modulesection.md#new) method.

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
> This method calls the abstract method [remove_from_parent](pydoc-modulesection.md#remove_from_parent) which must perform
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



## file_name


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



File name were to write the page

The file name is built by joining [chapter_prefix](pydoc-modulesection.md#chapter_prefix) with the name of section.

> [!NOTE]
> top chapter returns "index.md"

Returns
-------
- str : file name


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



## get_content

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



Returns the text to write in the page

A page is built by:
- joining section and comment
- optionnally joining a table of content
- recursively joining the content of the children

Returns
-------
- str : section and sub section content


#### Returns:
- **str** : section and sub section content



#### Returns:
- **str** : section and sub section content



#### Returns:
- **str** : section and sub section content



#### Returns:
- **str** : section and sub section content



## get_create_section

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



Get an existing section or create a new one

> [!NOTE]
> Contrary to ['#get_section' not found](), this method searchs the section only
> in the direct children, not in all the hierarchy.

Arguments
---------
- title (str) : section title
- comment (str) : section comment
- kwargs : valid section attribute settings

Returns
-------
- Section : chapter section


#### Arguments:
- **title** (_str_) : section title
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : chapter section



#### Arguments:
- **title** (_str_) : section title
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : chapter section



#### Arguments:
- **title** (_str_) : section title
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : chapter section



#### Arguments:
- **title** (_str_) : section title
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : chapter section



## get_toc

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



Build the list of toc items

The methods return a list of paris giving:
- the level of the item
- the MD links

Arguments
---------
- flat (bool) : toc is a flat list or hierarchical
- sort (bool) : sort the list (force **flat** if True)
- max_length (int) : use alphabetical list if the number of items in the toc
  is greater thant this value
- max_depth (int) : max relative depth for a hierarchical toc

Returns
-------
- list of strs : one entry per line


#### Arguments:
- **flat** (_bool_ = None) : toc is a flat list or hierarchical
- **sort** (_bool_ = None) : sort the list (force **flat** if True)
- **max_length** (_int_ = 10) : use alphabetical list if the number of items in the toc is greater thant this value
- **max_depth** (_int_ = 2) : max relative depth for a hierarchical toc



#### Returns:
- **list** : one entry per line



#### Arguments:
- **flat** (_bool_ = None) : toc is a flat list or hierarchical
- **sort** (_bool_ = None) : sort the list (force **flat** if True)
- **max_length** (_int_ = 10) : use alphabetical list if the number of items in the toc is greater thant this value
- **max_depth** (_int_ = 2) : max relative depth for a hierarchical toc



#### Returns:
- **list** : one entry per line



#### Arguments:
- **flat** (_bool_ = None) : toc is a flat list or hierarchical
- **sort** (_bool_ = None) : sort the list (force **flat** if True)
- **max_length** (_int_ = 10) : use alphabetical list if the number of items in the toc is greater thant this value
- **max_depth** (_int_ = 2) : max relative depth for a hierarchical toc



#### Returns:
- **list** : one entry per line



#### Arguments:
- **flat** (_bool_ = None) : toc is a flat list or hierarchical
- **sort** (_bool_ = None) : sort the list (force **flat** if True)
- **max_length** (_int_ = 10) : use alphabetical list if the number of items in the toc is greater thant this value
- **max_depth** (_int_ = 2) : max relative depth for a hierarchical toc



#### Returns:
- **list** : one entry per line



## get_toc_sections

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



Return the dictionary of sections being part of the toc

If **flat** is True, the search for sub sections in the toc continues
within sections in the toc.

If **flat** is False, the exploration stops as soon as a section is
in the toc.

Arguments
---------
- flat (bool = None) : returns the sections without hierarchy, use default if None

Returns
-------
- list : sections in the table of content of the page


#### Arguments:
- **flat** (_bool_ = None) : returns the sections without hierarchy, use default if None



#### Returns:
- **list** : sections in the table of content of the page



#### Arguments:
- **flat** (_bool_ = None) : returns the sections without hierarchy, use default if None



#### Returns:
- **list** : sections in the table of content of the page



#### Arguments:
- **flat** (_bool_ = None) : returns the sections without hierarchy, use default if None



#### Returns:
- **list** : sections in the table of content of the page



#### Arguments:
- **flat** (_bool_ = None) : returns the sections without hierarchy, use default if None



#### Returns:
- **list** : sections in the table of content of the page



## has_content


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>



## has_toc


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>



## header_depth


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



Header depth relatively to the page

The header depth doesn't include transparent parents. It aloso take
the ['#depth_shift' not found]() into account

Returns
-------
- int : distance to the page, excluding transparent parents and taking shift into account


## homonyms_count


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



Count the number of sections have the same title

This number is used to suffix the title anchor if needed.

> [!NOTE]
> The number of homonymes is count up the the section iself, not after

Returns
-------
- int: number of above sections sharing the same title


## insert_toc

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



Insert the toc section

Returns
-------
- Section : None if no toc


#### Returns:
- **Section** : None if no toc



#### Returns:
- **Section** : None if no toc



#### Returns:
- **Section** : None if no toc



#### Returns:
- **Section** : None if no toc



## is_chapter


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>



## is_hidden


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>



## is_page


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>



## is_text


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>



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


## is_transparent


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>



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


## link_to

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



Returns the link to a target from this section

> [!NOTE]
> Make sure to call this method once the full document structure is terminated

**target** can be one of the following keywords:
- INDEX : index page of the documentation
- TOP : top of the page
- TOC : table of content in the page
- UP : parent section

If **target** is a string other than one of the keywords above, it is considered
as the title of the section to reach. Since sections can share the same name,
the section is searched in the following order:
- in the child sections, including child pages
- in this page
- as a page title
- in the whole documentation

Arguments
---------
- target (str = None) : target of the link, self if None
- absolute (bool = True) : include file name, only the anchor otherwise
- title (str = None) : link title, use self.['#title' not found]() if None

Returns
-------
- str : link in md format `[title](file.md#anchor)`


#### Arguments:
- **target** (_str_ = None) : target of the link, self if None
- **title** (_str_ = None) : link title, use self.['#title' not found]() if None



#### Returns:
- **str** : link in md format `[title](file.md#anchor)`



#### Arguments:
- **target** (_str_ = None) : target of the link, self if None
- **title** (_str_ = None) : link title, use self.['#title' not found]() if None



#### Returns:
- **str** : link in md format `[title](file.md#anchor)`



#### Arguments:
- **target** (_str_ = None) : target of the link, self if None
- **title** (_str_ = None) : link title, use self.['#title' not found]() if None



#### Returns:
- **str** : link in md format `[title](file.md#anchor)`



#### Arguments:
- **target** (_str_ = None) : target of the link, self if None
- **title** (_str_ = None) : link title, use self.['#title' not found]() if None



#### Returns:
- **str** : link in md format `[title](file.md#anchor)`



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

This methods basically calls [detach](pydoc-modulesection.md#detach) and then [add](pydoc-modulesection.md#add).

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



## navigation_md


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>



Get navigation markdown

Navigation bar is built with ['#navigation' not found]() list


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



Add a section

Arguments
---------
- title (str) : section title
- comment (str) : section comment
- kwargs : valid section attribute settings

Returns
-------
- Section : created section


#### Arguments:
- **title** (_str_) : section title
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : created section



#### Arguments:
- **title** (_str_) : section title
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : created section



#### Arguments:
- **title** (_str_) : section title
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : created section



#### Arguments:
- **title** (_str_) : section title
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : created section



## new_chapter

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



Add a chapter section

Arguments
---------
- chapter (str) : name of the chapter to create
- comment (str) : section comment
- kwargs : valid section attribute settings

Returns
-------
- Section : chapter section


#### Arguments:
- **chapter** (_str_) : name of the chapter to create
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : chapter section



#### Arguments:
- **chapter** (_str_) : name of the chapter to create
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : chapter section



#### Arguments:
- **chapter** (_str_) : name of the chapter to create
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : chapter section



#### Arguments:
- **chapter** (_str_) : name of the chapter to create
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : chapter section



## new_page

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



Add a page section

Arguments
---------
- title (str) : section title
- comment (str) : section comment
- kwargs : valid section attribute settings

Returns
-------
- Section : page section


#### Arguments:
- **title** (_str_) : section title
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : page section



#### Arguments:
- **title** (_str_) : section title
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : page section



#### Arguments:
- **title** (_str_) : section title
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : page section



#### Arguments:
- **title** (_str_) : section title
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : page section



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

Basically, this method call [new](pydoc-modulesection.md#new) for each provided path.

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



## new_sections_group

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



Create a section from a list of sections

The section is created only if the list has items.

The sections are move to the newly created section using [move_to_parent](tree-tree.md#move_to_parent).

Arguments
---------
- title (str) : title of the section to create
- sections (list of Sections) : the section to move into the created section
- parameters : parameters for the section to create

Returns
-------
- Section : the created section


#### Arguments:
- **title** (_str_) : title of the section to create
- **sections** (_list of Sections_) : the section to move into the created section
- **parameters** : parameters for the section to create



#### Returns:
- **Section** : the created section



#### Arguments:
- **title** (_str_) : title of the section to create
- **sections** (_list of Sections_) : the section to move into the created section
- **parameters** : parameters for the section to create



#### Returns:
- **Section** : the created section



#### Arguments:
- **title** (_str_) : title of the section to create
- **sections** (_list of Sections_) : the section to move into the created section
- **parameters** : parameters for the section to create



#### Returns:
- **Section** : the created section



#### Arguments:
- **title** (_str_) : title of the section to create
- **sections** (_list of Sections_) : the section to move into the created section
- **parameters** : parameters for the section to create



#### Returns:
- **Section** : the created section



## new_tag_group

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



Create a section grouping all the sub sections having a given tag

The section is created only if sections have the tag

The group is created by calling [new_sections_group](pydoc-modulesection.md#new_sections_group).

Arguments
---------
- tag (str) : tag to group sections
- parameters : parameters for the section to create

Returns
-------
- Section : the created section


#### Arguments:
- **tag** (_str_) : tag to group sections
- **parameters** : parameters for the section to create



#### Returns:
- **Section** : the created section



#### Arguments:
- **tag** (_str_) : tag to group sections
- **parameters** : parameters for the section to create



#### Returns:
- **Section** : the created section



#### Arguments:
- **tag** (_str_) : tag to group sections
- **parameters** : parameters for the section to create



#### Returns:
- **Section** : the created section



#### Arguments:
- **tag** (_str_) : tag to group sections
- **parameters** : parameters for the section to create



#### Returns:
- **Section** : the created section



## page


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



Get the page this section belongs to

> [!CAUTION]
> Since a page returns self, a misuse could lead to infinite recurrence loop

Returns
-------
- Section : page this section belongs to


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
> Missing nodes in the path are created with method [create_path](pydoc-modulesection.md#create_path)
 
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


## user_prop

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



Get a user defined property

User can can define property with $ DOC SET property syntax
within source comment

Arguments
---------
- name (str) : property name
- default (any = None) : default if not defined

Returns
-------
- any


#### Arguments:
- **name** (_str_) : property name
- **default** (_any_ = None) : default if not defined



#### Returns:
- **any** : 



#### Arguments:
- **name** (_str_) : property name
- **default** (_any_ = None) : default if not defined



#### Returns:
- **any** : 



#### Arguments:
- **name** (_str_) : property name
- **default** (_any_ = None) : default if not defined



#### Returns:
- **any** : 



#### Arguments:
- **name** (_str_) : property name
- **default** (_any_ = None) : default if not defined



#### Returns:
- **any** : 



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


## write

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



Append text to the header comment

Arguments
---------
- text (str) : the text to write


#### Arguments:
- **text** (_str_) : the text to write



#### Arguments:
- **text** (_str_) : the text to write



#### Arguments:
- **text** (_str_) : the text to write



#### Arguments:
- **text** (_str_) : the text to write



## write_header

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



Write a section in the text stream

This method write markdonw text corresponding to a header followed by text.

> [!NOTE]
> This method doesn't create a section in the hierarchy, contrary to ['#add_section' not found]()

Arguments
---------
- level (int) : header level
- title (str) : header title
- text (str) : text


#### Arguments:
- **level** (_int_) : header level
- **title** (_str_) : header title
- **text** (_str_) : text



#### Arguments:
- **level** (_int_) : header level
- **title** (_str_) : header title
- **text** (_str_) : text



#### Arguments:
- **level** (_int_) : header level
- **title** (_str_) : header title
- **text** (_str_) : text



#### Arguments:
- **level** (_int_) : header level
- **title** (_str_) : header title
- **text** (_str_) : text



## write_source

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



Append source code to the header comment

Arguments
---------
- source (str) : source code to append


#### Arguments:
- **source** (_str_) : source code to append



#### Arguments:
- **source** (_str_) : source code to append



#### Arguments:
- **source** (_str_) : source code to append



#### Arguments:
- **source** (_str_) : source code to append


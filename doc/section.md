# Section



``` python
Section(title, comment=None, tag=None, **parameters)
```

Document section

Project documentation is made of **pages** organized in **chapters**.

The documentation is based on the versatile class [Section](section.md) which can be:
- a text section in a page
- a documentation page
- a chapter
- the whole documentation itself

A [Section](section.md) is basically a list of **sub sections** with a header [comment](section.md#comment).


#### Arguments:
- **title** (_str_) : section title
- **comment** (_str_ = None) : text to display just below the section title
- **tag** ( = None)
- **parameters** : initial values for properties



### Inherited

list.\_\_add__ :black_small_square: list.\_\_contains__ :black_small_square: list.\_\_delitem__ :black_small_square: list.\_\_eq__ :black_small_square: list.\_\_ge__ :black_small_square: list.\_\_getattribute__ :black_small_square: list.\_\_gt__ :black_small_square: list.\_\_iadd__ :black_small_square: list.\_\_imul__ :black_small_square: list.\_\_le__ :black_small_square: list.\_\_len__ :black_small_square: list.\_\_lt__ :black_small_square: list.\_\_mul__ :black_small_square: list.\_\_ne__ :black_small_square: list.\_\_repr__ :black_small_square: list.\_\_reversed__ :black_small_square: list.\_\_rmul__ :black_small_square: list.\_\_sizeof__ :black_small_square: list.append :black_small_square: list.clear :black_small_square: list.copy :black_small_square: list.extend :black_small_square: list.index :black_small_square: list.insert :black_small_square: list.pop :black_small_square: list.remove :black_small_square: list.reverse :black_small_square: list.sort :black_small_square: 

## Content

- **A** : [add](section.md#add) :black_small_square: [all_count](section.md#all_count) :black_small_square: [all_items](section.md#all_items) :black_small_square: [all_paths](section.md#all_paths) :black_small_square: [all_values](section.md#all_values) :black_small_square: [anchor](section.md#anchor)
- **C** : [chapter](section.md#chapter) :black_small_square: [chapter_prefix](section.md#chapter_prefix) :black_small_square: [comment](section.md#comment) :black_small_square: [cook](section.md#cook) :black_small_square: [count](section.md#count) :black_small_square: [create_path](section.md#create_path)
- **D** : [depth](section.md#depth) :black_small_square: [depth_shift](section.md#depth_shift) :black_small_square: [detach](section.md#detach) :black_small_square: [DOT](section.md#dot)
- **F** : [file_name](section.md#file_name) :black_small_square: [find](section.md#find) :black_small_square: [FromFile](section.md#fromfile) :black_small_square: [FromInspect](section.md#frominspect)
- **G** : [get](section.md#get) :black_small_square: [get_child](section.md#get_child) :black_small_square: [get_content](section.md#get_content) :black_small_square: [get_create_section](section.md#get_create_section) :black_small_square: [get_toc](section.md#get_toc) :black_small_square: [get_toc_sections](section.md#get_toc_sections)
- **H** : [has_content](section.md#has_content) :black_small_square: [has_toc](section.md#has_toc) :black_small_square: [header_depth](section.md#header_depth) :black_small_square: [hidden](section.md#hidden) :black_small_square: [homonyms_count](section.md#homonyms_count)
- **I** : [ignore_if_empty](section.md#ignore_if_empty) :black_small_square: [insert_toc](section.md#insert_toc) :black_small_square: [in_toc](section.md#in_toc) :black_small_square: [is_chapter](section.md#is_chapter) :black_small_square: [is_hidden](section.md#is_hidden) :black_small_square: [is_page](section.md#is_page) :black_small_square: [is_text](section.md#is_text) :black_small_square: [is_toc](section.md#is_toc) :black_small_square: [is_top](section.md#is_top) :black_small_square: [is_transparent](section.md#is_transparent) :black_small_square: [items](section.md#items)
- **J** : [join_keys](section.md#join_keys)
- **K** : [keys](section.md#keys)
- **L** : [link_to](section.md#link_to)
- **M** : [move_to_parent](section.md#move_to_parent)
- **N** : [navigation](section.md#navigation) :black_small_square: [navigation_md](section.md#navigation_md) :black_small_square: [new](section.md#new) :black_small_square: [new_chapter](section.md#new_chapter) :black_small_square: [new_page](section.md#new_page) :black_small_square: [new_paths](section.md#new_paths) :black_small_square: [new_sections_group](section.md#new_sections_group) :black_small_square: [new_tag_group](section.md#new_tag_group)
- **P** : [page](section.md#page) :black_small_square: [path](section.md#path)
- **R** : [remove_from_parent](section.md#remove_from_parent)
- **S** : [SEP](section.md#sep) :black_small_square: [set_child](section.md#set_child) :black_small_square: [solve_path](section.md#solve_path) :black_small_square: [solve_to_missing](section.md#solve_to_missing) :black_small_square: [sort_sections](section.md#sort_sections)
- **T** : [tags](section.md#tags) :black_small_square: [title](section.md#title) :black_small_square: [toc](section.md#toc) :black_small_square: [toc_depth_shift](section.md#toc_depth_shift) :black_small_square: [toc_flat](section.md#toc_flat) :black_small_square: [toc_sort](section.md#toc_sort) :black_small_square: [toc_title](section.md#toc_title) :black_small_square: [top](section.md#top) :black_small_square: [top_bar](section.md#top_bar) :black_small_square: [transparent](section.md#transparent)
- **V** : [values](section.md#values)
- **W** : [write](section.md#write) :black_small_square: [write_header](section.md#write_header) :black_small_square: [write_source](section.md#write_source)



## Properties

### all_count


<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>

Total number of children


### anchor


<table><tbody>
<tr><td>type</td><td><b>str</b> , section anchor</td></tr>
</tbody></table>

The anchor of this section within the page


### chapter


<table><tbody>
<tr><td>type</td><td><b>Section</b> , chapter this section belongs to</td></tr>
</tbody></table>

Get the chapter this section belongs to

> [!CAUTION]
> Since a chapter returns self, a misuse could lead to infinite recurrence loop


### chapter_prefix


<table><tbody>
<tr><td>type</td><td><b>str</b> , chapter path with - char as separator</td></tr>
</tbody></table>

Get the prefix to use in the file names of pages in this chapter

To avoid to long names, prefix uses the 5 first chars plus a number
if collision


### comment


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>

text to display just below the section title


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


### depth_shift


<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
<tr><td>default</td><td><b>0</b</td></tr>
</tbody></table>

value to add to its depth for its header level in the final documentation, see [header_depth](#header_depth)


### DOT


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>.</b</td></tr>
</tbody></table>




### file_name


<table><tbody>
<tr><td>type</td><td><b>str</b> , file name</td></tr>
</tbody></table>

File name were to write the page

The file name is built by joining [chapter_prefix](#chapter_prefix) with the name of section.

> [!NOTE]
> top chapter returns "index.md"


### has_content


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>

the section has a not empty comment or has sections with content


### has_toc


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>

(for page only) the page must display a table of content section


### header_depth


<table><tbody>
<tr><td>type</td><td><b>int</b> , distance to the page, excluding transparent parents and taking shift into account</td></tr>
</tbody></table>

Header depth relatively to the page

The header depth doesn't include transparent parents. It aloso take
the [depth_shift](#depth_shift) into account


### hidden


<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>

hide this section


### homonyms_count


<table><tbody>
<tr><td>type</td><td><b>int</b> , number of above sections sharing the same title</td></tr>
</tbody></table>

Count the number of sections have the same title

This number is used to suffix the title anchor if needed.

> [!NOTE]
> The number of homonymes is count up the the section iself, not after


### ignore_if_empty


<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>

don't display the section if it has no content


### in_toc


<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>

put this section in its page table of content


### is_chapter


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>

the section is a chapter


### is_hidden


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>

the section, and its sub sections, are ignored


### is_page


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>

the section is a page


### is_text


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>

the section is text (neither a page nor a chapter)


### is_toc


<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
<tr><td>default</td><td><b>False</b</td></tr>
</tbody></table>

this section is the toc, don't create a new one


### is_top


<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

True if owner is None


### is_transparent


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>

the section is not displayed by itself, its content are attached to its parent


### navigation


<table><tbody>
<tr><td>type</td><td><b>list</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>

bottom navigation bar content


### navigation_md


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>

Get navigation markdown

Navigation bar is built with [navigation](#navigation) list


### page


<table><tbody>
<tr><td>type</td><td><b>Section</b> , page this section belongs to</td></tr>
</tbody></table>

Get the page this section belongs to

> [!CAUTION]
> Since a page returns self, a misuse could lead to infinite recurrence loop


### path


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

Node path up to the top node


### SEP


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>/</b</td></tr>
</tbody></table>




### sort_sections


<table><tbody>
<tr><td>type</td><td><b>bool or str</b></td></tr>
<tr><td>default</td><td><b>False</b</td></tr>
</tbody></table>

sort sections in alphabetical order when added (case sensitive if 'CASE')


### tags


<table><tbody>
<tr><td>type</td><td><b>set</b></td></tr>
<tr><td>default</td><td><b>empty set</b</td></tr>
</tbody></table>

a set of tags


### title


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>

section title


### toc


<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
<tr><td>default</td><td><b>False</b</td></tr>
</tbody></table>

insert a toc


### toc_depth_shift


<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
<tr><td>default</td><td><b>0</b</td></tr>
</tbody></table>

toc section [depth_shift](#depth_shift) (if any)


### toc_flat


<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
<tr><td>default</td><td><b>False</b</td></tr>
</tbody></table>

flat toc (if any)


### toc_sort


<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
<tr><td>default</td><td><b>False</b</td></tr>
</tbody></table>

sorted toc (if any)


### toc_title


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>'Content'</b</td></tr>
</tbody></table>

name of the toc (if any)


### top


<table><tbody>
<tr><td>type</td><td><b>Section</b></td></tr>
</tbody></table>

Get the topmost section


### top_bar


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>None or '-'</b</td></tr>
</tbody></table>

char to use to display an horizontal bar before the section


### transparent


<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
<tr><td>default</td><td><b>False</b</td></tr>
</tbody></table>

force [is_transparent](#is_transparent)


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Section](#section)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### cook



``` python
cook()
```

Cook the section and child sections

Default behavior is:
- sort the sections if ['#sort_section' not found]() is set
- cook the child sections
- insert the toc

Hidden sections are not cooked!


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### get_child



``` python
get_child(key)
```

Get a direct child by its key


#### Arguments:
- **key**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### get_content



``` python
get_content()
```

Returns the text to write in the page

A page is built by:
- joining section and comment
- optionnally joining a table of content
- recursively joining the content of the children


#### Returns:
- **str** : section and sub section content



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### get_create_section



``` python
get_create_section(title, comment=None, **parameters)
```

Get an existing section or create a new one

> [!NOTE]
> Contrary to ['#get_section' not found](), this method searchs the section only
> in the direct children, not in all the hierarchy.


#### Arguments:
- **title** (_str_) : section title
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : chapter section



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### get_toc



``` python
get_toc(flat=None, sort=None, max_length=10, max_depth=2)
```

Build the list of toc items

The methods return a list of paris giving:
- the level of the item
- the MD links


#### Arguments:
- **flat** (_bool_ = None) : toc is a flat list or hierarchical
- **sort** (_bool_ = None) : sort the list (force **flat** if True)
- **max_length** (_int_ = 10) : use alphabetical list if the number of items in the toc is greater thant this value
- **max_depth** (_int_ = 2) : max relative depth for a hierarchical toc



#### Returns:
- **list** : one entry per line



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### get_toc_sections



``` python
get_toc_sections(flat=None)
```

Return the dictionary of sections being part of the toc

If **flat** is True, the search for sub sections in the toc continues
within sections in the toc.

If **flat** is False, the exploration stops as soon as a section is
in the toc.


#### Arguments:
- **flat** (_bool_ = None) : returns the sections without hierarchy, use default if None



#### Returns:
- **list** : sections in the table of content of the page



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### insert_toc



``` python
insert_toc()
```

Insert the toc section


#### Returns:
- **Section** : None if no toc



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### items



``` python
items()
```

Iterate on (key, value) pais


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### keys



``` python
keys()
```

Iterate on keys


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### link_to



``` python
link_to(target=None, /, title=None)
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


#### Arguments:
- **target** (_str_ = None) : target of the link, self if None
- **title** (_str_ = None) : link title, use self.[title](#title) if None



#### Returns:
- **str** : link in md format `[title](file.md#anchor)`



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### new



``` python
new(title, comment=None, **parameters)
```

Add a section


#### Arguments:
- **title** (_str_) : section title
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : created section



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### new_chapter



``` python
new_chapter(chapter, comment=None, **parameters)
```

Add a chapter section


#### Arguments:
- **chapter** (_str_) : name of the chapter to create
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : chapter section



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### new_page



``` python
new_page(title, comment=None, **parameters)
```

Add a page section


#### Arguments:
- **title** (_str_) : section title
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : page section



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### new_sections_group



``` python
new_sections_group(title, sections, **parameters)
```

Create a section from a list of sections

The section is created only if the list has items.

The sections are move to the newly created section using [move_to_parent](tree-tree.md#move_to_parent).


#### Arguments:
- **title** (_str_) : title of the section to create
- **sections** (_list of Sections_) : the section to move into the created section
- **parameters** : parameters for the section to create



#### Returns:
- **Section** : the created section



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### new_tag_group



``` python
new_tag_group(tag, **parameters)
```

Create a section grouping all the sub sections having a given tag

The section is created only if sections have the tag

The group is created by calling [new_sections_group](#new_sections_group).


#### Arguments:
- **tag** (_str_) : tag to group sections
- **parameters** : parameters for the section to create



#### Returns:
- **Section** : the created section



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### remove_from_parent



``` python
remove_from_parent()
```

Remove the section from its parent list of children


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### values



``` python
values()
```

Iterate on childs


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### write



``` python
write(text)
```

Append text to the header comment


#### Arguments:
- **text** (_str_) : the text to write



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### write_header



``` python
write_header(level, title, text)
```

Write a section in the text stream

This method write markdonw text corresponding to a header followed by text.

> [!NOTE]
> This method doesn't create a section in the hierarchy, contrary to ['#add_section' not found]()


#### Arguments:
- **level** (_int_) : header level
- **title** (_str_) : header title
- **text** (_str_) : text



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### write_source



``` python
write_source(source)
```

Append source code to the header comment


#### Arguments:
- **source** (_str_) : source code to append



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>


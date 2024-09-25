# Section

``` python
Section(title, comment=None, tag=None, **parameters)
```

Document section

Project documentation is made of **pages** organized in **chapters**.

The documentation is based on the versatile class [Section](docum-section.md) which can be:
- a text section in a page
- a documentation page
- a chapter
- the whole documentation itself

A [Section](docum-section.md) is basically a list of **sub sections** with a header [comment](docum-section.md#comment).

#### Arguments:
- **title** (_str_) : section title
- **comment** (_str_ = None) : text to display just below the section title
- **tag** ( = None)
- **parameters** : initial values for properties

### Inherited

list.\_\_add__ :black_small_square: list.\_\_contains__ :black_small_square: list.\_\_delitem__ :black_small_square: list.\_\_eq__ :black_small_square: list.\_\_ge__ :black_small_square: list.\_\_getattribute__ :black_small_square: list.\_\_gt__ :black_small_square: list.\_\_iadd__ :black_small_square: list.\_\_imul__ :black_small_square: list.\_\_le__ :black_small_square: list.\_\_len__ :black_small_square: list.\_\_lt__ :black_small_square: list.\_\_mul__ :black_small_square: list.\_\_ne__ :black_small_square: list.\_\_repr__ :black_small_square: list.\_\_reversed__ :black_small_square: list.\_\_rmul__ :black_small_square: list.\_\_sizeof__ :black_small_square: list.append :black_small_square: list.clear :black_small_square: list.copy :black_small_square: list.extend :black_small_square: list.index :black_small_square: list.insert :black_small_square: list.pop :black_small_square: list.remove :black_small_square: list.reverse :black_small_square: list.sort :black_small_square:

## title

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

section title

## comment

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

text to display just below the section title

## sort_sections

<table><tbody>
<tr><td>type</td><td><b>bool or str</b></td></tr>
<tr><td>default</td><td><b>False</b</td></tr>
</tbody></table>

sort sections in alphabetical order when added (case sensitive if 'CASE')

## hidden

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

hide this section

## ignore_if_empty

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

don't display the section if it has no content

## top_bar

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>None or '-'</b</td></tr>
</tbody></table>

char to use to display an horizontal bar before the section

## depth_shift

<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
<tr><td>default</td><td><b>0</b</td></tr>
</tbody></table>

value to add to its depth for its header level in the final documentation, see [header_depth](docum-section.md#header_depth)

## is_chapter

<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>

the section is a chapter

## is_page

<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>

the section is a page

## is_text

<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>

the section is text (neither a page nor a chapter)

## is_hidden

<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>

the section, and its sub sections, are ignored

## is_transparent

<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>

the section is not displayed by itself, its content are attached to its parent

## transparent

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
<tr><td>default</td><td><b>False</b</td></tr>
</tbody></table>

force [is_transparent](docum-section.md#is_transparent)

## in_toc

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

put this section in its page table of content

## has_toc

<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>

(for page only) the page must display a table of content section

## has_content

<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>

the section has a not empty comment or has sections with content

## toc

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
<tr><td>default</td><td><b>False</b</td></tr>
</tbody></table>

insert a toc

## toc_title

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>'Content'</b</td></tr>
</tbody></table>

name of the toc (if any)

## toc_flat

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
<tr><td>default</td><td><b>False</b</td></tr>
</tbody></table>

flat toc (if any)

## toc_sort

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
<tr><td>default</td><td><b>False</b</td></tr>
</tbody></table>

sorted toc (if any)

## toc_depth_shift

<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
<tr><td>default</td><td><b>0</b</td></tr>
</tbody></table>

toc section [depth_shift](docum-section.md#depth_shift) (if any)

## is_toc

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
<tr><td>default</td><td><b>False</b</td></tr>
</tbody></table>

this section is the toc, don't create a new one

## navigation

<table><tbody>
<tr><td>type</td><td><b>list</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>

bottom navigation bar content

## tags

<table><tbody>
<tr><td>type</td><td><b>set</b></td></tr>
<tr><td>default</td><td><b>empty set</b</td></tr>
</tbody></table>

a set of tags

## user_props

<table><tbody>
<tr><td>type</td><td><b>dict</b></td></tr>
<tr><td>default</td><td><b>{}</b</td></tr>
</tbody></table>

properties defined by user with $ DOC syntax

## \_linked

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
<tr><td>default</td><td><b>False</b</td></tr>
</tbody></table>

the section is targeted by at least one link

## FromFile

``` python
FromFile(folder, pattern='*.*', ignore=('.*', '_*'))
```

Read the content of a drive

This methods shows how to use method [add](docum-section.md#add) to recursively load folder files and sub folders.

#### Arguments:
- **folder** (_str_) : folder to load
- **pattern** (_str or tuple of strs_ = *.*) : file selection
- **ignore** (_str or tuple of strs_ = ('.*', '_*')) : files starting by one of the characters in the string are ignored



#### Returns:
- **Tree** :

## FromInspect

``` python
FromInspect(obj)
```

Load python module

Load module and module members using inspect

#### Arguments:
- **obj** (_any_) : object to inspect



#### Returns:
- **Tree** :

## add

``` python
add(path, node, complete_path=False)
```

Add a new node at the path

This method calls [set_child](docum-section.md#set_child).

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

Total number of children

## all_items

``` python
all_items(include_self=False)
```

All items iterator

Iterate on all items in the folder and sub folders.

#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** :

## all_paths

``` python
all_paths(include_self=False)
```

All paths iterator

Iterate on all paths in the folder and sub folders.

#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** :

## all_values

``` python
all_values(include_self=False)
```

All values iterator

Iterate on all values in the folder and sub folders.

#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** :

## anchor

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

The anchor of this section within the page

## chapter

<table><tbody>
<tr><td>type</td><td><b>Section</b></td></tr>
</tbody></table>

Get the chapter this section belongs to

> [!CAUTION]
> Since a chapter returns self, a misuse could lead to infinite recurrence loop

## chapter_prefix

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

Get the prefix to use in the file names of pages in this chapter

To avoid to long names, prefix uses the 5 first chars plus a number
if collision

## cook

``` python
cook()
```

Cook the section and child sections

Default behavior is:
- sort the sections if ['#sort_section' not found]() is set
- cook the child sections
- insert the toc

Hidden sections are not cooked!

## count

<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>

Number of direct children, equivalent to `len(self)`

## create_path

``` python
create_path(*keys)
```

Create nodes in a path

Nodes are create by calling [new](docum-section.md#new) method.

#### Arguments:
- **keys** (_list of strs_) : key forming the path to create



#### Returns:
- **Tree** : last created node

## depth

<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>

Distance to the top (0 for top section)

## detach

``` python
detach()
```

Detach the section from its parent children

> [!IMPORANT]
> This method calls the abstract method [remove_from_parent](docum-section.md#remove_from_parent) which must perform
> the actual removal from the parent's list of children.

#### Returns:
- **Tree** : self

## file_name

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

File name were to write the page

The file name is built by joining [chapter_prefix](docum-section.md#chapter_prefix) with the name of section.

> [!NOTE]
> top chapter returns "index.md"

## find

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

## get

``` python
get(path, default=None)
```

Get the node at path

#### Arguments:
- **path** (_str_) : the node path
- **default** (_Tree_ = None) : the node to return if the path is not solved



#### Returns:
- **Tree** :

## get_child

``` python
get_child(key)
```

Get a direct child by its key

#### Arguments:
- **key**

## get_content

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

## get_create_section

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

## get_toc

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

## get_toc_sections

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

## header_depth

<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>

Header depth relatively to the page

The header depth doesn't include transparent parents. It aloso take
the [depth_shift](docum-section.md#depth_shift) into account

## homonyms_count

<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>

Count the number of sections have the same title

This number is used to suffix the title anchor if needed.

> [!NOTE]
> The number of homonymes is count up the the section iself, not after

## insert_toc

``` python
insert_toc()
```

Insert the toc section

#### Returns:
- **Section** : None if no toc

## is_displayed

<table><tbody>
<tr><td>type</td><td><b>True</b></td></tr>
</tbody></table>

Does the section appear in the doc

Returns False if the section if [is_hidden](docum-section.md#is_hidden).

Otherwise, it returns False if it is empty and [ignore_if_empty](docum-section.md#ignore_if_empty) is set.

## is_top

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

True if owner is None

## items

``` python
items()
```

Iterate on (key, value) pais

## join_keys

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

## keys

``` python
keys()
```

Iterate on keys

## link_to

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
- **title** (_str_ = None) : link title, use self.<#title> if None



#### Returns:
- **str** : link in md format `[title](file.md#anchor)`

## move_to_parent

``` python
move_to_parent(new_parent, new_key=None)
```

Change the position of a node from one parent to another

This methods basically calls [detach](docum-section.md#detach) and then [add](docum-section.md#add).


Returns
- Tree : self

#### Arguments:
- **new_parent** (_Tree_) : where to locate the node
- **new_key** (_str_ = None) : new key, uses the current key is None

## navigation_md

<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>

Get navigation markdown

Navigation bar is built with [navigation](docum-section.md#navigation) list

## new

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

## new_chapter

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

## new_page

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

## new_paths

``` python
new_paths(*paths, complete_path=False, **kwargs)
```

Create several nodes defined by their path

Basically, this method call [new](docum-section.md#new) for each provided path.

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

## new_sections_group

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

## new_tag_group

``` python
new_tag_group(tag, **parameters)
```

Create a section grouping all the sub sections having a given tag

The section is created only if sections have the tag

The group is created by calling [new_sections_group](docum-section.md#new_sections_group).

#### Arguments:
- **tag** (_str_) : tag to group sections
- **parameters** : parameters for the section to create



#### Returns:
- **Section** : the created section

## page

<table><tbody>
<tr><td>type</td><td><b>Section</b></td></tr>
</tbody></table>

Get the page this section belongs to

> [!CAUTION]
> Since a page returns self, a misuse could lead to infinite recurrence loop

## path

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

Node path up to the top node

## remove_from_parent

``` python
remove_from_parent()
```

Remove the section from its parent list of children

## set_child

``` python
set_child(key, child, index=None)
```

set a direct child by its key

#### Arguments:
- **key**
- **child**
- **index** ( = None)

## solve_path

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
> Missing nodes in the path are created with method [create_path](docum-section.md#create_path)

#### Raises:
- **PathError** : if the path can't be solved up to the last, or last but one



#### Arguments:
- **path** (_str_) : the path to solve
- **complete_path** (_bool_ = False) : create missing nodes (but the last one) if necessary



#### Returns:
- **Tree** : (found node, None) or (parent node, missing key)

## solve_to_missing

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

## top

<table><tbody>
<tr><td>type</td><td><b>Section</b></td></tr>
</tbody></table>

Get the topmost section

## user_prop

``` python
user_prop(name, default=None)
```

Get a user defined property

User can can define property with $ DOC SET property syntax
within source comment

#### Arguments:
- **name** (_str_) : property name
- **default** (_any_ = None) : default if not defined



#### Returns:
- **any** :

## values

``` python
values()
```

Iterate on childs

## write

``` python
write(text)
```

Append text to the header comment

#### Arguments:
- **text** (_str_) : the text to write

## write_header

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

## write_source

``` python
write_source(source)
```

Append source code to the header comment

#### Arguments:
- **source** (_str_) : source code to append
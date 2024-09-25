# ObjectSection

``` python
ObjectSection(name, comment=None, tag=None, **parameters)
```

Root class for informations on python objects

The minimum information is [name](pydoc-objectsection.md#name) and [comment](docum-section.md#comment) can be completed
by sub classes.

#### Arguments:
- **name** (_str_) : object name
- **comment** (_str_ = None) : comment
- **tag** (_str_ = None) : section tag
- **parameters** : parameter initial values

### Inherited

list.\_\_add__ :black_small_square: list.\_\_contains__ :black_small_square: list.\_\_delitem__ :black_small_square: list.\_\_eq__ :black_small_square: list.\_\_ge__ :black_small_square: list.\_\_getattribute__ :black_small_square: list.\_\_gt__ :black_small_square: list.\_\_iadd__ :black_small_square: list.\_\_imul__ :black_small_square: list.\_\_le__ :black_small_square: list.\_\_len__ :black_small_square: list.\_\_lt__ :black_small_square: list.\_\_mul__ :black_small_square: list.\_\_ne__ :black_small_square: list.\_\_repr__ :black_small_square: list.\_\_reversed__ :black_small_square: list.\_\_rmul__ :black_small_square: list.\_\_sizeof__ :black_small_square: list.append :black_small_square: list.clear :black_small_square: list.copy :black_small_square: list.extend :black_small_square: list.index :black_small_square: list.insert :black_small_square: list.pop :black_small_square: list.remove :black_small_square: list.reverse :black_small_square: list.sort :black_small_square:

## Content

- [all_count](pydoc-objectsection.md#all_count)
- [anchor](pydoc-objectsection.md#anchor)
- [chapter](pydoc-objectsection.md#chapter)
- [chapter_prefix](pydoc-objectsection.md#chapter_prefix)
- [count](pydoc-objectsection.md#count)
- [depth](pydoc-objectsection.md#depth)
- [file_name](pydoc-objectsection.md#file_name)
- [header_depth](pydoc-objectsection.md#header_depth)
- [homonyms_count](pydoc-objectsection.md#homonyms_count)
- [is_displayed](pydoc-objectsection.md#is_displayed)
- [is_top](pydoc-objectsection.md#is_top)
- [name](pydoc-objectsection.md#name)
- [navigation_md](pydoc-objectsection.md#navigation_md)
- [page](pydoc-objectsection.md#page)
- [path](pydoc-objectsection.md#path)
- [top](pydoc-objectsection.md#top)
- [add](pydoc-objectsection.md#add)
- [all_items](pydoc-objectsection.md#all_items)
- [all_paths](pydoc-objectsection.md#all_paths)
- [all_values](pydoc-objectsection.md#all_values)
- [cook](pydoc-objectsection.md#cook)
- [create_path](pydoc-objectsection.md#create_path)
- [detach](pydoc-objectsection.md#detach)
- [find](pydoc-objectsection.md#find)
- [FromFile](pydoc-objectsection.md#fromfile)
- [FromInspect](pydoc-objectsection.md#frominspect)
- [get](pydoc-objectsection.md#get)
- [get_child](pydoc-objectsection.md#get_child)
- [get_content](pydoc-objectsection.md#get_content)
- [get_create_section](pydoc-objectsection.md#get_create_section)
- [get_toc](pydoc-objectsection.md#get_toc)
- [get_toc_sections](pydoc-objectsection.md#get_toc_sections)
- [insert_toc](pydoc-objectsection.md#insert_toc)
- [items](pydoc-objectsection.md#items)
- [join_keys](pydoc-objectsection.md#join_keys)
- [keys](pydoc-objectsection.md#keys)
- [link_to](pydoc-objectsection.md#link_to)
- [move_to_parent](pydoc-objectsection.md#move_to_parent)
- [new](pydoc-objectsection.md#new)
- [new_chapter](pydoc-objectsection.md#new_chapter)
- [new_page](pydoc-objectsection.md#new_page)
- [new_paths](pydoc-objectsection.md#new_paths)
- [new_sections_group](pydoc-objectsection.md#new_sections_group)
- [new_tag_group](pydoc-objectsection.md#new_tag_group)
- [remove_from_parent](pydoc-objectsection.md#remove_from_parent)
- [set_child](pydoc-objectsection.md#set_child)
- [solve_path](pydoc-objectsection.md#solve_path)
- [solve_to_missing](pydoc-objectsection.md#solve_to_missing)
- [user_prop](pydoc-objectsection.md#user_prop)
- [values](pydoc-objectsection.md#values)
- [write](pydoc-objectsection.md#write)
- [write_header](pydoc-objectsection.md#write_header)
- [write_source](pydoc-objectsection.md#write_source)

## Properties



### all_count

> _type_: **int**
>

Total number of children

### anchor

> _type_: **str**
>

The anchor of this section within the page

### chapter

> _type_: **Section**
>

Get the chapter this section belongs to

> [!CAUTION]
> Since a chapter returns self, a misuse could lead to infinite recurrence loop

### chapter_prefix

> _type_: **str**
>

Get the prefix to use in the file names of pages in this chapter

To avoid to long names, prefix uses the 5 first chars plus a number
if collision

### count

> _type_: **int**
>

Number of direct children, equivalent to `len(self)`

### depth

> _type_: **int**
>

Distance to the top (0 for top section)

### file_name

> _type_: **str**
>

File name were to write the page

The file name is built by joining [chapter_prefix](pydoc-objectsection.md#chapter_prefix) with the name of section.

> [!NOTE]
> top chapter returns "index.md"

### header_depth

> _type_: **int**
>

Header depth relatively to the page

The header depth doesn't include transparent parents. It aloso take
the [depth_shift](docum-section.md#depth_shift) into account

### homonyms_count

> _type_: **int**
>

Count the number of sections have the same title

This number is used to suffix the title anchor if needed.

> [!NOTE]
> The number of homonymes is count up the the section iself, not after

### is_displayed

> _type_: **True**
>

Does the section appear in the doc

Returns False if the section if [is_hidden](pydoc-objectsection.md#is_hidden).

Otherwise, it returns False if it is empty and [ignore_if_empty](docum-section.md#ignore_if_empty) is set.

### is_hidden

> _type_: **?**
>

### is_top

> _type_: **bool**
>

True if owner is None

### name

> _type_: **str**
>

module name, class name, property name...

### navigation_md

> _type_: **?**
>

Get navigation markdown

Navigation bar is built with [navigation](docum-section.md#navigation) list

### page

> _type_: **Section**
>

Get the page this section belongs to

> [!CAUTION]
> Since a page returns self, a misuse could lead to infinite recurrence loop

### path

> _type_: **str**
>

Node path up to the top node

### top

> _type_: **Section**
>

Get the topmost section

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [ObjectSection](pydoc-objectsection.md)</sub>

## Methods



----------
### add

> method

``` python
add(path, node, complete_path=False)
```

Add a new node at the path

This method calls [set_child](pydoc-objectsection.md#set_child).

#### Arguments:
- **path** (_str_) : the path where to locate the node
- **node** (_Tree_) : the node to set at the path
- **complete_path** ( = False)



#### Returns:
- **Tree** : the node argument

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### all_items

> method

``` python
all_items(include_self=False)
```

All items iterator

Iterate on all items in the folder and sub folders.

#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### all_paths

> method

``` python
all_paths(include_self=False)
```

All paths iterator

Iterate on all paths in the folder and sub folders.

#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### all_values

> method

``` python
all_values(include_self=False)
```

All values iterator

Iterate on all values in the folder and sub folders.

#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### cook

> method

``` python
cook()
```

Cook the section and child sections

Default behavior is:
- sort the sections if ['#sort_section' not found]() is set
- cook the child sections
- insert the toc

Hidden sections are not cooked!

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### create_path

> method

``` python
create_path(*keys)
```

Create nodes in a path

Nodes are create by calling [new](pydoc-objectsection.md#new) method.

#### Arguments:
- **keys** (_list of strs_) : key forming the path to create



#### Returns:
- **Tree** : last created node

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### detach

> method

``` python
detach()
```

Detach the section from its parent children

> [!IMPORANT]
> This method calls the abstract method [remove_from_parent](pydoc-objectsection.md#remove_from_parent) which must perform
> the actual removal from the parent's list of children.

#### Returns:
- **Tree** : self

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### find

> method

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### FromFile

> classmethod

``` python
FromFile(folder, pattern='*.*', ignore=('.*', '_*'))
```

Read the content of a drive

This methods shows how to use method [add](pydoc-objectsection.md#add) to recursively load folder files and sub folders.

#### Arguments:
- **folder** (_str_) : folder to load
- **pattern** (_str or tuple of strs_ = *.*) : file selection
- **ignore** (_str or tuple of strs_ = ('.*', '_*')) : files starting by one of the characters in the string are ignored



#### Returns:
- **Tree** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### FromInspect

> classmethod

``` python
FromInspect(obj)
```

Load python module

Load module and module members using inspect

#### Arguments:
- **obj** (_any_) : object to inspect



#### Returns:
- **Tree** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### get

> method

``` python
get(path, default=None)
```

Get the node at path

#### Arguments:
- **path** (_str_) : the node path
- **default** (_Tree_ = None) : the node to return if the path is not solved



#### Returns:
- **Tree** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### get_child

> method

``` python
get_child(key)
```

Get a direct child by its key

#### Arguments:
- **key**

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### get_content

> method

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### get_create_section

> method

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### get_toc

> method

``` python
get_toc(flat=None, sort=None, max_length=None, max_depth=2)
```

Build the list of toc items

The methods return a list of paris giving:
- the level of the item
- the MD links

#### Arguments:
- **flat** (_bool_ = None) : toc is a flat list or hierarchical
- **sort** (_bool_ = None) : sort the list (force **flat** if True)
- **max_length** (_int_ = None) : use alphabetical list if the number of items in the toc is greater thant this value
- **max_depth** (_int_ = 2) : max relative depth for a hierarchical toc



#### Returns:
- **list** : one entry per line

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### get_toc_sections

> method

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### insert_toc

> method

``` python
insert_toc()
```

Insert the toc section

#### Returns:
- **Section** : None if no toc

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### items

> method

``` python
items()
```

Iterate on (key, value) pais

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### join_keys

> method

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### keys

> method

``` python
keys()
```

Iterate on keys

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### link_to

> method

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### move_to_parent

> method

``` python
move_to_parent(new_parent, new_key=None)
```

Change the position of a node from one parent to another

This methods basically calls [detach](pydoc-objectsection.md#detach) and then [add](pydoc-objectsection.md#add).


Returns
- Tree : self

#### Arguments:
- **new_parent** (_Tree_) : where to locate the node
- **new_key** (_str_ = None) : new key, uses the current key is None

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### new

> method

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### new_chapter

> method

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### new_page

> method

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### new_paths

> method

``` python
new_paths(*paths, complete_path=False, **kwargs)
```

Create several nodes defined by their path

Basically, this method call [new](pydoc-objectsection.md#new) for each provided path.

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### new_sections_group

> method

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### new_tag_group

> method

``` python
new_tag_group(tag, **parameters)
```

Create a section grouping all the sub sections having a given tag

The section is created only if sections have the tag

The group is created by calling [new_sections_group](pydoc-objectsection.md#new_sections_group).

#### Arguments:
- **tag** (_str_) : tag to group sections
- **parameters** : parameters for the section to create



#### Returns:
- **Section** : the created section

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### remove_from_parent

> method

``` python
remove_from_parent()
```

Remove the section from its parent list of children

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### set_child

> method

``` python
set_child(key, child, index=None)
```

set a direct child by its key

#### Arguments:
- **key**
- **child**
- **index** ( = None)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### solve_path

> method

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
> Missing nodes in the path are created with method [create_path](pydoc-objectsection.md#create_path)

#### Raises:
- **PathError** : if the path can't be solved up to the last, or last but one



#### Arguments:
- **path** (_str_) : the path to solve
- **complete_path** (_bool_ = False) : create missing nodes (but the last one) if necessary



#### Returns:
- **Tree** : (found node, None) or (parent node, missing key)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### solve_to_missing

> method

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### user_prop

> method

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### values

> method

``` python
values()
```

Iterate on childs

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### write

> method

``` python
write(text)
```

Append text to the header comment

#### Arguments:
- **text** (_str_) : the text to write

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### write_header

> method

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

----------
### write_source

> method

``` python
write_source(source)
```

Append source code to the header comment

#### Arguments:
- **source** (_str_) : source code to append

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-objectsection.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objectsection) :black_small_square: [Content](#content) :black_small_square: [ObjectSection](pydoc-objectsection.md)</sub>
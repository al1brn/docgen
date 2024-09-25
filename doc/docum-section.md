# Section

> Bases classes: [TreeList](tree-treelist.md)

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

[\_\_getitem__](tree-tree.md#__getitem__) :black_small_square: [\_\_iter__](tree-tree.md#__iter__) :black_small_square: [\_\_setitem__](tree-tree.md#__setitem__) :black_small_square: [add](tree-tree.md#add) :black_small_square: [all_items](tree-tree.md#all_items) :black_small_square: [all_paths](tree-tree.md#all_paths) :black_small_square: [all_values](tree-tree.md#all_values) :black_small_square: [create_path](tree-tree.md#create_path) :black_small_square: [detach](tree-tree.md#detach) :black_small_square: [dump](tree-tree.md#dump) :black_small_square: [find](tree-tree.md#find) :black_small_square: [FromFile](tree-tree.md#fromfile) :black_small_square: [FromInspect](tree-tree.md#frominspect) :black_small_square: [get](tree-tree.md#get) :black_small_square: [get_child](tree-treelist.md#get_child) :black_small_square: [items](tree-treelist.md#items) :black_small_square: [join_keys](tree-tree.md#join_keys) :black_small_square: [keys](tree-treelist.md#keys) :black_small_square: [move_to_parent](tree-tree.md#move_to_parent) :black_small_square: [new_paths](tree-tree.md#new_paths) :black_small_square: [remove_from_parent](tree-treelist.md#remove_from_parent) :black_small_square: [set_child](tree-treelist.md#set_child) :black_small_square: [solve_path](tree-tree.md#solve_path) :black_small_square: [solve_to_missing](tree-tree.md#solve_to_missing) :black_small_square: [test](parse---parser.md#test) :black_small_square: [test_numpy](tree-tree.md#test_numpy) :black_small_square: [values](tree-treelist.md#values) :black_small_square:

## Content

- **A** : [all_count](docum-section.md#all_count) :black_small_square: [anchor](docum-section.md#anchor)
- **C** : [chapter](docum-section.md#chapter) :black_small_square: [chapter_prefix](docum-section.md#chapter_prefix) :black_small_square: [comment](docum-section.md#comment) :black_small_square: [cook](docum-section.md#cook) :black_small_square: [count](docum-section.md#count)
- **D** : [depth](docum-section.md#depth) :black_small_square: [depth_shift](docum-section.md#depth_shift)
- **F** : [file_name](docum-section.md#file_name)
- **G** : [get_content](docum-section.md#get_content) :black_small_square: [get_create_section](docum-section.md#get_create_section) :black_small_square: [get_toc](docum-section.md#get_toc) :black_small_square: [get_toc_sections](docum-section.md#get_toc_sections)
- **H** : [has_content](docum-section.md#has_content) :black_small_square: [has_toc](docum-section.md#has_toc) :black_small_square: [header_depth](docum-section.md#header_depth) :black_small_square: [hidden](docum-section.md#hidden) :black_small_square: [homonyms_count](docum-section.md#homonyms_count)
- **I** : [ignore_if_empty](docum-section.md#ignore_if_empty) :black_small_square: [insert_toc](docum-section.md#insert_toc) :black_small_square: [in_toc](docum-section.md#in_toc) :black_small_square: [is_chapter](docum-section.md#is_chapter) :black_small_square: [is_displayed](docum-section.md#is_displayed) :black_small_square: [is_hidden](docum-section.md#is_hidden) :black_small_square: [is_page](docum-section.md#is_page) :black_small_square: [is_text](docum-section.md#is_text) :black_small_square: [is_toc](docum-section.md#is_toc) :black_small_square: [is_top](docum-section.md#is_top) :black_small_square: [is_transparent](docum-section.md#is_transparent)
- **L** : [\_linked](docum-section.md#_linked) :black_small_square: [link_to](docum-section.md#link_to)
- **N** : [navigation](docum-section.md#navigation) :black_small_square: [navigation_md](docum-section.md#navigation_md) :black_small_square: [new](docum-section.md#new) :black_small_square: [new_chapter](docum-section.md#new_chapter) :black_small_square: [new_page](docum-section.md#new_page) :black_small_square: [new_sections_group](docum-section.md#new_sections_group) :black_small_square: [new_tag_group](docum-section.md#new_tag_group)
- **P** : [page](docum-section.md#page) :black_small_square: [path](docum-section.md#path)
- **S** : [sort_sections](docum-section.md#sort_sections)
- **T** : [tags](docum-section.md#tags) :black_small_square: [title](docum-section.md#title) :black_small_square: [toc](docum-section.md#toc) :black_small_square: [toc_depth_shift](docum-section.md#toc_depth_shift) :black_small_square: [toc_flat](docum-section.md#toc_flat) :black_small_square: [toc_max_depth](docum-section.md#toc_max_depth) :black_small_square: [toc_max_length](docum-section.md#toc_max_length) :black_small_square: [toc_sort](docum-section.md#toc_sort) :black_small_square: [toc_title](docum-section.md#toc_title) :black_small_square: [top](docum-section.md#top) :black_small_square: [top_bar](docum-section.md#top_bar) :black_small_square: [transparent](docum-section.md#transparent)
- **U** : [user_prop](docum-section.md#user_prop) :black_small_square: [user_props](docum-section.md#user_props)
- **W** : [write](docum-section.md#write) :black_small_square: [write_header](docum-section.md#write_header) :black_small_square: [write_source](docum-section.md#write_source)

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

### comment

> _type_: **str**
>

text to display just below the section title

### count

> _type_: **int**
>

Number of direct children, equivalent to `len(self)`

### depth

> _type_: **int**
>

Distance to the top (0 for top section)

### depth_shift

> _type_: **int**<br> _default_: **0**
>

value to add to its depth for its header level in the final documentation, see [header_depth](docum-section.md#header_depth)

### file_name

> _type_: **str**
>

File name were to write the page

The file name is built by joining [chapter_prefix](docum-section.md#chapter_prefix) with the name of section.

> [!NOTE]
> top chapter returns "index.md"

### has_content

> _type_: **?**
>

the section has a not empty comment or has sections with content

### has_toc

> _type_: **?**
>

(for page only) the page must display a table of content section

### header_depth

> _type_: **int**
>

Header depth relatively to the page

The header depth doesn't include transparent parents. It aloso take
the [depth_shift](docum-section.md#depth_shift) into account

### hidden

> _type_: **bool**
>

hide this section

### homonyms_count

> _type_: **int**
>

Count the number of sections have the same title

This number is used to suffix the title anchor if needed.

> [!NOTE]
> The number of homonymes is count up the the section iself, not after

### ignore_if_empty

> _type_: **bool**
>

don't display the section if it has no content

### in_toc

> _type_: **bool**
>

put this section in its page table of content

### is_chapter

> _type_: **?**
>

the section is a chapter

### is_displayed

> _type_: **True**
>

Does the section appear in the doc

Returns False if the section if [is_hidden](docum-section.md#is_hidden).

Otherwise, it returns False if it is empty and [ignore_if_empty](docum-section.md#ignore_if_empty) is set.

### is_hidden

> _type_: **?**
>

the section, and its sub sections, are ignored

### is_page

> _type_: **?**
>

the section is a page

### is_text

> _type_: **?**
>

the section is text (neither a page nor a chapter)

### is_toc

> _type_: **bool**<br> _default_: **False**
>

this section is the toc, don't create a new one

### is_top

> _type_: **bool**
>

True if owner is None

### is_transparent

> _type_: **?**
>

the section is not displayed by itself, its content are attached to its parent

### \_linked

> _type_: **bool**<br> _default_: **False**
>

the section is targeted by at least one link

### navigation

> _type_: **list**<br> _default_: **None**
>

bottom navigation bar content

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

### sort_sections

> _type_: **bool or str**<br> _default_: **False**
>

sort sections in alphabetical order when added (case sensitive if 'CASE')

### tags

> _type_: **set**<br> _default_: **empty set**
>

a set of tags

### title

> _type_: **str**
>

section title

### toc

> _type_: **bool**<br> _default_: **False**
>

insert a toc

### toc_depth_shift

> _type_: **int**<br> _default_: **0**
>

toc section [depth_shift](docum-section.md#depth_shift) (if any)

### toc_flat

> _type_: **bool**<br> _default_: **False**
>

flat toc (if any)

### toc_max_depth

> _type_: **int**<br> _default_: **2**
>

tox max depth

### toc_max_length

> _type_: **int**<br> _default_: **10**
>

maximum number of entries in a flat toc before indexing by initial

### toc_sort

> _type_: **bool**<br> _default_: **False**
>

sorted toc (if any)

### toc_title

> _type_: **str**<br> _default_: **'Content'**
>

name of the toc (if any)

### top

> _type_: **Section**
>

Get the topmost section

### top_bar

> _type_: **str**<br> _default_: **None or '-'**
>

char to use to display an horizontal bar before the section

### transparent

> _type_: **bool**<br> _default_: **False**
>

force [is_transparent](docum-section.md#is_transparent)

### user_props

> _type_: **dict**<br> _default_: **{}**
>

properties defined by user with $ DOC syntax

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Section](docum-section.md)</sub>

## Methods



----------
### cook()

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](docum-section.md#methods)</sub>

----------
### get_content()

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](docum-section.md#methods)</sub>

----------
### get_create_section()

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](docum-section.md#methods)</sub>

----------
### get_toc()

> method

``` python
get_toc(flat=None, sort=None, max_length=None, max_depth=None)
```

Build the list of toc items

The methods return a list of paris giving:
- the level of the item
- the MD links

#### Arguments:
- **flat** (_bool_ = None) : toc is a flat list or hierarchical
- **sort** (_bool_ = None) : sort the list (force **flat** if True)
- **max_length** (_int_ = None) : use alphabetical list if the number of items in the toc is greater thant this value
- **max_depth** (_int_ = None) : max relative depth for a hierarchical toc



#### Returns:
- **list** : one entry per line

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](docum-section.md#methods)</sub>

----------
### get_toc_sections()

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](docum-section.md#methods)</sub>

----------
### insert_toc()

> method

``` python
insert_toc()
```

Insert the toc section

#### Returns:
- **Section** : None if no toc

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](docum-section.md#methods)</sub>

----------
### link_to()

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](docum-section.md#methods)</sub>

----------
### new()

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](docum-section.md#methods)</sub>

----------
### new_chapter()

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](docum-section.md#methods)</sub>

----------
### new_page()

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](docum-section.md#methods)</sub>

----------
### new_sections_group()

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](docum-section.md#methods)</sub>

----------
### new_tag_group()

> method

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](docum-section.md#methods)</sub>

----------
### user_prop()

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](docum-section.md#methods)</sub>

----------
### write()

> method

``` python
write(text)
```

Append text to the header comment

#### Arguments:
- **text** (_str_) : the text to write

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](docum-section.md#methods)</sub>

----------
### write_header()

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](docum-section.md#methods)</sub>

----------
### write_source()

> method

``` python
write_source(source)
```

Append source code to the header comment

#### Arguments:
- **source** (_str_) : source code to append

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](docum-section.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Section](docum-section.md)</sub>
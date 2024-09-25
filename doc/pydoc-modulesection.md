# ModuleSection

``` python
ModuleSection(name, comment=None, tag=None, **parameters)
```

Modulesection

#### Arguments:
- **name** (_str_) : object name
- **comment** (_str_ = None) : comment
- **tag** (_str_ = None) : section tag
- **parameters** : parameter initial values

### Inherited

[FromFile](tree-tree.md#fromfile) :black_small_square: [ModuleTest](docum-section.md#moduletest) :black_small_square: [Test](docum-section.md#test) :black_small_square: [\_\_getitem__](tree-tree.md#__getitem__) :black_small_square: [\_\_iter__](tree-tree.md#__iter__) :black_small_square: [\_\_setitem__](tree-tree.md#__setitem__) :black_small_square: [\_\_str__](pydoc-objectsection.md#__str__) :black_small_square: [\_title_sort](docum-section.md#_title_sort) :black_small_square: [add](tree-tree.md#add) :black_small_square: [after_comment](docum-section.md#after_comment) :black_small_square: [all_items](tree-tree.md#all_items) :black_small_square: [all_paths](tree-tree.md#all_paths) :black_small_square: [all_values](tree-tree.md#all_values) :black_small_square: [before_comment](docum-section.md#before_comment) :black_small_square: [cook](docum-section.md#cook) :black_small_square: [create_path](tree-tree.md#create_path) :black_small_square: [del_tag](docum-section.md#del_tag) :black_small_square: [detach](tree-tree.md#detach) :black_small_square: [dump](tree-tree.md#dump) :black_small_square: [dump_pages](docum-section.md#dump_pages) :black_small_square: [dump_title](docum-section.md#dump_title) :black_small_square: [dump_titles](docum-section.md#dump_titles) :black_small_square: [dump_toc](docum-section.md#dump_toc) :black_small_square: [find](tree-tree.md#find) :black_small_square: [get](tree-tree.md#get) :black_small_square: [get_child](tree-treelist.md#get_child) :black_small_square: [get_content](docum-section.md#get_content) :black_small_square: [get_create_section](docum-section.md#get_create_section) :black_small_square: [get_doc](pydoc-objectsection.md#get_doc) :black_small_square: [get_toc](docum-section.md#get_toc) :black_small_square: [get_toc_sections](docum-section.md#get_toc_sections) :black_small_square: [has_any_tag](docum-section.md#has_any_tag) :black_small_square: [has_tag](docum-section.md#has_tag) :black_small_square: [insert_toc](docum-section.md#insert_toc) :black_small_square: [items](tree-treelist.md#items) :black_small_square: [join_keys](tree-tree.md#join_keys) :black_small_square: [keys](tree-treelist.md#keys) :black_small_square: [link_to](docum-section.md#link_to) :black_small_square: [move_to_parent](tree-tree.md#move_to_parent) :black_small_square: [new](docum-section.md#new) :black_small_square: [new_chapter](docum-section.md#new_chapter) :black_small_square: [new_page](docum-section.md#new_page) :black_small_square: [new_paths](tree-tree.md#new_paths) :black_small_square: [new_sections_group](docum-section.md#new_sections_group) :black_small_square: [new_tag_group](docum-section.md#new_tag_group) :black_small_square: [parse_comment](docum-section.md#parse_comment) :black_small_square: [remove_from_parent](tree-treelist.md#remove_from_parent) :black_small_square: [set_child](tree-treelist.md#set_child) :black_small_square: [set_tag](docum-section.md#set_tag) :black_small_square: [solve_path](tree-tree.md#solve_path) :black_small_square: [solve_to_missing](tree-tree.md#solve_to_missing) :black_small_square: [test](parse---parser.md#test) :black_small_square: [test_numpy](tree-tree.md#test_numpy) :black_small_square: [user_prop](docum-section.md#user_prop) :black_small_square: [values](tree-treelist.md#values) :black_small_square: [write](docum-section.md#write) :black_small_square: [write_header](docum-section.md#write_header) :black_small_square: [write_source](docum-section.md#write_source) :black_small_square:

## Content

- **A** : [all_count](pydoc-modulesection.md#all_count) :black_small_square: [anchor](pydoc-modulesection.md#anchor)
- **C** : [chapter](pydoc-modulesection.md#chapter) :black_small_square: [chapter_prefix](pydoc-modulesection.md#chapter_prefix) :black_small_square: [count](pydoc-modulesection.md#count)
- **D** : [depth](pydoc-modulesection.md#depth)
- **F** : [file_name](pydoc-modulesection.md#file_name) :black_small_square: [FromInspect](pydoc-modulesection.md#frominspect)
- **H** : [header_depth](pydoc-modulesection.md#header_depth) :black_small_square: [homonyms_count](pydoc-modulesection.md#homonyms_count)
- **I** : [\_init](pydoc-modulesection.md#_init) :black_small_square: [is_displayed](pydoc-modulesection.md#is_displayed) :black_small_square: [is_top](pydoc-modulesection.md#is_top)
- **N** : [navigation_md](pydoc-modulesection.md#navigation_md)
- **P** : [package](pydoc-modulesection.md#package) :black_small_square: [page](pydoc-modulesection.md#page) :black_small_square: [path](pydoc-modulesection.md#path)
- **T** : [top](pydoc-modulesection.md#top)

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

The file name is built by joining [chapter_prefix](pydoc-modulesection.md#chapter_prefix) with the name of section.

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

### \_init

> _type_: **ModuleSection**
>

[ModuleSection](pydoc-modulesection.md) __init__ file if exists

### is_displayed

> _type_: **True**
>

Does the section appear in the doc

Returns False if the section if [is_hidden](pydoc-modulesection.md#is_hidden).

Otherwise, it returns False if it is empty and [ignore_if_empty](docum-section.md#ignore_if_empty) is set.

### is_hidden

> _type_: **?**
>

### is_top

> _type_: **bool**
>

True if owner is None

### navigation_md

> _type_: **?**
>

Get navigation markdown

Navigation bar is built with [navigation](docum-section.md#navigation) list

### package

> _type_: **str**
>

module package

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#modulesection) :black_small_square: [Content](#content) :black_small_square: [ModuleSection](pydoc-modulesection.md)</sub>

## Methods



----------
### FromInspect()

> classmethod

``` python
FromInspect(name, module_object)
```

Create a ModuleSection by inspecting a module object

#### Arguments:
- **name** (_str_) : module name
- **module_object** (_module_) : the module to scan

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#modulesection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-modulesection.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#modulesection) :black_small_square: [Content](#content) :black_small_square: [ModuleSection](pydoc-modulesection.md)</sub>
# PropertySection

> Bases classes: [ObjectSection](pydoc-objectsection.md)

``` python
PropertySection(name, comment=None, tag=None, **parameters)
```

Information on property

A property can be defined:
- in a user list such as name (type = default) : description
- from a fget method

In case both exist, user list description is ignored if the
fget provides a comment.

#### Arguments:
- **name** (_str_) : object name
- **comment** (_str_ = None) : comment
- **tag** (_str_ = None) : section tag
- **parameters** : parameter initial values

### Inherited

[add](tree-tree.md#add) :black_small_square: [after_comment](docum-section.md#after_comment) :black_small_square: [all_count](tree-tree.md#all_count) :black_small_square: [all_items](tree-tree.md#all_items) :black_small_square: [all_paths](tree-tree.md#all_paths) :black_small_square: [all_values](tree-tree.md#all_values) :black_small_square: [anchor](docum-section.md#anchor) :black_small_square: [chapter](docum-section.md#chapter) :black_small_square: [chapter_prefix](docum-section.md#chapter_prefix) :black_small_square: [comment](docum-section.md#comment) :black_small_square: [cook](docum-section.md#cook) :black_small_square: [count](tree-tree.md#count) :black_small_square: [create_path](tree-tree.md#create_path) :black_small_square: [del_tag](docum-section.md#del_tag) :black_small_square: [depth](tree-tree.md#depth) :black_small_square: [depth_shift](docum-section.md#depth_shift) :black_small_square: [detach](tree-tree.md#detach) :black_small_square: [display_title](docum-section.md#display_title) :black_small_square: [dump](tree-tree.md#dump) :black_small_square: [dump_pages](docum-section.md#dump_pages) :black_small_square: [dump_title](docum-section.md#dump_title) :black_small_square: [dump_titles](docum-section.md#dump_titles) :black_small_square: [dump_toc](docum-section.md#dump_toc) :black_small_square: [file_name](docum-section.md#file_name) :black_small_square: [find](tree-tree.md#find) :black_small_square: [FromFile](tree-tree.md#fromfile) :black_small_square: [get](tree-tree.md#get) :black_small_square: [get_child](tree-treelist.md#get_child) :black_small_square: [get_content](docum-section.md#get_content) :black_small_square: [get_create_section](docum-section.md#get_create_section) :black_small_square: [get_doc](pydoc-objectsection.md#get_doc) :black_small_square: [get_function_class](pydoc-objectsection.md#get_function_class) :black_small_square: [\_\_getitem__](tree-tree.md#__getitem__) :black_small_square: [get_property_class](pydoc-objectsection.md#get_property_class) :black_small_square: [get_toc](docum-section.md#get_toc) :black_small_square: [get_toc_sections](docum-section.md#get_toc_sections) :black_small_square: [has_any_tag](docum-section.md#has_any_tag) :black_small_square: [has_content](docum-section.md#has_content) :black_small_square: [has_tag](docum-section.md#has_tag) :black_small_square: [has_toc](docum-section.md#has_toc) :black_small_square: [header_depth](docum-section.md#header_depth) :black_small_square: [hidden](docum-section.md#hidden) :black_small_square: [homonyms_count](docum-section.md#homonyms_count) :black_small_square: [ignore_if_empty](docum-section.md#ignore_if_empty) :black_small_square: [insert_toc](docum-section.md#insert_toc) :black_small_square: [in_toc](docum-section.md#in_toc) :black_small_square: [is_chapter](docum-section.md#is_chapter) :black_small_square: [is_displayed](docum-section.md#is_displayed) :black_small_square: [is_hidden](docum-section.md#is_hidden) :black_small_square: [is_page](docum-section.md#is_page) :black_small_square: [is_text](docum-section.md#is_text) :black_small_square: [is_toc](docum-section.md#is_toc) :black_small_square: [is_top](tree-tree.md#is_top) :black_small_square: [is_transparent](docum-section.md#is_transparent) :black_small_square: [items](tree-treelist.md#items) :black_small_square: [\_\_iter__](tree-tree.md#__iter__) :black_small_square: [join_keys](tree-tree.md#join_keys) :black_small_square: [key](tree-tree.md#key) :black_small_square: [keys](tree-treelist.md#keys) :black_small_square: [\_linked](docum-section.md#_linked) :black_small_square: [link_to](docum-section.md#link_to) :black_small_square: [ModuleTest](docum-section.md#moduletest) :black_small_square: [move_to_parent](tree-tree.md#move_to_parent) :black_small_square: [name](pydoc-objectsection.md#name) :black_small_square: [navigation](docum-section.md#navigation) :black_small_square: [navigation_md](docum-section.md#navigation_md) :black_small_square: [new](docum-section.md#new) :black_small_square: [new_chapter](docum-section.md#new_chapter) :black_small_square: [new_page](docum-section.md#new_page) :black_small_square: [new_paths](tree-tree.md#new_paths) :black_small_square: [new_sections_group](docum-section.md#new_sections_group) :black_small_square: [new_tag_group](docum-section.md#new_tag_group) :black_small_square: [page](docum-section.md#page) :black_small_square: [parent](tree-tree.md#parent) :black_small_square: [parse_comment](docum-section.md#parse_comment) :black_small_square: [path](tree-tree.md#path) :black_small_square: [regroup](pydoc-objectsection.md#regroup) :black_small_square: [remove_from_parent](tree-treelist.md#remove_from_parent) :black_small_square: [set_child](tree-treelist.md#set_child) :black_small_square: [\_\_setitem__](tree-tree.md#__setitem__) :black_small_square: [set_tag](docum-section.md#set_tag) :black_small_square: [solve_path](tree-tree.md#solve_path) :black_small_square: [solve_to_missing](tree-tree.md#solve_to_missing) :black_small_square: [sort_sections](docum-section.md#sort_sections) :black_small_square: [\_\_str__](pydoc-objectsection.md#__str__) :black_small_square: [tag](docum-section.md#tag) :black_small_square: [tags](docum-section.md#tags) :black_small_square: [Test](docum-section.md#test) :black_small_square: [test](parse---parser.md#test) :black_small_square: [test_numpy](tree-tree.md#test_numpy) :black_small_square: [title](docum-section.md#title) :black_small_square: [\_title_sort](docum-section.md#_title_sort) :black_small_square: [toc](docum-section.md#toc) :black_small_square: [toc_depth_shift](docum-section.md#toc_depth_shift) :black_small_square: [toc_flat](docum-section.md#toc_flat) :black_small_square: [toc_max_depth](docum-section.md#toc_max_depth) :black_small_square: [toc_max_length](docum-section.md#toc_max_length) :black_small_square: [toc_sort](docum-section.md#toc_sort) :black_small_square: [toc_title](docum-section.md#toc_title) :black_small_square: [top](tree-tree.md#top) :black_small_square: [top_bar](docum-section.md#top_bar) :black_small_square: [transparent](docum-section.md#transparent) :black_small_square: [user_prop](docum-section.md#user_prop) :black_small_square: [user_props](docum-section.md#user_props) :black_small_square: [values](tree-treelist.md#values) :black_small_square: [write](docum-section.md#write) :black_small_square: [write_header](docum-section.md#write_header) :black_small_square: [write_source](docum-section.md#write_source) :black_small_square:

## Content

- [complete_with](pydoc-propertysection.md#complete_with)
- [default](pydoc-propertysection.md#default)
- [fget](pydoc-propertysection.md#fget)
- [FromDict](pydoc-propertysection.md#fromdict)
- [FromInspect](pydoc-propertysection.md#frominspect)
- [FromListItem](pydoc-propertysection.md#fromlistitem)
- [FromStatic](pydoc-propertysection.md#fromstatic)
- [fset](pydoc-propertysection.md#fset)
- [type](pydoc-propertysection.md#type)

## Properties



### default

> _type_: **str**
>

default value

### fget

> _type_: **Function_**
>

getter [fget](pydoc-propertysection.md#fget)

### fset

> _type_: **Function_**
>

setter [fset](pydoc-propertysection.md#fset)

### type

> _type_: **str**
>

type of the property

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#propertysection) :black_small_square: [Content](#content) :black_small_square: [PropertySection](pydoc-propertysection.md)</sub>

## Methods



----------
### complete_with()

> method

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#propertysection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-propertysection.md#methods)</sub>

----------
### FromDict()

> classmethod

``` python
FromDict(item)
```

Create a property from a dict

#### Arguments:
- **item** (_dict_) : information on the property to create



#### Returns:
- **PropertySection** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#propertysection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-propertysection.md#methods)</sub>

----------
### FromInspect()

> classmethod

``` python
FromInspect(name, property_object)
```

Create a PropertySection by inspect a property

> [!NOTE]
> If name is None, the name is read from fget

#### Arguments:
- **name** (_str_) : name
- **property_object** (_property_) : the object the scan



#### Returns:
- **PropertySection** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#propertysection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-propertysection.md#methods)</sub>

----------
### FromListItem()

> classmethod

``` python
FromListItem(item)
```

Create a property from a list item

#### Arguments:
- **item** (_ListItem_) : information on the property to create



#### Returns:
- **PropertySection** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#propertysection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-propertysection.md#methods)</sub>

----------
### FromStatic()

> classmethod

``` python
FromStatic(name, property_object)
```

Creare a Property_ instance from a static property in a module or a class

#### Arguments:
- **name** (_str_ = None)
- **property_object** : 



#### Returns:
- **Property_** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#propertysection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-propertysection.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#propertysection) :black_small_square: [Content](#content) :black_small_square: [PropertySection](pydoc-propertysection.md)</sub>
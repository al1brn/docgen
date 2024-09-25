# get_function_class

> Bases classes: [get_function_class](get_f2-get_function_class.md)

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

[add](tree-tree.md#add) :black_small_square: ['#after_comment' not found]() :black_small_square: [all_count](tree-tree.md#all_count) :black_small_square: [all_items](tree-tree.md#all_items) :black_small_square: [all_paths](tree-tree.md#all_paths) :black_small_square: [all_values](tree-tree.md#all_values) :black_small_square: ['#anchor' not found]() :black_small_square: ['#chapter' not found]() :black_small_square: ['#chapter_prefix' not found]() :black_small_square: ['#comment' not found]() :black_small_square: ['#cook' not found]() :black_small_square: [count](tree-tree.md#count) :black_small_square: [create_path](tree-tree.md#create_path) :black_small_square: ['#del_tag' not found]() :black_small_square: [depth](tree-tree.md#depth) :black_small_square: ['#depth_shift' not found]() :black_small_square: [detach](tree-tree.md#detach) :black_small_square: ['#display_title' not found]() :black_small_square: [dump](tree-tree.md#dump) :black_small_square: ['#dump_pages' not found]() :black_small_square: ['#dump_title' not found]() :black_small_square: ['#dump_titles' not found]() :black_small_square: ['#dump_toc' not found]() :black_small_square: ['#file_name' not found]() :black_small_square: [find](tree-tree.md#find) :black_small_square: [FromFile](tree-tree.md#fromfile) :black_small_square: [get](tree-tree.md#get) :black_small_square: [get_child](tree-treelist.md#get_child) :black_small_square: ['#get_content' not found]() :black_small_square: ['#get_create_section' not found]() :black_small_square: ['#get_doc' not found]() :black_small_square: [get_function_class](get_f2-get_function_class.md#get_function_class) :black_small_square: [\_\_getitem__](tree-tree.md#__getitem__) :black_small_square: ['#get_property_class' not found]() :black_small_square: ['#get_toc' not found]() :black_small_square: ['#get_toc_sections' not found]() :black_small_square: ['#has_any_tag' not found]() :black_small_square: ['#has_content' not found]() :black_small_square: ['#has_tag' not found]() :black_small_square: ['#has_toc' not found]() :black_small_square: ['#header_depth' not found]() :black_small_square: ['#hidden' not found]() :black_small_square: ['#homonyms_count' not found]() :black_small_square: ['#ignore_if_empty' not found]() :black_small_square: ['#insert_toc' not found]() :black_small_square: ['#in_toc' not found]() :black_small_square: ['#is_chapter' not found]() :black_small_square: ['#is_displayed_OLD' not found]() :black_small_square: ['#is_hidden' not found]() :black_small_square: ['#is_page' not found]() :black_small_square: ['#is_text' not found]() :black_small_square: ['#is_toc' not found]() :black_small_square: [is_top](tree-tree.md#is_top) :black_small_square: ['#is_transparent' not found]() :black_small_square: [items](tree-treelist.md#items) :black_small_square: [\_\_iter__](tree-tree.md#__iter__) :black_small_square: [join_keys](tree-tree.md#join_keys) :black_small_square: [key](tree-tree.md#key) :black_small_square: [keys](tree-treelist.md#keys) :black_small_square: ['#_linked' not found]() :black_small_square: ['#link_to' not found]() :black_small_square: ['#ModuleTest' not found]() :black_small_square: [move_to_parent](tree-tree.md#move_to_parent) :black_small_square: ['#name' not found]() :black_small_square: ['#navigation' not found]() :black_small_square: ['#navigation_md' not found]() :black_small_square: [new](tree-tree.md#new) :black_small_square: ['#new_chapter' not found]() :black_small_square: ['#new_page' not found]() :black_small_square: [new_paths](tree-tree.md#new_paths) :black_small_square: ['#new_sections_group' not found]() :black_small_square: ['#new_tag_group' not found]() :black_small_square: ['#page' not found]() :black_small_square: [parent](tree-tree.md#parent) :black_small_square: ['#parse_comment' not found]() :black_small_square: [path](tree-tree.md#path) :black_small_square: ['#regroup' not found]() :black_small_square: [remove_from_parent](tree-treelist.md#remove_from_parent) :black_small_square: [set_child](tree-treelist.md#set_child) :black_small_square: [\_\_setitem__](tree-tree.md#__setitem__) :black_small_square: ['#set_tag' not found]() :black_small_square: [solve_path](tree-tree.md#solve_path) :black_small_square: [solve_to_missing](tree-tree.md#solve_to_missing) :black_small_square: ['#sort_sections' not found]() :black_small_square: ['#__str__' not found]() :black_small_square: ['#tag' not found]() :black_small_square: ['#tags' not found]() :black_small_square: ['#Test' not found]() :black_small_square: ['#test' not found]() :black_small_square: [test_numpy](tree-tree.md#test_numpy) :black_small_square: ['#title' not found]() :black_small_square: ['#_title_sort' not found]() :black_small_square: ['#toc' not found]() :black_small_square: ['#toc_depth_shift' not found]() :black_small_square: ['#toc_flat' not found]() :black_small_square: ['#toc_max_depth' not found]() :black_small_square: ['#toc_max_length' not found]() :black_small_square: ['#toc_sort' not found]() :black_small_square: ['#toc_title' not found]() :black_small_square: [top](tree-tree.md#top) :black_small_square: ['#top_bar' not found]() :black_small_square: ['#transparent' not found]() :black_small_square: ['#user_prop' not found]() :black_small_square: ['#user_props' not found]() :black_small_square: [values](tree-treelist.md#values) :black_small_square: ['#write' not found]() :black_small_square: ['#write_header' not found]() :black_small_square: ['#write_source' not found]() :black_small_square:

## get_function_class

- [complete_with](pydoc-propertysection.md#complete_with)
- [default](pydoc-propertysection.md#default)
- [fget](pydoc-propertysection.md#fget)
- [FromDict](pydoc-propertysection.md#fromdict)
- [FromInspect](pydoc-propertysection.md#frominspect)
- [FromListItem](pydoc-propertysection.md#fromlistitem)
- [FromStatic](pydoc-propertysection.md#fromstatic)
- [fset](pydoc-propertysection.md#fset)
- [type](pydoc-propertysection.md#type)

## get_function_class



### get_function_class

> _type_: **str**
>

default value

### get_function_class

> _type_: **Function_**
>

getter [fget](pydoc-propertysection.md#fget)

### get_function_class

> _type_: **Function_**
>

setter [fset](pydoc-propertysection.md#fset)

### get_function_class

> _type_: **str**
>

type of the property

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#get_function_class) :black_small_square: [get_function_class](#get_function_class) :black_small_square: [get_function_class](get_f2-get_function_class.md)</sub>

## get_function_class



----------
### before_comment()

> method

``` python
before_comment()
```

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#get_function_class) :black_small_square: [get_function_class](#get_function_class) :black_small_square: [get_function_class](get_f2-get_function_class.md#get_function_class-11)</sub>

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#get_function_class) :black_small_square: [get_function_class](#get_function_class) :black_small_square: [get_function_class](get_f2-get_function_class.md#get_function_class-11)</sub>

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#get_function_class) :black_small_square: [get_function_class](#get_function_class) :black_small_square: [get_function_class](get_f2-get_function_class.md#get_function_class-11)</sub>

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#get_function_class) :black_small_square: [get_function_class](#get_function_class) :black_small_square: [get_function_class](get_f2-get_function_class.md#get_function_class-11)</sub>

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#get_function_class) :black_small_square: [get_function_class](#get_function_class) :black_small_square: [get_function_class](get_f2-get_function_class.md#get_function_class-11)</sub>

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#get_function_class) :black_small_square: [get_function_class](#get_function_class) :black_small_square: [get_function_class](get_f2-get_function_class.md#get_function_class-11)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#get_function_class) :black_small_square: [get_function_class](#get_function_class) :black_small_square: [get_function_class](get_f2-get_function_class.md)</sub>
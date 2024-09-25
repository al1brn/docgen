# documentation

Created on Fri Sep 13 08:33:58 2024

@author: alain

## Content

- [Documentation](docum-documentation.md)
  - [hooks](docum-documentation.md#hooks)
  - [create_documentation](docum-documentation.md#create_documentation)
  - [set_hook](docum-documentation.md#set_hook)
  - [solve_hooks](docum-documentation.md#solve_hooks)
  - [solve_section_links](docum-documentation.md#solve_section_links)
- [Section](docum-section.md)
  - [all_count](docum-section.md#all_count)
  - [anchor](docum-section.md#anchor)
  - [chapter](docum-section.md#chapter)
  - [chapter_prefix](docum-section.md#chapter_prefix)
  - [comment](docum-section.md#comment)
  - [count](docum-section.md#count)
  - [depth](docum-section.md#depth)
  - [depth_shift](docum-section.md#depth_shift)
  - [file_name](docum-section.md#file_name)
  - [has_content](docum-section.md#has_content)
  - [has_toc](docum-section.md#has_toc)
  - [header_depth](docum-section.md#header_depth)
  - [hidden](docum-section.md#hidden)
  - [homonyms_count](docum-section.md#homonyms_count)
  - [ignore_if_empty](docum-section.md#ignore_if_empty)
  - [in_toc](docum-section.md#in_toc)
  - [is_chapter](docum-section.md#is_chapter)
  - [is_displayed](docum-section.md#is_displayed)
  - [is_hidden](docum-section.md#is_hidden)
  - [is_page](docum-section.md#is_page)
  - [is_text](docum-section.md#is_text)
  - [is_toc](docum-section.md#is_toc)
  - [is_top](docum-section.md#is_top)
  - [is_transparent](docum-section.md#is_transparent)
  - [_linked](docum-section.md#_linked)
  - [navigation](docum-section.md#navigation)
  - [navigation_md](docum-section.md#navigation_md)
  - [page](docum-section.md#page)
  - [path](docum-section.md#path)
  - [sort_sections](docum-section.md#sort_sections)
  - [tags](docum-section.md#tags)
  - [title](docum-section.md#title)
  - [toc](docum-section.md#toc)
  - [toc_depth_shift](docum-section.md#toc_depth_shift)
  - [toc_flat](docum-section.md#toc_flat)
  - [toc_max_length](docum-section.md#toc_max_length)
  - [toc_sort](docum-section.md#toc_sort)
  - [toc_title](docum-section.md#toc_title)
  - [top](docum-section.md#top)
  - [top_bar](docum-section.md#top_bar)
  - [transparent](docum-section.md#transparent)
  - [user_props](docum-section.md#user_props)
  - [add](docum-section.md#add)
  - [all_items](docum-section.md#all_items)
  - [all_paths](docum-section.md#all_paths)
  - [all_values](docum-section.md#all_values)
  - [cook](docum-section.md#cook)
  - [create_path](docum-section.md#create_path)
  - [detach](docum-section.md#detach)
  - [find](docum-section.md#find)
  - [FromFile](docum-section.md#fromfile)
  - [FromInspect](docum-section.md#frominspect)
  - [get](docum-section.md#get)
  - [get_child](docum-section.md#get_child)
  - [get_content](docum-section.md#get_content)
  - [get_create_section](docum-section.md#get_create_section)
  - [get_toc](docum-section.md#get_toc)
  - [get_toc_sections](docum-section.md#get_toc_sections)
  - [insert_toc](docum-section.md#insert_toc)
  - [items](docum-section.md#items)
  - [join_keys](docum-section.md#join_keys)
  - [keys](docum-section.md#keys)
  - [link_to](docum-section.md#link_to)
  - [move_to_parent](docum-section.md#move_to_parent)
  - [new](docum-section.md#new)
  - [new_chapter](docum-section.md#new_chapter)
  - [new_page](docum-section.md#new_page)
  - [new_paths](docum-section.md#new_paths)
  - [new_sections_group](docum-section.md#new_sections_group)
  - [new_tag_group](docum-section.md#new_tag_group)
  - [remove_from_parent](docum-section.md#remove_from_parent)
  - [set_child](docum-section.md#set_child)
  - [solve_path](docum-section.md#solve_path)
  - [solve_to_missing](docum-section.md#solve_to_missing)
  - [user_prop](docum-section.md#user_prop)
  - [values](docum-section.md#values)
  - [write](docum-section.md#write)
  - [write_header](docum-section.md#write_header)
  - [write_source](docum-section.md#write_source)
- [title_to_anchor](docum---documentation.md#title_to_anchor)
- [title_to_file_name](docum---documentation.md#title_to_file_name)

## Classes



- [Documentation](docum-documentation.md)
- [Section](docum-section.md)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#documentation) :black_small_square: [Content](#content) :black_small_square: [documentation](docum---documentation.md)</sub>

## Functions



----------
### title_to_anchor()

> function

``` python
title_to_anchor(title)
```

Convert the title into markdown anchor

#### Arguments:
- **title** (_str_) : title



#### Returns:
- **str** : anchor

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#documentation) :black_small_square: [Content](#content) :black_small_square: [Functions](docum---documentation.md#functions)</sub>

----------
### title_to_file_name()

> function

``` python
title_to_file_name(title)
```

Get the file name from the title

#### Arguments:
- **title** (_str_) : title



#### Returns:
- **str** : file name (file.md)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#documentation) :black_small_square: [Content](#content) :black_small_square: [Functions](docum---documentation.md#functions)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#documentation) :black_small_square: [Content](#content) :black_small_square: [documentation](docum---documentation.md)</sub>
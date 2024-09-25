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

Tree.FromFile :black_small_square: Section.ModuleTest :black_small_square: Section.Test :black_small_square: list.\_\_add__ :black_small_square: list.\_\_contains__ :black_small_square: list.\_\_delitem__ :black_small_square: list.\_\_eq__ :black_small_square: list.\_\_ge__ :black_small_square: list.\_\_getattribute__ :black_small_square: Tree.\_\_getitem__ :black_small_square: list.\_\_gt__ :black_small_square: list.\_\_iadd__ :black_small_square: list.\_\_imul__ :black_small_square: Tree.\_\_iter__ :black_small_square: list.\_\_le__ :black_small_square: list.\_\_len__ :black_small_square: list.\_\_lt__ :black_small_square: list.\_\_mul__ :black_small_square: list.\_\_ne__ :black_small_square: list.\_\_repr__ :black_small_square: list.\_\_reversed__ :black_small_square: list.\_\_rmul__ :black_small_square: Tree.\_\_setitem__ :black_small_square: list.\_\_sizeof__ :black_small_square: ObjectSection.\_\_str__ :black_small_square: Section.\_title_sort :black_small_square: Tree.add :black_small_square: Section.after_comment :black_small_square: Tree.all_items :black_small_square: Tree.all_paths :black_small_square: Tree.all_values :black_small_square: list.append :black_small_square: Section.before_comment :black_small_square: list.clear :black_small_square: Section.cook :black_small_square: list.copy :black_small_square: Tree.create_path :black_small_square: Section.del_tag :black_small_square: Tree.detach :black_small_square: Tree.dump :black_small_square: Section.dump_pages :black_small_square: Section.dump_title :black_small_square: Section.dump_titles :black_small_square: Section.dump_toc :black_small_square: list.extend :black_small_square: Tree.find :black_small_square: Tree.get :black_small_square: TreeList.get_child :black_small_square: Section.get_content :black_small_square: Section.get_create_section :black_small_square: ObjectSection.get_doc :black_small_square: Section.get_toc :black_small_square: Section.get_toc_sections :black_small_square: Section.has_any_tag :black_small_square: Section.has_tag :black_small_square: list.index :black_small_square: list.insert :black_small_square: Section.insert_toc :black_small_square: TreeList.items :black_small_square: Tree.join_keys :black_small_square: TreeList.keys :black_small_square: Section.link_to :black_small_square: Tree.move_to_parent :black_small_square: Section.new :black_small_square: Section.new_chapter :black_small_square: Section.new_page :black_small_square: Tree.new_paths :black_small_square: Section.new_sections_group :black_small_square: Section.new_tag_group :black_small_square: Section.parse_comment :black_small_square: list.pop :black_small_square: list.remove :black_small_square: TreeList.remove_from_parent :black_small_square: list.reverse :black_small_square: TreeList.set_child :black_small_square: Section.set_tag :black_small_square: Tree.solve_path :black_small_square: Tree.solve_to_missing :black_small_square: list.sort :black_small_square: Tree.test :black_small_square: Tree.test_numpy :black_small_square: Section.user_prop :black_small_square: TreeList.values :black_small_square: Section.write :black_small_square: Section.write_header :black_small_square: Section.write_source :black_small_square:

## Content

- **A** : [all_count](pydoc-modulesection.md#all_count) :black_small_square: [anchor](pydoc-modulesection.md#anchor)
- **C** : [chapter](pydoc-modulesection.md#chapter) :black_small_square: [chapter_prefix](pydoc-modulesection.md#chapter_prefix) :black_small_square: [count](pydoc-modulesection.md#count)
- **D** : [depth](pydoc-modulesection.md#depth)
- **F** : [file_name](pydoc-modulesection.md#file_name) :black_small_square: [FromInspect](pydoc-modulesection.md#frominspect)
- **H** : [header_depth](pydoc-modulesection.md#header_depth) :black_small_square: [homonyms_count](pydoc-modulesection.md#homonyms_count)
- **I** : [_init](pydoc-modulesection.md#_init) :black_small_square: [is_displayed](pydoc-modulesection.md#is_displayed) :black_small_square: [is_top](pydoc-modulesection.md#is_top)
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
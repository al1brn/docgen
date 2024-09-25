# FunctionSection

``` python
FunctionSection(name, comment=None, tag=None, **parameters)
```

Function section

#### Arguments:
- **name** (_str_) : object name
- **comment** (_str_ = None) : comment
- **tag** (_str_ = None) : section tag
- **parameters** : parameter initial values

### Inherited

T.r.e.e.FromFileS.e.c.t.i.o.n.ModuleTestS.e.c.t.i.o.n.Testlist.\_\_add__list.\_\_contains__list.\_\_delitem__list.\_\_eq__list.\_\_ge__list.\_\_getattribute__T.r.e.e.\_\_getitem__list.\_\_gt__list.\_\_iadd__list.\_\_imul__T.r.e.e.\_\_iter__list.\_\_le__list.\_\_len__list.\_\_lt__list.\_\_mul__list.\_\_ne__list.\_\_repr__list.\_\_reversed__list.\_\_rmul__T.r.e.e.\_\_setitem__list.\_\_sizeof__S.e.c.t.i.o.n.\_title_sortT.r.e.e.addT.r.e.e.all_itemsT.r.e.e.all_pathsT.r.e.e.all_valueslist.appendlist.clearS.e.c.t.i.o.n.cooklist.copyT.r.e.e.create_pathS.e.c.t.i.o.n.del_tagT.r.e.e.detachT.r.e.e.dumpS.e.c.t.i.o.n.dump_pagesS.e.c.t.i.o.n.dump_titleS.e.c.t.i.o.n.dump_titlesS.e.c.t.i.o.n.dump_toclist.extendT.r.e.e.findT.r.e.e.getT.r.e.e.L.i.s.t.get_childS.e.c.t.i.o.n.get_contentS.e.c.t.i.o.n.get_create_sectionO.b.j.e.c.t.S.e.c.t.i.o.n.get_docS.e.c.t.i.o.n.get_tocS.e.c.t.i.o.n.get_toc_sectionsS.e.c.t.i.o.n.has_any_tagS.e.c.t.i.o.n.has_taglist.indexlist.insertS.e.c.t.i.o.n.insert_tocT.r.e.e.L.i.s.t.itemsT.r.e.e.join_keysT.r.e.e.L.i.s.t.keysS.e.c.t.i.o.n.link_toT.r.e.e.move_to_parentS.e.c.t.i.o.n.newS.e.c.t.i.o.n.new_chapterS.e.c.t.i.o.n.new_pageT.r.e.e.new_pathsS.e.c.t.i.o.n.new_sections_groupS.e.c.t.i.o.n.new_tag_groupS.e.c.t.i.o.n.parse_commentlist.popO.b.j.e.c.t.S.e.c.t.i.o.n.regrouplist.removeT.r.e.e.L.i.s.t.remove_from_parentlist.reverseT.r.e.e.L.i.s.t.set_childS.e.c.t.i.o.n.set_tagT.r.e.e.solve_pathT.r.e.e.solve_to_missinglist.sortT.r.e.e.testT.r.e.e.test_numpyS.e.c.t.i.o.n.user_propT.r.e.e.L.i.s.t.valuesS.e.c.t.i.o.n.writeS.e.c.t.i.o.n.write_headerS.e.c.t.i.o.n.write_source

## Content

- **A** : [all_count](pydoc-functionsection.md#all_count) :black_small_square: [anchor](pydoc-functionsection.md#anchor) :black_small_square: [arguments](pydoc-functionsection.md#arguments)
- **C** : [chapter](pydoc-functionsection.md#chapter) :black_small_square: [chapter_prefix](pydoc-functionsection.md#chapter_prefix) :black_small_square: [count](pydoc-functionsection.md#count)
- **D** : [depth](pydoc-functionsection.md#depth)
- **F** : [file_name](pydoc-functionsection.md#file_name) :black_small_square: [FromInspect](pydoc-functionsection.md#frominspect) :black_small_square: [ftype](pydoc-functionsection.md#ftype)
- **H** : [header_depth](pydoc-functionsection.md#header_depth) :black_small_square: [homonyms_count](pydoc-functionsection.md#homonyms_count)
- **I** : [is_displayed](pydoc-functionsection.md#is_displayed) :black_small_square: [is_top](pydoc-functionsection.md#is_top)
- **N** : [navigation_md](pydoc-functionsection.md#navigation_md)
- **P** : [page](pydoc-functionsection.md#page) :black_small_square: [path](pydoc-functionsection.md#path)
- **R** : [raises](pydoc-functionsection.md#raises)
- **S** : [signature](pydoc-functionsection.md#signature)
- **T** : [top](pydoc-functionsection.md#top)

## Properties



### all_count

> _type_: **int**
>

Total number of children

### anchor

> _type_: **str**
>

The anchor of this section within the page

### arguments

> _type_: **DescriptionList**<br> _default_: **[]**
>

argument descriptions

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

The file name is built by joining [chapter_prefix](pydoc-functionsection.md#chapter_prefix) with the name of section.

> [!NOTE]
> top chapter returns "index.md"

### ftype

> _type_: **str**
>

function type (function, static, class, ...)

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

Returns False if the section if [is_hidden](pydoc-functionsection.md#is_hidden).

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

### raises

> _type_: **DescriptionList**<br> _default_: **None**
>

list of raised exceptions

### signature

> _type_: **str**
>

function signature

### top

> _type_: **Section**
>

Get the topmost section

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#functionsection) :black_small_square: [Content](#content) :black_small_square: [FunctionSection](pydoc-functionsection.md)</sub>

## Methods



----------
### FromInspect()

> classmethod

``` python
FromInspect(name, function_object)
```

Create a FunctionSection by inspecting a function object

#### Arguments:
- **name** (_str_ = None) : name of the function
- **function_object**

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#functionsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-functionsection.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#functionsection) :black_small_square: [Content](#content) :black_small_square: [FunctionSection](pydoc-functionsection.md)</sub>
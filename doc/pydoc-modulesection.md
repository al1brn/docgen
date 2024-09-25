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

T.r.e.e.FromFileS.e.c.t.i.o.n.ModuleTestS.e.c.t.i.o.n.Testlist.\_\_add__list.\_\_contains__list.\_\_delitem__list.\_\_eq__list.\_\_ge__list.\_\_getattribute__T.r.e.e.\_\_getitem__list.\_\_gt__list.\_\_iadd__list.\_\_imul__T.r.e.e.\_\_iter__list.\_\_le__list.\_\_len__list.\_\_lt__list.\_\_mul__list.\_\_ne__list.\_\_repr__list.\_\_reversed__list.\_\_rmul__T.r.e.e.\_\_setitem__list.\_\_sizeof__O.b.j.e.c.t.S.e.c.t.i.o.n.\_\_str__S.e.c.t.i.o.n.\_title_sortT.r.e.e.addS.e.c.t.i.o.n.after_commentT.r.e.e.all_itemsT.r.e.e.all_pathsT.r.e.e.all_valueslist.appendS.e.c.t.i.o.n.before_commentlist.clearS.e.c.t.i.o.n.cooklist.copyT.r.e.e.create_pathS.e.c.t.i.o.n.del_tagT.r.e.e.detachT.r.e.e.dumpS.e.c.t.i.o.n.dump_pagesS.e.c.t.i.o.n.dump_titleS.e.c.t.i.o.n.dump_titlesS.e.c.t.i.o.n.dump_toclist.extendT.r.e.e.findT.r.e.e.getT.r.e.e.L.i.s.t.get_childS.e.c.t.i.o.n.get_contentS.e.c.t.i.o.n.get_create_sectionO.b.j.e.c.t.S.e.c.t.i.o.n.get_docS.e.c.t.i.o.n.get_tocS.e.c.t.i.o.n.get_toc_sectionsS.e.c.t.i.o.n.has_any_tagS.e.c.t.i.o.n.has_taglist.indexlist.insertS.e.c.t.i.o.n.insert_tocT.r.e.e.L.i.s.t.itemsT.r.e.e.join_keysT.r.e.e.L.i.s.t.keysS.e.c.t.i.o.n.link_toT.r.e.e.move_to_parentS.e.c.t.i.o.n.newS.e.c.t.i.o.n.new_chapterS.e.c.t.i.o.n.new_pageT.r.e.e.new_pathsS.e.c.t.i.o.n.new_sections_groupS.e.c.t.i.o.n.new_tag_groupS.e.c.t.i.o.n.parse_commentlist.poplist.removeT.r.e.e.L.i.s.t.remove_from_parentlist.reverseT.r.e.e.L.i.s.t.set_childS.e.c.t.i.o.n.set_tagT.r.e.e.solve_pathT.r.e.e.solve_to_missinglist.sortT.r.e.e.testT.r.e.e.test_numpyS.e.c.t.i.o.n.user_propT.r.e.e.L.i.s.t.valuesS.e.c.t.i.o.n.writeS.e.c.t.i.o.n.write_headerS.e.c.t.i.o.n.write_source

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
# ClassSection

``` python
ClassSection(name, comment=None, tag=None, **parameters)
```

Class section

#### Arguments:
- **name** (_str_) : object name
- **comment** (_str_ = None) : comment
- **tag** (_str_ = None) : section tag
- **parameters** : parameter initial values

### Inherited

## Content

- **A** : [all_count](pydoc-classsection.md#all_count) :black_small_square: [anchor](pydoc-classsection.md#anchor)
- **B** : [bases](pydoc-classsection.md#bases)
- **C** : [chapter](pydoc-classsection.md#chapter) :black_small_square: [chapter_prefix](pydoc-classsection.md#chapter_prefix) :black_small_square: [count](pydoc-classsection.md#count)
- **D** : [depth](pydoc-classsection.md#depth)
- **F** : [file_name](pydoc-classsection.md#file_name) :black_small_square: [FromInspect](pydoc-classsection.md#frominspect)
- **H** : [header_depth](pydoc-classsection.md#header_depth) :black_small_square: [homonyms_count](pydoc-classsection.md#homonyms_count)
- **I** : [inherited](pydoc-classsection.md#inherited) :black_small_square: [\_init](pydoc-classsection.md#_init) :black_small_square: [is_displayed](pydoc-classsection.md#is_displayed) :black_small_square: [is_top](pydoc-classsection.md#is_top)
- **N** : [navigation_md](pydoc-classsection.md#navigation_md)
- **P** : [page](pydoc-classsection.md#page) :black_small_square: [path](pydoc-classsection.md#path)
- **T** : [top](pydoc-classsection.md#top)

## Properties



### all_count

> _type_: **int**
>

Total number of children

### anchor

> _type_: **str**
>

The anchor of this section within the page

### bases

> _type_: **list**<br> _default_: **[]**
>

list of base classes

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

The file name is built by joining [chapter_prefix](pydoc-classsection.md#chapter_prefix) with the name of section.

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

### inherited

> _type_: **dict**<br> _default_: **{}**
>

inherited methods

### \_init

> _type_: **FunctionSection**
>

[FunctionSection](pydoc-functionsection.md) description for __init__ function if it exists

### is_displayed

> _type_: **True**
>

Does the section appear in the doc

Returns False if the section if [is_hidden](pydoc-classsection.md#is_hidden).

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

### top

> _type_: **Section**
>

Get the topmost section

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classsection) :black_small_square: [Content](#content) :black_small_square: [ClassSection](pydoc-classsection.md)</sub>

## Methods



----------
### FromInspect()

> classmethod

``` python
FromInspect(name, class_object)
```

Create a FunctionSection by inspecting a class object

> [!NOTE]
> All dunder methods are ignored in this version

#### Arguments:
- **name** (_str_) : class name
- **class_object** (_class_) : the class to inspect

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classsection) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-classsection.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#classsection) :black_small_square: [Content](#content) :black_small_square: [ClassSection](pydoc-classsection.md)</sub>
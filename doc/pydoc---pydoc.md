# pydoc

Python object info

Documentation is based on structure information on objects to document

created : 2024 09 14

## Content

- [capture_inheritance](pydoc---pydoc.md#capture_inheritance)
- [capture_inheritances](pydoc---pydoc.md#capture_inheritances)
- [ClassSection](pydoc-classsection.md)
  - [all_count](pydoc-classsection.md#all_count)
  - [anchor](pydoc-classsection.md#anchor)
  - [bases](pydoc-classsection.md#bases)
  - [chapter](pydoc-classsection.md#chapter)
  - [chapter_prefix](pydoc-classsection.md#chapter_prefix)
  - [count](pydoc-classsection.md#count)
  - [depth](pydoc-classsection.md#depth)
  - [file_name](pydoc-classsection.md#file_name)
  - [header_depth](pydoc-classsection.md#header_depth)
  - [homonyms_count](pydoc-classsection.md#homonyms_count)
  - [inherited](pydoc-classsection.md#inherited)
  - [\_init](pydoc-classsection.md#_init)
  - [is_displayed](pydoc-classsection.md#is_displayed)
  - [is_top](pydoc-classsection.md#is_top)
  - [navigation_md](pydoc-classsection.md#navigation_md)
  - [page](pydoc-classsection.md#page)
  - [path](pydoc-classsection.md#path)
  - [top](pydoc-classsection.md#top)
  - [FromInspect](pydoc-classsection.md#frominspect)
- [DescriptionList](pydoc-descriptionlist.md)
  - [complete_with](pydoc-descriptionlist.md#complete_with)
  - [get](pydoc-descriptionlist.md#get)
- [FunctionSection](pydoc-functionsection.md)
  - [all_count](pydoc-functionsection.md#all_count)
  - [anchor](pydoc-functionsection.md#anchor)
  - [arguments](pydoc-functionsection.md#arguments)
  - [chapter](pydoc-functionsection.md#chapter)
  - [chapter_prefix](pydoc-functionsection.md#chapter_prefix)
  - [count](pydoc-functionsection.md#count)
  - [depth](pydoc-functionsection.md#depth)
  - [file_name](pydoc-functionsection.md#file_name)
  - [ftype](pydoc-functionsection.md#ftype)
  - [header_depth](pydoc-functionsection.md#header_depth)
  - [homonyms_count](pydoc-functionsection.md#homonyms_count)
  - [is_displayed](pydoc-functionsection.md#is_displayed)
  - [is_top](pydoc-functionsection.md#is_top)
  - [navigation_md](pydoc-functionsection.md#navigation_md)
  - [page](pydoc-functionsection.md#page)
  - [path](pydoc-functionsection.md#path)
  - [raises](pydoc-functionsection.md#raises)
  - [signature](pydoc-functionsection.md#signature)
  - [top](pydoc-functionsection.md#top)
  - [FromInspect](pydoc-functionsection.md#frominspect)
- [ListItem](pydoc-listitem.md)
  - [default](pydoc-listitem.md#default)
  - [description](pydoc-listitem.md#description)
  - [has_default](pydoc-listitem.md#has_default)
  - [has_description](pydoc-listitem.md#has_description)
  - [has_type](pydoc-listitem.md#has_type)
  - [name](pydoc-listitem.md#name)
  - [type](pydoc-listitem.md#type)
  - [complete_with](pydoc-listitem.md#complete_with)
  - [FromOther](pydoc-listitem.md#fromother)
  - [FromParameter](pydoc-listitem.md#fromparameter)
  - [get_prop](pydoc-listitem.md#get_prop)
- [ModuleSection](pydoc-modulesection.md)
  - [all_count](pydoc-modulesection.md#all_count)
  - [anchor](pydoc-modulesection.md#anchor)
  - [chapter](pydoc-modulesection.md#chapter)
  - [chapter_prefix](pydoc-modulesection.md#chapter_prefix)
  - [count](pydoc-modulesection.md#count)
  - [depth](pydoc-modulesection.md#depth)
  - [file_name](pydoc-modulesection.md#file_name)
  - [header_depth](pydoc-modulesection.md#header_depth)
  - [homonyms_count](pydoc-modulesection.md#homonyms_count)
  - [\_init](pydoc-modulesection.md#_init)
  - [is_displayed](pydoc-modulesection.md#is_displayed)
  - [is_top](pydoc-modulesection.md#is_top)
  - [navigation_md](pydoc-modulesection.md#navigation_md)
  - [package](pydoc-modulesection.md#package)
  - [page](pydoc-modulesection.md#page)
  - [path](pydoc-modulesection.md#path)
  - [top](pydoc-modulesection.md#top)
  - [FromInspect](pydoc-modulesection.md#frominspect)
- [ObjectSection](pydoc-objectsection.md)
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
- [PropertySection](pydoc-propertysection.md)
  - [all_count](pydoc-propertysection.md#all_count)
  - [anchor](pydoc-propertysection.md#anchor)
  - [chapter](pydoc-propertysection.md#chapter)
  - [chapter_prefix](pydoc-propertysection.md#chapter_prefix)
  - [count](pydoc-propertysection.md#count)
  - [default](pydoc-propertysection.md#default)
  - [depth](pydoc-propertysection.md#depth)
  - [fget](pydoc-propertysection.md#fget)
  - [file_name](pydoc-propertysection.md#file_name)
  - [fset](pydoc-propertysection.md#fset)
  - [header_depth](pydoc-propertysection.md#header_depth)
  - [homonyms_count](pydoc-propertysection.md#homonyms_count)
  - [is_displayed](pydoc-propertysection.md#is_displayed)
  - [is_top](pydoc-propertysection.md#is_top)
  - [navigation_md](pydoc-propertysection.md#navigation_md)
  - [page](pydoc-propertysection.md#page)
  - [path](pydoc-propertysection.md#path)
  - [top](pydoc-propertysection.md#top)
  - [type](pydoc-propertysection.md#type)
  - [complete_with](pydoc-propertysection.md#complete_with)
  - [FromDict](pydoc-propertysection.md#fromdict)
  - [FromInspect](pydoc-propertysection.md#frominspect)
  - [FromListItem](pydoc-propertysection.md#fromlistitem)
  - [FromStatic](pydoc-propertysection.md#fromstatic)

## EMPTY

> _type_: **str**
>

## Classes



- [ClassSection](pydoc-classsection.md)
- [DescriptionList](pydoc-descriptionlist.md)
- [FunctionSection](pydoc-functionsection.md)
- [ListItem](pydoc-listitem.md)
- [ModuleSection](pydoc-modulesection.md)
- [ObjectSection](pydoc-objectsection.md)
- [PackageDoc](pydoc-packagedoc.md)
- [PropertySection](pydoc-propertysection.md)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#pydoc) :black_small_square: [Content](#content) :black_small_square: [pydoc](pydoc---pydoc.md)</sub>

## Functions



----------
### capture_inheritance()

> function

``` python
capture_inheritance(class_, base_, remove=True)
```

Capture properties et methods from another class

Allow to document class items as it were not inherited.

> [!Note]
> if the name of the base class is in the inherits list, it is removed from it

#### Arguments:
- **class_** (_dict_) : the class to enrich
- **base_** (_dict_) : the class to capture properties and methods from
- **remove** (_bool_ = True) : remove base name from inheritance list

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#pydoc) :black_small_square: [Content](#content) :black_small_square: [Functions](pydoc---pydoc.md#functions)</sub>

----------
### capture_inheritances()

> function

``` python
capture_inheritances(class_, files_, include=None, exclude=[], verbose=False)
```

Capture inheritances

Allow to document class items as it were not inherited.

> [!Note]
> if the name of the base class is in the inherits list, it is removed from it

#### Arguments:
- **class_** (_dict_) : the class to enrich
- **files_** (_dict_) : the hierarchy containing base classes to capture from
- **include** (_list_ = None) : limit capture to the given list
- **exclude** (_list_ = []) : exclude classes in the given list
- **verbose** ( = False)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#pydoc) :black_small_square: [Content](#content) :black_small_square: [Functions](pydoc---pydoc.md#functions)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#pydoc) :black_small_square: [Content](#content) :black_small_square: [pydoc](pydoc---pydoc.md)</sub>
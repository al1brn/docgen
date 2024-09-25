# pydoc

Python object info

Documentation is based on structure information on objects to document

created : 2024 09 14

## Content

- [capture_inheritance](pydoc---pydoc.md#capture_inheritance)
- [capture_inheritances](pydoc---pydoc.md#capture_inheritances)
- [ClassSection](pydoc-classsection.md)
  - [bases](pydoc-classsection.md#bases)
  - [inherited](pydoc-classsection.md#inherited)
  - [\_init](pydoc-classsection.md#_init)
  - [FromInspect](pydoc-classsection.md#frominspect)
- [DescriptionList](pydoc-descriptionlist.md)
  - [complete_with](pydoc-descriptionlist.md#complete_with)
  - [get](pydoc-descriptionlist.md#get)
- [FunctionSection](pydoc-functionsection.md)
  - [arguments](pydoc-functionsection.md#arguments)
  - [ftype](pydoc-functionsection.md#ftype)
  - [raises](pydoc-functionsection.md#raises)
  - [signature](pydoc-functionsection.md#signature)
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
  - [\_init](pydoc-modulesection.md#_init)
  - [package](pydoc-modulesection.md#package)
  - [FromInspect](pydoc-modulesection.md#frominspect)
- [ObjectSection](pydoc-objectsection.md)
  - [name](pydoc-objectsection.md#name)
  - [get_doc](pydoc-objectsection.md#get_doc)
- [PropertySection](pydoc-propertysection.md)
  - [default](pydoc-propertysection.md#default)
  - [fget](pydoc-propertysection.md#fget)
  - [fset](pydoc-propertysection.md#fset)
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
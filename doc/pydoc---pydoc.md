# pydoc

Python object info

Documentation is based on structure information on objects to document

created : 2024 09 14

## Content

- [ClassSection](pydoc-classsection.md)
- [DescriptionList](pydoc-descriptionlist.md)
- [FunctionSection](pydoc-functionsection.md)
- [ListItem](pydoc-listitem.md)
- [ModuleSection](pydoc-modulesection.md)
- [ObjectSection](pydoc-objectsection.md)
- [PackageDoc](pydoc-packagedoc.md)
- [PropertySection](pydoc-propertysection.md)
- [capture_inheritance](pydoc---pydoc.md#capture_inheritance)
- [capture_inheritances](pydoc---pydoc.md#capture_inheritances)

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
### capture_inheritance

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
### capture_inheritances

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
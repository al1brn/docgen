# ListItem

``` python
ListItem(name, type=None, default='_EMPTY', description=None, **kwargs)
```

An information line into a list

This class is used to information displayed in a single lines.

The line is intended to be displayed as `name (type = default) : description`.

#### Arguments:
- **name**
- **type** ( = None)
- **default**
- **description** ( = None)
- **kwargs**

## Content

- **C** : [complete_with](pydoc-listitem.md#complete_with)
- **D** : [default](pydoc-listitem.md#default) :black_small_square: [description](pydoc-listitem.md#description)
- **F** : [FromOther](pydoc-listitem.md#fromother) :black_small_square: [FromParameter](pydoc-listitem.md#fromparameter)
- **G** : [get_prop](pydoc-listitem.md#get_prop)
- **H** : [has_default](pydoc-listitem.md#has_default) :black_small_square: [has_description](pydoc-listitem.md#has_description) :black_small_square: [has_type](pydoc-listitem.md#has_type)
- **N** : [name](pydoc-listitem.md#name)
- **T** : [type](pydoc-listitem.md#type)

## Properties



### default

> _type_: **str**
>

default attribute

### description

> _type_: **str**
>

description

### has_default

> _type_: **bool**
>

Check if [default](pydoc-listitem.md#default) is different from [EMPTY](pydoc---pydoc.md#empty)

### has_description

> _type_: **bool**
>

Check if [description](pydoc-listitem.md#description) is not None

### has_type

> _type_: **bool**
>

Check if [type](pydoc-listitem.md#type) is not None

### name

> _type_: **str**
>

name attribute

### type

> _type_: **str**
>

type attribute

> <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [ListItem](pydoc-listitem.md#listitem) :black_small_square: [Content](pydoc-listitem.md#content) :black_small_square: [ListItem](pydoc-listitem.md#listitem)</sub>

## Methods



----------
### complete_with()

> method

``` python
complete_with(other: 'ListItem')
```

Complete with another list item.

Replace empty attributes by values coming from the other ListItem.

#### Arguments:
- **other** (_ListItem_)

> <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [ListItem](pydoc-listitem.md#listitem) :black_small_square: [Content](pydoc-listitem.md#content) :black_small_square: [Methods](pydoc-listitem.md#methods)</sub>

----------
### FromOther()

> classmethod

``` python
FromOther(other)
```

Create from another ListItem or from a dict

#### Arguments:
- **other** (_ListItem or dict_) : the source



#### Returns:
- **ListItem** :

> <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [ListItem](pydoc-listitem.md#listitem) :black_small_square: [Content](pydoc-listitem.md#content) :black_small_square: [Methods](pydoc-listitem.md#methods)</sub>

----------
### FromParameter()

> classmethod

``` python
FromParameter(param, description=None)
```

Create an instance from the python paramer description.

#### Arguments:
- **param**
- **description** ( = None)



#### Returns:
- **ListItem** :

> <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [ListItem](pydoc-listitem.md#listitem) :black_small_square: [Content](pydoc-listitem.md#content) :black_small_square: [Methods](pydoc-listitem.md#methods)</sub>

----------
### get_prop()

> method

``` python
get_prop(attribute, default=None)
```

Get a custom attribute value

#### Arguments:
- **attribute** (_str_) : attribute name
- **default** ( = None) : value to return if the attribute doesn't exist



#### Returns:
- **Any** : attribute value or default if it doesn't exist

> <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [ListItem](pydoc-listitem.md#listitem) :black_small_square: [Content](pydoc-listitem.md#content) :black_small_square: [Methods](pydoc-listitem.md#methods)</sub>

> <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [ListItem](pydoc-listitem.md#listitem) :black_small_square: [Content](pydoc-listitem.md#content) :black_small_square: [ListItem](pydoc-listitem.md#listitem)</sub>
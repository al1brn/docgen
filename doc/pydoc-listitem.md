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

## Properties



### default

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

default attribute

### description

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

description

### has_default

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

Check if [default](pydoc-listitem.md#default) is different from [EMPTY](pydoc---pydoc.md#empty)

### has_description

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

Check if [description](pydoc-listitem.md#description) is not None

### has_type

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

Check if [type](pydoc-listitem.md#type) is not None

### name

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

name attribute

### type

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

type attribute

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#listitem) :black_small_square: [Content](#content) :black_small_square: [ListItem](pydoc-listitem.md)</sub>

## Methods



----------
### complete_with

``` python
complete_with(other: 'ListItem')
```

Complete with another list item.

Replace empty attributes by values coming from the other ListItem.

#### Arguments:
- **other** (_ListItem_)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#listitem) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-listitem.md#methods)</sub>

----------
### FromOther

``` python
FromOther(other)
```

Create from another ListItem or from a dict

#### Arguments:
- **other** (_ListItem or dict_) : the source



#### Returns:
- **ListItem** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#listitem) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-listitem.md#methods)</sub>

----------
### FromParameter

``` python
FromParameter(param, description=None)
```

Create an instance from the python paramer description.

#### Arguments:
- **param**
- **description** ( = None)



#### Returns:
- **ListItem** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#listitem) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-listitem.md#methods)</sub>

----------
### get_prop

``` python
get_prop(attribute, default=None)
```

Get a custom attribute value

#### Arguments:
- **attribute** (_str_) : attribute name
- **default** ( = None) : value to return if the attribute doesn't exist



#### Returns:
- **Any** : attribute value or default if it doesn't exist

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#listitem) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-listitem.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#listitem) :black_small_square: [Content](#content) :black_small_square: [ListItem](pydoc-listitem.md)</sub>
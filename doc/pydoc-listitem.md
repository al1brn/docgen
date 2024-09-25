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

## name

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

name attribute

## type

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

type attribute

## default

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

default attribute

## description

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

description

----------
## FromOther

``` python
FromOther(other)
```

Create from another ListItem or from a dict

#### Arguments:
- **other** (_ListItem or dict_) : the source



#### Returns:
- **ListItem** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#listitem) :black_small_square:  :black_small_square: [ListItem](pydoc-listitem.md)</sub>

----------
## FromParameter

``` python
FromParameter(param, description=None)
```

Create an instance from the python paramer description.

#### Arguments:
- **param**
- **description** ( = None)



#### Returns:
- **ListItem** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#listitem) :black_small_square:  :black_small_square: [ListItem](pydoc-listitem.md)</sub>

----------
## complete_with

``` python
complete_with(other: 'ListItem')
```

Complete with another list item.

Replace empty attributes by values coming from the other ListItem.

#### Arguments:
- **other** (_ListItem_)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#listitem) :black_small_square:  :black_small_square: [ListItem](pydoc-listitem.md)</sub>

----------
## get_prop

``` python
get_prop(attribute, default=None)
```

Get a custom attribute value

#### Arguments:
- **attribute** (_str_) : attribute name
- **default** ( = None) : value to return if the attribute doesn't exist



#### Returns:
- **Any** : attribute value or default if it doesn't exist

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#listitem) :black_small_square:  :black_small_square: [ListItem](pydoc-listitem.md)</sub>

## has_default

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

Check if [default](pydoc-listitem.md#default) is different from [EMPTY](pydoc---pydoc.md#empty)

## has_description

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

Check if [description](pydoc-listitem.md#description) is not None

## has_type

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

Check if [type](pydoc-listitem.md#type) is not None
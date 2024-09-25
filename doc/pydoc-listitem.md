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

### has_default

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

Check if [default](pydoc-listitem.md#default) is different from ['#EMPTY' not found]()

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

Check if [default](pydoc-listitem.md#default) is different from ['#EMPTY' not found]()

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#listitem) :black_small_square:  :black_small_square: [ListItem](pydoc-listitem.md)</sub>

## Methods



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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#listitem) :black_small_square:  :black_small_square: [Methods](pydoc-listitem.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#listitem) :black_small_square:  :black_small_square: [ListItem](pydoc-listitem.md)</sub>
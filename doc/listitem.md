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

- [complete_with](listitem.md#complete_with)
- [FromOther](listitem.md#fromother)
- [FromParameter](listitem.md#fromparameter)
- [get_prop](listitem.md#get_prop)
- [has_default](listitem.md#has_default)
- [has_description](listitem.md#has_description)
- [has_type](listitem.md#has_type)
- [markdown](listitem.md#markdown)
- [__str__](listitem.md#__str__)



## Properties

### has_default


<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

Check if ['#default' not found]() is different from [EMPTY](index.md#empty)

### has_description


<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

Check if ['#description' not found]() is not None

### has_type


<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

Check if ['#type' not found]() is not None

### markdown


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#listitem) :black_small_square: [Content](#content) :black_small_square: [ListItem](#listitem)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#listitem) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#listitem) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#listitem) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#listitem) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### \_\_str__



``` python
__str__()
```

Return str(self).


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#listitem) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>


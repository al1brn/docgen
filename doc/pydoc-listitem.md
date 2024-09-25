# ListItem

``` python
ListItem(name, type=None, default='_EMPTY', description=None, **kwargs)
```



``` python
ListItem(name, type=None, default='_EMPTY', description=None, **kwargs)
```



An information line into a list

This class is used to information displayed in a single lines.

The line is intended to be displayed as `name (type = default) : description`.

Properties
----------
- name (str) : name attribute
- type (str)  : type attribute
- default (str) : default attribute
- description (str) : description


#### Arguments:
- **name**
- **type** ( = None)
- **default**
- **description** ( = None)
- **kwargs**



#### Arguments:
- **name**
- **type** ( = None)
- **default**
- **description** ( = None)
- **kwargs**



## FromOther

``` python
FromOther(other)
```



``` python
FromOther(other)
```



``` python
FromOther(other)
```



``` python
FromOther(other)
```



Create from another ListItem or from a dict

Arguments
---------
- other (ListItem or dict) : the source

Returns
-------
- ListItem


#### Arguments:
- **other** (_ListItem or dict_) : the source



#### Returns:
- **ListItem** : 



#### Arguments:
- **other** (_ListItem or dict_) : the source



#### Returns:
- **ListItem** : 



#### Arguments:
- **other** (_ListItem or dict_) : the source



#### Returns:
- **ListItem** : 



#### Arguments:
- **other** (_ListItem or dict_) : the source



#### Returns:
- **ListItem** : 



## FromParameter

``` python
FromParameter(param, description=None)
```



``` python
FromParameter(param, description=None)
```



``` python
FromParameter(param, description=None)
```



``` python
FromParameter(param, description=None)
```



Create an instance from the python paramer description.

Returns
-------
- ListItem


#### Arguments:
- **param**
- **description** ( = None)



#### Returns:
- **ListItem** : 



#### Arguments:
- **param**
- **description** ( = None)



#### Returns:
- **ListItem** : 



#### Arguments:
- **param**
- **description** ( = None)



#### Returns:
- **ListItem** : 



#### Arguments:
- **param**
- **description** ( = None)



#### Returns:
- **ListItem** : 



## complete_with

``` python
complete_with(other: 'ListItem')
```



``` python
complete_with(other: 'ListItem')
```



``` python
complete_with(other: 'ListItem')
```



``` python
complete_with(other: 'ListItem')
```



Complete with another list item.

Replace empty attributes by values coming from the other ListItem.


#### Arguments:
- **other** (_ListItem_)



#### Arguments:
- **other** (_ListItem_)



#### Arguments:
- **other** (_ListItem_)



#### Arguments:
- **other** (_ListItem_)



## get_prop

``` python
get_prop(attribute, default=None)
```



``` python
get_prop(attribute, default=None)
```



``` python
get_prop(attribute, default=None)
```



``` python
get_prop(attribute, default=None)
```



Get a custom attribute value

Arguments
---------
- attribute (str) : attribute name
- default : value to return if the attribute doesn't exist

Returns
-------
- Any : attribute value or default if it doesn't exist


#### Arguments:
- **attribute** (_str_) : attribute name
- **default** ( = None) : value to return if the attribute doesn't exist



#### Returns:
- **Any** : attribute value or default if it doesn't exist



#### Arguments:
- **attribute** (_str_) : attribute name
- **default** ( = None) : value to return if the attribute doesn't exist



#### Returns:
- **Any** : attribute value or default if it doesn't exist



#### Arguments:
- **attribute** (_str_) : attribute name
- **default** ( = None) : value to return if the attribute doesn't exist



#### Returns:
- **Any** : attribute value or default if it doesn't exist



#### Arguments:
- **attribute** (_str_) : attribute name
- **default** ( = None) : value to return if the attribute doesn't exist



#### Returns:
- **Any** : attribute value or default if it doesn't exist



## has_default


<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>



Check if ['#default' not found]() is different from [EMPTY](pydoc---pydoc.md#empty)

Returns
-------
- bool


## has_description


<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>



Check if ['#description' not found]() is not None

Returns
-------
- bool


## has_type


<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>



Check if ['#type' not found]() is not None

Returns
-------
- bool


## markdown


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>


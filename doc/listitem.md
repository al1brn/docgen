# ListItem

An information line into a list

This class is used to information displayed in a single lines.

The line is intended to be displayed as `name (type = default) : description`.

Properties
----------
- name (str) : name attribute
- type (str)  : type attribute
- default (str) : default attribute
- description (str) : description

``` python
ListItem(name, type=None, default=EMPTY, description=None, **kwargs)
```



## Content

[FromOther](#fromother)
- [FromParameter](#fromparameter)
- [__str__](#__str__)
- [complete_with](#complete_with)
- [get](#get)
- [has_default](#has_default)
- [has_description](#has_description)
- [has_type](#has_type)
- [markdown](#markdown)



## Properties

----------
### has_default

Check if [LINK ERROR: section 'default' not found]() is different from [LINK ERROR: section 'EMPTY' not found]()

Returns
-------
- bool

- getter 


<sub>[top](#listitem) [index](index.md)</sub>



----------
### has_description

Check if [LINK ERROR: section 'description' not found]() is not None

Returns
-------
- bool

- getter 


<sub>[top](#listitem) [index](index.md)</sub>



----------
### has_type

Check if [LINK ERROR: section 'type' not found]() is not None

Returns
-------
- bool

- getter 


<sub>[top](#listitem) [index](index.md)</sub>



----------
### markdown



- getter 


<sub>[top](#listitem) [index](index.md)</sub>



## Methods

----------
### FromOther



``` python
FromOther(other)
```



<sub>[top](#listitem) [index](index.md)</sub>



----------
### FromParameter

Create an instance from the python paramer description.

Returns
-------
- ListItem

``` python
FromParameter(param, description=None)
```



<sub>[top](#listitem) [index](index.md)</sub>



----------
### __str__



``` python
__str__()
```



<sub>[top](#listitem) [index](index.md)</sub>



----------
### complete_with

Complete with another list item.

Replace empty attributes by values coming from the other ListItem.

``` python
complete_with(other:"7")
```



<sub>[top](#listitem) [index](index.md)</sub>



----------
### get

Get a custom attribute value

Arguments
---------
- attribute (str) : attribute name
- default : value to return if the attribute doesn't exist

Returns
-------
- Any : attribute value or default if it doesn't exist

``` python
get(attribute, default=None)
```



<sub>[top](#listitem) [index](index.md)</sub>


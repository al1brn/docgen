# Property_

Information on property

Properties
----------
- type (str) : type of the property
- default (str) : default value
- fget (Function_) : getter [Function_](function_.md)
- fset (Function_) : setter [Function_](function_.md)

Arguments
---------
- name (str) : object name
- comment (str = None) : comment
- type (str = None) : type of the property
- default (str = EMPTY) : default value
- fget (Function_ = None) : getter [Function_](function_.md)
- fset (Function_ = None) : setter [Function_](function_.md)

``` python
Property_(name, comment=None, type=None, default=EMPTY, fget=None, fset=None, **kwargs)
```



## Content

[FromListItem](#fromlistitem)
- [FromObject](#fromobject)
- [FromStatic](#fromstatic)
- [complete_with](#complete_with)
- [print](#print)



## Methods

----------
### FromListItem

Create a property from a list item

Arguments
---------
- item (ListItem) : information on the property to create

Returns
-------
- Property_

``` python
FromListItem(item)
```



<sub>[top](#property_) [index](index.md)</sub>



----------
### FromObject

Create a Property_ instance from a property

> [!NOTE]
> If name is None, the name is read from fget

Arguments
---------
- object (property) : the object the scan
- name (str = None) : name

Returns
-------
- Property_

``` python
FromObject(object, name=None, verbose=False)
```



<sub>[top](#property_) [index](index.md)</sub>



----------
### FromStatic

Creare a Property_ instance from a static property in a module or a class

Arguments
---------
- object
- name (str = None)

Returns
-------
- Property_

``` python
FromStatic(object, name=None)
```



<sub>[top](#property_) [index](index.md)</sub>



----------
### complete_with

Enrich the description with another one

A Property_ can be created either in properties list in a comment
or by scaning object.
This function allows to merge information coming from these two sources

Arguments
---------
- other (Property) : contains complementary description

``` python
complete_with(other)
```



<sub>[top](#property_) [index](index.md)</sub>



----------
### print



``` python
print()
```



<sub>[top](#property_) [index](index.md)</sub>


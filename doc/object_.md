# Object_

Root class for informations on python objects

The minimum information is [LINK ERROR: section 'name' not found]() and [LINK ERROR: section 'comment' not found]() can be completed
by sub classes.

Properties
----------
- name (str) : module name, class name, property name...
- comment (str) : comment in __doc__
- obj_type (str) : (read only) name of the object type
- meta_props (dict) : dictionary of options set by meta instruction $ SET
- meta_lists (ditc) : dictionary of [DescriptionList](descriptionlist.md) extracted in the comment

Arguments
---------
- name (str) : object name
- comment (str = None) : comment
- kwargs : additional properties

``` python
Object_(name, comment=None, **kwargs)
```



## Content

[FromObject](#fromobject)
- [__str__](#__str__)
- [document](#document)
- [get](#get)
- [parse_comment](#parse_comment)
- [print](#print)



## Methods

----------
### FromObject



``` python
FromObject(object, name=None)
```



<sub>[top](#object_) [index](index.md)</sub>



----------
### __str__



``` python
__str__()
```



<sub>[top](#object_) [index](index.md)</sub>



----------
### document



``` python
document(doc)
```



<sub>[top](#object_) [index](index.md)</sub>



----------
### get

Get an optional property

Arguments
---------
- prop_name (str) : name of the property to read
- default (any = None) : default value if the property doesn't exist

Returns
-------
- any : the property or None if it doesn't exist

``` python
get(prop_name, default=None)
```



<sub>[top](#object_) [index](index.md)</sub>



----------
### parse_comment

Collect extra information from the comment

Inline commands
---------------
- $ DOC START : ignore lines above
- $ DO END : ignore lines after
- $ SET prop = 123 : pass properties to the doc generator

In addition, special lists are extracted to create [DescriptionList](descriptionlist.md)

Extracted lists
---------------
- raises
- arguments
- returns
- properties

``` python
parse_comment()
```



<sub>[top](#object_) [index](index.md)</sub>



----------
### print



``` python
print()
```



<sub>[top](#object_) [index](index.md)</sub>


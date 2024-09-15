# Function_

Description of a function

Properties
----------
- signature (str) : function signature
- decorators(list) : list of decorators
- arguments (list) : list of [ListItem](listitem.md)
- raises (list) : list of [ListItem](listitem.md)
- returns (list) : list of [ListItem](listitem.md)

Arguments
---------
- name (str) : object name
- comment (str = None) : comment
- signature (str = None) : function signature
- decorators(list = None) : list of decorators
- arguments (list = None) : list of [ListItem](listitem.md)
- raises (list = None) : list of [ListItem](listitem.md)
- returns (list = None) : list of [ListItem](listitem.md)

``` python
Function_(name, comment=None, signature=None, decorators=None, arguments=None, raises=None, returns=None, **kwargs)
```



## Content

[FromObject](#fromobject)
- [print](#print)



## Methods

----------
### FromObject

Create a Function_ instance from a function

> [!NOTE]
> If **name** argument is none, `object.__name__` is taken.

Arguments
---------
- object (function) : the object to scan
- name (str = None) : name of the object

``` python
FromObject(object, name=None, verbose=False)
```



<sub>[top](#function_) [index](index.md)</sub>



----------
### print



``` python
print()
```



<sub>[top](#function_) [index](index.md)</sub>


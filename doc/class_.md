# Class_

Information on a class

Properties
----------
- bases (list) : list of base classes
- _init (Function_) : [Function_](function_.md) description for __init__ function if it exists 

Arguments
---------
- name (str) : class name
- comment (str) : comment
- bases (list) : list of base classes
- kwargs : complementary information

``` python
Class_(name, comment=None, bases=None, **kwargs)
```



## Content

[FromObject](#fromobject)
- [print](#print)



## Methods

----------
### FromObject

Create an Class_ instance from a python class

> [!NOTE]
> If **name** argument is none, `object.__name__` is taken.

The method `__init__` is not stored in the [LINK ERROR: section 'members' not found]() dictionary but in [LINK ERROR: section '_init' not found]() property.

> [!CAUTION]
> All dunder methods are ignored in this version

Arguments
---------
- object (function) : the object to scan
- name (str = None) : name of the object

``` python
FromObject(object, name=None, verbose=False)
```



<sub>[top](#class_) [index](index.md)</sub>



----------
### print



``` python
print()
```



<sub>[top](#class_) [index](index.md)</sub>


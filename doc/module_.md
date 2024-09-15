# Module_

Information on a module

Arguments
---------
- name (str) : class name
- comment (str) : comment
- package (str) : package
- kwargs : complementary information

``` python
Module_(name, comment=None, package=None, **kwargs)
```



## Content

[FromObject](#fromobject)
- [LoadMe](#loadme)
- [is_same_package](#is_same_package)
- [print](#print)



## Methods

----------
### FromObject

Create an Module_ instance from a python module

> [!NOTE]
> If **name** argument is none, `object.__name__` is taken.

Arguments
---------
- object (function) : the object to scan
- name (str = None) : name of the object

``` python
FromObject(object, name=None, verbose=False)
```



<sub>[top](#module_) [index](index.md)</sub>



----------
### LoadMe



``` python
LoadMe()
```



<sub>[top](#module_) [index](index.md)</sub>



----------
### is_same_package



``` python
is_same_package(package)
```



<sub>[top](#module_) [index](index.md)</sub>



----------
### print



``` python
print()
```



<sub>[top](#module_) [index](index.md)</sub>


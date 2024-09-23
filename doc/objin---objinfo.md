# objinfo


Python object info

Documentation is based on structure information on objects to document



## Content

- [EMPTY](objin---objinfo.md#empty)
- [doc](objin---objinfo.md#doc)
- [module_](objin---objinfo.md#module_)
- [ClassFunc_](objin-classfunc_.md#classfunc_)
- [Class_](objin-class_.md#class_)
- [DescriptionList](objin-descriptionlist.md#descriptionlist)
- [Function_](objin-function_.md#function_)
- [ListItem](objin-listitem.md#listitem)
- [Module_](objin-module_.md#module_)
- [Object_](objin-object_.md#object_)
- [Property_](objin-property_.md#property_)
- [capture_inheritance](objin---objinfo.md#capture_inheritance)
- [capture_inheritances](objin---objinfo.md#capture_inheritances)



## Global variables

### doc

> TYPE: **dict**<br> DEFAULT: **{'index.md': '# Test\n\n\nThis...**



### EMPTY

> TYPE: **str**



### module_

> TYPE: **Module_**<br> DEFAULT: **<Module_ docgen>**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objinfo) :black_small_square: [Content](#content) :black_small_square: [objinfo](#objinfo)</sub>



## Classes


- [Class_](objin-class_.md#class_)
- [ClassFunc_](objin-classfunc_.md#classfunc_)
- [DescriptionList](objin-descriptionlist.md#descriptionlist)
- [Function_](objin-function_.md#function_)
- [ListItem](objin-listitem.md#listitem)
- [Module_](objin-module_.md#module_)
- [Object_](objin-object_.md#object_)
- [Property_](objin-property_.md#property_)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objinfo) :black_small_square: [Content](#content) :black_small_square: [objinfo](#objinfo)</sub>



## Functions

----------
### capture_inheritance



``` python
capture_inheritance(class_, base_, remove=True)
```

Capture properties et methods from another class

Allow to document class items as it were not inherited.

> [!Note]
> if the name of the base class is in the inherits list, it is removed from it


#### Arguments:
- **class_** (_dict_) : the class to enrich
- **base_** (_dict_) : the class to capture properties and methods from
- **remove** (_bool_ = True) : remove base name from inheritance list



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objinfo) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### capture_inheritances



``` python
capture_inheritances(class_, files_, include=None, exclude=[], verbose=False)
```

Capture inheritances

Allow to document class items as it were not inherited.

> [!Note]
> if the name of the base class is in the inherits list, it is removed from it


#### Arguments:
- **class_** (_dict_) : the class to enrich
- **files_** (_dict_) : the hierarchy containing base classes to capture from
- **include** (_list_ = None) : limit capture to the given list
- **exclude** (_list_ = []) : exclude classes in the given list
- **verbose** ( = False)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objinfo) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objinfo) :black_small_square: [Content](#content) :black_small_square: [objinfo](#objinfo)</sub>


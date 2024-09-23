# objinfo


Python object info

Documentation is based on structure information on objects to document



## Content

- [EMPTY](objin---objinfo.md#empty)
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
- [parse_file_source](objin---objinfo.md#parse_file_source)
- [parse_files](objin---objinfo.md#parse_files)
- [parse_meta_comment_OLD](objin---objinfo.md#parse_meta_comment_old)



## Global variables

### EMPTY

> TYPE: **str**



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



----------
### parse_files



``` python
parse_files(folder, key='', verbose=False)
```

Load files from a folder.

All the files with `.py` extension are parsed.


#### Arguments:
- **folder** (_str_) : main folder
- **key** ( = )
- **verbose** ( = False)



#### Returns:
- **dict** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objinfo) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### parse_file_source



``` python
parse_file_source(text, file_name='File')
```

Parse a python file source

The parser returns a dictionary giving the content of the file:

- file
  - comment
  - subs : dict of classes and functions
- class
  - name
  - comment
  - inherits (list)
  - subs : dict of properties and functions (methods)
- function
  - name
  - comment
  - args (str)
  - decorators (list of strs)
  - raises: list of dicts for raises
  - arguments: list of dicts for arguments
  - returns: list of dicts for returns
- property
  - name
  - comment
  - type
  - default
  - setter : function
  - getter : function

The parsing is done with regular expressions.


#### Arguments:
- **text** (_str_) : source code to parse
- **file_name** ( = File)



#### Returns:
- **dict** : classes and functions



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objinfo) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### parse_meta_comment_OLD



``` python
parse_meta_comment_OLD(comment)
```

Parse the comment itsel to extract meta tags

Tags are `$` starting at the beginin of the line followed by a command line:
    
- DOC START : extract comment from here
- DOC END : don't extract after after
- SET property value : property value pair


#### Arguments:
- **comment**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objinfo) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#objinfo) :black_small_square: [Content](#content) :black_small_square: [objinfo](#objinfo)</sub>


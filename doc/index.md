# Test


This module generates a simple but yet acceptable project documentation package
for a python package.

Documentation files are generated in markdown format which can be used on GitHub.

The documentation is generated in 3 majors steps:
1. Loading descriptors
2. Setting up the documentation structure
3. Creating the files

## Loading descriptors

Descriptors are dictionaries giving informations on each element to document such as
files, classes, functions, properties...

Descriptors can come from 3 sources:
- by parsing source files
- by getting description from python inspect module (future dev)
- by manually creating python objects descriptors

> [!NOTE]
> The capability to build descriptors directly by parsing source files
  avoids to have to import the modules in main program
  
Some changes can be made before passing to the next step.

## Setting up the documentation structure

Use select which descriptors must be part of the documentation.

## Creating the files

Documentation files are created

## Example

The piece of code below gives the structure of building a documentation package:

  
``` python

# Initialize the documentation

doc = Documentation("Project documentation", doc_folder="/Documentation/Folder", source_folder="python/project/demo")

# STEP 1 : Load source files relatively to source_folder

doc.load_folder(".")
doc.load_folder("core")

# STEP 2 : documentation structure

doc.document_folder('.')
doc.document_folder('core')

# STEP 3 : create the documentation files

doc.get_documentation()
```


This is not displayed


## Content

- [folder](index.md#folder)
- [module_](index.md#module_)



### folder

> <small>TYPE</small>: **str**<br> <small>DEFAULT</small>: **/Users/alain/Documents/blender...**



### module_

> <small>TYPE</small>: **Module_**<br> <small>DEFAULT</small>: **<Module_ docgen>**



## Modules


- [parser](parse---parser.md#parser)
- [tree](tree---tree.md#tree)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#test) :black_small_square:  :black_small_square: [Test](#test)</sub>



## Global variables

### CHAPTER

> <small>TYPE</small>: **int**<br> <small>DEFAULT</small>: **2**



### doc

> <small>TYPE</small>: **dict**<br> <small>DEFAULT</small>: **{'index.md': '# Test\n\n\nThis...**



### EMPTY

> <small>TYPE</small>: **str**



### folder

> <small>TYPE</small>: **str**<br> <small>DEFAULT</small>: **/Users/alain/Documents/blender...**



### module_

> <small>TYPE</small>: **Module_**<br> <small>DEFAULT</small>: **<Module_ docgen>**



### PAGE

> <small>TYPE</small>: **int**<br> <small>DEFAULT</small>: **1**



### TEXT

> <small>TYPE</small>: **int**<br> <small>DEFAULT</small>: **0**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#test) :black_small_square:  :black_small_square: [Test](#test)</sub>



## Classes


- [Class_](class_.md#class_)
- [ClassFunc_](classfunc_.md#classfunc_)
- [DescriptionList](descriptionlist.md#descriptionlist)
- [Doc](doc.md#doc)
- [Function_](function_.md#function_)
- [ListItem](listitem.md#listitem)
- [Module_](module_.md#module_)
- [Object_](object_.md#object_)
- [Property_](property_.md#property_)
- [Section](section.md#section)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#test) :black_small_square:  :black_small_square: [Test](#test)</sub>



## Functions

----------
### title_to_anchor



``` python
title_to_anchor(title)
```

Convert the title into markdown anchor


#### Arguments:
- **title** (_str_) : title



#### Returns:
- **str** : anchor



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#test) :black_small_square:  :black_small_square: [Functions](#functions)</sub>



----------
### title_to_file_name



``` python
title_to_file_name(title)
```

Get the file name from the title


#### Arguments:
- **title** (_str_) : title



#### Returns:
- **str** : file name (file.md)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#test) :black_small_square:  :black_small_square: [Functions](#functions)</sub>



----------
### under_to_md



``` python
under_to_md(title)
```




#### Arguments:
- **title**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#test) :black_small_square:  :black_small_square: [Functions](#functions)</sub>



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#test) :black_small_square:  :black_small_square: [Test](#test)</sub>


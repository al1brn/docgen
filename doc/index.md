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


## Modules

#### Content

- [CHAPTER](index.md#chapter)
- [PAGE](index.md#page)
- [TEXT](index.md#text)
- [Doc](mddoc-doc.md#doc)
- [Section](mddoc-section.md#section)
- [title_to_anchor](index.md#title_to_anchor)
- [title_to_file_name](index.md#title_to_file_name)
- [under_to_md](index.md#under_to_md)



#### Global variables

##### CHAPTER

> TYPE: **int**<br> DEFAULT: **2**



##### PAGE

> TYPE: **int**<br> DEFAULT: **1**



##### TEXT

> TYPE: **int**<br> DEFAULT: **0**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#test) :black_small_square:  :black_small_square: [mddoc](#mddoc)</sub>



#### Classes


- [Doc](mddoc-doc.md#doc)
- [Section](mddoc-section.md#section)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#test) :black_small_square:  :black_small_square: [mddoc](#mddoc)</sub>



#### Functions

----------
##### title_to_anchor



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
##### title_to_file_name



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
##### under_to_md



``` python
under_to_md(title)
```




#### Arguments:
- **title**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#test) :black_small_square:  :black_small_square: [Functions](#functions)</sub>



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#test) :black_small_square:  :black_small_square: [mddoc](#mddoc)</sub>



- [objinfo](objin---objinfo.md#objinfo)
- [parser](parse---parser.md#parser)
- [tree](tree---tree.md#tree)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#test) :black_small_square:  :black_small_square: [Test](#test)</sub>


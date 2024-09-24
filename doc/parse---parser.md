# parser

Created on Tue Sep 10 07:44:18 2024

@author: alain


File parser

This module implements a simple python parser which extract comments
form a source code file.

The parsing returns nested dicts where a dict contains information on the documented item

A base dict structure is:

- obj      : file, class, function, ...
- name     : python name
- comment  : the first multilines string after item declaration
- subs     : dict of dicts containing sub items

In addition to this structure, a dict can contain complementory values such as inheritance for
classes or arguments for functions


## Content

- [Text](parse-text.md#text)
- [struct_list](parse---parser.md#struct_list)
- [struct_search](parse---parser.md#struct_search)
- [test](parse---parser.md#test)
- [test_folder](parse---parser.md#test_folder)
- [regex_csource](parse---parser.md#regex_csource)
- [regex_source](parse---parser.md#regex_source)
- [regex_string1](parse---parser.md#regex_string1)
- [regex_string2](parse---parser.md#regex_string2)
- [dump_dict](parse---parser.md#dump_dict)
- [extract_lists](parse---parser.md#extract_lists)
- [extract_source](parse---parser.md#extract_source)
- [extract_strings](parse---parser.md#extract_strings)
- [format_list_line](parse---parser.md#format_list_line)
- [new_class](parse---parser.md#new_class)
- [new_file](parse---parser.md#new_file)
- [new_function](parse---parser.md#new_function)
- [new_property](parse---parser.md#new_property)
- [new_struct](parse---parser.md#new_struct)
- [parse_files](parse---parser.md#parse_files)
- [parse_file_source](parse---parser.md#parse_file_source)
- [parse_list_line](parse---parser.md#parse_list_line)
- [parse_meta_comment](parse---parser.md#parse_meta_comment)
- [replace_source](parse---parser.md#replace_source)
- [replace_strings](parse---parser.md#replace_strings)
- [struct_iter](parse---parser.md#struct_iter)
- [struct_list](parse---parser.md#struct_list)
- [struct_search](parse---parser.md#struct_search)
- [test](parse---parser.md#test)
- [test_folder](parse---parser.md#test_folder)



----------
### struct_list



``` python
struct_list(struct, name_only=True, **kwargs)
```




#### Arguments:
- **struct**
- **name_only** ( = True)
- **kwargs**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### struct_search



``` python
struct_search(struct, **kwargs)
```




#### Arguments:
- **struct**
- **kwargs**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### test



``` python
test()
```




<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### test_folder



``` python
test_folder(folder=None, sub_folders=[])
```




#### Arguments:
- **folder** ( = None)
- **sub_folders** ( = [])



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



## Global variables

### regex_csource

> TYPE: **Pattern**<br> DEFAULT: **re.compile('`((``[^`]*``)|([^`...**



### regex_source

> TYPE: **str**<br> DEFAULT: **`((``[^`]*``)|([^`\n]*))`**



### regex_string1

> TYPE: **str**<br> DEFAULT: **("[^"\\]*(?:\\.[^"\\]*)*")**



### regex_string2

> TYPE: **str**<br> DEFAULT: **('[^'\\]*(?:\\.[^'\\]*)*')**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [parser](#parser)</sub>



## Functions

----------
### dump_dict



``` python
dump_dict(d, indent=0)
```




#### Arguments:
- **d**
- **indent** ( = 0)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### extract_lists



``` python
extract_lists(comment, *titles)
```

Extract lists from a comment.

This parser extracts Properties, Arguments and Returns sections.
The corresponding lines are removed to build the 'new_comment' text.

The lists are generated from the structure


#### Arguments:
- **comment** (_str_) : the raw comment
- **titles** (_str or list of strs_) : the titles of the lists to extract



#### Returns:
- **str** : comment without the lists, lists as dict



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### extract_source



``` python
extract_source(text)
```

Replace source code block by an index.

This pretreatment ensure that the content of sourcode won't interfer with
regular expression


#### Arguments:
- **text** (_str_) : text to extract source code from



#### Returns:
- **str** : cleaned text and list of extracted pieces of code



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### extract_strings



``` python
extract_strings(text)
```

Replace string by an index.

This pretreatment ensure that the content of strings won't interfer with
regular expression


#### Arguments:
- **text** (_str_) : text to extract strings from



#### Returns:
- **str** : cleaned text and list of extracted strings



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### format_list_line



``` python
format_list_line(d)
```




#### Arguments:
- **d**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### new_class



``` python
new_class(name, comment=None, subs=None, inherits=None)
```




#### Arguments:
- **name**
- **comment** ( = None)
- **subs** ( = None)
- **inherits** ( = None)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### new_file



``` python
new_file(name, comment=None, subs=None)
```




#### Arguments:
- **name**
- **comment** ( = None)
- **subs** ( = None)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### new_function



``` python
new_function(name, comment=None, decorators=None, args=None, arguments=None, raises=None, returns=None)
```




#### Arguments:
- **name**
- **comment** ( = None)
- **decorators** ( = None)
- **args** ( = None)
- **arguments** ( = None)
- **raises** ( = None)
- **returns** ( = None)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### new_property



``` python
new_property(name, comment=None, type=None, default=None, setter=None, getter=None)
```




#### Arguments:
- **name**
- **comment** ( = None)
- **type** ( = None)
- **default** ( = None)
- **setter** ( = None)
- **getter** ( = None)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### new_struct



``` python
new_struct(obj, name, comment=None, subs=None, **kwargs)
```




#### Arguments:
- **obj**
- **name**
- **comment** ( = None)
- **subs** ( = None)
- **kwargs**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### parse_list_line



``` python
parse_list_line(line)
```

Parse a list line in a comment

syntax:
- name (type = default) : description

Default value could contain parenthesis as in `Vector = (1, 2, 3)`,
the parsing is done by reading the line char per char to handle
parenthesis nesting.

``` python
line = "- text (str = None) : text to parse"
pprint(parse_list_line(line))
# > {'default': 'None',
# > 'description': 'text to parse',
# > 'name': 'text',
# > 'obj' : 'str'}
```


#### Arguments:
- **line**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### parse_meta_comment



``` python
parse_meta_comment(comment)
```

Parse the comment itself to extract meta tags

Tags are `$` starting at the beginin of the line followed by a command line:
    
- $ DOC START : extract comment from here
- $ DOC END : don't extract after after
- $ DOC SET var = value  : a valid python set instruction
- $ DOC var : equivalent to DOC SET var = True
- $ DOC NOT var : equivalent to DOC SET var = False


#### Arguments:
- **comment**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### replace_source



``` python
replace_source(text, strings)
```

Replace the extracted strings.


#### Arguments:
- **text** (_str_) : text with replaced pieces of code
- **strings** : list of pieces of code



#### Returns:
- **Text** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### replace_strings



``` python
replace_strings(text, strings)
```

Replace the extracted strings.


#### Arguments:
- **text** (_str_) : text with replaced strings
- **strings** : list of strings



#### Returns:
- **Text** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### struct_iter



``` python
struct_iter(struct, f, *args, **kwargs)
```




#### Arguments:
- **struct**
- **f**
- **args**
- **kwargs**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### struct_list



``` python
struct_list(struct, name_only=True, **kwargs)
```




#### Arguments:
- **struct**
- **name_only** ( = True)
- **kwargs**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### struct_search



``` python
struct_search(struct, **kwargs)
```




#### Arguments:
- **struct**
- **kwargs**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### test



``` python
test()
```




<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



----------
### test_folder



``` python
test_folder(folder=None, sub_folders=[])
```




#### Arguments:
- **folder** ( = None)
- **sub_folders** ( = [])



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](#functions)</sub>



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [parser](#parser)</sub>



- [Text](parse-text.md#text)


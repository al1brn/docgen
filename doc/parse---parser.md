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

- **C** : [capture_inheritance](parse---parser.md#capture_inheritance) :black_small_square: [capture_inheritances](parse---parser.md#capture_inheritances) :black_small_square: [clean_python](parse---parser.md#clean_python)
- **D** : [del_margin](parse---parser.md#del_margin)
- **E** : [extract_lists](parse---parser.md#extract_lists) :black_small_square: [extract_source](parse---parser.md#extract_source) :black_small_square: [extract_strings](parse---parser.md#extract_strings)
- **P** : [parse_files](parse---parser.md#parse_files) :black_small_square: [parse_file_source](parse---parser.md#parse_file_source) :black_small_square: [parse_list_line](parse---parser.md#parse_list_line) :black_small_square: [parse_meta_comment](parse---parser.md#parse_meta_comment)
- **R** : [replace_source](parse---parser.md#replace_source) :black_small_square: [replace_strings](parse---parser.md#replace_strings)
- **T** : [Text](parse-text.md)

## Classes



- [Text](parse-text.md)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [parser](parse---parser.md)</sub>

## Functions



----------
### capture_inheritance()

> function

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](parse---parser.md#functions)</sub>

----------
### capture_inheritances()

> function

``` python
capture_inheritances(class_, files_, include=None, exclude=[], verbose=True)
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
- **verbose** ( = True)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](parse---parser.md#functions)</sub>

----------
### clean_python()

> function

``` python
clean_python(text)
```

Clean python source code

- Replace the comments by an comment index
- Replace the strings by an index
- Remove the blank lines
- Group multilines instructions between ( and )

Comments and strings are store in lists.
Comments are replaced by <COMMENT index> and strings by "index"

#### Arguments:
- **text** (_str_) : source code to clean



#### Returns:
- **str** : cleaned text
- **list** : list of comments
- **list** : list of strings

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](parse---parser.md#functions)</sub>

----------
### del_margin()

> function

``` python
del_margin(comment)
```

Move lines leftwards to suppress margin.

Comment read in source code can have a non nul left margin whcih is interprated in markdown.
This method:
- suppresses the margin of the first line
- move leftwards the lines after in order that the leftmost line has no margin and
  that the relative indentation remains the same

The following text:
|     Example of text
|               This text is aligned
|               with a margin:
|               - because it is written as a multiline comment string
|                 with indentation
|               Text continues here

Is realigned:
| Example of text
| This texte is aligned
| with a margin:
| - because it is written as a multiline comment string
|   with indentation
| Text continues here

#### Arguments:
- **comment** (_str_) : the comment



#### Returns:
- **str** : the realigned comment

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](parse---parser.md#functions)</sub>

----------
### extract_lists()

> function

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](parse---parser.md#functions)</sub>

----------
### extract_source()

> function

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](parse---parser.md#functions)</sub>

----------
### extract_strings()

> function

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](parse---parser.md#functions)</sub>

----------
### parse_files()

> function

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](parse---parser.md#functions)</sub>

----------
### parse_file_source()

> function

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](parse---parser.md#functions)</sub>

----------
### parse_list_line()

> function

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](parse---parser.md#functions)</sub>

----------
### parse_meta_comment()

> function

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](parse---parser.md#functions)</sub>

----------
### replace_source()

> function

``` python
replace_source(text, strings)
```

Replace the extracted strings.

#### Arguments:
- **text** (_str_) : text with replaced pieces of code
- **strings** : list of pieces of code



#### Returns:
- **Text** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](parse---parser.md#functions)</sub>

----------
### replace_strings()

> function

``` python
replace_strings(text, strings)
```

Replace the extracted strings.

#### Arguments:
- **text** (_str_) : text with replaced strings
- **strings** : list of strings



#### Returns:
- **Text** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [Functions](parse---parser.md#functions)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#parser) :black_small_square: [Content](#content) :black_small_square: [parser](parse---parser.md)</sub>
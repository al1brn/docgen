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


## capture_inheritance

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Capture properties et methods from another class

Allow to document class items as it were not inherited.

> [!Note]
> if the name of the base class is in the inherits list, it is removed from it

Arguments
---------
- class_ (dict) : the class to enrich
- base_ (dict) : the class to capture properties and methods from
- remove (bool = True) : remove base name from inheritance list


#### Arguments:
- **class_** (_dict_) : the class to enrich
- **base_** (_dict_) : the class to capture properties and methods from
- **remove** (_bool_ = True) : remove base name from inheritance list



#### Arguments:
- **class_** (_dict_) : the class to enrich
- **base_** (_dict_) : the class to capture properties and methods from
- **remove** (_bool_ = True) : remove base name from inheritance list



## capture_inheritances

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Capture inheritances

Allow to document class items as it were not inherited.

> [!Note]
> if the name of the base class is in the inherits list, it is removed from it

Arguments
---------
- class_ (dict) : the class to enrich
- files_ (dict) : the hierarchy containing base classes to capture from
- include (list = None) : limit capture to the given list
- exclude (list = []) : exclude classes in the given list


#### Arguments:
- **class_** (_dict_) : the class to enrich
- **files_** (_dict_) : the hierarchy containing base classes to capture from
- **include** (_list_ = None) : limit capture to the given list
- **exclude** (_list_ = []) : exclude classes in the given list
- **verbose** ( = True)



#### Arguments:
- **class_** (_dict_) : the class to enrich
- **files_** (_dict_) : the hierarchy containing base classes to capture from
- **include** (_list_ = None) : limit capture to the given list
- **exclude** (_list_ = []) : exclude classes in the given list
- **verbose** ( = True)



## clean_python

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Clean python source code

- Replace the comments by an comment index
- Replace the strings by an index
- Remove the blank lines
- Group multilines instructions between ( and )

Comments and strings are store in lists.
Comments are replaced by <COMMENT index> and strings by "index"

Arguments
---------
- text (str) : source code to clean

Returns
-------
- str  : cleaned text
- list : list of comments
- list : list of strings


#### Arguments:
- **text** (_str_) : source code to clean



#### Returns:
- **str** : cleaned text
- **list** : list of comments
- **list** : list of strings



#### Arguments:
- **text** (_str_) : source code to clean



#### Returns:
- **str** : cleaned text
- **list** : list of comments
- **list** : list of strings



## del_margin

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
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

Arguments
---------
- comment (str) : the comment

Returns
-------
- str : the realigned comment


#### Arguments:
- **comment** (_str_) : the comment



#### Returns:
- **str** : the realigned comment



#### Arguments:
- **comment** (_str_) : the comment



#### Returns:
- **str** : the realigned comment



## dump_dict

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



#### Arguments:
- **d**
- **indent** ( = 0)



#### Arguments:
- **d**
- **indent** ( = 0)



## extract_lists

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Extract lists from a comment.

This parser extracts Properties, Arguments and Returns sections.
The corresponding lines are removed to build the 'new_comment' text.

The lists are generated from the structure

Arguments
---------
- comment (str) : the raw comment
- titles (str or list of strs) : the titles of the lists to extract

Returns
-------
- str, dict: comment without the lists, lists as dict


#### Arguments:
- **comment** (_str_) : the raw comment
- **titles** (_str or list of strs_) : the titles of the lists to extract



#### Returns:
- **str** : comment without the lists, lists as dict



#### Arguments:
- **comment** (_str_) : the raw comment
- **titles** (_str or list of strs_) : the titles of the lists to extract



#### Returns:
- **str** : comment without the lists, lists as dict



## extract_source

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Replace source code block by an index.

This pretreatment ensure that the content of sourcode won't interfer with
regular expression

Arguments
---------
- text (str) : text to extract source code from

Returns
-------
- str, list : cleaned text and list of extracted pieces of code


#### Arguments:
- **text** (_str_) : text to extract source code from



#### Returns:
- **str** : cleaned text and list of extracted pieces of code



#### Arguments:
- **text** (_str_) : text to extract source code from



#### Returns:
- **str** : cleaned text and list of extracted pieces of code



## extract_strings

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Replace string by an index.

This pretreatment ensure that the content of strings won't interfer with
regular expression

Arguments
---------
- text (str) : text to extract strings from

Returns
-------
- str, list : cleaned text and list of extracted strings


#### Arguments:
- **text** (_str_) : text to extract strings from



#### Returns:
- **str** : cleaned text and list of extracted strings



#### Arguments:
- **text** (_str_) : text to extract strings from



#### Returns:
- **str** : cleaned text and list of extracted strings



## format_list_line

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



#### Arguments:
- **d**



#### Arguments:
- **d**



## new_class

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



#### Arguments:
- **name**
- **comment** ( = None)
- **subs** ( = None)
- **inherits** ( = None)



#### Arguments:
- **name**
- **comment** ( = None)
- **subs** ( = None)
- **inherits** ( = None)



## new_file

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



#### Arguments:
- **name**
- **comment** ( = None)
- **subs** ( = None)



#### Arguments:
- **name**
- **comment** ( = None)
- **subs** ( = None)



## new_function

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



#### Arguments:
- **name**
- **comment** ( = None)
- **decorators** ( = None)
- **args** ( = None)
- **arguments** ( = None)
- **raises** ( = None)
- **returns** ( = None)



#### Arguments:
- **name**
- **comment** ( = None)
- **decorators** ( = None)
- **args** ( = None)
- **arguments** ( = None)
- **raises** ( = None)
- **returns** ( = None)



## new_property

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



#### Arguments:
- **name**
- **comment** ( = None)
- **type** ( = None)
- **default** ( = None)
- **setter** ( = None)
- **getter** ( = None)



#### Arguments:
- **name**
- **comment** ( = None)
- **type** ( = None)
- **default** ( = None)
- **setter** ( = None)
- **getter** ( = None)



## new_struct

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



#### Arguments:
- **obj**
- **name**
- **comment** ( = None)
- **subs** ( = None)
- **kwargs**



#### Arguments:
- **obj**
- **name**
- **comment** ( = None)
- **subs** ( = None)
- **kwargs**



## parse_file_source

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
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

Arguments
---------
- text (str) : source code to parse

Returns
-------
- dict : classes and functions


#### Arguments:
- **text** (_str_) : source code to parse
- **file_name** ( = File)



#### Returns:
- **dict** : classes and functions



#### Arguments:
- **text** (_str_) : source code to parse
- **file_name** ( = File)



#### Returns:
- **dict** : classes and functions



## parse_files

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Load files from a folder.

All the files with `.py` extension are parsed.

Arguments
---------
- folder (str) : main folder
- root (str=None) :

Returns
-------
- dict


#### Arguments:
- **folder** (_str_) : main folder
- **key** ( = )
- **verbose** ( = False)



#### Returns:
- **dict** : 



#### Arguments:
- **folder** (_str_) : main folder
- **key** ( = )
- **verbose** ( = False)



#### Returns:
- **dict** : 



## parse_list_line

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
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



#### Arguments:
- **line**



## parse_meta_comment

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
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



#### Arguments:
- **comment**



## regex_csource


<table><tbody>
<tr><td>type</td><td><b>Pattern</b></td></tr>
<tr><td>default</td><td><b>re.compile('`((``[^`]*``)|([^`...</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>Pattern</b></td></tr>
<tr><td>default</td><td><b>re.compile('`((``[^`]*``)|([^`...</b</td></tr>
</tbody></table>



## regex_source


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>`((``[^`]*``)|([^`\n]*))`</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>`((``[^`]*``)|([^`\n]*))`</b</td></tr>
</tbody></table>



## regex_string1


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>("[^"\\]*(?:\\.[^"\\]*)*")</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>("[^"\\]*(?:\\.[^"\\]*)*")</b</td></tr>
</tbody></table>



## regex_string2


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>('[^'\\]*(?:\\.[^'\\]*)*')</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>('[^'\\]*(?:\\.[^'\\]*)*')</b</td></tr>
</tbody></table>



## replace_source

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Replace the extracted strings.

Arguments
---------
- text (str) : text with replaced pieces of code
- strings : list of pieces of code

Returns
-------
- Text with original strings


#### Arguments:
- **text** (_str_) : text with replaced pieces of code
- **strings** : list of pieces of code



#### Returns:
- **Text** : 



#### Arguments:
- **text** (_str_) : text with replaced pieces of code
- **strings** : list of pieces of code



#### Returns:
- **Text** : 



## replace_strings

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Replace the extracted strings.

Arguments
---------
- text (str) : text with replaced strings
- strings : list of strings

Returns
-------
- Text with original strings


#### Arguments:
- **text** (_str_) : text with replaced strings
- **strings** : list of strings



#### Returns:
- **Text** : 



#### Arguments:
- **text** (_str_) : text with replaced strings
- **strings** : list of strings



#### Returns:
- **Text** : 



## struct_iter

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



#### Arguments:
- **struct**
- **f**
- **args**
- **kwargs**



#### Arguments:
- **struct**
- **f**
- **args**
- **kwargs**



## struct_list

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



#### Arguments:
- **struct**
- **name_only** ( = True)
- **kwargs**



#### Arguments:
- **struct**
- **name_only** ( = True)
- **kwargs**



## struct_search

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



#### Arguments:
- **struct**
- **kwargs**



#### Arguments:
- **struct**
- **kwargs**



## test

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



## test_folder

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



#### Arguments:
- **folder** ( = None)
- **sub_folders** ( = [])



#### Arguments:
- **folder** ( = None)
- **sub_folders** ( = [])


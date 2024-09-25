# docgen




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


## title_to_anchor

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Convert the title into markdown anchor

Arguments
---------
- title (str) : title

Returns
-------
- str : anchor


#### Arguments:
- **title** (_str_) : title



#### Returns:
- **str** : anchor



#### Arguments:
- **title** (_str_) : title



#### Returns:
- **str** : anchor



## title_to_file_name

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



Get the file name from the title

Arguments
---------
- title (str) : title

Returns
-------
- str : file name (file.md)


#### Arguments:
- **title** (_str_) : title



#### Returns:
- **str** : file name (file.md)



#### Arguments:
- **title** (_str_) : title



#### Returns:
- **str** : file name (file.md)



## under_to_md

``` python
{self.name}{sig}
```



``` python
{self.name}{sig}
```



#### Arguments:
- **title**



#### Arguments:
- **title**



## EMPTY


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>



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
- **verbose** ( = False)



#### Arguments:
- **class_** (_dict_) : the class to enrich
- **files_** (_dict_) : the hierarchy containing base classes to capture from
- **include** (_list_ = None) : limit capture to the given list
- **exclude** (_list_ = []) : exclude classes in the given list
- **verbose** ( = False)



## doc


<table><tbody>
<tr><td>type</td><td><b>PackageDoc</b></td></tr>
<tr><td>default</td><td><b><Documentation docgen, 258 sec...</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>PackageDoc</b></td></tr>
<tr><td>default</td><td><b><Documentation docgen, 258 sec...</b</td></tr>
</tbody></table>



## files


<table><tbody>
<tr><td>type</td><td><b>dict</b></td></tr>
<tr><td>default</td><td><b>{'index.md': '# docgen\n\n\n\n...</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>dict</b></td></tr>
<tr><td>default</td><td><b>{'index.md': '# docgen\n\n\n\n...</b</td></tr>
</tbody></table>



## folder


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>/Users/alain/Documents/blender...</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>/Users/alain/Documents/blender...</b</td></tr>
</tbody></table>


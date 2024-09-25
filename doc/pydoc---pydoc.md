# pydoc






Python object info

Documentation is based on structure information on objects to document

created : 2024 09 14


## EMPTY


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>



## capture_inheritance

``` python
capture_inheritance(class_, base_, remove=True)
```



``` python
capture_inheritance(class_, base_, remove=True)
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
capture_inheritances(class_, files_, include=None, exclude=[], verbose=False)
```



``` python
capture_inheritances(class_, files_, include=None, exclude=[], verbose=False)
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
<tr><td>default</td><td><b><Documentation docgen, 306 sec...</b</td></tr>
</tbody></table>




<table><tbody>
<tr><td>type</td><td><b>PackageDoc</b></td></tr>
<tr><td>default</td><td><b><Documentation docgen, 306 sec...</b</td></tr>
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


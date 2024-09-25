# pydoc

Python object info

Documentation is based on structure information on objects to document

created : 2024 09 14

## EMPTY

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

## Classes



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#pydoc) :black_small_square:  :black_small_square: [pydoc](pydoc---pydoc.md)</sub>

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#pydoc) :black_small_square:  :black_small_square: [Functions](pydoc---pydoc.md#functions)</sub>

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#pydoc) :black_small_square:  :black_small_square: [Functions](pydoc---pydoc.md#functions)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#pydoc) :black_small_square:  :black_small_square: [pydoc](pydoc---pydoc.md)</sub>
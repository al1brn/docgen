# DescriptionList

``` python
DescriptionList(/, *args, **kwargs)
```

Description list made

A description list is a list of Listtem

A description is coming from the following syntax in a comment:

```
title
-----
- name (type = default) : description
- name (type = default) : description
```

Only `name` is mandatory.

> [!NOTE]
> A description list for the arguments is built from the signature of a function
> and can be enriched by a 'Arguments' list in a comment. See [complete_with](pydoc-descriptionlist.md#complete_with).

#### Arguments:
- **args**
- **kwargs**

### Inherited

list.\_\_add__ :black_small_square: list.\_\_contains__ :black_small_square: list.\_\_delitem__ :black_small_square: list.\_\_eq__ :black_small_square: list.\_\_ge__ :black_small_square: list.\_\_getattribute__ :black_small_square: list.\_\_getitem__ :black_small_square: list.\_\_gt__ :black_small_square: list.\_\_iadd__ :black_small_square: list.\_\_imul__ :black_small_square: list.\_\_iter__ :black_small_square: list.\_\_le__ :black_small_square: list.\_\_len__ :black_small_square: list.\_\_lt__ :black_small_square: list.\_\_mul__ :black_small_square: list.\_\_ne__ :black_small_square: list.\_\_repr__ :black_small_square: list.\_\_reversed__ :black_small_square: list.\_\_rmul__ :black_small_square: list.\_\_setitem__ :black_small_square: list.\_\_sizeof__ :black_small_square: list.append :black_small_square: list.clear :black_small_square: list.copy :black_small_square: list.count :black_small_square: list.extend :black_small_square: list.index :black_small_square: list.insert :black_small_square: list.pop :black_small_square: list.remove :black_small_square: list.reverse :black_small_square: list.sort :black_small_square:

## Content

- [complete_with](pydoc-descriptionlist.md#complete_with)
- [get](pydoc-descriptionlist.md#get)

## Methods



----------
### complete_with()

> method

``` python
complete_with(other_list)
```

Complete a list with another list

If a list item doesn't exist, it is created
If it already exists, empty fields ([type](pydoc-listitem.md#type), [default](pydoc-listitem.md#default)and [description](pydoc-listitem.md#description))
are set with values coming from other.

This feature is used to build arguments list. 
    
``` python
def foo(arg1, arg2:int, arg3='value', arg4:float=3.14):
```

Will generate the following argument list:

````

This list can be enriched with the following list written in the function comment:


````

Which will produce the final enriched list:

````

#### Arguments:
- **other_list** : DescriptionList

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#descriptionlist) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-descriptionlist.md#methods)</sub>

----------
### get()

> method

``` python
get(name)
```

Get a list item by its name

Argument
--------
- name (str) : item name

#### Arguments:
- **name**



#### Returns:
- **ListItem** : None if not found

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#descriptionlist) :black_small_square: [Content](#content) :black_small_square: [Methods](pydoc-descriptionlist.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#descriptionlist) :black_small_square: [Content](#content) :black_small_square: [DescriptionList](pydoc-descriptionlist.md)</sub>
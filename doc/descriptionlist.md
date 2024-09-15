# DescriptionList

Description list made

A description list is a list of Listtem

A description is coming from the following syntax in a comment:

````
title
-----
- name (type = default) : description
- name (type = default) : description
```

Only `name` is mandatory.

> [!NOTE]
> A description list for the arguments is built from the signature of a function
> and can be enriched by a 'Arguments' list in a comment. See [complete_with](#complete_with).

## Content

[complete_with](#complete_with)
- [get](#get)
- [markdown](#markdown)
- [print](#print)



## Methods

----------
### complete_with

Complete a list with another list

If a list item doesn't exist, it is created
If it already exists, empty fields ([LINK ERROR: section 'type' not found](listitem.md), [LINK ERROR: section 'default ' not found](listitem.md)and [LINK ERROR: section 'description' not found](listitem.md))
are set with values coming from other.

This feature is used to build arguments list. 
    
``` python
def foo(arg1, arg2:int, arg3='value', arg4:float=3.14):
```

Will generate the following argument list:

````
Arguments
---------
- arg1
- arg2 (int)
- arg3 (='value')
- arg4 (float = 3.14)
```

This list can be enriched with the following list written in the function comment:


````
Arguments
---------
- arg1 (int) : first argument
- arg3 (str) : third argument        
```

Which will produce the final enriched list:

````
Arguments
---------
- arg1(int) : first argument
- arg2 (int)
- arg3 (str='value') : third argument 
- arg4 (float = 3.14)
```

Arguments
---------
- other_list : DescriptionList

``` python
complete_with(other_list)
```



<sub>[top](#descriptionlist) [index](index.md)</sub>



----------
### get

Get a list item by its name

Argument
--------
- name (str) : item name

Returns
-------
- ListItem : None if not found

``` python
get(name)
```



<sub>[top](#descriptionlist) [index](index.md)</sub>



----------
### markdown



``` python
markdown(title)
```



<sub>[top](#descriptionlist) [index](index.md)</sub>



----------
### print



``` python
print(title)
```



<sub>[top](#descriptionlist) [index](index.md)</sub>


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
> and can be enriched by a 'Arguments' list in a comment. See <#complete_with>.Description list made

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
> and can be enriched by a 'Arguments' list in a comment. See <#complete_with>.

## Content


- A : [append](#append)
- C : [clear](#clear) :black_small_square: [complete_with](#complete_with) :black_small_square: [copy](#copy) :black_small_square: [count](#count)
- E : [extend](#extend)
- G : [get](#get)
- I : [index](#index) :black_small_square: [insert](#insert)
- M : [markdown](#markdown)
- P : [pop](#pop) :black_small_square: [print](#print)
- R : [remove](#remove) :black_small_square: [reverse](#reverse)
- S : [sort](#sort)



## Properties

### append


> type append ( = <method 'append' of 'list' obj...)



### clear


> type clear ( = <method 'clear' of 'list' obje...)



### copy


> type copy ( = <method 'copy' of 'list' objec...)



### count


> type count ( = <method 'count' of 'list' obje...)



### extend


> type extend ( = <method 'extend' of 'list' obj...)



### index


> type index ( = <method 'index' of 'list' obje...)



### insert


> type insert ( = <method 'insert' of 'list' obj...)



### pop


> type pop ( = <method 'pop' of 'list' object...)



### remove


> type remove ( = <method 'remove' of 'list' obj...)



### reverse


> type reverse ( = <method 'reverse' of 'list' ob...)



### sort


> type sort ( = <method 'sort' of 'list' objec...)



## Methods

### complete_with

----------



``` python
complete_with(self, other_list)
```

Complete a list with another list

If a list item doesn't exist, it is created
If it already exists, empty fields (<!ListItem#type>, <!ListItem#default >and <!ListItem#description>)
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

Arguments:
- **self**
- **other_list**



### get

----------



``` python
get(self, name)
```

Get a list item by its name

Argument
--------
- name (str) : item name

Arguments:
- **self**
- **name**



Returns:
- **ListItem** : None if not found



### markdown

----------



``` python
markdown(self, title)
```



Arguments:
- **self**
- **title**



### print

----------



``` python
print(self, title)
```



Arguments:
- **self**
- **title**


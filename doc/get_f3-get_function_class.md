# get_function_class

> Bases classes: [get_function_class](get_f3-get_function_class.md)

``` python
TreeList()
```

Tree interface based on a list

This class inherits from [Tree](tree-tree.md) and list. Direct children are store in the list.

Several children can share the same key.

This implementation can be chosen when direct children can share a same key and / or when there is
a need to control the order of the children### Inherited

['#add' not found]() :black_small_square: ['#all_count' not found]() :black_small_square: ['#all_items' not found]() :black_small_square: ['#all_paths' not found]() :black_small_square: ['#all_values' not found]() :black_small_square: ['#count' not found]() :black_small_square: ['#create_path' not found]() :black_small_square: ['#depth' not found]() :black_small_square: ['#detach' not found]() :black_small_square: ['#dump' not found]() :black_small_square: ['#find' not found]() :black_small_square: ['#FromFile' not found]() :black_small_square: ['#FromInspect' not found]() :black_small_square: ['#get' not found]() :black_small_square: ['#__getitem__' not found]() :black_small_square: ['#is_top' not found]() :black_small_square: ['#__iter__' not found]() :black_small_square: ['#join_keys' not found]() :black_small_square: ['#key' not found]() :black_small_square: ['#move_to_parent' not found]() :black_small_square: ['#new' not found]() :black_small_square: ['#new_paths' not found]() :black_small_square: ['#parent' not found]() :black_small_square: ['#path' not found]() :black_small_square: ['#__setitem__' not found]() :black_small_square: ['#solve_path' not found]() :black_small_square: ['#solve_to_missing' not found]() :black_small_square: ['#__str__' not found]() :black_small_square: ['#Test' not found]() :black_small_square: ['#test' not found]() :black_small_square: ['#test_numpy' not found]() :black_small_square: ['#top' not found]() :black_small_square:

## get_function_class

- [get_child](tree-treelist.md#get_child)
- [items](tree-treelist.md#items)
- [keys](tree-treelist.md#keys)
- [remove_from_parent](tree-treelist.md#remove_from_parent)
- [set_child](tree-treelist.md#set_child)
- [values](tree-treelist.md#values)

## get_function_class



----------
### get_child()

> method

``` python
get_child(key)
```

Get a direct child by its key

#### Arguments:
- **key**

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#get_function_class) :black_small_square: [get_function_class](#get_function_class) :black_small_square: [get_function_class](get_f3-get_function_class.md#get_function_class-2)</sub>

----------
### items()

> method

``` python
items()
```

Iterate on (key, value) pais

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#get_function_class) :black_small_square: [get_function_class](#get_function_class) :black_small_square: [get_function_class](get_f3-get_function_class.md#get_function_class-2)</sub>

----------
### keys()

> method

``` python
keys()
```

Iterate on keys

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#get_function_class) :black_small_square: [get_function_class](#get_function_class) :black_small_square: [get_function_class](get_f3-get_function_class.md#get_function_class-2)</sub>

----------
### remove_from_parent()

> method

``` python
remove_from_parent()
```

Remove the section from its parent list of children

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#get_function_class) :black_small_square: [get_function_class](#get_function_class) :black_small_square: [get_function_class](get_f3-get_function_class.md#get_function_class-2)</sub>

----------
### set_child()

> method

``` python
set_child(key, child, index=None)
```

set a direct child by its key

#### Arguments:
- **key**
- **child**
- **index** ( = None)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#get_function_class) :black_small_square: [get_function_class](#get_function_class) :black_small_square: [get_function_class](get_f3-get_function_class.md#get_function_class-2)</sub>

----------
### values()

> method

``` python
values()
```

Iterate on childs

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#get_function_class) :black_small_square: [get_function_class](#get_function_class) :black_small_square: [get_function_class](get_f3-get_function_class.md#get_function_class-2)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#get_function_class) :black_small_square: [get_function_class](#get_function_class) :black_small_square: [get_function_class](get_f3-get_function_class.md)</sub>
# tdict

dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
    for k, v in iterable:
        d[k] = v
dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
    for k, v in iterable:
        d[k] = v
dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)

## Content


- A : [all_folders](#all_folders) :black_small_square: [all_items](#all_items) :black_small_square: [all_paths](#all_paths) :black_small_square: [all_values](#all_values)
- C : [clear](#clear) :black_small_square: [copy](#copy)
- D : [depth](#depth) :black_small_square: [dump](#dump)
- F : [FromFolder](#fromfolder) :black_small_square: [FromModule](#frommodule) :black_small_square: [folders](#folders) :black_small_square: [fromkeys](#fromkeys)
- G : [get](#get) :black_small_square: [get_folder](#get_folder) :black_small_square: [get_value](#get_value)
- I : [is_folder](#is_folder) :black_small_square: [is_top](#is_top) :black_small_square: [is_value](#is_value) :black_small_square: [items](#items)
- J : [join_keys](#join_keys)
- K : [keys](#keys)
- N : [name](#name) :black_small_square: [new_folder](#new_folder)
- P : [parent](#parent) :black_small_square: [path](#path) :black_small_square: [pop](#pop) :black_small_square: [popitem](#popitem)
- S : [sepa](#sepa) :black_small_square: [setdefault](#setdefault)
- T : [Test](#test) :black_small_square: [test](#test) :black_small_square: [top](#top)
- U : [update](#update)
- V : [values](#values)
- _ : [_setitem](#_setitem) :black_small_square: [_solve_path](#_solve_path)



## Properties

### clear


> type clear ( = <method 'clear' of 'dict' obje...)



### copy


> type copy ( = <method 'copy' of 'dict' objec...)



### depth


> type property ( = <property object at 0x1273c93f...)



### fromkeys


> type fromkeys ( = <built-in method fromkeys of t...)



### is_top


> type property ( = <property object at 0x1273c921...)



### name


> type property ( = <property object at 0x1273c8b3...)



### parent


> type property ( = <property object at 0x1273eae3...)



### path


> type property ( = <property object at 0x1273c8bd...)



### pop


> type pop ( = <method 'pop' of 'dict' object...)



### popitem


> type popitem ( = <method 'popitem' of 'dict' ob...)



### sepa


> type property ( = <property object at 0x1273c8c2...)



### setdefault


> type setdefault ( = <method 'setdefault' of 'dict'...)



### top


> type property ( = <property object at 0x1273c93a...)



### update


> type update ( = <method 'update' of 'dict' obj...)



## Methods

### FromFolder

----------



``` python
FromFolder(cls, path, pattern='[!._]*/*')
```

Read the content of a drive

Arguments:
- **cls**
- **path** (_str_)
- **pattern** (_str_ = [!._]*/*)



Returns:
- **tdict** : 



### FromModule

----------



``` python
FromModule(cls, module)
```



Arguments:
- **cls**
- **module**



### Test

----------



``` python
Test(cls)
```



Arguments:
- **cls**



### _setitem

----------



``` python
_setitem(self, key, value)
```

Add a key item in the dict

When the value is a **tdict**, its <#parent> and <#name> values are set to
their proper value

Raises:
- **Exception** : if the current value at key is a folder



Arguments:
- **self**
- **key** (_str_)
- **value** (_any_)



Returns:
- **value** : 



### _solve_path

----------



``` python
_solve_path(self, path)
```

Solve a path

Search for the last existing item in the tree and return a dict giving:
- folder : the last folder in the path (never None)
- key : the key of the item within this folder (never None)
- item : folder.get(key)
- remain : remaining path after the key

This method raises an error if the path leads to an non folder item and a remaining path.

If item is None, it is up to the caller to create the element, to stop its operation
or to raise an error.

Here after are the three possible results:

| item | remain | path complete | item exists
+------+--------+---------------------------------------------
| None | None   | Yes           | No
| item | None   | Yes           | Yes
| None | Yes    | No            | No, parent folder(s) neither
| item | Yes    | Imossible     | Raises an error

Raises:
- **Exception** : if a key in the path exists and is not a folder



Arguments:
- **self**
- **path** (_str_)



Returns:
- **dict** : 



### all_folders

----------



``` python
all_folders(self)
```

All folders iterator

Iterate on all folders in the folder and sub folders.

> [!NOTE] To iterates only on direct folders in this folder,
> use <#folders>

Arguments:
- **self**



Returns:
- **iterator** : 



### all_items

----------



``` python
all_items(self)
```

All items iterator

Iterate on all items in the folder and sub folders.

> [!NOTE] To iterates only on direct items in this folder,
> use <#items>

Arguments:
- **self**



Returns:
- **iterator** : 



### all_paths

----------



``` python
all_paths(self)
```

All paths iterator

Iterate on all paths in the folder and sub folders.

> [!NOTE] To iterates only on direct keys in this folder,
> use <#keys>

Arguments:
- **self**



Returns:
- **iterator** : 



### all_values

----------



``` python
all_values(self)
```

All values iterator

Iterate on all values in the folder and sub folders.

> [!NOTE] To iterates only on direct values in this folder,
> use <#values>

Arguments:
- **self**



Returns:
- **iterator** : 



### dump

----------



``` python
dump(self)
```



Arguments:
- **self**



### folders

----------



``` python
folders(self)
```

Folders iterator

Iterate on the direct folders only, not the values.

> [!NOTE] Iterates only on folders directly in this folder.
> To iterate on sub folders, use <#all_folders>

Arguments:
- **self**



Returns:
- **iterator** : 



### get

----------



``` python
get(self, name, default=None)
```

Get the object at the given path

Arguments:
- **self**
- **name** (_str_)
- **default** (_any_ = None)



Returns:
- **any** : 



### get_folder

----------



``` python
get_folder(self, name, default=None)
```

Get the folder at the given path

Raises:
- **Exception** : if an object is found and is not a folder



Arguments:
- **self**
- **name** (_str_)
- **default** (_any_ = None)



Returns:
- **tdict** : 



### get_value

----------



``` python
get_value(self, name, default=None)
```

Get the value at the given path

Raises:
- **Exception** : if an object is found and is a folder



Arguments:
- **self**
- **name** (_str_)
- **default** (_any_ = None)



Returns:
- **tdict** : 



### is_folder

----------



``` python
is_folder(item)
```

True if the argument is an instance of tdict

Arguments:
- **item** (_any_)



Returns:
- **bool** : item is an instance of tdict



### is_value

----------



``` python
is_value(item)
```

True if the argument is not an instance of tdict

Arguments:
- **item** (_any_)



Returns:
- **bool** : item is not an instance of tdict



### items

----------



``` python
items(self)
```

Items iterator

Iterate on the direct items only, not the folders.

> [!NOTE] Iterates only on items in this folder.
> To iterate on sub folders, use <#all_items>

Arguments:
- **self**



Returns:
- **iterator** : 



### join_keys

----------



``` python
join_keys(self, *keys)
```



Arguments:
- **self**
- **keys**



### keys

----------



``` python
keys(self)
```

Keys iterator

Iterate on the direct values only, not the folders.

> [!NOTE] Iterates only on values in this folder.
> To iterate on sub folders, use <#all_paths>

Arguments:
- **self**



Returns:
- **iterator** : 



### new_folder

----------



``` python
new_folder(self, name)
```

Create a new folder of the given name

Arguments:
- **self**
- **name** (_str_)



Returns:
- **tdict** : the created folder



### test

----------



``` python
test(td)
```



Arguments:
- **td**



### values

----------



``` python
values(self)
```

Values iterator

Iterate on the direct values only, not the folders.

> [!NOTE] Iterates only on values in this folder.
> To iterate on sub folders, use <#all_values>

Arguments:
- **self**



Returns:
- **iterator** : 


# Module_

Information on a moduleInformation on a module

## Content


- A : [add_member](#add_member)
- D : [document](#document)
- F : [FromObject](#fromobject)
- G : [get](#get) :black_small_square: [get_member](#get_member)
- I : [is_same_package](#is_same_package) :black_small_square: [is_top_module](#is_top_module)
- L : [LoadMe](#loadme)
- M : [meta](#meta)
- O : [obj_type](#obj_type)
- P : [PACKAGES](#packages) :black_small_square: [parse_comment](#parse_comment) :black_small_square: [print](#print)



## Properties

### PACKAGES


> type list ( = [<__main__.Module_ object at 0...)



### is_top_module


> type property ( = <property object at 0x1477b71f...)



### obj_type


> type str ( = module)



## Methods

### FromObject

----------



``` python
FromObject(cls, object, name=None, verbose=False)
```

Create an Module_ instance from a python module

> [!NOTE]
> If **name** argument is none, `object.__name__` is taken.

Arguments:
- **cls**
- **object** (_function_)
- **name** (_str_ = None)
- **verbose** ( = False)



### LoadMe

----------



``` python
LoadMe(cls)
```



Arguments:
- **cls**



### add_member

----------



``` python
add_member(self, object_)
```

Add a member

Raises:
- **AttributeError** : if called on a descriptor which has not members



Arguments:
- **self**
- **object_**



Returns:
- **Object_** : the added member



### document

----------



``` python
document(self, doc)
```



Arguments:
- **self**
- **doc**



### get

----------



``` python
get(self, prop_name, default=None)
```

Get an optional property

Arguments:
- **self**
- **prop_name** (_str_)
- **default** (_any_ = None)



Returns:
- **any** : the property or None if it doesn't exist



### get_member

----------



``` python
get_member(self, name)
```

Get a member by its name

Raises:
- **AttributeError** : if called on a descriptor which has not members



Arguments:
- **self**
- **name**



Returns:
- **Object_** : member by its name or None if not found



### is_same_package

----------



``` python
is_same_package(self, package)
```



Arguments:
- **self**
- **package**



### meta

----------



``` python
meta(self, meta_name, default=None)
```

Get a meta property

A meta property can be set in the comment with the syntax
```
 $ SET meta_name = value
```

Arguments:
- **self**
- **meta_name** (_str_)
- **default** (_any_ = None)



Returns:
- **any** : the meta property value or None if it doesn't exist



### parse_comment

----------



``` python
parse_comment(self)
```

Collect extra information from the comment

Inline commands
---------------
- $ DOC START : ignore lines above
- $ DO END : ignore lines after
- $ SET prop = 123 : pass properties to the doc generator

In addition, special lists are extracted to create <!DescriptionList>

Extracted lists
---------------
- raises
- arguments
- returns
- properties

Arguments:
- **self**



### print

----------



``` python
print(self)
```



Arguments:
- **self**


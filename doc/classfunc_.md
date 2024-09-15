# ClassFunc_

Classes and function root description

Classes and functions have arguments and raises listsClasses and function root description

Classes and functions have arguments and raises lists

## Content

[FromObject](#fromobject)
- [add_member](#add_member)
- [document](#document)
- [get](#get)
- [get_member](#get_member)
- [meta](#meta)
- [obj_type](#obj_type)
- [parse_comment](#parse_comment)
- [print](#print)



## Properties

### obj_type


> type NoneType ( = None)



## Methods

### FromObject

----------



``` python
FromObject(cls, object, name=None)
```



Arguments:
- **cls**
- **object**
- **name** ( = None)



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

#### Inline commands
- $ DOC START : ignore lines above
- $ DO END : ignore lines after
- $ SET prop = 123 : pass properties to the doc generator

In addition, special lists are extracted to create <!DescriptionList>

#### Extracted lists
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


# Property_

Information on propertyInformation on property

## Content


- A : [add_member](#add_member)
- C : [complete_with](#complete_with)
- D : [document](#document)
- F : [FromListItem](#fromlistitem) :black_small_square: [FromObject](#fromobject) :black_small_square: [FromStatic](#fromstatic)
- G : [get](#get) :black_small_square: [get_member](#get_member)
- M : [meta](#meta)
- O : [obj_type](#obj_type)
- P : [parse_comment](#parse_comment) :black_small_square: [print](#print)



## Properties

### obj_type


> type str ( = property)



## Methods

### FromListItem

----------



``` python
FromListItem(self, item)
```

Create a property from a list item

Arguments:
- **self**
- **item** (_ListItem_)



Returns:
- **Property_** : 



### FromObject

----------



``` python
FromObject(cls, object, name=None, verbose=False)
```

Create a Property_ instance from a property

> [!NOTE]
> If name is None, the name is read from fget

Arguments:
- **cls**
- **object** (_property_)
- **name** (_str_ = None)
- **verbose** ( = False)



Returns:
- **Property_** : 



### FromStatic

----------



``` python
FromStatic(cls, object, name=None)
```

Creare a Property_ instance from a static property in a module or a class

Arguments:
- **cls**
- **object**
- **name** (_str_ = None)



Returns:
- **Property_** : 



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



### complete_with

----------



``` python
complete_with(self, other)
```

Enrich the description with another one

A Property_ can be created either in properties list in a comment
or by scaning object.
This function allows to merge information coming from these two sources

Arguments:
- **self**
- **other** (_Property_)



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


# ListItem

An information line into a list

This class is used to information displayed in a single lines.

The line is intended to be displayed as `name (type = default) : description`.An information line into a list

This class is used to information displayed in a single lines.

The line is intended to be displayed as `name (type = default) : description`.

## Content

[FromOther](#fromother)
- [FromParameter](#fromparameter)
- [complete_with](#complete_with)
- [get](#get)
- [has_default](#has_default)
- [has_description](#has_description)
- [has_type](#has_type)
- [markdown](#markdown)



## Properties

### has_default


> type property ( = <property object at 0x14751ee8...)



### has_description


> type property ( = <property object at 0x147c8063...)



### has_type


> type property ( = <property object at 0x1649966b...)



### markdown


> type property ( = <property object at 0x147c8225...)



## Methods

### FromOther

----------



``` python
FromOther(cls, other)
```



Arguments:
- **cls**
- **other**



### FromParameter

----------



``` python
FromParameter(cls, param, description=None)
```

Create an instance from the python paramer description.

Arguments:
- **cls**
- **param**
- **description** ( = None)



Returns:
- **ListItem** : 



### complete_with

----------



``` python
complete_with(self, other: 'ListItem')
```

Complete with another list item.

Replace empty attributes by values coming from the other ListItem.

Arguments:
- **self**
- **other** (_ListItem_)



### get

----------



``` python
get(self, attribute, default=None)
```

Get a custom attribute value

Arguments:
- **self**
- **attribute** (_str_)
- **default** ( = None)



Returns:
- **Any** : attribute value or default if it doesn't exist


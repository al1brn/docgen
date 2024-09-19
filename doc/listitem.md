# ListItem

An information line into a list

This class is used to information displayed in a single lines.

The line is intended to be displayed as `name (type = default) : description`.An information line into a list

This class is used to information displayed in a single lines.

The line is intended to be displayed as `name (type = default) : description`.

## Content


- C : [complete_with](#complete_with)
- F : [FromParameter](#fromparameter)
- G : [get_prop](#get_prop)
- H : [has_default](#has_default) :black_small_square: [has_description](#has_description) :black_small_square: [has_type](#has_type)
- M : [markdown](#markdown)
- _ : [__delattr__](#__delattr__) :black_small_square: [__dict__](#__dict__) :black_small_square: [__dir__](#__dir__) :black_small_square: [__doc__](#__doc__) :black_small_square: [__eq__](#__eq__) :black_small_square: [__format__](#__format__) :black_small_square: [__ge__](#__ge__) :black_small_square: [__getattribute__](#__getattribute__) :black_small_square: [__getstate__](#__getstate__) :black_small_square: [__gt__](#__gt__) :black_small_square: [__hash__](#__hash__) :black_small_square: [__init_subclass__](#__init_subclass__) :black_small_square: [__le__](#__le__) :black_small_square: [__lt__](#__lt__) :black_small_square: [__module__](#__module__) :black_small_square: [__ne__](#__ne__) :black_small_square: [__new__](#__new__) :black_small_square: [__reduce__](#__reduce__) :black_small_square: [__reduce_ex__](#__reduce_ex__) :black_small_square: [__repr__](#__repr__) :black_small_square: [__setattr__](#__setattr__) :black_small_square: [__sizeof__](#__sizeof__) :black_small_square: [__str__](#__str__) :black_small_square: [__subclasshook__](#__subclasshook__) :black_small_square: [__weakref__](#__weakref__)



## Properties

### __delattr__


> type __delattr__ ( = <slot wrapper '__delattr__' of...)



### __dict__


> type mappingproxy ( = {'__module__': '__main__', '__...)



### __dir__


> type __dir__ ( = <method '__dir__' of 'object' ...)



### __doc__


> type NoneType ( = None)



### __eq__


> type __eq__ ( = <slot wrapper '__eq__' of 'obj...)



### __format__


> type __format__ ( = <method '__format__' of 'objec...)



### __ge__


> type __ge__ ( = <slot wrapper '__ge__' of 'obj...)



### __getattribute__


> type __getattribute__ ( = <slot wrapper '__getattribute_...)



### __getstate__


> type __getstate__ ( = <method '__getstate__' of 'obj...)



### __gt__


> type __gt__ ( = <slot wrapper '__gt__' of 'obj...)



### __hash__


> type __hash__ ( = <slot wrapper '__hash__' of 'o...)



### __init_subclass__


> type __init_subclass__ ( = <built-in method __init_subcla...)



### __le__


> type __le__ ( = <slot wrapper '__le__' of 'obj...)



### __lt__


> type __lt__ ( = <slot wrapper '__lt__' of 'obj...)



### __module__


> type str ( = __main__)



### __ne__


> type __ne__ ( = <slot wrapper '__ne__' of 'obj...)



### __new__


> type __new__ ( = <built-in method __new__ of ty...)



### __reduce__


> type __reduce__ ( = <method '__reduce__' of 'objec...)



### __reduce_ex__


> type __reduce_ex__ ( = <method '__reduce_ex__' of 'ob...)



### __repr__


> type __repr__ ( = <slot wrapper '__repr__' of 'o...)



### __setattr__


> type __setattr__ ( = <slot wrapper '__setattr__' of...)



### __sizeof__


> type __sizeof__ ( = <method '__sizeof__' of 'objec...)



### __subclasshook__


> type __subclasshook__ ( = <built-in method __subclasshoo...)



### __weakref__


> type __weakref__ ( = <attribute '__weakref__' of 'L...)



### has_default


> type property ( = <property object at 0x14187b10...)



### has_description


> type property ( = <property object at 0x14189270...)



### has_type


> type property ( = <property object at 0x14187a11...)



### markdown


> type property ( = <property object at 0x141891e9...)



## Methods

### FromParameter

----------



``` python
FromParameter(param, description=None)
```

Create an instance from the python paramer description.

Arguments:
- **param**
- **description** ( = None)



Returns:
- **ListItem** : 



### __str__

----------



``` python
__str__(self)
```

Return str(self).

Arguments:
- **self**



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



### get_prop

----------



``` python
get_prop(self, attribute, default=None)
```

Get a custom attribute value

Arguments:
- **self**
- **attribute** (_str_)
- **default** ( = None)



Returns:
- **Any** : attribute value or default if it doesn't exist


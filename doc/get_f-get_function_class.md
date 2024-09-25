# get_function_class

``` python
SectionTag(section)
```

Utility class

This utilty class is just intended to allow string compararison
syntax when testing a tag:

``` python
if section.tag == "MyTag":
    pass

# is equivalent to
if section.has_tag("MyTag"):
    pass
```

#### Arguments:
- **section**
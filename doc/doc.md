# Doc

Markdown documentation package

This class is a subclass of <!Section> and is to top section of the
hierarchy of sections.

It provides <#hooks> facility for documentation post treatment such as text replacement
or links resolution.Markdown documentation package

This class is a subclass of <!Section> and is to top section of the
hierarchy of sections.

It provides <#hooks> facility for documentation post treatment such as text replacement
or links resolution.

## Content


- A : [add_module](#add_module) :black_small_square: [add_page](#add_page) :black_small_square: [add_section](#add_section) :black_small_square: [anchor](#anchor) :black_small_square: [append](#append)
- D : [depth](#depth) :black_small_square: [depth_in_page](#depth_in_page)
- F : [file_name](#file_name)
- G : [get_content](#get_content) :black_small_square: [get_create_section](#get_create_section) :black_small_square: [get_documentation](#get_documentation) :black_small_square: [get_module](#get_module) :black_small_square: [get_page](#get_page) :black_small_square: [get_section](#get_section) :black_small_square: [get_toc](#get_toc)
- H : [has_content](#has_content) :black_small_square: [has_toc](#has_toc) :black_small_square: [homonyms_count](#homonyms_count)
- I : [is_module](#is_module) :black_small_square: [is_page](#is_page) :black_small_square: [is_top](#is_top) :black_small_square: [iteration](#iteration)
- L : [link_to](#link_to)
- M : [module](#module) :black_small_square: [module_path](#module_path)
- P : [page](#page)
- S : [set_hook](#set_hook) :black_small_square: [solve_hooks](#solve_hooks) :black_small_square: [solve_links](#solve_links) :black_small_square: [sort](#sort)
- T : [top](#top)
- W : [write](#write) :black_small_square: [write_header](#write_header) :black_small_square: [write_navigation](#write_navigation) :black_small_square: [write_source](#write_source)
- _ : [__delattr__](#__delattr__) :black_small_square: [__dict__](#__dict__) :black_small_square: [__dir__](#__dir__) :black_small_square: [__doc__](#__doc__) :black_small_square: [__eq__](#__eq__) :black_small_square: [__format__](#__format__) :black_small_square: [__ge__](#__ge__) :black_small_square: [__getattribute__](#__getattribute__) :black_small_square: [__getstate__](#__getstate__) :black_small_square: [__gt__](#__gt__) :black_small_square: [__hash__](#__hash__) :black_small_square: [__init_subclass__](#__init_subclass__) :black_small_square: [__le__](#__le__) :black_small_square: [__lt__](#__lt__) :black_small_square: [__module__](#__module__) :black_small_square: [__ne__](#__ne__) :black_small_square: [__new__](#__new__) :black_small_square: [__reduce__](#__reduce__) :black_small_square: [__reduce_ex__](#__reduce_ex__) :black_small_square: [__repr__](#__repr__) :black_small_square: [__setattr__](#__setattr__) :black_small_square: [__sizeof__](#__sizeof__) :black_small_square: [__str__](#__str__) :black_small_square: [__subclasshook__](#__subclasshook__) :black_small_square: [__weakref__](#__weakref__)



## Properties

### __delattr__


> type __delattr__ ( = <slot wrapper '__delattr__' of...)



### __dict__


> type mappingproxy ( = {'__module__': 'mddoc', '__ini...)



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


> type str ( = mddoc)



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


> type __weakref__ ( = <attribute '__weakref__' of 'S...)



### anchor


> type property ( = <property object at 0x14189261...)



### depth


> type property ( = <property object at 0x141892de...)



### depth_in_page


> type property ( = <property object at 0x14189379...)



### file_name


> type property ( = <property object at 0x1418932e...)



### has_content


> type property ( = <property object at 0x14189130...)



### has_toc


> type property ( = <property object at 0x141892a7...)



### homonyms_count


> type property ( = <property object at 0x14189239...)



### is_module


> type property ( = <property object at 0x14189284...)



### is_page


> type property ( = <property object at 0x1418909f...)



### is_top


> type property ( = <property object at 0x141890db...)



### module


> type property ( = <property object at 0x1418928e...)



### module_path


> type property ( = <property object at 0x141891f3...)



### page


> type property ( = <property object at 0x141892f7...)



### top


> type property ( = <property object at 0x14189040...)



## Methods

### __str__

----------



``` python
__str__(self)
```

Return str(self).

Arguments:
- **self**



### add_module

----------



``` python
add_module(self, module, title, comment=None, **kwargs)
```

Add a module section

Arguments:
- **self**
- **module** (_str_)
- **title** (_str_)
- **comment** (_str_ = None)
- **kwargs**



Returns:
- **Section** : module section



### add_page

----------



``` python
add_page(self, title, comment=None, **kwargs)
```

Add a page section

Arguments:
- **self**
- **title** (_str_)
- **comment** (_str_ = None)
- **kwargs**



Returns:
- **Section** : page section



### add_section

----------



``` python
add_section(self, title, comment=None, **kwargs)
```

Add a section

Arguments:
- **self**
- **title** (_str_)
- **comment** (_str_ = None)
- **kwargs**



Returns:
- **Section** : module section



### append

----------



``` python
append(self, section)
```

Append a new section.

This is were the owner is set in the child section.

> [!NOTE]
> If the property <#sort_sections> is True, the section is inserted in alphabetical order

Arguments:
- **self**
- **section** (_Section_)



Returns:
- **section** : the added section



### get_content

----------



``` python
get_content(self)
```

Returns the text to write in the page

A page is built by:
- joining section and comment
- optionnally joining a table of content
- recursively joining the content of the children

Arguments:
- **self**



Returns:
- **str** : section and sub section content



### get_create_section

----------



``` python
get_create_section(self, title, comment=None, **kwargs)
```

Get an existing section or create a new one

> [!NOTE]
> Contrary to <#get_section>, this method searchs the section only
> in the direct children, not in all the hierarchy.

Arguments:
- **self**
- **title** (_str_)
- **comment** (_str_ = None)
- **kwargs**



Returns:
- **Section** : module section



### get_documentation

----------



``` python
get_documentation(self, create_files=True)
```

Build and write the whole documentation

The documentation is returned as a dictionary of pages keyed
by their file name.

Files are actually written if:
- create_files is True
- top section as not None <!Doc#doc_folder> attribute

Arguments:
- **self**
- **create_files** ( = True)



Returns:
- **dict** : documentation files content



### get_module

----------



``` python
get_module(self, title, condition=None, **kwargs)
```

Get a module Section matching some conditions

Basically call <#get_section> while addinf a supplementary condition
on the attribute <#is_module>:
    
``` python
return self.get_section(..., is_module=True, ...)
```

Arguments:
- **self**
- **title** (_str_)
- **condition** (_function_ = None)
- **kwargs**



Returns:
- **Section** : the first module section matching the conditions, None if not found



### get_page

----------



``` python
get_page(self, title, condition=None, **kwargs)
```

Get a page Section matching some conditions

Basically call <#get_section> while addinf a supplementary condition
on the attribute <#is_module>:
    
``` python
return self.get_section(..., is_page=True, ...)
```

Arguments:
- **self**
- **title** (_str_)
- **condition** (_function_ = None)
- **kwargs**



Returns:
- **Section** : the first page section matching the conditions, None if not found



### get_section

----------



``` python
get_section(self, title=None, condition=None, **kwargs)
```

Get a section matching conditons

There are several possible conditions:
- Section <#title> matches the argument **title**
- The function **condition** returns True
- Sections properties match the keyword arguments **kwargs**

This methods call <#iteration> with the following function (simplified version)

``` python
def check_section(section):
    
    # In this simplified version, we supposed all the conditions
    # are required
    
    if not section.title == title and condition(section):
        return False
    
    for k, v in kwargs.items():
        if getattr(section, k) != v:
            return False
        
    # Only matches
    return True

# main
return self.iteration(check_section)
```

> [!NOTE]
> See <!get_module> or <!get_page> for an example of use

Arguments:
- **self**
- **title** (_str_ = None)
- **condition** (_function_ = None)
- **kwargs**



Returns:
- **Section** : the first section matching the conditions, None if not found



### get_toc

----------



``` python
get_toc(self, title='Content', level=2)
```

Build the text for table of content

> [!NOTE]
> The toc is inserted directly after the <#comment> and not as a
> specific section

Arguments:
- **self**
- **title** (_str_ = Content)
- **level** (_int_ = 2)



Returns:
- **str** : markdown text for the table of content



### iteration

----------



``` python
iteration(self, func, *args, include_top=True)
```

Iterate on the section and child sections

This method calls the function **func** on the section hierarchy.

The **func** template must be:
    
```python
def func(section, *args):
````

The following rules apply:
- The function is not called on `self` if **include_top*$ is False
- The function is not called on the child sections if it returns 'NO CHILDREN'
  when call on `self` (see <#get_toc>)
- The iteration stops if the function **func** return True. It returns
  the section for which it is the case (see <#get_section> for instance)

Arguments:
- **self**
- **func** (_function_)
- **args**
- **include_top** (_bool_ = True)



Returns:
- **Section** : section for which the function return True, None otherwise



### link_to

----------



``` python
link_to(self, absolute=True, title=None)
```

returns the link to this section

> [!NOTE]
> The result could be wrong if sections with the same title are later inserted above this section

Arguments:
- **self**
- **absolute** ( = True)
- **title** ( = None)
- **Absolute** (_bool_ = True) : include file name, only the anchor otherwise



Returns:
- **str** : link in md format `[title](file.md#anchor)`



### set_hook

----------



``` python
set_hook(self, expr, repl)
```

Replace a regular expression by as substitution string

Hooks are applied to the documentation at compilation time.

``` python
# Instance of [!TOKEN] will be replaced by the substitution text.

proj.set_hook(r"\[!TOKEN\]", "substitution text")
```

Due to the piece of code above, the anchor `[!TOKEN]` is replaced here: **[!TOKEN]**

> [!NOTE]
> Text embedded in a _source code_ zone is not replaced

A function can be passed rather than a string as for `re.sub(expr, repl, text)`.

Here, the passed function can accept a second positional argument if a reference
to the current section is required:

``` python
def replace(match_obj, section):
    # section is the Section instance where the replacement occurs
    pass
```

> [!NOTE]
> By default, a hook is used to define links between pages based on the
> syntax : `<!Section title#Sub section title>` which is converted in <!Project#set_hook>.

Arguments:
- **self**
- **expr** (_str_)
- **repl**



### solve_hooks

----------



``` python
solve_hooks(self, include_links=True)
```

Solve all the hooks for a section.

Arguments:
- **self**
- **include_links** (_bool_ = True)



### solve_links

----------



``` python
solve_links(self, ignore_source=False)
```

Solve user links into MD links.

Syntax of user link is made of three parts is
`<!Page title#Section title"Display string>`:
- _Page title_ : title of the page to link to. If no given,
  an intra page link is returned
- _Section title_ : title of the section within the page, or
  within the current page if first parameter is not given
- _Display string_ : display string of the link, _Section title_ or
  _Page title_ is taken in this order
 
> [!NOTE]
> If a link can't be solved, the links contains an error message.

> [!IMPORTANT]
> <#_anchor> and <#is_page> must have been set correctly before solving the links.

Arguments:
- **self**
- **ignore_source** (_bool_ = False)



### sort

----------



``` python
sort(self)
```

Sort the child sections

Arguments:
- **self**



### write

----------



``` python
write(self, text)
```

Append text to the header comment

Arguments:
- **self**
- **text** (_str_)



### write_header

----------



``` python
write_header(self, level, title, text)
```

Write a section in the text stream

This method write markdonw text corresponding to a header followed by text.

> [!NOTE]
> This method doesn't create a section in the hierarchy, contrary to <#add_section>

Arguments:
- **self**
- **level** (_int_)
- **title** (_str_)
- **text** (_str_)



### write_navigation

----------



``` python
write_navigation(self)
```

Write navigation bar

Arguments:
- **self**



### write_source

----------



``` python
write_source(self, source)
```

Append source code to the header comment

Arguments:
- **self**
- **source** (_str_)


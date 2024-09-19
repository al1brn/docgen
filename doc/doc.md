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
- D : [demo](#demo) :black_small_square: [depth](#depth) :black_small_square: [depth_in_page](#depth_in_page) :black_small_square: [dump](#dump) :black_small_square: [dump_pages](#dump_pages) :black_small_square: [dump_structure](#dump_structure)
- F : [file_name](#file_name)
- G : [get_content](#get_content) :black_small_square: [get_create_section](#get_create_section) :black_small_square: [get_documentation](#get_documentation) :black_small_square: [get_module](#get_module) :black_small_square: [get_page](#get_page) :black_small_square: [get_section](#get_section) :black_small_square: [get_toc](#get_toc)
- H : [has_content](#has_content) :black_small_square: [has_toc](#has_toc) :black_small_square: [homonyms_count](#homonyms_count)
- I : [is_module](#is_module) :black_small_square: [is_page](#is_page) :black_small_square: [is_top](#is_top) :black_small_square: [iteration](#iteration)
- L : [link_to](#link_to)
- M : [module](#module) :black_small_square: [module_path](#module_path)
- P : [page](#page) :black_small_square: [print](#print)
- S : [set_hook](#set_hook) :black_small_square: [solve_hooks](#solve_hooks) :black_small_square: [solve_links](#solve_links) :black_small_square: [solve_section_links](#solve_section_links) :black_small_square: [sort](#sort)
- T : [TestStructure](#teststructure) :black_small_square: [test_doc](#test_doc) :black_small_square: [test_dump](#test_dump) :black_small_square: [test_file](#test_file) :black_small_square: [test_get](#test_get) :black_small_square: [top](#top)
- W : [write](#write) :black_small_square: [write_header](#write_header) :black_small_square: [write_navigation](#write_navigation) :black_small_square: [write_source](#write_source)



## Properties

### anchor


> type property ( = <property object at 0x1276d594...)



### depth


> type property ( = <property object at 0x1273b792...)



### depth_in_page


> type property ( = <property object at 0x1273b7b0...)



### file_name


> type property ( = <property object at 0x1276d58a...)



### has_content


> type property ( = <property object at 0x1276d585...)



### has_toc


> type property ( = <property object at 0x1276d580...)



### homonyms_count


> type property ( = <property object at 0x1276d58f...)



### is_module


> type property ( = <property object at 0x1276d44f...)



### is_page


> type property ( = <property object at 0x1276d422...)



### is_top


> type property ( = <property object at 0x1273ca70...)



### module


> type property ( = <property object at 0x1276d576...)



### module_path


> type property ( = <property object at 0x1276d57b...)



### page


> type property ( = <property object at 0x1273b7a1...)



### top


> type property ( = <property object at 0x1273ca84...)



## Methods

### TestStructure

----------



``` python
TestStructure(cls)
```



Arguments:
- **cls**



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



### demo

----------



``` python
demo()
```



### dump

----------



``` python
dump(self, depth=3, max_lines=10)
```



Arguments:
- **self**
- **depth** ( = 3)
- **max_lines** ( = 10)



### dump_pages

----------



``` python
dump_pages(self)
```



Arguments:
- **self**



### dump_structure

----------



``` python
dump_structure(self, depth=1)
```



Arguments:
- **self**
- **depth** ( = 1)



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



### print

----------



``` python
print(self, text_max=100)
```



Arguments:
- **self**
- **text_max** ( = 100)



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



### solve_section_links

----------



``` python
solve_section_links(self, section, ignore_source=False)
```



Arguments:
- **self**
- **section**
- **ignore_source** ( = False)



### sort

----------



``` python
sort(self)
```

Sort the child sections

Arguments:
- **self**



### test_doc

----------



``` python
test_doc()
```



### test_dump

----------



``` python
test_dump()
```



### test_file

----------



``` python
test_file(cls, file_name=None, doc_folder=None)
```



Arguments:
- **cls**
- **file_name** ( = None)
- **doc_folder** ( = None)



### test_get

----------



``` python
test_get()
```



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


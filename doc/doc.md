# Doc

Markdown documentation package

This class is a subclass of [Section](section.md) and is to top section of the
hierarchy of sections.

It provides [LINK ERROR: section 'hooks' not found]() facility for documentation post treatment such as text replacement
or links resolution.

Properties
----------
- doc_folder (str) : target folder for documentation files
- hooks (list) : list of regular expressions and hook function to apply on the documentation

Arguments
---------
- title (str) : documentation title, displayed as title of index.md file
- doc_folder (str) : target folder for documentation

``` python
Doc(title, doc_folder)
```



## Content

[demo](#demo)
- [set_hook](#set_hook)
- [solve_hooks](#solve_hooks)
- [solve_links](#solve_links)
- [solve_section](#solve_section)
- [solve_section_links](#solve_section_links)
- [test_file](#test_file)



## Methods

----------
### demo



``` python
demo()
```



<sub>[top](#doc) [index](index.md)</sub>



----------
### set_hook

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
> syntax : `<!Section title#Sub section title>` which is converted in [LINK ERROR: page 'Project' not found]().

Arguments
---------
    - expr (str) : RegEx expression
    - repl (str or function) : replacement string or function

``` python
set_hook(expr, repl)
```



<sub>[top](#doc) [index](index.md)</sub>



----------
### solve_hooks

Solve all the hooks for a section.

Arguments
---------
- include_links (bool = True) : solve also the links

``` python
solve_hooks(include_links=True)
```



<sub>[top](#doc) [index](index.md)</sub>



----------
### solve_links

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
> [LINK ERROR: section '_anchor' not found]() and [LINK ERROR: section 'is_page' not found]() must have been set correctly before solving the links.
 
Arguments
---------
- ignore_source (bool = False)) : Do not extract source before solving (already done)

``` python
solve_links(ignore_source=False)
```



<sub>[top](#doc) [index](index.md)</sub>



----------
### solve_section



``` python
solve_section(section)
```



<sub>[top](#doc) [index](index.md)</sub>



----------
### solve_section_links



``` python
solve_section_links(section, ignore_source=False)
```



<sub>[top](#doc) [index](index.md)</sub>



----------
### test_file



``` python
test_file(file_name=None, doc_folder=None)
```



<sub>[top](#doc) [index](index.md)</sub>


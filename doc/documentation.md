# Documentation

Project Documentation

Properties
----------
- doc_folder (str) : target folder for documentation files
- source_folder (str) : root folder for files
- parsed (dict) : dictionary of loaded and parsed filed
- hooks (list) : list of regular expressions and hook function to apply on the documentation

Arguments
---------
- title (str) : documentation title, displayed as title of index.md file
- doc_folder (str) : target folder for documentation
- source_folder (str) : root folder where to load files from

``` python
Documentation(title, doc_folder, source_folder=None)
```



## Content


- C : [classes_list](#classes_list)
- D : [docgen_documentation](#docgen_documentation) :black_small_square: [document_folder](#document_folder)
- F : [file_info](#file_info) :black_small_square: [files](#files) :black_small_square: [files_content](#files_content) :black_small_square: [files_iter](#files_iter) :black_small_square: [files_list](#files_list) :black_small_square: [files_search](#files_search)
- G : [get_class](#get_class)
- H : [hide](#hide) :black_small_square: [hide_classes](#hide_classes)
- L : [load_file](#load_file) :black_small_square: [load_folder](#load_folder) :black_small_square: [load_source](#load_source)
- S : [set_hook](#set_hook) :black_small_square: [solve_hooks](#solve_hooks) :black_small_square: [solve_links](#solve_links) :black_small_square: [solve_section](#solve_section) :black_small_square: [solve_section_links](#solve_section_links)
- T : [test_file](#test_file)



## Properties

----------
### classes_list

List of classes

Returns
-------
- list : list of class dictionaries

- getter 


<sub>[top](#documentation) [index](index.md)</sub>



----------
### files

Dictionary of parsed files.

Returns
-------
- dict

- getter 


<sub>[top](#documentation) [index](index.md)</sub>



## Methods

----------
### docgen_documentation



``` python
docgen_documentation()
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### document_folder



``` python
document_folder(folder_key)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### file_info



``` python
file_info(key)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### files_content



``` python
files_content()
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### files_iter



``` python
files_iter(f, *args, **kwargs)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### files_list



``` python
files_list(name_only=True, **kwargs)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### files_search



``` python
files_search(**kwargs)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### get_class



``` python
get_class(class_name)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### hide



``` python
hide(class_)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### hide_classes

Undocument classes

Properties and methods of undocumented classes are capture by inherited classes

``` python
hide_classes(classes, verbose=True)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### load_file

Enrich the reference doc by parsing source files.

All the files with `.py` extension are parsed.

Arguments
---------
- file_key (str) : file key in [files](#files)
- file_name (str) : file path

``` python
load_file(file_key, file_name, verbose=False)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### load_folder

Enrich the reference doc by parsing source files.

> [!CAUTION]
> if [LINK ERROR: section 'source_folder' not found]() is not None, folder is relative to it

All the files with `.py` extension are parsed.

Arguments
---------
- folder (str) : absolute folder or folder relative to [LINK ERROR: section 'source_folder' not found]() if not None

Returns
-------
- self

``` python
load_folder(folder, verbose=True)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### load_source

Add a source code.

The source code is parsed and the resulting dict is stored in the [LINK ERROR: page '' not found]() dict.

Arguments
---------
- key (str) : source file key
- text (str) : the source code

Returns
-------
- Section

``` python
load_source(key, text)
```



<sub>[top](#documentation) [index](index.md)</sub>



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



<sub>[top](#documentation) [index](index.md)</sub>



----------
### solve_hooks

Solve all the hooks for a section.

Arguments
---------
- include_links (bool = True) : solve also the links

``` python
solve_hooks(include_links=True)
```



<sub>[top](#documentation) [index](index.md)</sub>



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



<sub>[top](#documentation) [index](index.md)</sub>



----------
### solve_section



``` python
solve_section(section)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### solve_section_links



``` python
solve_section_links(section, ignore_source=False)
```



<sub>[top](#documentation) [index](index.md)</sub>



----------
### test_file



``` python
test_file(file_name=None, doc_folder=None)
```



<sub>[top](#documentation) [index](index.md)</sub>


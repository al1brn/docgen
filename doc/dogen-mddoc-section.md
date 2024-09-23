# Section



``` python
Section(title, comment=None, **parameters)
```

Tree interface based on a list

This class inherits from [Tree](dogen-tree3-tree.md) and list. Direct children are store in the list.

Several children can share the same key.

This implementation can be chosen when direct children can share a same key and / or when there is
a need to control the order of the children

#### Arguments:
- **title** (_str_) : section title
- **comment** (_str_ = None) : text to display just below the section title
- **parameters**



### Inherited

list.\_\_add__ :black_small_square: list.\_\_contains__ :black_small_square: list.\_\_delitem__ :black_small_square: list.\_\_eq__ :black_small_square: list.\_\_ge__ :black_small_square: list.\_\_getattribute__ :black_small_square: list.\_\_gt__ :black_small_square: list.\_\_iadd__ :black_small_square: list.\_\_imul__ :black_small_square: list.\_\_le__ :black_small_square: list.\_\_len__ :black_small_square: list.\_\_lt__ :black_small_square: list.\_\_mul__ :black_small_square: list.\_\_ne__ :black_small_square: list.\_\_repr__ :black_small_square: list.\_\_reversed__ :black_small_square: list.\_\_rmul__ :black_small_square: list.\_\_sizeof__ :black_small_square: list.append :black_small_square: list.clear :black_small_square: list.copy :black_small_square: list.extend :black_small_square: list.index :black_small_square: list.insert :black_small_square: list.pop :black_small_square: list.remove :black_small_square: list.reverse :black_small_square: list.sort :black_small_square: 

## Content

- **A** : [add](dogen-mddoc-section.md#add) :black_small_square: [all_count](dogen-mddoc-section.md#all_count) :black_small_square: [all_items](dogen-mddoc-section.md#all_items) :black_small_square: [all_paths](dogen-mddoc-section.md#all_paths) :black_small_square: [all_values](dogen-mddoc-section.md#all_values) :black_small_square: [anchor](dogen-mddoc-section.md#anchor)
- **C** : [chapter](dogen-mddoc-section.md#chapter) :black_small_square: [chapter_prefix](dogen-mddoc-section.md#chapter_prefix) :black_small_square: [count](dogen-mddoc-section.md#count) :black_small_square: [create_path](dogen-mddoc-section.md#create_path)
- **D** : [depth](dogen-mddoc-section.md#depth) :black_small_square: [depth_in_page](dogen-mddoc-section.md#depth_in_page) :black_small_square: [DOT](dogen-mddoc-section.md#dot)
- **F** : [file_name](dogen-mddoc-section.md#file_name) :black_small_square: [find](dogen-mddoc-section.md#find) :black_small_square: [FromFile](dogen-mddoc-section.md#fromfile) :black_small_square: [FromInspect](dogen-mddoc-section.md#frominspect)
- **G** : [get](dogen-mddoc-section.md#get) :black_small_square: [get_child](dogen-mddoc-section.md#get_child) :black_small_square: [get_content](dogen-mddoc-section.md#get_content) :black_small_square: [get_create_section](dogen-mddoc-section.md#get_create_section) :black_small_square: [get_documentation](dogen-mddoc-section.md#get_documentation) :black_small_square: [get_toc](dogen-mddoc-section.md#get_toc) :black_small_square: [get_toc_sections](dogen-mddoc-section.md#get_toc_sections)
- **H** : [has_content](dogen-mddoc-section.md#has_content) :black_small_square: [has_toc](dogen-mddoc-section.md#has_toc) :black_small_square: [homonyms_count](dogen-mddoc-section.md#homonyms_count)
- **I** : [insert_toc](dogen-mddoc-section.md#insert_toc) :black_small_square: [is_chapter](dogen-mddoc-section.md#is_chapter) :black_small_square: [is_hidden](dogen-mddoc-section.md#is_hidden) :black_small_square: [is_page](dogen-mddoc-section.md#is_page) :black_small_square: [is_text](dogen-mddoc-section.md#is_text) :black_small_square: [is_top](dogen-mddoc-section.md#is_top) :black_small_square: [is_transparent](dogen-mddoc-section.md#is_transparent) :black_small_square: [items](dogen-mddoc-section.md#items)
- **J** : [join_keys](dogen-mddoc-section.md#join_keys)
- **K** : [keys](dogen-mddoc-section.md#keys)
- **L** : [link_to](dogen-mddoc-section.md#link_to)
- **N** : [navigation_md](dogen-mddoc-section.md#navigation_md) :black_small_square: [new](dogen-mddoc-section.md#new) :black_small_square: [new_chapter](dogen-mddoc-section.md#new_chapter) :black_small_square: [new_page](dogen-mddoc-section.md#new_page) :black_small_square: [new_paths](dogen-mddoc-section.md#new_paths)
- **P** : [page](dogen-mddoc-section.md#page) :black_small_square: [path](dogen-mddoc-section.md#path)
- **S** : [SEP](dogen-mddoc-section.md#sep) :black_small_square: [set_child](dogen-mddoc-section.md#set_child) :black_small_square: [solve_path](dogen-mddoc-section.md#solve_path) :black_small_square: [solve_to_missing](dogen-mddoc-section.md#solve_to_missing)
- **T** : [top](dogen-mddoc-section.md#top)
- **V** : [values](dogen-mddoc-section.md#values)
- **W** : [write](dogen-mddoc-section.md#write) :black_small_square: [write_header](dogen-mddoc-section.md#write_header) :black_small_square: [write_source](dogen-mddoc-section.md#write_source)



## Properties

### all_count

> TYPE: **int**

Total number of children

### anchor

> TYPE: **str** , section anchor

The anchor of this section within the page

### chapter

> TYPE: **Section** , chapter this section belongs to

Get the chapter this section belongs to

> [!CAUTION]
> Since a chapter returns self, a misuse could lead to infinite recurrence loop

### chapter_prefix

> TYPE: **str** , chapter path with - char as separator

Get the prefix to use in the file names of pages in this chapter

To avoid to long names, prefix uses the 5 first chars plus a number
if collision

### count

> TYPE: **int**

Number of direct children, equivalent to `len(self)`

### depth

> TYPE: **int**

Distance to the top (0 for top section)

### depth_in_page

> TYPE: **int** , Distance to the page(0 for page sections)

Distance to the page

### DOT

> TYPE: **str**<br> DEFAULT: **.**



### file_name

> TYPE: **str** , file name

File name were to write the page

The file name is built by joining [chapter_prefix](#chapter_prefix) with the name of section.

> [!NOTE]
> top chapter returns "index.md"

### has_content

> TYPE: **?**



### has_toc

> TYPE: **?**



### homonyms_count

> TYPE: **int** , number of above sections sharing the same title

Count the number of sections have the same title

This number is used to suffix the title anchor if needed.

> [!NOTE]
> The number of homonymes is count up the the section iself, not after

### is_chapter

> TYPE: **?**



### is_hidden

> TYPE: **?**



### is_page

> TYPE: **?**



### is_text

> TYPE: **?**



### is_top

> TYPE: **bool**

True if owner is None

### is_transparent

> TYPE: **?**



### navigation_md

> TYPE: **?**

Get navigation markdown

Navigation bar is built with ['#navigation' not found]() list

### page

> TYPE: **Section** , page this section belongs to

Get the page this section belongs to

> [!CAUTION]
> Since a page returns self, a misuse could lead to infinite recurrence loop

### path

> TYPE: **str**

Node path up to the top node

### SEP

> TYPE: **str**<br> DEFAULT: **/**



### top

> TYPE: **Section**

Get the topmost section

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Section](#section)</sub>



## Methods

----------
### add



``` python
add(path, node, complete_path=False)
```

Add a new node at the path

This method calls [set_child](#set_child).


#### Arguments:
- **path** (_str_) : the path where to locate the node
- **node** (_Tree_) : the node to set at the path
- **complete_path** ( = False)



#### Returns:
- **Tree** : the node argument



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### all_items



``` python
all_items(include_self=False)
```

All items iterator

Iterate on all items in the folder and sub folders.


#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### all_paths



``` python
all_paths(include_self=False)
```

All paths iterator

Iterate on all paths in the folder and sub folders.


#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### all_values



``` python
all_values(include_self=False)
```

All values iterator

Iterate on all values in the folder and sub folders.


#### Arguments:
- **include_self** ( = False)



#### Returns:
- **iterator** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### create_path



``` python
create_path(*keys)
```

Create nodes in a path

Nodes are create by calling [new](#new) method.


#### Arguments:
- **keys** (_list of strs_) : key forming the path to create



#### Returns:
- **Tree** : last created node



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### find



``` python
find(*keys, first=False, **criteria)
```

Find one or more keys in the tree.


#### Arguments:
- **keys** (_list of strs_) : the keys to look for
- **first** (_boolean_ = False) : stop on the first match an return the found node
- **criteria** : search the node with attributes match keyword arguments



#### Returns:
- **Tree** : on single tree if first is Trur



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### FromFile



``` python
FromFile(folder, pattern='*.*', ignore=('.*', '_*'))
```

Read the content of a drive

This methods shows how to use method [add](#add) to recursively load folder files and sub folders.


#### Arguments:
- **folder** (_str_) : folder to load
- **pattern** (_str or tuple of strs_ = *.*) : file selection
- **ignore** (_str or tuple of strs_ = ('.*', '_*')) : files starting by one of the characters in the string are ignored



#### Returns:
- **Tree** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### FromInspect



``` python
FromInspect(obj)
```

Load python module

Load module and module members using inspect


#### Arguments:
- **obj** (_any_) : object to inspect



#### Returns:
- **Tree** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### get



``` python
get(path, default=None)
```

Get the node at path


#### Arguments:
- **path** (_str_) : the node path
- **default** (_Tree_ = None) : the node to return if the path is not solved



#### Returns:
- **Tree** : 



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### get_child



``` python
get_child(key)
```

Get a direct child by its key


#### Arguments:
- **key**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### get_content



``` python
get_content()
```

Returns the text to write in the page

A page is built by:
- joining section and comment
- optionnally joining a table of content
- recursively joining the content of the children


#### Returns:
- **str** : section and sub section content



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### get_create_section



``` python
get_create_section(title, comment=None, **parameters)
```

Get an existing section or create a new one

> [!NOTE]
> Contrary to ['#get_section' not found](), this method searchs the section only
> in the direct children, not in all the hierarchy.


#### Arguments:
- **title** (_str_) : section title
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : chapter section



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### get_documentation



``` python
get_documentation(create_files=True)
```

Build and write the whole documentation

The documentation is returned as a dictionary of pages keyed
by their file name.

Files are actually written if:
- create_files is True
- top section as not None [impossible to find the section 'doc_folder' in page 'Doc'](page.file_name) attribute


#### Arguments:
- **create_files** ( = True)



#### Returns:
- **dict** : documentation files content



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### get_toc



``` python
get_toc(flat=None, sort=None, max_length=10, max_depth=2)
```

Build the list of toc items

The methods return a list of paris giving:
- the level of the item
- the MD links


#### Arguments:
- **flat** (_bool_ = None) : toc is a flat list or hierarchical
- **sort** (_bool_ = None) : sort the list (force **flat** if True)
- **max_length** (_int_ = 10) : use alphabetical list if the number of items in the toc is greater thant this value
- **max_depth** (_int_ = 2) : max relative depth for a hierarchical toc



#### Returns:
- **list** : one entry per line



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### get_toc_sections



``` python
get_toc_sections(flat=None)
```

Return the dictionary of sections being part of the toc

If **flat** is True, the search for sub sections in the toc continues
within sections in the toc.

If **flat** is False, the exploration stops as soon as a section is
in the toc.


#### Arguments:
- **flat** (_bool_ = None) : returns the sections without hierarchy, use default if None



#### Returns:
- **list** : sections in the table of content of the page



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### insert_toc



``` python
insert_toc()
```

Insert the toc section


#### Returns:
- **Section** : None if no toc



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### items



``` python
items()
```

Iterate on (key, value) pais


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### join_keys



``` python
join_keys(*keys)
```

Join keys to form a path

Joins the keys with the key separator avoiding double separators: `join_keys("AAA", "BBB")`
and `join_keys("AAA/", "BBB")` will both give `"AAA/BBB"`.


#### Arguments:
- **keys**



#### Returns:
- **str** : key joined by key separator



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### keys



``` python
keys()
```

Iterate on keys


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### link_to



``` python
link_to(target=None, /, title=None)
```

Returns the link to a target from this section

> [!NOTE]
> Make sure to call this method once the full document structure is terminated

**target** can be one of the following keywords:
- INDEX : index page of the documentation
- TOP : top of the page
- TOC : table of content in the page
- UP : parent section

If **target** is a string other than one of the keywords above, it is considered
as the title of the section to reach. Since sections can share the same name,
the section is searched in the following order:
- in the child sections, including child pages
- in this page
- as a page title
- in the whole documentation


#### Arguments:
- **target** (_str_ = None) : target of the link, self if None
- **title** (_str_ = None) : link title, use self.['#title' not found]() if None



#### Returns:
- **str** : link in md format `[title](file.md#anchor)`



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### new



``` python
new(title, comment=None, **parameters)
```

Add a section


#### Arguments:
- **title** (_str_) : section title
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : created section



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### new_chapter



``` python
new_chapter(chapter, comment=None, **parameters)
```

Add a chapter section


#### Arguments:
- **chapter** (_str_) : name of the chapter to create
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : chapter section



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### new_page



``` python
new_page(title, comment=None, **parameters)
```

Add a page section


#### Arguments:
- **title** (_str_) : section title
- **comment** (_str_ = None) : section comment
- **parameters**



#### Returns:
- **Section** : page section



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### new_paths



``` python
new_paths(*paths, complete_path=False, **kwargs)
```

Create several nodes defined by their path

Basically, this method call [new](#new) for each provided path.

The following rules apply:            
- paths starting by '/' are created at top level
- paths starting by '.' are created at the *last created node* level
- paths starting by '..' are created at parent level of *last created node* level
- otherwise, nodes are created at at the node level

``` python
node = tree.new("MyNode")
node.new_paths("AAA", "BBB", "./under BBB", "../after 'under BBB'", "/After MyNode")
# - MyNode
#   - AAA
#   - BBB
#     - under BBB
#     - after 'under BBB'
# - After MyNode
```


#### Arguments:
- **paths** (_list of str_) : the paths of the nodes to create
- **complete_path** (_bool_ = False) : create intermediary nodes in paths
- **kwargs** : default constructor arguments when creating intermediary is required



#### Returns:
- **Tree** : the created child



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### set_child



``` python
set_child(key, child, index=None)
```

set a direct child by its key


#### Arguments:
- **key**
- **child**
- **index** ( = None)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### solve_path



``` python
solve_path(path, complete_path=False)
```

Solve a path

Returns the node corresponding to the path.

If it doesn't exist, two cases are possible:
- only the last key in the path is missing: the methods return the parent
  and the missing key
- an intermediary node is missing: the methods raises an error or creates
  the missing nodes depending on the arguments **complete_path**.
  
> [!NOTE]
> Missing nodes in the path are created with method [create_path](#create_path)


#### Raises:
- **PathError** : if the path can't be solved up to the last, or last but one



#### Arguments:
- **path** (_str_) : the path to solve
- **complete_path** (_bool_ = False) : create missing nodes (but the last one) if necessary



#### Returns:
- **Tree** : (found node, None) or (parent node, missing key)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### solve_to_missing



``` python
solve_to_missing(path)
```

Solve a path to missing keys

Solve a path, return the existing node and the list of non existing keys.


#### Raises:
- **PathError** : if path is incorrect



#### Arguments:
- **path** (_str_) : path to solve



#### Returns:
- **node** : last existing node, list of missing keys



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### values



``` python
values()
```

Iterate on childs


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### write



``` python
write(text)
```

Append text to the header comment


#### Arguments:
- **text** (_str_) : the text to write



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### write_header



``` python
write_header(level, title, text)
```

Write a section in the text stream

This method write markdonw text corresponding to a header followed by text.

> [!NOTE]
> This method doesn't create a section in the hierarchy, contrary to ['#add_section' not found]()


#### Arguments:
- **level** (_int_) : header level
- **title** (_str_) : header title
- **text** (_str_) : text



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### write_source



``` python
write_source(source)
```

Append source code to the header comment


#### Arguments:
- **source** (_str_) : source code to append



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#section) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>


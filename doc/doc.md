# Doc



``` python
Doc(title, comment=None)
```

Markdown documentation package

This class is a subclass of [Section](section.md) and is to top section of the
hierarchy of sections.

It provides [hooks](#hooks) facility for documentation post treatment such as text replacement
or links resolution.


#### Arguments:
- **title** (_str_) : documentation title, displayed as title of index.md file
- **comment** ( = None)



### Inherited

list.\_\_add__ :black_small_square: list.\_\_contains__ :black_small_square: list.\_\_delitem__ :black_small_square: list.\_\_eq__ :black_small_square: list.\_\_ge__ :black_small_square: list.\_\_getattribute__ :black_small_square: list.\_\_gt__ :black_small_square: list.\_\_iadd__ :black_small_square: list.\_\_imul__ :black_small_square: list.\_\_le__ :black_small_square: list.\_\_len__ :black_small_square: list.\_\_lt__ :black_small_square: list.\_\_mul__ :black_small_square: list.\_\_ne__ :black_small_square: list.\_\_repr__ :black_small_square: list.\_\_reversed__ :black_small_square: list.\_\_rmul__ :black_small_square: list.\_\_sizeof__ :black_small_square: list.append :black_small_square: list.clear :black_small_square: list.copy :black_small_square: list.extend :black_small_square: list.index :black_small_square: list.insert :black_small_square: list.pop :black_small_square: list.remove :black_small_square: list.reverse :black_small_square: list.sort :black_small_square: 

## Content

- **A** : [add](doc.md#add) :black_small_square: [all_count](doc.md#all_count) :black_small_square: [all_items](doc.md#all_items) :black_small_square: [all_paths](doc.md#all_paths) :black_small_square: [all_values](doc.md#all_values) :black_small_square: [anchor](doc.md#anchor)
- **C** : [chapter](doc.md#chapter) :black_small_square: [chapter_prefix](doc.md#chapter_prefix) :black_small_square: [count](doc.md#count) :black_small_square: [create_documentation](doc.md#create_documentation) :black_small_square: [create_path](doc.md#create_path)
- **D** : [depth](doc.md#depth) :black_small_square: [detach](doc.md#detach) :black_small_square: [DOT](doc.md#dot)
- **F** : [file_name](doc.md#file_name) :black_small_square: [find](doc.md#find) :black_small_square: [FromFile](doc.md#fromfile) :black_small_square: [FromInspect](doc.md#frominspect)
- **G** : [get](doc.md#get) :black_small_square: [get_child](doc.md#get_child) :black_small_square: [get_content](doc.md#get_content) :black_small_square: [get_create_section](doc.md#get_create_section) :black_small_square: [get_toc](doc.md#get_toc) :black_small_square: [get_toc_sections](doc.md#get_toc_sections)
- **H** : [has_content](doc.md#has_content) :black_small_square: [has_toc](doc.md#has_toc) :black_small_square: [header_depth](doc.md#header_depth) :black_small_square: [homonyms_count](doc.md#homonyms_count) :black_small_square: [hooks](doc.md#hooks)
- **I** : [insert_toc](doc.md#insert_toc) :black_small_square: [is_chapter](doc.md#is_chapter) :black_small_square: [is_hidden](doc.md#is_hidden) :black_small_square: [is_page](doc.md#is_page) :black_small_square: [is_text](doc.md#is_text) :black_small_square: [is_top](doc.md#is_top) :black_small_square: [is_transparent](doc.md#is_transparent) :black_small_square: [items](doc.md#items)
- **J** : [join_keys](doc.md#join_keys)
- **K** : [keys](doc.md#keys)
- **L** : [link_to](doc.md#link_to)
- **M** : [move_to_parent](doc.md#move_to_parent)
- **N** : [navigation_md](doc.md#navigation_md) :black_small_square: [new](doc.md#new) :black_small_square: [new_chapter](doc.md#new_chapter) :black_small_square: [new_page](doc.md#new_page) :black_small_square: [new_paths](doc.md#new_paths) :black_small_square: [new_sections_group](doc.md#new_sections_group) :black_small_square: [new_tag_group](doc.md#new_tag_group)
- **P** : [page](doc.md#page) :black_small_square: [path](doc.md#path)
- **R** : [remove_from_parent](doc.md#remove_from_parent)
- **S** : [SEP](doc.md#sep) :black_small_square: [set_child](doc.md#set_child) :black_small_square: [set_hook](doc.md#set_hook) :black_small_square: [solve_hooks](doc.md#solve_hooks) :black_small_square: [solve_links](doc.md#solve_links) :black_small_square: [solve_path](doc.md#solve_path) :black_small_square: [solve_to_missing](doc.md#solve_to_missing)
- **T** : [top](doc.md#top)
- **V** : [values](doc.md#values)
- **W** : [write](doc.md#write) :black_small_square: [write_header](doc.md#write_header) :black_small_square: [write_source](doc.md#write_source)



## Properties

### all_count


<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>

Total number of children


### anchor


<table><tbody>
<tr><td>type</td><td><b>str</b> , section anchor</td></tr>
</tbody></table>

The anchor of this section within the page


### chapter


<table><tbody>
<tr><td>type</td><td><b>Section</b> , chapter this section belongs to</td></tr>
</tbody></table>

Get the chapter this section belongs to

> [!CAUTION]
> Since a chapter returns self, a misuse could lead to infinite recurrence loop


### chapter_prefix


<table><tbody>
<tr><td>type</td><td><b>str</b> , chapter path with - char as separator</td></tr>
</tbody></table>

Get the prefix to use in the file names of pages in this chapter

To avoid to long names, prefix uses the 5 first chars plus a number
if collision


### count


<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>

Number of direct children, equivalent to `len(self)`


### depth


<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>

Distance to the top (0 for top section)


### DOT


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>.</b</td></tr>
</tbody></table>




### file_name


<table><tbody>
<tr><td>type</td><td><b>str</b> , file name</td></tr>
</tbody></table>

File name were to write the page

The file name is built by joining [chapter_prefix](#chapter_prefix) with the name of section.

> [!NOTE]
> top chapter returns "index.md"


### has_content


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




### has_toc


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




### header_depth


<table><tbody>
<tr><td>type</td><td><b>int</b> , distance to the page, excluding transparent parents and taking shift into account</td></tr>
</tbody></table>

Header depth relatively to the page

The header depth doesn't include transparent parents. It aloso take
the [depth_shift](section.md#depth_shift) into account


### homonyms_count


<table><tbody>
<tr><td>type</td><td><b>int</b> , number of above sections sharing the same title</td></tr>
</tbody></table>

Count the number of sections have the same title

This number is used to suffix the title anchor if needed.

> [!NOTE]
> The number of homonymes is count up the the section iself, not after


### hooks


<table><tbody>
<tr><td>type</td><td><b>list</b></td></tr>
<tr><td>default</td><td><b>None</b</td></tr>
</tbody></table>

list of regular expressions and hook function to apply on the documentation


### is_chapter


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




### is_hidden


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




### is_page


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




### is_text


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




### is_top


<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

True if owner is None


### is_transparent


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>




### navigation_md


<table><tbody>
<tr><td>type</td><td><b>?</b></td></tr>
</tbody></table>

Get navigation markdown

Navigation bar is built with [navigation](section.md#navigation) list


### page


<table><tbody>
<tr><td>type</td><td><b>Section</b> , page this section belongs to</td></tr>
</tbody></table>

Get the page this section belongs to

> [!CAUTION]
> Since a page returns self, a misuse could lead to infinite recurrence loop


### path


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

Node path up to the top node


### SEP


<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
<tr><td>default</td><td><b>/</b</td></tr>
</tbody></table>




### top


<table><tbody>
<tr><td>type</td><td><b>Section</b></td></tr>
</tbody></table>

Get the topmost section


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Doc](#doc)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### create_documentation



``` python
create_documentation(folder=None)
```

Build and the whole documentation

The documentation is returned as a dictionary of pages keyed
by their file name.

If argument **folder** is not None, the documentation files are written
in it.


#### Arguments:
- **folder** (_str_ = None) : folder where to write the documentation files



#### Returns:
- **dict** : documentation files content



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### detach



``` python
detach()
```

Detach the section from its parent children

> [!IMPORANT]
> This method calls the abstract method [remove_from_parent](#remove_from_parent) which must perform
> the actual removal from the parent's list of children.


#### Returns:
- **Tree** : self



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### get_child



``` python
get_child(key)
```

Get a direct child by its key


#### Arguments:
- **key**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### insert_toc



``` python
insert_toc()
```

Insert the toc section


#### Returns:
- **Section** : None if no toc



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### items



``` python
items()
```

Iterate on (key, value) pais


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### keys



``` python
keys()
```

Iterate on keys


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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
- **title** (_str_ = None) : link title, use self.[title](section.md#title) if None



#### Returns:
- **str** : link in md format `[title](file.md#anchor)`



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### move_to_parent



``` python
move_to_parent(new_parent, new_key=None)
```

Change the position of a node from one parent to another

This methods basically calls [detach](#detach) and then [add](#add).


Returns
- Tree : self


#### Arguments:
- **new_parent** (_Tree_) : where to locate the node
- **new_key** (_str_ = None) : new key, uses the current key is None



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### new_sections_group



``` python
new_sections_group(title, sections, **parameters)
```

Create a section from a list of sections

The section is created only if the list has items.

The sections are move to the newly created section using [move_to_parent](tree-tree.md#move_to_parent).


#### Arguments:
- **title** (_str_) : title of the section to create
- **sections** (_list of Sections_) : the section to move into the created section
- **parameters** : parameters for the section to create



#### Returns:
- **Section** : the created section



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### new_tag_group



``` python
new_tag_group(tag, **parameters)
```

Create a section grouping all the sub sections having a given tag

The section is created only if sections have the tag

The group is created by calling [new_sections_group](#new_sections_group).


#### Arguments:
- **tag** (_str_) : tag to group sections
- **parameters** : parameters for the section to create



#### Returns:
- **Section** : the created section



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### remove_from_parent



``` python
remove_from_parent()
```

Remove the section from its parent list of children


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### set_hook



``` python
set_hook(expr, repl)
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
> syntax : `<!Section title#Sub section title>` which is converted in [page 'Project' not found in '!Project#set_hook']().


#### Arguments:
- **expr** (_str_) : RegEx expression - repl (str or function) : replacement string or function
- **repl**



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### solve_hooks



``` python
solve_hooks(include_links=True)
```

Solve all the hooks for a section.


#### Arguments:
- **include_links** (_bool_ = True) : solve also the links



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### solve_links



``` python
solve_links(ignore_source=False)
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
> ['#_anchor' not found]() and [is_page](#is_page) must have been set correctly before solving the links.


#### Arguments:
- **ignore_source** (_bool_ = False) : Do not extract source before solving (already done)



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### values



``` python
values()
```

Iterate on childs


<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### write



``` python
write(text)
```

Append text to the header comment


#### Arguments:
- **text** (_str_) : the text to write



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



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



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>



----------
### write_source



``` python
write_source(source)
```

Append source code to the header comment


#### Arguments:
- **source** (_str_) : source code to append



<sub>:arrow_right: [index](index.md) :black_small_square: [top](#doc) :black_small_square: [Content](#content) :black_small_square: [Methods](#methods)</sub>

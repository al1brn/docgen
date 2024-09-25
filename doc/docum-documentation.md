# Documentation

``` python
Documentation(top_section=None)
```

Documentation package

A documentation is made of a top [Section](docum-section.md) and provides documentation level
methods and properties

It provides [hooks](docum-documentation.md#hooks) facility for documentation post treatment such as text replacement
or links resolution.

#### Arguments:
- **top_section** (_Section_ = None) : documentation content

## Content

- [create_documentation](docum-documentation.md#create_documentation)
- [hooks](docum-documentation.md#hooks)
- [set_hook](docum-documentation.md#set_hook)
- [solve_hooks](docum-documentation.md#solve_hooks)
- [solve_section_links](docum-documentation.md#solve_section_links)

## Properties



### hooks

> _type_: **list**
>

list of (regular expressions, hook function) pairs to apply on the documentation

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#documentation) :black_small_square: [Content](#content) :black_small_square: [Documentation](docum-documentation.md)</sub>

## Methods



----------
### cook()

> method

``` python
cook()
```

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#documentation) :black_small_square: [Content](#content) :black_small_square: [Methods](docum-documentation.md#methods)</sub>

----------
### create_documentation()

> method

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

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#documentation) :black_small_square: [Content](#content) :black_small_square: [Methods](docum-documentation.md#methods)</sub>

----------
### set_hook()

> method

``` python
set_hook(expr, repl)
```

Replace a regular expression by as substitution string

Hooks are applied to the documentation at cooking time.

``` python
# Instance of [!TOKEN] will be replaced by the substitution text.

doc.set_hook(r"\[!TOKEN\]", "substitution text")
```

Due to the piece of code above, the anchor `[!TOKEN]` is replaced here: **[!TOKEN]**

> [!tIP]
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
> This mechanism is used to solve links using the syntax `<!page#section " title>`

#### Arguments:
- **expr** (_str_) : RegEx expression - repl (str or function) : replacement string or function
- **repl**

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#documentation) :black_small_square: [Content](#content) :black_small_square: [Methods](docum-documentation.md#methods)</sub>

----------
### solve_hooks()

> method

``` python
solve_hooks()
```

Solve all the hooks for a section.

> [!NOTE]
> This method also solve links

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#documentation) :black_small_square: [Content](#content) :black_small_square: [Methods](docum-documentation.md#methods)</sub>

----------
### solve_section_links()

> method

``` python
solve_section_links(section, ignore_source=False)
```

Solve the links of a section

Syntax of user link is made of three parts is
`<!Page title#Section title"Display string>`:
- _Page title_ : title of the page to link to. If no given,
  an intra page link is returned
- _Section title_ : title of the section within the page, or
  within the current page if first parameter is not given
- _Display string_ : display string of the link, _Section title_ or
  _Page title_ is taken in this order
 
> [!NOTE]
> If all parts are optional, at least a _page title_ or a _section title_ is required

> [!NOTE]
> If a link can't be solved, the links contains an error message and this error
  message is displayed in the console

#### Arguments:
- **section** (_Section_) : section to handle
- **ignore_source** (_bool_ = False) : do not try to extract source code before operation

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#documentation) :black_small_square: [Content](#content) :black_small_square: [Methods](docum-documentation.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#documentation) :black_small_square: [Content](#content) :black_small_square: [Documentation](docum-documentation.md)</sub>
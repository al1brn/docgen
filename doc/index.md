# docgen

This module generates a simple but yet acceptable project documentation package
for a python package.

Documentation files are generated in markdown format which can be used on GitHub.

## Classes

### Tree Structure

Documentation is structured in a tree hierarchy : documentation / chapters / pages / sections / ...

For this purpose, a generic reusable Tree interface is written:
- [Tree](tree-tree.md#tree) : root class providing base methods, such as iterators on the whole structure
- [TreeDict](tree-treedict.md#treedict) : implementation of the [Tree](tree-tree.md#tree) interface on a dict
- [TreeList](tree-treelist.md#treelist) : implementation of the [Tree](tree-tree.md#tree) interface on a list
- [TreeChain](tree-treechain.md#treechain) : implementation of the [Tree](tree-tree.md#tree) interface using chaining between peer nodes

### Section

A [Section](docum-section.md#section) is the base class for the documentation. It is based on [TreeDict](tree-treedict.md#treedict).

A [Section](docum-section.md#section) is basically a [title](docum-section.md#title), a text (called [comment](docum-section.md#comment)) and child sections.

Parameters control the appearance of the section.

The parameters can be set within the [comment](docum-section.md#comment) using a dedicated syntax.

### Documentation

[Documentation](docum-documentation.md#documentation) class is to create the documentation files from a tree of [Section](docum-section.md#section)s.

Before creating the documentation files, the documentation is "[cooked](docum-documentation.md#cook)" to perform
the following operations:
- Restructure the documentation according parameters
- Insert tables of contents
- Solve the links
- Apply custome hooks

### Python documentation

['PyDocumentation' not found]() is a documentation which is initialized by inspecting
a python package.

It uses classes based on [Section](docum-section.md#section):
- [ObjectSection](pydoc-objectsection.md#objectsection)
- [PropertySection](pydoc-propertysection.md#propertysection)
- [FunctionSection](pydoc-functionsection.md#functionsection)
- [ClassSection](pydoc-classsection.md#classsection)
- [ModuleSection](pydoc-modulesection.md#modulesection)

## Sample

The following example show how this documentation is generated:
    
``` python
pass
````



Creation : 2024 09 14
Update   : 2024 09 25

## Content

- [documentation](docum---documentation.md#documentation)
  - [Documentation](docum-documentation.md#documentation)
  - [Section](docum-section.md#section)
  - [SectionTag](docum-sectiontag.md#sectiontag)
  - [title_to_anchor](docum---documentation.md#title_to_anchor)
  - [title_to_file_name](docum---documentation.md#title_to_file_name)
- [parser](parse---parser.md#parser)
  - [Text](parse-text.md#text)
  - [capture_inheritance](parse---parser.md#capture_inheritance)
  - [capture_inheritances](parse---parser.md#capture_inheritances)
  - [clean_python](parse---parser.md#clean_python)
  - [del_margin](parse---parser.md#del_margin)
  - [extract_lists](parse---parser.md#extract_lists)
  - [extract_source](parse---parser.md#extract_source)
  - [extract_strings](parse---parser.md#extract_strings)
  - [parse_files](parse---parser.md#parse_files)
  - [parse_file_source](parse---parser.md#parse_file_source)
  - [parse_list_line](parse---parser.md#parse_list_line)
  - [parse_meta_comment](parse---parser.md#parse_meta_comment)
  - [replace_source](parse---parser.md#replace_source)
  - [replace_strings](parse---parser.md#replace_strings)
- [pydoc](pydoc---pydoc.md#pydoc)
  - [ClassSection](pydoc-classsection.md#classsection)
  - [DescriptionList](pydoc-descriptionlist.md#descriptionlist)
  - [FunctionSection](pydoc-functionsection.md#functionsection)
  - [ListItem](pydoc-listitem.md#listitem)
  - [ModuleSection](pydoc-modulesection.md#modulesection)
  - [ObjectSection](pydoc-objectsection.md#objectsection)
  - [PropertySection](pydoc-propertysection.md#propertysection)
- [tree](tree---tree.md#tree)
  - [PathError](tree-patherror.md#patherror)
  - [Tree](tree-tree.md#tree)
  - [TreeChain](tree-treechain.md#treechain)
  - [TreeDict](tree-treedict.md#treedict)
  - [TreeIterator](tree-treeiterator.md#treeiterator)
  - [TreeList](tree-treelist.md#treelist)

## Modules



- [documentation](docum---documentation.md#documentation)
- [parser](parse---parser.md#parser)
- [pydoc](pydoc---pydoc.md#pydoc)
- [tree](tree---tree.md#tree)

<sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [docgen](index.md#docgen) :black_small_square: [Content](index.md#content) :black_small_square: [docgen](index.md#docgen)</sub>
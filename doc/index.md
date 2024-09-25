# docgen

This module generates a simple but yet acceptable project documentation package
for a python package.

Documentation files are generated in markdown format which can be used on GitHub.

## Classes

### Tree Structure

Documentation is structured in a tree hierarchy : documentation / chapters / pages / sections / ...

For this purpose, a generic reusable Tree interface is written:
- [Tree](tree-tree.md) : root class providing base methods, such as iterators on the whole structure
- [TreeDict](tree-treedict.md) : implementation of the [Tree](tree-tree.md) interface on a dict
- [TreeList](tree-treelist.md) : implementation of the [Tree](tree-tree.md) interface on a list
- [TreeChain](tree-treechain.md) : implementation of the [Tree](tree-tree.md) interface using chaining between peer nodes

### Section

A [Section](docum-section.md) is the base class for the documentation. It is based on [TreeDict](tree-treedict.md).

A [Section](docum-section.md) is basically a [title](docum-section.md#title), a text (called [comment](docum-section.md#comment)) and child sections.

Parameters control the appearance of the section.

The parameters can be set within the [comment](docum-section.md#comment) using a dedicated syntax.

### Documentation

[Documentation](docum-documentation.md) class is to create the documentation files from a tree of [Section](docum-section.md)s.

Before creating the documentation files, the documentation is "[cooked](docum-documentation.md#cook)" to perform
the following operations:
- Restructure the documentation according parameters
- Insert tables of contents
- Solve the links
- Apply custome hooks

### Python documentation

[Python documentation](index.md) is a documentation which is initialized by inspecting
a python package.

It uses classes based on [Section](docum-section.md):
- [ObjectSection](pydoc-objectsection.md)
- [PropertySection](pydoc-propertysection.md)
- [FunctionSection](pydoc-functionsection.md)
- [ClassSection](pydoc-classsection.md)
- [ModuleSection](pydoc-modulesection.md)

## Sample

The following example show how this documentation is generated:
    
``` python
pass
````



Creation : 2024 09 14
Update   : 2024 09 25

## Content

- [documentation](docum---documentation.md)
  - [Documentation](docum-documentation.md)
  - [Section](docum-section.md)
  - [title_to_anchor](docum---documentation.md#title_to_anchor)
  - [title_to_file_name](docum---documentation.md#title_to_file_name)
- [parser](parse---parser.md)
  - [Text](parse-text.md)
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
- [pydoc](pydoc---pydoc.md)
  - [ClassSection](pydoc-classsection.md)
  - [DescriptionList](pydoc-descriptionlist.md)
  - [FunctionSection](pydoc-functionsection.md)
  - [ListItem](pydoc-listitem.md)
  - [ModuleSection](pydoc-modulesection.md)
  - [ObjectSection](pydoc-objectsection.md)
  - [PropertySection](pydoc-propertysection.md)
  - [capture_inheritance](pydoc---pydoc.md#capture_inheritance)
  - [capture_inheritances](pydoc---pydoc.md#capture_inheritances)
- [tree](tree---tree.md)
  - [PathError](tree-patherror.md)
  - [Tree](tree-tree.md)
  - [TreeChain](tree-treechain.md)
  - [TreeDict](tree-treedict.md)
  - [TreeIterator](tree-treeiterator.md)
  - [TreeList](tree-treelist.md)

## Modules



- [documentation](docum---documentation.md)
- [parser](parse---parser.md)
- [pydoc](pydoc---pydoc.md)
- [tree](tree---tree.md)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#docgen) :black_small_square: [Content](#content) :black_small_square: [docgen](index.md)</sub>
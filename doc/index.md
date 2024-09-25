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
- [parser](parse---parser.md)
- [pydoc](pydoc---pydoc.md)
- [tree](tree---tree.md)

## Modules



- [documentation](docum---documentation.md)
- [parser](parse---parser.md)
- [pydoc](pydoc---pydoc.md)
- [tree](tree---tree.md)

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#docgen) :black_small_square: [Content](#content) :black_small_square: [docgen](index.md)</sub>
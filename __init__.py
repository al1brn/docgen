#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 07:41:35 2024

@author: alain

$ DOC START

This module generates a simple but yet acceptable project documentation package
for a python package.

Documentation files are generated in markdown format which can be used on GitHub.

## Classes

### Tree Structure

Documentation is structured in a tree hierarchy : documentation / chapters / pages / sections / ...

For this purpose, a generic reusable Tree interface is written:
- <!Tree> : root class providing base methods, such as iterators on the whole structure
- <!TreeDict> : implementation of the <!Tree> interface on a dict
- <!TreeList> : implementation of the <!Tree> interface on a list
- <!TreeChain> : implementation of the <!Tree> interface using chaining between peer nodes

### Section

A <!Section> is the base class for the documentation. It is based on <!TreeDict>.

A <!Section> is basically a <!Section#title>, a text (called <!Section#comment>) and child sections.

Parameters control the appearance of the section.

The parameters can be set within the <!Section#comment> using a dedicated syntax.

### Documentation

<!Documentation> class is to create the documentation files from a tree of <!Section>s.

Before creating the documentation files, the documentation is "<!Documentation#cook" cooked>" to perform
the following operations:
- Restructure the documentation according parameters
- Insert tables of contents
- Solve the links
- Apply custome hooks

### Python documentation

<!PyDocumentation "Python documentation> is a documentation which is initialized by inspecting
a python package.

It uses classes based on <!Section>:
- <!ObjectSection>
- <!PropertySection>
- <!FunctionSection>
- <!ClassSection>
- <!ModuleSection>

## Sample

The following example show how this documentation is generated:
    
``` python
pass
````

$ DOC toc_max_depth = 1

$ DOC STOP

Creation : 2024 09 14
Update   : 2024 09 25
"""

from .parser import del_margin, Text, extract_strings, replace_strings, extract_source, replace_source
from .tree import Tree, TreeDict, TreeList, TreeChain, TreeIterator, PathError
from .documentation import Section, Documentation
from .packagedoc import ObjectSection, PropertySection, FunctionSection, ClassSection, ModuleSection, PackageDoc

from .packagedoc import TestClass





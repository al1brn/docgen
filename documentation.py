#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 08:33:58 2024

@author: alain

$ DOC NOT transparent

"""

from pathlib import Path
import re
import itertools
import inspect

#import sys
#sys.path.append(str(Path(__file__).parents[1]))
#sys.path.append(str(Path(__file__).parents[0]))

from parser import parse_meta_comment, del_margin, extract_source, replace_source
from tree import TreeList

# =============================================================================================================================
# Utilities

def under_to_md(title):
    expr = r"\b(?P<under>_+)(?P<word>\w*)\b"
    return re.sub(expr, lambda m: '\\_'*len(m.group("under")) + m.group("word"), title)

def title_to_file_name(title):
    """ Get the file name from the title
    
    Arguments
    ---------
    - title (str) : title
    
    Returns
    -------
    - str : file name (file.md)
    """
    return f"{title.lower().replace(' ', '_')}.md"

def title_to_anchor(title):
    """ Convert the title into markdown anchor
    
    Arguments
    ---------
    - title (str) : title
    
    Returns
    -------
    - str : anchor
    """
    return title.lower().replace(' ', '_')

# =============================================================================================================================
# Base section


class Section(TreeList):
    
    TEXT    = 0
    PAGE    = 1
    CHAPTER = 2
    
    def __init__(self, title, comment=None, tag=None, **parameters):
        """ Document section
        
        Project documentation is made of **pages** organized in **chapters**.
        
        The documentation is based on the versatile class <!Section> which can be:
        - a text section in a page
        - a documentation page
        - a chapter
        - the whole documentation itself
        
        A <!Section> is basically a list of **sub sections** with a header <!Section#comment>.
        
        Properties
        ----------
        - title (str) : section title
        - comment (str) : text to display just below the section title
        - sort_sections (bool or str = False) : sort sections in alphabetical order when added (case sensitive if 'CASE')
        - hidden (bool) : hide this section
        - ignore_if_empty (bool) : don't display the section if it has no content
        - top_bar (str = None or '-') : char to use to display an horizontal bar before the section 
        - depth_shift (int = 0) : value to add to its depth for its header level in the final documentation, see <#header_depth>
        - is_chapter : the section is a chapter
        - is_page : the section is a page
        - is_text : the section is text (neither a page nor a chapter)
        - is_hidden : the section, and its sub sections, are ignored
        - is_transparent : the section is not displayed by itself, its content are attached to its parent
        - transparent (bool = False) : force <#is_transparent>
        - in_toc (bool) : put this section in its page table of content
        - has_toc : (for page only) the page must display a table of content section
        - has_content : the section has a not empty comment or has sections with content
        - toc (bool = False) : insert a toc
        - toc_title (str = 'Content') : name of the toc (if any)
        - toc_flat (bool = False) : flat toc (if any)
        - toc_sort (bool = False) : sorted toc (if any)
        - toc_depth_shift (int = 0) : toc section <#depth_shift> (if any)
        - toc_max_length (int = 10) : maximum number of entries in a flat toc before indexing by initial
        - is_toc (bool = False) : this section is the toc, don't create a new one
        - navigation (list = None) : bottom navigation bar content
        - tags (set = empty set) : a set of tags 
        - user_props (dict = {}) : properties defined by user with $ DOC syntax
        - _linked (bool = False) : the section is targeted by at least one link
        
        Arguments
        ---------
        - title (str) : section title
        - comment (str) : text to display just below the section title
        - tags (set of strs) : tags to set
        - parameters : initial values for properties
        """        
        self.parent    = None
        self._rupture  = Section.TEXT
        
        self.children = []
        
        # Header content
        self.title   = title
        self.comment = del_margin(comment)
        
        # Default parameters
        
        self.sort_sections   = False
        self.in_toc          = False
        self.hidden          = False # Force is_hidden
        self.transparent     = False # Force is_transparent
        self.ignore_if_empty = True
        self.top_bar         = None
        self.depth_shift     = 0
        self._linked         = False
        
        self.toc             = False
        self.is_toc          = False
        self.toc_title       = 'Content'
        self.toc_sort        = False
        self.toc_flat        = False
        self.toc_max_length  = 10
        self.toc_depth_shift = 0
        
        self.navigation      = None

        self.user_props    = {}
        
        # Tags
        
        if tag is None:
            self.tags = set()
        elif isinstance(tag, str):
            self.tags = set((tag,))
        else:
            self.tags = set(tag)
        
        # Parameters customization
        
        for name, value in parameters.items():
            setattr(self, name, value)
            
        # Parse comment can also overrides parameters
        
        self.parse_comment()

    def __str__(self):
        stype   = "P" if self.is_page else " "
        if self.is_chapter:
            stype = "C"
        if self.is_top:
            stype = "T"
        shidden = "!" if self.is_hidden  else " "
            
        return f"<{self.depth} {shidden}{stype} {self.title}>"

    # =============================================================================================================================
    # Custom properties

    def user_prop(self, name, default=None):
        """ Get a user defined property
        
        User can can define property with $ DOC SET property syntax
        within source comment
        
        Arguments
        ---------
        - name (str) : property name
        - default (any = None) : default if not defined
        
        Returns
        -------
        - any
        """        
        return self.user_props.get(name, default)
    
    def parse_comment(self):
        
        self.comment, props = parse_meta_comment(self.comment)
        
        for name, value in props.items():
            if hasattr(self, name):
                setattr(self, name, value)
                
            self.user_props[name] = value

    # =============================================================================================================================
    # Flags
    
    @property
    def is_displayed(self):
        """ Does the section appear in the doc
        
        Returns False if the section if <#is_hidden>.
        
        Otherwise, it returns False if it is empty and <#ignore_if_empty> is set.
        
        Returns
        -------
        - True : if the section is to be displayed
        """
        if self.is_hidden:
            if self._linked:
                print(f"CAUTION: Section '{self.title}' is hidden but there are links pointing to it.")
            return False
        
        if self._linked:
            return True
        
        if self.ignore_if_empty and self.comment is None and self.count == 0:
            return False
        
        return True
    
    @property
    def is_chapter(self):
        return self.is_top or self._rupture == Section.CHAPTER

    @property
    def is_page(self):
        return self.is_chapter or self._rupture == Section.PAGE
    
    @property
    def is_text(self):
        if self.is_top:
            return False
        else:
            return self._rupture == Section.TEXT
        
    @property
    def is_hidden(self):
        if self.is_top:
            return False
        else:
            return self.hidden
    
    @property
    def is_transparent(self):
        if self.is_top:
            return False
        
        if self.transparent:
            return True
        
        # A chapter is transparent if it doesn't have comment nor text sections
        
        if self.is_chapter:
        
            if self.comment is not None:
                return False
        
            for section in self.values():
                if section.is_text and section.has_content:
                    return False
            
            return True
        
        return False
    
    @property
    def has_content(self):
        if self.is_hidden:
            return False
        
        if self.comment is not None:
            return True
        
        if not self.ignore_if_empty:
            return True
        
        child_iter = self.all_values()
        for section in child_iter:
            if section.is_hidden:
                child_iter.no_child()
                continue
            
            if section.is_transparent:
                continue
            
            if section.is_page:
                if section.has_content and section.in_toc:
                    return True
                child_iter.no_child()
                
            elif section.has_content:
                return True
            
        return False
    
    @property
    def has_toc(self):
        if not self.is_page:
            return False
        
        if self.hidden:
            return False
        
        if not self.toc:
            return False
        
        child_iter = self.all_values()
        for section in child_iter:
            if section.is_hidden:
                child_iter.no_child()
                continue
            
            if section.is_transparent:
                continue
            
            if section.has_content and section.in_toc:
                return True
            
            if section.is_page:
                child_iter.no_child()
            
        return False
    
    # =============================================================================================================================
    # Plan items
    
    @property
    def chapter(self):
        """ Get the chapter this section belongs to
        
        > [!CAUTION]
        > Since a chapter returns self, a misuse could lead to infinite recurrence loop
        
        Returns
        -------
        - Section : chapter this section belongs to
        """
        return self if self.is_chapter else self.parent.chapter
        
    
    @property
    def page(self):
        """ Get the page this section belongs to
        
        > [!CAUTION]
        > Since a page returns self, a misuse could lead to infinite recurrence loop
        
        Returns
        -------
        - Section : page this section belongs to
        """
        if self.is_top:
            return self
        
        if self.is_chapter:
            if self.is_transparent:
                return self.parent.page
            else:
                return self
            
        elif self.is_page:
            return self
        
        else:
            return self.parent.page

    @property
    def header_depth(self):
        """ Header depth relatively to the page
        
        The header depth doesn't include transparent parents. It aloso take
        the <#depth_shift> into account
        
        Returns
        -------
        - int : distance to the page, excluding transparent parents and taking shift into account
        """
        if self.is_top:
            return 0
        
        elif self.is_transparent:
            return self.parent.header_depth
        
        elif self.is_page:
            return 0

        else:
            return self.parent.header_depth + self.depth_shift +  1
        
    @property
    def chapter_prefix(self):
        """ Get the prefix to use in the file names of pages in this chapter
        
        To avoid to long names, prefix uses the 5 first chars plus a number
        if collision
        
        Returns
        -------
        - str : chapter path with - char as separator
        """
        if self.is_top:
            return ""
        
        elif self.is_chapter:
            
            prefix = title_to_anchor(self.title.replace(' ', ''))[:5]
            super_chapter = self.parent.chapter
            
            count = 0
            child_iter = super_chapter.all_values()
            for child in child_iter:
                if child is self:
                    break
                if not child.is_chapter:
                    continue
                if title_to_anchor(child.title.replace(' ', ''))[:5] == prefix:
                    count += 1
                    child_iter.no_child()
                    
            if count > 0:
                prefix = f"{prefix}{count}"
                
            if super_chapter.is_top:
                return prefix
            else:
                return '-'.join((super_chapter.chapter_prefix, prefix))
                                
        else:
            return self.parent.chapter_prefix
            
    # -----------------------------------------------------------------------------------------------------------------------------
    # File name / anchor

    @property
    def file_name(self):
        """ File name were to write the page
        
        The file name is built by joining <#chapter_prefix> with the name of section.

        > [!NOTE]
        > top chapter returns "index.md"
        
        Returns
        -------
        - str : file name
        """
        if self.is_top:
            return "index.md"
        
        chapter_prefix = self.chapter_prefix
        if chapter_prefix != '':
            chapter_prefix += '-'
        
        if self.is_chapter:
            chapter_prefix += "--"
        
        if self.is_page:
            return chapter_prefix + title_to_file_name(self.title)
        
        else:
            return self.page.file_name
        
    @property
    def homonyms_count(self):
        """ Count the number of sections have the same title
        
        This number is used to suffix the title anchor if needed.
        
        > [!NOTE]
        > The number of homonymes is count up the the section iself, not after
        
        Returns
        -------
        - int: number of above sections sharing the same title
        """
        
        if self.is_page:
            return 0
        
        anchor = title_to_anchor(self.title)
        count = 0

        for section in self.page.all_values():
            if self == section:
                break
            
            if title_to_anchor(section.title) == anchor:
                count += 1
                
        return count
        
    @property
    def anchor(self):
        """ The anchor of this section within the page
        
        Returns
        -------
        - str : section anchor
        """
        anchor = title_to_anchor(self.title)
        if self.is_page:
            return anchor
        else:
            count = self.homonyms_count
            if count == 0:
                return anchor
            else:
                return f"{anchor}-{count}"
            
    def link_to(self, target=None, /, title=None):
        """ Returns the link to a target from this section
        
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
        
        Arguments
        ---------
        - target (str = None) : target of the link, self if None
        - absolute (bool = True) : include file name, only the anchor otherwise
        - title (str = None) : link title, use self.<#title> if None
        
        Returns
        -------
        - str : link in md format `[title](file.md#anchor)`
        """
        
        # ----------------------------------------------------------------------------------------------------
        # Reserved keywords
        
        if target is None:
            target = '!'
            
        if target == '!':
            self._linked = True
            if title is None:
                title = self.title
            if self.is_page:
                return f"[{title}]({self.file_name})"
            else:
                return f"[{title}]({self.file_name}#{self.anchor})"
            
        elif target == '#':
            self._linked = True
            if title is None:
                title = self.title
            return f"[{title}](#{self.anchor})"
            
        elif target == 'INDEX':
            if title is None:
                title = 'index'
            return f"[{title}](index.md)"
        
        elif target.upper() == 'TOP':
            self.page._linked = True
            if title is None:
                title = 'top' if target == 'TOP' else self.page.title
            return f"[{title}](#{self.page.anchor})"
        
        elif target.upper() == 'UP':
            if self.is_top:
                return ""
            self.parent._linked = True
            if title is None:
                title = 'up' if target == 'UP' else self.parent.title
            return self.parent.link_to('!', title=title)
        
        elif target == 'TOC':            
            page = self.page
            if not page.has_toc:
                return ""
            for section in page.values():
                if section.is_toc:
                    section._linked = True
                    return f"[{section.title}](#{section.anchor})"
                
            return f"<#{page.toc_title}>"
        
        # ----------------------------------------------------------------------------------------------------
        # Simple or composed target ?
        
        expr = r"(!(?P<page>[^#]*))?(#?(?P<section>.*))"
        m = re.search(expr, target)
        
        page_target    = m.group('page')
        section_target = m.group('section')
        
        if page_target is not None:
            page_target = page_target.strip()
            if page_target == "":
                page_target = None

        if section_target is not None:
            section_target = section_target.strip()
            if section_target == "":
                section_target = None
                
        if title is not None:
            title = title.strip()
            if title == "":
                title = None
        
        page    = None
        section = None
        
        # ----------------------------------------------------------------------------------------------------
        # We have a target for the page
        
        if page_target is not None:
            
            # Let's find the page
            
            page_target = page_target.strip()
            
            child_iter = self.top.all_values(include_self=True)
            for child in child_iter:
                if child.is_hidden:
                    child_iter.no_child()
                    continue
                
                if child.is_transparent or not child.is_page:
                    continue
                
                if child.title == page_target:
                    page = child
                    break
                
            # Not found :-(
            
            if page is None:
                if section_target is None:
                    return self.link_to(section_target, title=title)
                
                else:
                    msg = f"page '{page_target}' not found in '{target}'"
                    print(f"UNSOLVED LINK in '{self.title}': {msg}")
                    return f"[{msg}]()"
            
            # No section target
            
            if section_target is None:
                page._linked = True
                if title is None:
                    title = page.title
                return f"[{title}]({page.file_name})"
            
            # Let's find the section
            
            child_iter = page.all_values()
            for child in child_iter:
                if child.is_hidden:
                    child_iter.no_child()
                    continue
                
                if child.is_transparent:
                    continue
                
                if child.title == section_target:
                    section = child
                    break
                
            # Not found
            
            if section is None:
                msg = f"impossible to find the section '{section_target}' in page '{page.title}'"
                print(f"UNSOLVED LINK in '{self.title}': {msg}")
                return f"[{msg}](page.file_name)"
            
            # Everything worked well !
            
            section._linked = True
            if title is None:
                title = section.title
            return f"[{title}]({page.file_name}#{section.anchor})"
        
        # ----------------------------------------------------------------------------------------------------
        # We have only a target for the section
        
        # Let's be idiotproof
        
        if section_target is None or section_target.strip() == "":
            return m.group(0)
        
        section_target = section_target.strip()
        
        for scope, pages_only in [(self, False), (self.page, False), (self.top, True), (self.top, False)]:
        
            child_iter = scope.all_values()
            for child in child_iter:
                if child.is_hidden:
                    child_iter.no_child()
                    continue
                
                if child.is_transparent:
                    continue
                
                if pages_only and not child.is_page:
                    continue
                
                if child.title == section_target:
                    return child.link_to('!', title)
                    
                    child._linked = True
                    if title is None:
                        title = child.title
                    if scope is self or scope is self.page:
                        return f"[{title}](#{child.anchor})"
                    else:
                        return f"[{title}]({child.file_name}#{child.anchor})"
                    
        # ----------------------------------------------------------------------------------------------------
        # Not found
            
        msg = f"'{target}' not found"
        print(f"UNSOLVED LINK in '{self.title}': {msg}")
        return f"[{msg}]()"
    
    
    def _title_sort(self, sort=None):
        s = self.title.replace('_', '')
        if sort is None or sort is False:
            return 'A'
        elif sort == True:
            return s.lower()
        else:
            return s
        
    # =============================================================================================================================
    # Tags
    
    def set_tag(self, *tags):
        self.tags = self.tags.union(tags)
        
    def has_any_tag(self, *tags):
        for tag in tags:
            if tag in self.tags:
                return True
        return False
    
    def has_tag(self, *tags):
        for tag in tags:
            if tag not in self.tags:
                return False
        return True
    
    def del_tag(self, *tags):
        self.tags = set([tag for tag in self.tags if tag not in tags])
    
    # =============================================================================================================================
    # Creating section
    
    def new(self, title, comment=None, **parameters):
        """ Add a section
        
        Arguments
        ---------
        - title (str) : section title
        - comment (str) : section comment
        - kwargs : valid section attribute settings
        
        Returns
        -------
        - Section : created section
        """        
        return self.add(title, Section(title, comment, **parameters))
    
    def new_chapter(self, chapter, comment=None, **parameters):
        """ Add a chapter section
        
        Arguments
        ---------
        - chapter (str) : name of the chapter to create
        - comment (str) : section comment
        - kwargs : valid section attribute settings
        
        Returns
        -------
        - Section : chapter section
        """
        params = {**parameters}
        params['in_toc']   = params.get('in_toc',   True)
        params['toc']      = params.get('toc',      True)
        params['toc_flat'] = params.get('toc_flat', True)

        return self.new(chapter, comment, _rupture=Section.CHAPTER, **params)
    
    def new_page(self, title, comment=None, **parameters):
        """ Add a page section
        
        Arguments
        ---------
        - title (str) : section title
        - comment (str) : section comment
        - kwargs : valid section attribute settings
        
        Returns
        -------
        - Section : page section
        """
        params = {**parameters}
        params['in_toc']   = params.get('in_toc',   True)
        params['toc']      = params.get('toc',      True)
        params['toc_flat'] = params.get('toc_flat', True)

        return self.new(title, comment, _rupture=Section.PAGE, **params)
    
    def get_create_section(self, title, comment=None, **parameters):
        """ Get an existing section or create a new one
        
        > [!NOTE]
        > Contrary to <#get_section>, this method searchs the section only
        > in the direct children, not in all the hierarchy.
        
        Arguments
        ---------
        - title (str) : section title
        - comment (str) : section comment
        - kwargs : valid section attribute settings
        
        Returns
        -------
        - Section : chapter section
        """        
        for section in self.values():
            if section.title == title:
                return section
            
        return self.new(title, comment=comment, **parameters)
    
    # =============================================================================================================================
    # Table of content
    
    def get_toc_sections(self, flat=None):
        """ Return the dictionary of sections being part of the toc
        
        If **flat** is True, the search for sub sections in the toc continues
        within sections in the toc.
        
        If **flat** is False, the exploration stops as soon as a section is
        in the toc.
        
        Arguments
        ---------
        - flat (bool = None) : returns the sections without hierarchy, use default if None
        
        Returns
        -------
        - list : sections in the table of content of the page
        """
        toc = []
        
        if flat is None:
            flat = self.toc_flat
        
        tree_iter = self.all_values()
        for section in tree_iter:
            if section.is_hidden:
                tree_iter.no_child()
                continue
            
            if section.is_transparent:
                continue
            
            no_child = False
            
            if section.in_toc and section.has_content:
                toc.append(section)
                if not flat:
                    no_child = True
            
            if section.is_page:
                no_child = True
                
            if no_child:
                tree_iter.no_child()
                
        return toc
    
    def get_toc(self, flat=None, sort=None, max_length=None, max_depth=2):
        """ Build the list of toc items
        
        The methods return a list of paris giving:
        - the level of the item
        - the MD links
        
        Arguments
        ---------
        - flat (bool) : toc is a flat list or hierarchical
        - sort (bool) : sort the list (force **flat** if True)
        - max_length (int = None) : use alphabetical list if the number of items in the toc
          is greater thant this value
        - max_depth (int) : max relative depth for a hierarchical toc
        
        Returns
        -------
        - list of strs : one entry per line
        """
        
        if flat is None:
            flat = self.toc_flat
        if sort is None:
            sort = self.toc_sort
        
        if sort:
            flat = True
        
        sections = self.get_toc_sections(flat=flat)
        if not len(sections):
            return []
        
        if max_length is None:
            max_length = self.toc_max_length
        
        # ----------------------------------------------------------------------------------------------------
        # Flat table of content : 
        # - either an item per section
        # - or a line per first letter if there is too much items
        
        if flat:
            
            if sort:
                sections.sort(key = lambda s: s._title_sort(sort))
            
                if len(sections) > max_length:
                    alpha = []
                    last  = None
                    for section in sections:
                        first = section._title_sort(True)[0].upper()
                        if last is None or first != last:
                            alpha.append(f"- **{first}** : " + section.link_to())
                            last = first
                        else:
                            alpha[-1] += ' :black_small_square: ' + section.link_to()
                            
                    return alpha
            
            else:
                return ['- ' + section.link_to() for section in sections]
            
        # ----------------------------------------------------------------------------------------------------
        # Structured table of content
        
        toc = []
        for section in sections:

            toc.append('- ' + section.link_to())
            
            if max_depth > 0:
                for sub_item in section.get_toc(flat=False, sort=False, max_depth=max_depth-1):
                    toc.append('  ' + sub_item)
                    
        return toc                    
                    
    def insert_toc(self):
        """ Insert the toc section
        
        Returns
        -------
        - Section : None if no toc
        """ 
        
        if not self.toc:
            return None
        
        # ----- Already exists
        
        for section in self.values():
            if section.is_toc:
                return section
            
        # ----- Let's insert it
        
        toc = self.get_toc()        
        if not len(toc):
            return None
        
        md = ""
        for item in toc:
            md += item + '\n' 
            
        toc_section = Section(self.toc_title, md)
        toc_section.depth_shift = self.toc_depth_shift
        self.set_child(toc_section.title, toc_section, index=0)
        toc_section.is_toc = True
        
        return toc_section
    
    # =============================================================================================================================
    # Dynamic write
    
    def write(self, text):
        """ Append text to the header comment

        Arguments
        ---------
        - text (str) : the text to write
        """        
        if text is None:
            return

        if self.comment is None:
            self.comment = text
        else:
            self.comment += text

    def write_source(self, source):
        """ Append source code to the header comment

        Arguments
        ---------
        - source (str) : source code to append
        """
        self.write("\n\n``` python\n")
        self.write(source.replace("`", "'"))
        self.write("\n```\n\n")
        
    def write_header(self, level, title, text):
        """ Write a section in the text stream
        
        This method write markdonw text corresponding to a header followed by text.
        
        > [!NOTE]
        > This method doesn't create a section in the hierarchy, contrary to <#add_section>
        
        Arguments
        ---------
        - level (int) : header level
        - title (str) : header title
        - text (str) : text
        """
        self.write(f"\n\n{'#'*level} {title}\n\n{text}\n\n")
        
    @property
    def navigation_md(self):
        """ Get navigation markdown
        
        Navigation bar is built with <#navigation> list
        """
        
        navigation = self.navigation
        if navigation is None or self.is_top:
            return ""
        
        if navigation == True or not isinstance(navigation, (list, tuple)):
            navigation = ['INDEX', 'TOP', 'TOC', 'up']
            
        links = []
            
        for target in navigation:
            links.append(self.link_to(target))
                
        if len(links):
            #self.write(f"\n\n<sub>[top](#{self.page.anchor}) [index](index.md)</sub>\n\n")
            return f"\n\n<sub>:arrow_right: {' :black_small_square: '.join(links)}</sub>\n\n"
        else:
            return ""
        
    # =============================================================================================================================
    # Tags operations
    
    def new_sections_group(self, title, sections, **parameters):
        """ Create a section from a list of sections
        
        The section is created only if the list has items.
        
        The sections are move to the newly created section using <!Tree#move_to_parent>.
        
        Arguments
        ---------
        - title (str) : title of the section to create
        - sections (list of Sections) : the section to move into the created section
        - parameters : parameters for the section to create
        
        Returns
        -------
        - Section : the created section
        """
        
        if len(sections) == 0:
            return None
        
        group = self.new(title, **parameters)
        for section in sections:
            section.move_to_parent(group)
            
        return group
    
    def new_tag_group(self, tag, **parameters):
        """ Create a section grouping all the sub sections having a given tag
        
        The section is created only if sections have the tag
        
        The group is created by calling <#new_sections_group>.
        
        Arguments
        ---------
        - tag (str) : tag to group sections
        - parameters : parameters for the section to create
        
        Returns
        -------
        - Section : the created section
        """
        sections = []
        child_iter = self.all_values()
        for section in child_iter:
            if section.is_hidden:
                child_iter.no_child()
                continue
            
            if section.is_transparent:
                continue
            
            if section.has_tag(tag):
                sections.append(section)
                
            if section.is_page:
                child_iter.no_child()
                
        return self.new_sections_group(tag, sections, **parameters)
        
    # =============================================================================================================================
    # Cook
    
    def cook(self):
        """ Cook the section and child sections
        
        Default behavior is:
        - sort the sections if <#sort_section> is set
        - cook the child sections
        - insert the toc
        
        Hidden sections are not cooked!
        """        
        # ----- Cook the parent section
        
        if self.sort_sections is not None:
            self.sort(key=lambda s: s._title_sort(self.sort_sections))
            
        # ----- Cook the child sections
        
        child_iter = self.all_values()
        for section in child_iter:
            if section.is_hidden:
                child_iter.no_child()
                continue
            
            section.cook()
            
        # ----- Now we can insert the toc
            
        self.insert_toc()
        
    # =============================================================================================================================
    # Build the whole documentation
    
    def before_comment(self):
        yield ""
    
    def after_comment(self):
        yield ""
    
    
    def get_content(self):
        """ Returns the text to write in the page
        
        A page is built by:
        - joining section and comment
        - optionnally joining a table of content
        - recursively joining the content of the children
        
        Returns
        -------
        - str : section and sub section content
        """
        
        if (not self.is_displayed) or self.is_transparent:
            return None
        
        # ----- Before / Comment / After
        
        content = ""
        for line in self.before_comment():
            content += line
            
        if self.comment is not None:
            content = content.strip() + '\n\n' + self.comment
        
        for line in self.after_comment():
            content += line
            
        if content != "":
            content = content.strip()
            if content == "":
                content = None
        
        # ----- Header comment and sections
        
        links = []
        
        iter_child = self.all_values()
        
        for section in iter_child:
            
            if section.is_hidden:
                iter_child.no_child()
                continue
            
            if section.is_transparent:
                continue
            
            if section.is_page:
                if section.in_toc:
                    links.append(section.link_to('!'))
                iter_child.no_child()
                continue
            
            section_content = section.get_content()
            if section_content is not None:
                if content is None:
                    content = section_content
                else:
                    content += '\n\n' + section_content.strip()
            
            iter_child.no_child()
            
        # ----- We have a list of pages
        
        if len(links):
            if content is None:
                content = ""
            else:
                content += '\n'
            content += '\n- '.join([""] + links)
            
        # ----- No content
        
        if content is None:
            if self.ignore_if_empty:
                return None
            else:
                content = ""
            
        # ----- Header and sepa
        
        if self.top_bar is None:
            header = ""
        else:
            header = self.top_bar * 10 + "\n"
        header += f"#{'#'*self.header_depth} "
        
        header += under_to_md(self.title) + '\n\n'
        
        content = header + content
        
        return content + self.navigation_md

    # =============================================================================================================================
    # Structure
    
    def dump_title(self):
        
        if self.is_top:
            return f"Dump: {self.title}\n{'-'*50}\n(>) Chapter, (!) Transparent, ($) Page, (H)idden, (i)n_toc, has_[T]oc, has_[C]ontent\n\n"
        
        flags = "!" if self.is_transparent else " "
        
        if self.is_chapter:
            flags += ">"
            
        elif self.is_page:
            flags += "$"
            
        else:
            flags += " "
            
        flags += "H" if self.is_hidden else '.'
        flags += "i" if self.in_toc else '.'
        flags += "T" if self.has_toc else '.'
        flags += "C" if self.has_content else '.'
        
        return f"{'   '*(self.depth - 1)}{flags} {self.count:2d} {self.all_count:2d} {self.title}"
    
    def dump_pages(self):
        
        lines = [self.dump_title()]
        
        for page in self.all_values():
            if page.is_page:
                lines.append(page.dump_title())
                file_name = 'NO PAGE' if page.is_transparent else page.file_name
                lines.append(f"{'   '*(self.depth - 1)}          : {file_name}")
                
        return "\n".join(lines)
    
    def dump_titles(self, depth=None):
        
        s_iter = self.all_values()
        
        lines = [self.dump_title()]
        for section in s_iter:
            lines.append(section.dump_title())
            if depth is not None and section.depth >= depth:
                s_iter.no_child()
                
        return "\n".join(lines)
    
    def dump_toc(self):
        
        lines = []
        
        for page in itertools.chain([self], self.all_values()):
            toc = page.get_toc_sections()
            if not len(toc):
                continue
            
            lines.append("TOC of: " + ("INDEX" if page.is_top else page.path))
            lines.append('-'*50)
            for section in toc:
                lines.append(section.title)
            lines.append("")
            
        return "\n".join(lines)

    # =============================================================================================================================
    # dev and test

    @classmethod
    def Test(cls):
        
        top = cls("Demo Documentation", "This is for demo purpose")
        
        chapter = top.new_chapter("Chapter AAA", "Chapter with text and pages")
        page = chapter.new_page("Page AAA aaa", "Page content")
        page.new("Section A", "Section content", in_toc=True)
        page.new("Section B", "Section content", in_toc=True)
        page.new("Section C", "Section content", in_toc=True)
        
        page = chapter.new_page("Page AAA bbb", "Page content")
        page.new("Section A", "Section content")
        page.new("Section B", "Section content")
        page.new("Section C", "Section content")
        
        page = chapter.new_page("Page AAA ccc Empty")
        page.new("Section A")
        page.new("Section B")
        page.new("Section C")
        
        chapter = top.new_chapter("Chapter BBB", "Chapter with text and pages and chapters")
        page = chapter.new_page("Page BBB aaa", "Page content")
        page.new("Section A", "Section content", in_toc=True)
        page.new("Section B", "Section content", in_toc=True)
        page.new("Section C", "Section content", in_toc=True)
        
        page = chapter.new_page("Page BBB bbb", "Page content")
        page.new("Section A", "Section content")
        page.new("Section B", "Section content")
        page.new("Section C", "Section content")
        
        schap = chapter.new_chapter("CCC Transparent chapter in BBB with only pages and chapters")
        page = schap.new_page("Page CCC aaa", "Page content")
        page.new("Section A", "Section content", in_toc=True)
        page.new("Section B", "Section content", in_toc=True)
        page.new("Section C", "Section content", in_toc=True)
        
        page = schap.new_page("Page CCC bbb", "Page content")
        page.new("Section A", "Section content")
        page.new("Section B", "Section content")
        page.new("Section C", "Section content")
        
        s_schap = schap.new_chapter("DDD Chapter in CCC", "Chapter with content and pages")
        page = s_schap.new_page("Page DDD aaa", "Page content")
        page.new("Section A", "Section content", in_toc=True)
        page.new("Section B", "Section content", in_toc=True)
        page.new("Section C", "Section content", in_toc=True)
        
        page = s_schap.new_page("Page DDD bbb", "Page content")
        page.new("Section A", "Section content")
        page.new("Section B", "Section content")
        page.new("Section C", "Section content")
        
        return top
    
    # =============================================================================================================================
    # Module test
    
    @classmethod
    def ModuleTest(cls, module=None):
        
        import sys
        import importlib
        import inspect
        
        package = None
        
        def load_member(section, name, member):
            
            if inspect.ismodule(member):

                chapter = section.new_chapter(name, inspect.getdoc(member))
                chapter.package = member.__package__

                for n, m in inspect.getmembers(member):
                    
                    if inspect.ismodule(m):
                        if package is None:
                            continue
                        
                        if m.__package__ is not None and not m.__package__.startswith(package):
                            continue
                        
                    elif inspect.isclass(m):
                        if package is None:
                            if m.__module__ is not None:
                                continue
                        else:
                            if not m.__module__.startswith(package):
                                continue
                        
                    elif n.startswith('__'):
                        continue

                    load_member(chapter, n, m)
                    
            elif inspect.isclass(member):
                
                page = section.new_page(name)
                
                for n, m in inspect.getmembers(member):
                    
                    if n.startswith('__'):
                        continue
                    
                    if inspect.ismodule(m) or inspect.isclass(m):
                        continue
                    
                    load_member(page, n, m)
                    
                    comment = inspect.getdoc(member)
                    if comment is not None and comment.strip() != "":
                        page.new(n, comment.strip(), in_toc=True)
                    
            else:
                section.new(name, inspect.getdoc(member), in_toc=True)
                
        if module is None:
            module = sys.modules[__name__]
            package = '__main__'
        else:
            package = module.__package__
                
        doc = cls(f"Test with module {module}", None)
        doc.package = module.__package__

        load_member(doc, module.__name__, module)
        
        return doc

# =============================================================================================================================
# Documentation class

class Documentation:
    def __init__(self, top_section=None):
        """ Documentation package
        
        A documentation is made of a top <!Section> and provides documentation level
        methods and properties
        
        It provides <#hooks> facility for documentation post treatment such as text replacement
        or links resolution.
        
        Properties
        ----------
        - hooks (list) : list of (regular expressions, hook function) pairs to apply on
          the documentation
        
        Arguments
        ---------
        - top_section (Section = None) : documentation content
        """
        
        self.top_section = top_section
        self._cooked = False
        
        # ----- Compile regex expression to solve links
        
        self.solve_links_expr = r'<(?P<target>(!|#)[^">\n]*)("(?P<title>.*))?>'
        self.solve_links_re   = re.compile(self.solve_links_expr, flags=re.MULTILINE)
        
        # ----- Custom hooks
        
        self.hooks = []
        
    def __str__(self):
        if self.top_section is None:
            return "<Documentation None>"
        else:
            return f"<Documentation {self.top_section.title}, {self.top_section.all_count} sections>"

    # =============================================================================================================================
    # Hooks
    
    # ----------------------------------------------------------------------------------------------------
    # Set a hook

    def set_hook(self, expr, repl):
        """ Replace a regular expression by as substitution string

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

        Arguments
        ---------
            - expr (str) : RegEx expression
            - repl (str or function) : replacement string or function
        """
        self.hooks.append({'expr': expr, 'repl': repl, 'cexpr': re.compile(expr, flags=re.MULTILINE)})

    # -----------------------------------------------------------------------------------------------------------------------------
    # Custom links
    
    def solve_section_links(self, section, ignore_source=False):
        """ Solve the links of a section
        
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
        
        Arguments
        ---------
        - section (Section) : section to handle
        - ignore_source (bool = False) : do not try to extract source code before operation
        """
        if section.comment is None:
            return

        # Extract source code
        
        codes = None
        if not ignore_source:
            section.comment, codes = extract_source(section.comment)
            
        # Solve the links
        
        if section.comment is not None:
            section.comment = self.solve_links_re.sub(lambda m: section.link_to(m.group('target'), title=m.group('title')), section.comment)

        # Replace source code

        if not ignore_source:
            section.comment = replace_source(section.comment, codes)
        
    # =============================================================================================================================
    # Solve the hooks
    
    def solve_hooks(self):
        """ Solve all the hooks for a section.
        
        > [!NOTE]
        > This method also solve links
        """
        
        for section in self.top_section.all_values(include_self=True):
            
            if section.comment is None:
                continue
        
            # ---- Extract source code
            
            comment, sources = extract_source(section.comment)
            
            # ----- Loop on the hooks
        
            for hook in self.hooks:
    
                func = hook['repl']
                if isinstance(func, str):
                    repl = func
                    
                else:
                    if len(inspect.getfullargspec(func).args) == 1:
                        repl = func
                    else:
                        repl = lambda m: func(m, section)
    
                comment = hook['cexpr'].sub(repl, comment)
                
            section.comment = comment
                
            # ----- Finalize with the links
            
            self.solve_section_links(section, ignore_source = True)
        
            # ----- Replace source code
    
            section.comment = replace_source(section.comment, sources)            
        
    # =============================================================================================================================
    # Cook
    
    def cook(self):
        if self._cooked:
            return
        
        self.top_section.cook()
        
        self.solve_hooks()
        
        self._cooked = True
        
    # =============================================================================================================================
    # Build the documentation
    
    def create_documentation(self, folder=None):
        """ Build and the whole documentation
        
        The documentation is returned as a dictionary of pages keyed
        by their file name.
        
        If argument **folder** is not None, the documentation files are written
        in it.
        
        Arguments
        ---------
        - folder (str = None) : folder where to write the documentation files
        
        Returns
        -------
        - dict : documentation files content
        """
        
        # ----------------------------------------------------------------------------------------------------
        # Cook
        
        self.cook()

        # ----------------------------------------------------------------------------------------------------
        # Create the files
        
        print(f"Creating documentation for {self}")
        if folder is not None:
            print("Create files in folder:", folder)
        
        doc = {}
            
        pages_iter = self.top_section.all_values(include_self=True)
        for page in pages_iter:
            
            if not page.is_page or page.is_hidden:
                assert(not page.is_top)
                continue
            
            if page.is_hidden:
                assert(not page.is_top)
                pages_iter.no_child()
                continue
            
            text = page.get_content()
            if text is  None:
                assert(not page.is_top)
                continue
            
            file_name = page.file_name
            assert(file_name not in doc)
            doc[file_name] = text
            
            if folder is not None:
                print("Writing", file_name, "...")
            
                with (Path(folder) / str(file_name)).open(mode='w') as f:
                    f.write(text)
        
        return doc

        
    # =============================================================================================================================
    # Create self documentation
    
    @staticmethod
    def demo():
        
        
        documentation = Documentation(Section("Demo documentation"))
        doc = documentation.top_section
        
        doc.write("Some introduction")

        section1 = doc.new("A simple section", in_toc=True)
        section1.write("This is simple a section")
        section1.write_source("# With pyton sample\na = 123")
        
        section2 = doc.new("Another section", in_toc=True)
        section2.write("Another simple a section")
        section2.new("HOMONYM", "Shared named")

        section3 = doc.new("External pages", in_toc=False)
        section3.new_page("Page 1", "Some content 1", in_toc=True)
        page2 = section3.new_page("Page 2", "Some content 2", in_toc=True)
        section3.new_page("Page 3", "Some content 3", in_toc=True)
        s31 = page2.new("Section 1 in page 3", "Some content")
        s32 = page2.new("Section 2 in page 3", "Somme content")
        page2 = page2.new("HOMONYM", "Shared named")
        
        links = doc.new("Let try the links")
        links.write("- index : <!Demo documentation>\n")
        links.write("- intra section1 : <#A simple section>\n")
        links.write("- intra section2 : <#Another section>\n")
        
        links.write("- page 1 : <!Page 1>\n")
        links.write("- page 2 : <#Page 2>\n")
        links.write("- page 3 : <#Page 3 \" Page 3 with a custom title>\n")
        links.write("- Link error : <#Page 4>\n")        
        
        links.write(f"- section 1 on page 3 : <!{s31.title}>\n")
        links.write(f"- section 2 on page 3 : <#{s32.title}>\n")
        for section in (links, page2):
            section.write(" - Homonym in this page: <#HOMONYM>\n")
            section.write(" - Homonym as page: <!HOMONYM>\n")
            section.write(" - Homonym in page 2: <!Page 2#HOMONYM>\n")
        
        # ----- Create files
        
        files = documentation.create_documentation(None) 
        
        for k, v in files.items():
            print()
            print("="*80)
            print(k)
            print("-"*80)           
            print(v)
            
#Documentation.demo()            
            

        


        



    
    



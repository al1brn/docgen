#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:22:48 2024

@author: alain

$ DOC START

This module contains interface classes to implement tree hierarchy.

If comes with the root abstract interface <!Tree> and 3 useable child classes <!TreeDict>, <!TreeList> and <!TreeChain>
implementing the abstract methods respectively with a dict, a list and <!TreeChain#child>  <!TreeChain#next> chaining
between nodes.


Each node in a tree has a single parent and can have children. The top node in the tree
has no parent.

Each node, but the top one, has a key. A node can be considered as a dictionary of children keyed
by their key.

Keys can be composed with a key separator to form a path. A patch extends the scope of the "keys"
accepted by a node:
    
``` python
# default key separator is '/'

child = node['AAA']      # returns the child keyed by 'AAA'
child = node ['AAA/BBB'] # return child 'BBB' of child 'AAA'
````

### Tree methods

#### Getting child

A child can be addressed via a path relativelly to the caller:
    
```python
child = node['AAA/BBB']  # child BBB of child AAA
child = node['/AAA/BBB'] # same but starting from the top of the tree
```

A child, or a list of children can be found with <#find> method:
    
```python
child = node.find('AAA', 'BBB', first=False) # Find all children whose key is either 'AAA' or 'BBB'
child = node.find('AAA', 'BBB', first=True] # Find the first node with a key equal to 'AAA' or 'BBB'
```

#### Iterating on the children

One can iterate either on the direct children or on all the children in the hierarchy.
As for a dictionary, the iterators can return the node, the key or both in pair.

We have then 6 possible iterators:
- values() : direct children
- keys() : direct keys
- items() : direct (key, child) pairs
- all_values() : all children
- all_paths() : all paths
- all_items() : all (path, child) pairs

#### Abstract methods

Actual implementation of a Tree requires the following properties and methods:

- key (str property) : the key of the node
- get_child (method) : get a direct child by its key
- set_child (method) : add a child in the collection of direct children
- remove_from_parent(method) : remove the section from its parent list of children
- create_child (method) : create a new child
- values (method) : returns an iterator on the direct children
- keys (method) : returns an iterator on the keys of the direct children
- items (method) : returns an iterator on the (key, child) pairs of the direct children

### Implementation

#### With a dict

<!TreeDict> inherits from <!Tree> and dict. Direct children are managed from dict inheritance.

This implementation can be chosen when direct child keys must be unique and when there is no
particular need in controlling the order of the children.

#### With a list

<!TreeList> inherits from <!Tree> and list. Direct children are store in the list.

Several children can share the same key.

This implementation can be chosen when direct children can share a same key and / or when there is
a need to control the order of the children

#### Chaining implementation

<!TreeChain> implements directly the interface by chaining the nodes with <!TreeChain#child> and <!TreeChain#next>
properties:
- **child** : first child, the node has no children if Node
- **next** : next child in the collection of parent children, last child if None

Not sure if this implementation is better than one of the two above!

#### Testing

Testing can be made with <!Tree#test> method which provides basic testing.

One can also call <!Tree#FromFolder> and <!Tree#FromModule> which respectively create
a full tree from a disk folder and from python module.

$ DOC END

Created 2024/09/15
"""

from pprint import pprint
import inspect
from pathlib import Path
import re

class PathError(KeyError):
    def __init__(self, message, path, key=None, incomplete=False, incorrect=False):
        """ Exception raised when a path is incorrect or can't be solved
        
        Arguments
        ---------
        - path (str) : incorrect path
        - key (str) : key in the path
        - incomplete (bool = False) : path is incomplete
        - incorrect (bool = False) : path is incorrect
        """
        self.path       = path
        self;key        = key
        self.incomplete = incomplete
        self.incorrect  = incorrect
        
        super().__init__(message)
        
    @classmethod
    def Incomplete(cls, path, key):
        return cls(f"Incomplete path '{path}' : {key} is missing", path, key, incomplete=True)
        
    @classmethod
    def Incorrect(cls, path):
        return cls(f"Incorrect path '{path}'", path, incorrect=True)
    
    @classmethod
    def Empty(cls):
        return cls(f"Empty path is not allowed", "", incorrect=True)
        
# =============================================================================================================================
# Tree Iterator

class TreeIterator:
    
    def __init__(self, tree, include_self=False, values=True, paths=True):
        """ Iterator of a Tree
        
        This iterator iterates recursively on all the nodes in the <!Tree> in the order:
        - node
        - children
        
        The node on which the iterator is called is not yield.
        
        The example below illustrates the yielding order:
            
        ```
        - Top
          - AAA
            - a
            - b
          - BBB
            - c
            - d
            
        Iteration on 'top'' gives the nodes in the following order which doesn't
        include the top node istself:
            
        > AAA, a, b, BBB, c, d
        ```
        
        The iteration can be partially cut with method <#no_child> which prevents
        to explore the children and the followers of a node
        
        Arguments
        ---------
        - tree (Tree) : the tree to iterate
        - include_self (bool) : include the tree itself
        - values (bool) : return values
        - paths (bool) : return paths
        
        Returns
        -------
        - paths and/or values : depending on **values** and **paths** arguments
        """
        self.tree  = tree
        self.include_self = include_self
        
        if values and paths:
            self.returns = 2
        elif paths:
            self.returns = 1
        else:
            self.returns = 0
            
        self.sepa    = tree.SEP
        self.stack   = []
        self.first   = None
        
    def __iter__(self):
        """ The stack contains the current node and an iterator on its direct children
        """
        self.stack = [("", self.tree, None)]
        self.first = self.tree if self.include_self else None
        return self
    
    def __next__(self):
        """ Next 
        
        The algorithm is the following:
        
        ```
        while stack is not empty:
            - pop from the stack the current node and child itertor
            - get the next child
            - if got one:
                - restore the stack
                - push the child on the stack
                - return the child
            - else
                continue to pop the stack
        ```
        """
        
        if self.first is not None:
            first = self.first
            self.first = None
            return first
        
        while len(self.stack):
            
            path, node, child_iter = self.stack.pop()
            if child_iter is None:
                child_iter = ((k, v) for k, v in node.items())
        
            try:
                key, child = next(child_iter)
            except StopIteration:
                continue
            
            child_path = path + self.sepa + key
            
            self.stack.append((path,       node, child_iter))
            self.stack.append((child_path, child, None))
            
            if self.returns == 2:
                return child_path[1:], child
            
            elif self.returns == 1:
                return child_path[1:]
            
            else:
                return child
            
        raise StopIteration
            
    def no_child(self, up=0):
        """ Iteration partial break
    
        This partial break commands the iterator not to iterate on the children.
        
        In addtion, the **up** argument controls how many level to go up in the chain
        of parents:
        - up = 0 -> ignore children, continue with next node
        - up = 1 -> continue with parent's next node
        - up = 2 -> continue with grand parent's next node
        - ...
        
        Arguments
        ---------
        - up (int = 0) : number of levels to move up for the next node (0 = ignore children
          et continue on next node)
        """
        for i in range(-1, up):
            if not len(self.stack):
                return
            
            self.stack.pop()
        

# =============================================================================================================================
# Tree Base class

class Tree:
    
    SEP_DOT = ('/', '.') # Key separator and place holder
    
    def __init__(self):
        """ Tree interface
        
        This abstract class exposes an interface for a tree.
        
        Each node in a tree has a single parent and can have children. The top node in the tree
        has no parent.
        
        Each node, but the top one, has a key. A node can be considered as a dictionary of children keyed
        by their key.
        
        Keys can be composed with a key separator to form a path. A patch extends the scope of the "keys"
        accepted by a node:
            
        ``` python
        # default key separator is '/'
        
        child = node['AAA']      # returns the child keyed by 'AAA'
        child = node ['AAA/BBB'] # return child 'BBB' of child 'AAA'
        ````
        
        ### Abstract methods
        
        Actual implementation of a Tree requires the following properties and methods:
        
        - key (str property) : the key of the node
        - get_child (method) : get a direct child by its key
        - set_child (method) : insert a child in the collection of direct children
        - values (method) : returns an iterator on the direct children
        - keys (method) : returns an iterator on the keys of the direct children
        - items (method) : returns an iterator on the (key, child) pairs of the direct children
        
        
        ### Creating a whole tree
        
        A tree can be created using the <#add> method with the following pseudo code:
            
        ``` python
        class MyTree(TreeDict): # of TreeList or TreeChain or your own implementation
            def __init__(self, source):
                # Initialize self from source content
                ...
                
                # Loop on source children
                for key, child in source:
                    self.add(key, MyTree(child))
        ``` 
        
        The constructor <#FromFile> gives an actual implementation to load the arborescence
        of a disk folder:
            
        <$ Tree.FromFolder>
        
        Properties
        ----------
        - parent (Tree) : parent node, None if it is the top most node in the tree
        - key (str) : node key 
        """
        self.parent = None
            
    def __str__(self):
        """ str
        
        $ DOC SET hidden
        """
        return f"{'   '*self.depth}> {self.key} [{self.path}]"
    
    # =============================================================================================================================
    # Key separator and Dot char
    
    @property
    def SEP(self):
        if hasattr(self, '_SEP'):
            return self._SEP
        elif self.top is None:
            return self.SEP_DOT[0]
        else:
            return self.top.SEP
        
    @SEP.setter
    def SEP(self, value):
        self._SEP = value

    @property
    def DOT(self):
        if hasattr(self, '_DOT'):
            return self._DOT
        elif self.top is None:
            return self.SEP_DOT[10]
        else:
            return self.top.DOT

    @DOT.setter
    def DOT(self, value):
        self._DOT = value

    
    # =============================================================================================================================
    # Path

    @property
    def path(self):
        """ Node path up to the top node
        
        Returns
        -------
        - str
        """
        if self.parent is None:
            return ""
        else:
            return self.parent.path + self.SEP + self.key
        
    def join_keys(self, *keys):
        """ Join keys to form a path
        
        Joins the keys with the key separator avoiding double separators: `join_keys("AAA", "BBB")`
        and `join_keys("AAA/", "BBB")` will both give `"AAA/BBB"`.
        
        
        Returns
        -------
        - str : key joined by key separator
        """
        path = self.SEP
        for key in keys:
            if not path.endswith(self.SEP):
                path += self.SEP
            path += key
        return path[len(self.SEP):]
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # Hierarchy
    
    @property
    def is_top(self):
        """ True if owner is None
        
        Returns
        -------
        - bool
        """
        return self.parent is None
    
    @property
    def top(self):
        """ Get the topmost section
        
        Returns
        -------
        - Section
        """
        if self.parent is None:
            return self
        else:
            return self.parent.top

    @property
    def depth(self):
        """ Distance to the top (0 for top section)
        
        Returns
        -------
        - int
        """
        if self.parent is None:
            return 0
        else:
            return self.parent.depth + 1
        
    # =============================================================================================================================
    # Abstract methods
    
    def get_child(self, key):
        """ Get a direct child by its key
        """
        raise Exception("Tree.get_child is an abstract method")
        
    def set_child(self, key, child, index=None):
        """ Set a direct child by its key
        """
        raise Exception("Tree.set_child is an abstract method")

    def remove_from_parent(self):
        """ Remove the section from its parent list of children
        """
        raise Exception("Tree.remove_from_parent is an abstract method")
        

    # =============================================================================================================================
    # Detach and move
        
    def detach(self):
        """ Detach the section from its parent children
        
        > [!IMPORANT]
        > This method calls the abstract method <#remove_from_parent> which must perform
        > the actual removal from the parent's list of children.
        
        Returns
        -------
        - Tree : self
        """
        
        if self.parent is None:
            raise Exception("Tree top node can't be detached !")

        self.remove_from_parent()

        self.parent = None
        return self
    
    def move_to_parent(self, new_parent, new_key=None):
        """ Change the position of a node from one parent to another
        
        This methods basically calls <#detach> and then <#add>.
        
        Arguments
        ---------
        - new_parent (Tree) : where to locate the node
        - new_key (str = None) : new key, uses the current key is None
        
        Returns
        - Tree : self
        """
        
        old = self.parent
        
        
        if new_parent is self.parent:
            return self
        
        if new_key is None:
            new_key = self.key
        
        self.detach()
        
        assert(self.parent is None)
        for v in old.values():
            assert(v is not self)
        
        if new_parent is None:
            return self
        
        return new_parent.add(new_key, self)
        
    # =============================================================================================================================
    # Vertical navigation
    
    def solve_to_missing(self, path):
        """ Solve a path to missing keys
        
        Solve a path, return the existing node and the list of non existing keys.
        
        Raises
        ------
        - PathError : if path is incorrect
        
        
        Arguments
        ---------
        - path (str) : path to solve
    
        Returns
        -------
        - node, list : last existing node, list of missing keys
        """
        
        keys = path.split(self.SEP)
        
        if not len(keys):
            return self, []
        
        last = self
        
        # ----- Path starts with /
        
        if keys[0] == "":
            if len(keys) == 1:
                return self.top, []
            
            last = self.top
            keys = keys[1:]
            
            
        # ----- Parent
        
        if self.DOT is not None:
            
            while keys[0] in (self.DOT, self.DOT + self.DOT):
                
                if keys[0] == self.DOT + self.DOT:
                    last = last.parent
                    if last is None:
                        raise PathError.Incorrect(path)
                
                if len(keys) == 1:
                    return last, []
                
                keys = keys[1:]
                
        # ----- child keys
        
        for i_key, key in enumerate(keys):
            
            child = last.get_child(key)
            if child is None:
                return last, keys[i_key:]
            else:
                last = child
                
        # ----- Full solved
        
        return last, []
    
    # =============================================================================================================================
    # Create a math
    
    def create_path(self, *keys):
        """ Create nodes in a path
        
        Nodes are create by calling <#new> method.
        
        Arguments
        ---------
        - keys (list of strs) : key forming the path to create
        
        Returns
        -------
        - Tree : last created node
        """
        
        last = self
        for key in keys:
            last = last.new(key)
            
        return last

    def solve_path(self, path, complete_path=False):
        """ Solve a path
        
        Returns the node corresponding to the path.
        
        If it doesn't exist, two cases are possible:
        - only the last key in the path is missing: the methods return the parent
          and the missing key
        - an intermediary node is missing: the methods raises an error or creates
          the missing nodes depending on the arguments **complete_path**.
          
        > [!NOTE]
        > Missing nodes in the path are created with method <#create_path>
         
        Raises
        ------
        - PathError : if the path can't be solved up to the last, or last but one
        
        Arguments
        ---------
        - path (str) : the path to solve
        - complete_path (bool) : create missing nodes (but the last one) if necessary
        
        Returns
        -------
        - Tree, str : (found node, None) or (parent node, missing key)
        """
        
        # Solve to the last existing node
        
        last, keys = self.solve_to_missing(path)
        
        # found : we can be happy
        
        if len(keys) == 0:
            return last, None
        
        # Only the last one is missing : good enough
        
        if len(keys) == 1:
            return last, keys[0]
        
        # Intermediary nodes are missing : we have a problem
        
        if not complete_path:
            raise PathError.Incomplete(path, keys[0])
            
        # Let's create them and return the last with the ultimate missing key
            
        last = last.create_path(*keys[:-1])
        return last, keys[-1]
    
    # =============================================================================================================================
    # Get / set from path
    
    def get(self, path, default=None):
        """ Get the node at path
        
        Arguments
        ---------
        - path (str) : the node path
        - default (Tree) : the node to return if the path is not solved
        
        Returns
        -------
        - Tree
        """
        try:
            last, key = self.solve_path(path)
        except PathError as e:
            if e.incorrect:
                raise e
            return default
        
        if key is None:
            return last
        else:
            return default
        
    def add(self, path, node, complete_path=False):
        """ Add a new node at the path
        
        This method calls <#set_child>.
        
        Arguments
        ---------
        - path (str) : the path where to locate the node
        - node (Tree) : the node to set at the path
        
        Returns
        -------
        - Tree : the node argument
        """
        if path == "":
            raise PathError.Empty()
            
        last, key = self.solve_path(path, complete_path=complete_path)
        
        # Alreay exists, let's set at parent level
        if key is None:
            key = last.key
            last = last.parent
            
        return last.set_child(key, node)
    
    def new(self, path, complete_path=False, **kwargs):
        """ Create a new node at the given path
        
        The default implementation create a new node by calling the defaut constructor
        and adding it by calling <#add>:
            
        ``` python
        return self.add(path, type(self)(**kwargs), complete_path=complete_path)
        ``` 
        
        Raises
        ------
        - PathError : if nodes are missing in the path
        
        Arguments
        ---------
        - path (str) : the path where to create a new node
        - complete_path (set = None) : create the path if hole exist
        - kwargs : default constructor arguments
        
        Returns
        -------
        - Tree : the created node
        """
        return self.add(path, type(self)(**kwargs), complete_path=complete_path)
    
    def __getitem__(self, path):
        item, key = self.solve_path(path, complete_path=False)
        if key is not None:
            raise PathError.Incomplete(path, key)
        return item
        
    def __setitem__(self, path, value):
        self.add(path, value)
    
    def new_paths(self, *paths, complete_path=False, **kwargs):
        """ Create several nodes defined by their path
        
        Basically, this method call <#new> for each provided path.
        
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
        
        Arguments
        ---------
        - paths (list of str) : the paths of the nodes to create
        - complete_path (bool = False) : create intermediary nodes in paths
        - kwargs : default constructor arguments when creating intermediary is required
        
        Returns
        -------
        - Tree : the created child
        """
        nodes = []
        for path in paths:

            parent = self
            
            if path.startswith(self.DOT):
                if len(nodes) > 0:
                    parent = nodes[-1]

            nodes.append(parent.new(path, complete_path=complete_path, **kwargs))

        return nodes   
    
    # =============================================================================================================================
    # Iterators
                
    def __iter__(self):
        return (key for key in self.keys())

    # ----------------------------------------------------------------------------------------------------
    # All items structure
    # Values first, folders then
    
    def all_values(self, include_self=False):
        """ All values iterator
        
        Iterate on all values in the folder and sub folders.
        
        Returns
        -------
        - iterator
        """
        return TreeIterator(self, include_self=include_self, values=True, paths=False)

    def all_paths(self, include_self=False):
        """ All paths iterator
        
        Iterate on all paths in the folder and sub folders.
        Returns
        -------
        - iterator
        """        
        return TreeIterator(self, include_self=include_self, values=False, paths=True)

    def all_items(self, include_self=False):
        """ All items iterator
        
        Iterate on all items in the folder and sub folders.
        
        Returns
        -------
        - iterator
        """        
        return TreeIterator(self, include_self=include_self, values=True, paths=True)
            
    # =============================================================================================================================
    # Find
    
    def find(self, *keys, first=True, **criteria):
        """ Find one or more keys in the tree.
        
        Arguments
        ---------
        - keys (list of strs) : the keys to look for
        - first (boolean) : stop on the first match an return the found node
        - criteria : search the node with attributes match keyword arguments
        
        Returns
        -------
        - Tree or list of Trees: on single tree if first is Trur
        """
        
        nodes = []
        for child in self.all_values():
            if len(keys) == 0 or child.key in keys:
                ok = True
                for k, v in criteria.items():
                    if getattr(child, k, "nOT fOUND") != v:
                        ok = False
                        break
                if not ok:
                    continue
                        
                if first:
                    return child
                else:
                    nodes.append(child)
                    
        return None if first else nodes
    
    # =============================================================================================================================
    # Stats
    
    @property
    def count(self):
        """ Number of direct children, equivalent to `len(self)`
        
        Returns
        -------
        - int
        """
        return len(self)
    
    @property
    def all_count(self):
        """ Total number of children
        
        Returns
        -------
        - int
        """
        
        return len(list(self.all_paths()))
    

    # =============================================================================================================================
    # dump
        
    def dump(self):
        print("Dump")
        print('-'*50)
        for node in self.all_values():
            count = node.count
            all_count = node.all_count
            
            if count > 0:
                symb = '>'
                post = f" {count:2d} [{all_count:3d}]"
            else:
                symb = '-'
                post = ""
            
            print(f"{'  '*(node.depth-1)}{symb} {node.key}{post}")
        print()
        print("--- Total", self.all_count, "nodes")
        
        
    # =============================================================================================================================
    # Load from Path
    
    @classmethod
    def FromFile(cls, folder, pattern="*.*", ignore=(".*", "_*")):
        """ Read the content of a drive
        
        This methods shows how to use method <#add> to recursively load folder files and sub folders.
        
        Arguments
        ---------
        - folder (str) : folder to load
        - pattern (str or tuple of strs) : file selection
        - ignore (str or tuple of strs) : files starting by one of the characters in the string are ignored
        
        Returns
        -------
        - Tree
        """
        
        node = cls()
        node.file_path = Path(folder)
        node.name = node.file_path.name
        
        if not node.file_path.is_dir():
            return node
        
        # Load the files in the directory
        
        pattern = (pattern,) if isinstance(pattern, str) else pattern
        ignore  = (ignore,) if isinstance(ignore, str) else ignore
        
        for sub_path in node.file_path.iterdir():
            
            if ignore is not None:
                if any((sub_path.match(pat) for pat in ignore)):
                    continue
            
            if sub_path.is_file() and pattern is not None:
                if not any((sub_path.match(pat) for pat in pattern)):
                    continue
                
            node.add(sub_path.name, cls.FromFile(sub_path, pattern=pattern, ignore=ignore))
            
        return node

    # =============================================================================================================================
    # Dev
    
    @classmethod
    def Test(cls, **kwargs):
        """ A tree for test
        
        $ DOC SET hidden
        """
        test = cls()
        
        hierarchy = ("./aaa", "./a", "../b", "./c", "../../bbb", "./a", "./c")
        
        test.new_paths("AAA", "BBB", *hierarchy )
        test.new_paths("Copy", "./here")[-1].new_paths(*hierarchy)
        test.new_paths("CCC", "./folder")
        
        return test
    
    @classmethod
    def test(cls):
        """ Perform basic tests
        
        $ DOC hidden
        """
        
        test = cls.Test()
        test.dump()
        
        print('-'*80)
        for key in ['AAA', 'BBB', 'BBB/a', 'CCC/a/b/c', 'BBB/a/b', '/BBB/a/b']:
            a = test[key]
            print(f"get: {key:15s} ? {a.path}")
            
        for keys in [('AAA',), ('BBB',), ('b'), ('a', 'b'), ('nope')]:
            print("find", keys)
            a = test.find(*keys, first=True)
            b = test.find(*keys, first=False)
            sa = None if a is None else a.path
            sb = [c.path for c in b]
            print("     first =", sa)
            print("     all   =", sb)
            print()
        
        return test
    
    @classmethod
    def test_numpy(cls, count=10000):
        
        import numpy as np
        from time import time
        
        start = time()
        tree = cls.FromInspect(np)
        load = time() - start
        tree.dump()
        
        all_paths = list(tree.all_paths())
        paths = [all_paths[i] for i in np.random.default_rng(0).integers(0, len(all_paths), count)]
        start = time()
        for path in paths:
            _ = tree[path]
        print(f"Load: {load:.2f} s, get({count}): {time()-start:.2f} s")

# =============================================================================================================================
# Tree Dictionary
                
class TreeDict(Tree, dict):
    """ Tree interface based on a dict

    This class inherits from <!Tree> and dict. Direct children are managed from dict inheritance.
    
    This implementation can be chosen when direct child keys must be unique and when there is no
    particular need in controlling the order of the children.
    """
    
    #def __init__(self, d=None):
    #    super().__init__()
    #    Tree.__init__(self)
                
    # =============================================================================================================================
    # Abstract methods
    
    @property
    def key(self):
        """ Get the key
        
        In a **TreeDict**, the **key** is known by the parent. A node can retrieve it
        by searching for itself in the direct children of its parent.
        
        To make this process more efficient, **key** is cached by default in
        hidden property **_key**.
        
        Returns
        -------
        - str : None for top node
        """        
        if self.parent is None:
            return None
        
        key = getattr(self, '_key', None)
        if key is not None:
            return key
        
        for k, v in dict.items(self.parent):
            if v is self:
                return k
            
        raise Exception(f"TreeDict {self} is not a child of tdict {self.parent}")
    
    def get_child(self, key):
        """ Get a direct child by its key
        """
        return dict.get(self, key)
        
    def set_child(self, key, child, index=None):
        """ Set a direct child by its key
        """
        child.parent = self
        dict.__setitem__(self, key, child)
        
        if index is not None:
            d = {**self}
            self.clear()
            for i, (k, v) in enumerate(d.items()):
                if i == index:
                    self[key] = d[key]
                
                if k != key:
                    self[k] = v
        
        return child
    
    def remove_from_parent(self):
        """ Remove the section from its parent list of children
        """
        del self.parent[self.key]
    
# =============================================================================================================================
# Tree List
                
class TreeList(Tree, list):
    """ Tree interface based on a list
    
    This class inherits from <!Tree> and list. Direct children are store in the list.
    
    Several children can share the same key.
    
    This implementation can be chosen when direct children can share a same key and / or when there is
    a need to control the order of the children
    """
    
    def __init__(self):
        super().__init__()
        Tree.__init__(self)

        self.key = None
                
    # =============================================================================================================================
    # Abstract methods
    
    def get_child(self, key):
        """ Get a direct child by its key
        """
        for child in list.__iter__(self):
            if child.key == key:
                return child
            
        return None
        
    def set_child(self, key, child, index=None):
        """ set a direct child by its key
        """
        child.parent = self
        child.key    = key
        if index is None:
            self.append(child)
        else:
            self.insert(index, child)
        return child

    def remove_from_parent(self):
        """ Remove the section from its parent list of children
        """
        temp = [s for s in self.parent.values() if s is not self]
        self.parent.clear()
        self.parent.extend(temp)
        
        
    def values(self):
        """ Iterate on childs
        """
        return (child for child in list.__iter__(self))

    def keys(self):
        """ Iterate on keys
        """
        return (child.key for child in list.__iter__(self))

    def items(self):
        """ Iterate on (key, value) pais
        """
        return ((child.key, child) for child in list.__iter__(self))
    
# =============================================================================================================================
# Tree List
                
class TreeChain(Tree):
    """ Tree interface whith chained nodes
    
    This class implements directly the <!Tree> interface by chaining the nodes with <!TreeChain#child> and <!TreeChain#next>
    properties:
    - **child** : first child, the node has no children if Node
    - **next** : next child in the collection of parent children, last child if None
    
    Properties
    ----------
    - child (TreeChain) : the first child of the direct children. None if the node has node child
    - next (TreeChain) : the next next in the parent children series. None if it is the last one
    """
    
    def __init__(self, d=None):
        super().__init__()
        self.key      = None
        self.child    = None
        self.next     = None
        
    @property
    def last_child(self):
        for child in self.values():
            if child.next is None:
                return child
        return None
    
    def __len__(self):
        return len(list(self.keys()))
                
    # =============================================================================================================================
    # Abstract methods
    
    def get_child(self, key):
        """ Get a direct child by its key
        """
        for child in self.values():
            if child.key == key:
                return child
        return None
        
    def set_child(self, key, child, index=None):
        """ set a direct child by its key
        """
        child.parent = self
        child.key    = key
        child.next   = None
        
        if index is None:
            last = self.last_child
            if last is None:
                self.child = child
            else:
                last.next = child
                
        else:
            last = self.child
            if last is None:
                self.child = child
            elif index == 0:
                child.next = last
                self.child = child
            else:
                for i in range(index-1):
                    if last.next is None:
                        break
                    last = last.next
                    
                child.next = last.next
                last.next  = child

        return child
    
    def remove_from_parent(self):
        """ Remove the section from its parent list of children
        """
        if self.parent.child is self:
            self.parent.child = self.next
            
        else:
            prev = self.parent.child
            while prev.next is not self:
                prev = prev.next
            prev.next = self.next
            
        self.next = None
        
    def values(self):
        """ Iterate on childs
        """
        def iterate():
            child = self.child
            while child is not None:
                next_ = child.next
                yield child
                child = next_
        return iterate()

    def keys(self):
        """ Iterate on keys
        """
        def iterate():
            child = self.child
            while child is not None:
                next_ = child.next
                yield child.key
                child = next_
        return iterate()

    def items(self):
        """ Iterate on (key, value) pais
        """
        def iterate():
            child = self.child
            while child is not None:
                next_ = child.next
                yield child.key, child
                child = next_
        return iterate()
    
    # =============================================================================================================================
    # Sort the children
    
    def sort(self, key=None, reverse=False):
        """ Sort the direct children
        
        Arguments
        ---------
        - key (function = None) : function to use to sort the children
        - reverse (bool = False) : sort in rerverse order
        """
        
        if self.child is None or self.child.next is None:
            return
        
        children = list(self.values())
        if key is None:
            children.sort(key=lambda node: node.key, reverse=reverse)
        else:
            children.sort(key=key, reverse=reverse)
            
        for bef, aft in zip(children[:-1], children[1:]):
            bef.next = aft
            
        self.child = children[0]
        children[-1].next = None
        
# =============================================================================================================================
# Package : based on TreeDict
        
        
class Package(TreeDict):
    
    SEP_DOT = ('.', None)
    
    def __init__(self, name, object_):
        
        super().__init__()
        
        self.name    = name
        self.object_ = object_
        self.type_   = None
        self.refs    = {}
        
        # ----------------------------------------------------------------------------------------------------
        # Module
        
        if inspect.ismodule(object_):
            
            # ----- Folder of file
            
            if object_.__name__ == object_.__package__:
                self.type_ = 'FOLDER'
            else:
                self.type_ = 'FILE'
                
            # ----- Loop on the members
                
            for name, member in inspect.getmembers(object_):
                
                # Module
                
                if inspect.ismodule(member):
                    
                    # Only if folder
                    
                    if not self.is_folder:
                        continue
                    
                    # Only if sub folder or foler
                    
                    if not member.__name__.startswith(object_.__name__):
                        continue
                    
                    # Ok
                    
                    self.add(name, Package(name, member))
                    
                # Class
                    
                elif inspect.isclass(member):
                    
                    # Create if contained in file
                    
                    if member.__module__ == object_.__name__:
                        self.add(name, Package(name, member))
                        
                    # Otherwise store reference
                        
                    else:
                        self.refs[name] = object.__name__
                        
                # Function
                
                elif inspect.isfunction(member):
                    
                    self.add(name, Package(name, member))
                    
                # built inf
                
                elif inspect.isbuiltin(member):
                    
                    continue
                    
                # Global vars
                
                else:
                    if name.startswith('__') and name.endswith('__'):
                        if name not in []:
                            continue
                    
                    self.add(name, Package(name, member))
                    
                
        # ----------------------------------------------------------------------------------------------------
        # Class
        
        elif inspect.isclass(object_):
            
            self.type_ = 'CLASS'
            self.inherited = {}
            
            for name, member in inspect.getmembers(object_):
                
                if inspect.ismodule(member) or inspect.ismethodwrapper(member):
                    continue
                
                # Methods
                
                elif inspect.isfunction(member) or inspect.ismethod(member):
                    
                    # Inheritance
                    
                    class_ = '.'.join(member.__qualname__.split('.')[:-1])
                    if class_ == object_.__name__:
                        self.add(name, Package(name, member))
                    else:
                        self.inherited[name] = member.__qualname__
                        
                # Property
                
                elif isinstance(member, property):
                    self.add(name, Package(name, member))
                        
                # Other
                
                else:
                    if name.startswith('__') and name.endswith('__'):
                        if name not in []:
                            continue
                        
                    if type(member).__name__ in ['wrapper_descriptor']:
                        continue
                    
                    self.add(name, Package(name, member))
                    
        elif inspect.ismethod(object_):
            self.type_ = 'METHOD'
            
        elif inspect.isfunction(object_):
            self.type_ = 'FUNCTION'
            
        # ----------------------------------------------------------------------------------------------------
        # Class property
        
        elif isinstance(object_, property):
            self.type_ = 'PROPERTY' 
            
        else:
            self.type_ = 'OTHER'
            
    def __str__(self):
        return f"<{self.type_} {self.name}>"
                
    
    @property
    def key(self):
        return self.name
        
    @key.setter
    def key(self, key):
        self.name = key
        
    @property
    def is_folder(self):
        return self.type_ == 'FOLDER'
    
    @property
    def is_file(self):
        return self.type_ == 'FILE'
    
    @property
    def is_module(self):
        return self.is_folder or self.is_file
    
    @property
    def is_class(self):
        return self.type_ == 'CLASS'
    
    @property
    def is_method(self):
        return self.type_ in ['METHOD', 'FUNCTION']
    
    @property
    def is_property(self):
        return self.type_ == 'PROPERTY'
    
    @property
    def is_other(self):
        return self.type_ == 'OTHER'
    
    # ----- Content
    
    def counters(self):
        cs = {}
        for m in self.values():
            if m.type_ in cs:
                cs[m.type_] += 1
            else:
                cs[m.type_] = 1
        return cs
    
    def str_counters(self):
        cs = self.counters()
        return ", ".join([f"{name.title()}: {value}" for name, value in cs.items()])
    
    def dump_modules(self):
        for m in self.all_values():
            if not m.is_module:
                continue
            
            if m.is_folder:
                print(f"{'   '*m.depth}> {m.name} : {m.str_counters()}")
            else:
                print(f"{'   '*m.depth}- {m.name} : {m.str_counters()}")
                

    def dump_classes(self):
        for m in self.all_values():
            if not m.is_class:
                continue
            
            print(f"{'   '*m.depth}. {m.name} : {m.str_counters()}")
                
         
    

            
            
    
    
            
        
        
        
        
        
        
    

        
            


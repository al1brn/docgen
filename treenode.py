#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 08:33:58 2024

@author: alain
"""

from pathlib import Path

# =============================================================================================================================
# Base section

class tdict(dict):
    
    def __init__(self):
        """ Tree dict
        
        **tdict** implements a folder like structure.
        
        **tdict** is basically a dict of **tdicts**.
        **tdict** keys are intepretated as path within the structure:
            
        ``` python
        # Initialize a tdict
        
        td = tdict(...)
        
        # Getting an item
        
        item = td["AAA/BBB/CCC"]
        
        # is equivallent to
        
        item = td["AAA"]["BBB"]["CCC"]
        ```
        
        Properties
        ----------
        - parent (tdict) : parent tdict
        - name (str) : folder name
        - path (str) : full path
        
        > [!NOTE]
        > **tdict** <#name> is equal to its key in its <#parent> **tdict**
        """
        
        super().__init__(self)
        
        self._parent = None
        self._name   = None
        
            
    def __str__(self):
        return f"{'   '*self.depth}> {self.name} [{self.path}]"

    # -----------------------------------------------------------------------------------------------------------------------------
    # Read only properties
    
    @property
    def parent(self):
        return self._parent
    
    @property
    def name(self):
        return self._name
    
    @property
    def path(self):
        if self.parent is None:
            return ""
        else:
            return self.parent.path + '/' + self.name
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # Hierarchy
    
    @property
    def is_top(self):
        """ Is top section
        
        Returns
        -------
        - bool : True if owner is None
        """
        return self.parent is None
    
    @property
    def top(self):
        """ Get the topmost section
        
        Returns
        -------
        - Section : the top section
        """
        if self.parent is None:
            return self
        else:
            return self.parent.top

    @property
    def depth(self):
        """ Distance to the top
        
        Returns
        -------
        - int : Distance to the top (0 for top section)
        """
        if self.parent is None:
            return 0
        else:
            return self.parent.depth + 1
        
    # =============================================================================================================================
    # Utilities
    
    @staticmethod
    def is_folder(item):
        """ True if the argument is an instance of tdict
        
        Arguments
        ---------
        - item (any) : value to test
        
        Returns
        -------
        - bool : item is an instance of tdict
        """
        return isinstance(item, tdict)
    
    @staticmethod
    def is_value(item):
        """ True if the argument is not an instance of tdict
        
        Arguments
        ---------
        - item (any) : value to test
        
        Returns
        -------
        - bool : item is not an instance of tdict
        """
        return not isinstance(item, tdict)

    # =============================================================================================================================
    # Paths
    
    def _solve_path(self, path):
        """ Solve a path
        
        Search for the last existing item in the tree and return a dict giving:
        - folder : the last folder in the path (never None)
        - key : the key of the item within this folder (never None)
        - item : folder.get(key)
        - remain : remaining path after the key
        
        This method raises an error if the path leads to an non folder item and a remaining path.
        
        If item is None, it is up to the caller to create the element, to stop its operation
        or to raise an error.
        
        Here after are the three possible results:
        
        | item | remain | path complete | item exists
        +------+--------+---------------------------------------------
        | None | None   | Yes           | No
        | item | None   | Yes           | Yes
        | None | Yes    | No            | No, parent folder(s) neither
        | item | Yes    | Imossible     | Raises an error
        
        Raises
        ------
        - Exception : if a key in the path exists and is not a folder
        
        Arguments
        ---------
        - path (str) : path to solve
        
        Returns
        -------
        - dict ['folder', 'key', 'item', 'remain']
        """
        
        # ----------------------------------------------------------------------------------------------------
        # Path starts with /: let's start from the top
        
        if path[0] == '/':
            path = path[1:]
            if self.parent is not None:
                return self.top.get_folder(path)

        # ----------------------------------------------------------------------------------------------------
        # Path is a direct key: we return its value
            
        p = path.find('/')
        if p < 0:
            return {'folder': self, 'key': path, 'item': super().get(path), 'remain': None}

        # ----------------------------------------------------------------------------------------------------
        # Path is composed, we need a sub folder
        
        key    = path[:p]
        remain = path[p + 1:]
        if remain in ["", "/"]:
            remain = None
            
        item = super().get(path[:p])
        
        # Not found: self[key] is None with remaining path
        
        if item is None:
            return {'folder': self, 'key': key, 'item': None, 'remain': remain}
        
        # Found and it's a folder: let's continue with this folder
        
        elif isinstance(item, tdict):
            return item._solve_path(path[p+1:])
        
        # Found but not a folder : ok if no remaining path

        elif remain is None:
            return {'folder': self, 'key': key, 'item': item, 'remain': None}
        
        # Not a folder in the middle of the path: someting is wrong
        
        else:
            raise Exception(f"Impossible to solve path: {self.path}/{path}: {key} is not a folder")
        
    def __getitem__(self, path):
        
        item = self._solve_path(path)['item']

        if item is None:
            raise KeyError(path)
            
        return item
    
    def _setitem(self, key, value):
        """ Add a key item in the dict
        
        When the value is a **tdict**, its <#parent> and <#name> values are set to
        their proper value
        
        Arguments
        ---------
        - key (str) : dict key
        - value (any) : value to set
        
        Returns
        -------
        - value
        """
        if isinstance(value, tdict):
            value._parent = self
            value._name   = key
        
        super().__setitem__(key, value)
        
        return value
        

    def __setitem__(self, path, value):
        
        solve = self._solve_path(path)
        
        item = solve['item']
        
        # ----- No item exists
        
        if item is None:
            
            # Nothing remains in the path : we create at the key in the last folder
            
            if solve['remain'] is None:
                
                if solve['folder'] == self:
                    self._setitem(solve['key'], value)
                else:
                    solve['folder'][solve['key']] = value
            
            # Something remains, we must create an intermediary folder
            
            else:           
                folder = solve['folder'].new_folder(solve['key'])
                folder[solve['remain']] = value
                
        # An item exist, we can't replace if it as a folder
        
        elif isinstance(item, tdict):
            
            raise Exception(f"'{item.path}' is a folder: impossible to set key '{item.name}'")
            
        # We can set the value
        
        else:
            if solve['folder'] == self:                
                self._setitem(solve['key'], value)
            else:
                solve['folder'][solve['key']] = value
        
    # ----------------------------------------------------------------------------------------------------
    # dump
        
    def dump(self):

        print(self)

        for key, item in super().items():
            
            if isinstance(item, tdict):
                assert(key == item.name)
                item.dump()
                
            else:
                s = str(item).replace('\n', ' ')
                if len(s) > 30:
                    s = s[:30] + '...'
                print(f"{'   '*self.depth}   - {s}")
                
    # =============================================================================================================================
    # Iterators

    # ----------------------------------------------------------------------------------------------------
    # As dict
    
    def values(self):
        """ Values iterator
        
        Iterate on the direct values only, not the folders.
        
        > [!NOTE] Iterates only on values in this folder.
        > To iterate on sub folders, use <#all_values>
        
        Returns
        -------
        - iterator
        """        
        for value in super().values():
            if not isinstance(value, tdict):
                yield value

    def keys(self):
        """ Keys iterator
        
        Iterate on the direct values only, not the folders.
        
        > [!NOTE] Iterates only on values in this folder.
        > To iterate on sub folders, use <#all_paths>
        
        Returns
        -------
        - iterator
        """        
        for key, value in super().items():
            if not isinstance(value, tdict):
                yield key
                
    def items(self):
        """ Items iterator
        
        Iterate on the direct items only, not the folders.
        
        > [!NOTE] Iterates only on items in this folder.
        > To iterate on sub folders, use <#all_items>
        
        Returns
        -------
        - iterator
        """        
        for key, value in super().items():
            if not isinstance(value, tdict):
                yield key, value
                
    def folders(self):
        """ Folders iterator
        
        Iterate on the direct folders only, not the values.
        
        > [!NOTE] Iterates only on folders directly in this folder.
        > To iterate on sub folders, use <#all_folders>
        
        Returns
        -------
        - iterator
        """        
        for folder in super().values():
            if isinstance(folder, tdict):
                yield folder
                
    def __iter__(self):
        return (key for key in self.keys())

    # ----------------------------------------------------------------------------------------------------
    # All items structure
    # Values first, folders then
    
    def all_values(self):
        """ All values iterator
        
        Iterate on all values in the folder and sub folders.
        
        > [!NOTE] To iterates only on direct values in this folder,
        > use <#values>
        
        Returns
        -------
        - iterator
        """        
        for value in self.values():
            yield value
                
        for folder in self.all_folders():
            for value in folder.values():
                yield value

    def all_paths(self):
        """ All paths iterator
        
        Iterate on all paths in the folder and sub folders.
        
        > [!NOTE] To iterates only on direct keys in this folder,
        > use <#keys>
        
        Returns
        -------
        - iterator
        """        
        for key in self.keys():
            yield key
            
        for folder in self.folders():
            for path in folder.all_paths():
                yield folder.name + '/' + path

    def all_items(self):
        """ All items iterator
        
        Iterate on all items in the folder and sub folders.
        
        > [!NOTE] To iterates only on direct items in this folder,
        > use <#items>
        
        Returns
        -------
        - iterator
        """        
        for key, value in self.items():
            yield key, value

        for folder in self.folders():
            for key, value in folder.all_items():
                yield folder.name + '/' + key, value
                    
    def all_folders(self):
        """ All folders iterator
        
        Iterate on all folders in the folder and sub folders.
        
        > [!NOTE] To iterates only on direct folders in this folder,
        > use <#folders>
        
        Returns
        -------
        - iterator
        """        
        for folder in self.folders():
            
            yield folder
            
            for sub_folder in folder.all_folders():
                yield sub_folder
                    
    # =============================================================================================================================
    # Folder operations

    def new_folder(self, name):
        """ Create a new folder of the given name
        
        Arguments
        ---------
        - name (str) : name or path
        
        Returns
        -------
        - tdict : the created folder
        """
        solve = self._solve_path(name)
        
        folder = tdict()
        solve['folder'][solve['key']] = folder
        
        return folder

    
    def get(self, name, default=None):
        """ Get the object at the given path
        
        Arguments
        ---------
        - name (str) : name or path
        - default (any = None) : returned value if the object doesn't exist
        
        Returns
        -------
        - any 
        """        
        solve = self._solve_path(name)
        if solve['item'] is None:
            return default
        else:
            return solve['item']
        
    def get_folder(self, name, default=None):
        """ Get the folder at the given path
        
        Raises
        ------
        - Exception : if an object is found and is not a folder
        
        Arguments
        ---------
        - name (str) : name or path
        - default (any = None) : returned value if the folder doesn't exist
        
        Returns
        -------
        - tdict
        """        
        item = self.get(name, None)
        if item is None:
            return default
        
        elif not isinstance(item, tdict):
            raise Exception(f"Item '{self.path + '//' + name}' is not a folder")
            
        else:
            return item
        
    def get_value(self, name, default=None):
        """ Get the value at the given path
        
        Raises
        ------
        - Exception : if an object is found and is a folder
        
        Arguments
        ---------
        - name (str) : name or path
        - default (any = None) : returned value if the folder doesn't exist
        
        Returns
        -------
        - tdict
        """        
        item = self.get(name, None)
        if item is None:
            return default
        
        elif isinstance(item, tdict):
            raise Exception(f"Item '{self.path + '//' + name}' is a folder, not a value")
            
        else:
            return item
        
    # =============================================================================================================================
    # Load from Path
    
    @classmethod
    def FromFolder(cls, path, pattern='[!._]*/*'):
        """ Read the content of a drive
        
        Arguments
        ---------
        - path (str) : a valid drive path
        - pattern (str) : a valid pattern for pathlib.Path.glob
        
        Returns
        -------
        - tdict
        """
        root = Path(path)
        td   = tdict()
        
        for path in root.glob(pattern):
            if path.is_dir():
                continue
            td[str(path.relative_to(root))] = path.name
            
        return td
        
                    
    # =============================================================================================================================
    # Dev
    
    @classmethod
    def Test(cls):
        
        test = cls()
        test["A"] = "Content A"
        test["B"] = "Content B"
        test.new_folder("Folder 1")
        test.new_folder("Folder 2/Folder 2.1")
        test.new_folder("Folder 2/Folder 2.2")
        test.new_folder("Folder 3/Folder 3.1/Folder 3.1.1")
        test["Folder 1/A"] = "Content 1 A"
        test["Folder 1/B"] = "Content 1 B"
        test["Folder 2/Folder 2.1/A"] = "Content 2.1 A"
        test["Folder 2/Folder 2.1/B"] = "Content 2.1 B"
        test["Folder 3/Folder 3.1/Folder 3.1.1/A"] = "Content 3.1.1 A"
        test["Folder 3/Folder 3.1/Folder 3.1.1/B"] = "Content 3.1.1 B"
        
        return test
    
    @staticmethod
    def test(td):
        
        import numpy as np
        rng = np.random.default_rng()
        
        def header(title):        
            hrz = '\n' + '-'*80
            print('\n', title, hrz)
            
        def display(item):
            if isinstance(item, tdict):
                return str(item)
                #return f"> {str(item)}"
            else:
                s = str(item).replace('\n', ' ')
                if len(s) > 20:
                    s = s[:20] + '...'
                return f". {s}"
            
        header("Test " + str(td))
        
        header("Dump")
        td.dump()
        
        header("Loop on folders")
        for folder in td.folders():
            print(display(folder))
        print(':'*30)
        for folder in td.all_folders():
            print(display(folder))

        header("Loop on values")
        for value in td.values():
            print(display(value))
        print(':'*30)
        for value in td.all_values():
            print(display(value))

        header("Loop on items")
        for key, value in td.items():
            print(display(value), key)
        print(':'*30)
        for key, value in td.all_items():
            print(display(value), key)
            
        header("Loop on paths")
        for path in td.all_paths():
            print(path)
            
        header("Getting")
        paths = list(td.all_paths())
        for i in rng.integers(0, len(paths), 5):
            item = td.get_value(paths[i])
            assert(item is not None)            
            print(f"{paths[i]} --> {item}")
        print(':'*30)            
        paths = [folder.path for folder in td.all_folders()]
        for i in rng.integers(0, len(paths), 5):
            item = td.get_folder(paths[i])
            assert(item is not None)            
            print(f"{paths[i]} --> {item}")
            
        header("Errors")
        try:
            a = td["ERROR"]
            assert(False)
        except Exception as e:
            print("KEY ERROR>", str(e))
            
        paths = list(td.all_paths())
        for i in rng.integers(0, len(paths), 3):
            path = paths[i]
            a = td.get(path)
            
            try:
                a = td.get_folder(path)
            except Exception as e:
                print("NOT A FOLDER>", str(e))
                
            try:
                a = td.get(path + '/ERROR' )
            except Exception as e:
                print("SOLVE ERROR>", str(e))
                
        
#tdict.test(tdict.Test())
        
        
td = tdict.FromFolder("/Users/alain/Documents/blender/scripts/modules/docgen")      
td.dump()              

        
            


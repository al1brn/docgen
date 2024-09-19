# Path

PurePath subclass that can make system calls.

Path represents a filesystem path but unlike PurePath, also offers
methods to do system calls on path objects. Depending on your system,
instantiating a Path will return either a PosixPath or a WindowsPath
object. You can also instantiate a PosixPath or WindowsPath directly,
but cannot instantiate a WindowsPath on a POSIX system or vice versa.PurePath subclass that can make system calls.

Path represents a filesystem path but unlike PurePath, also offers
methods to do system calls on path objects. Depending on your system,
instantiating a Path will return either a PosixPath or a WindowsPath
object. You can also instantiate a PosixPath or WindowsPath directly,
but cannot instantiate a WindowsPath on a POSIX system or vice versa.

## Content


- A : [absolute](#absolute) :black_small_square: [anchor](#anchor) :black_small_square: [as_posix](#as_posix) :black_small_square: [as_uri](#as_uri)
- C : [chmod](#chmod) :black_small_square: [cwd](#cwd)
- D : [drive](#drive)
- E : [exists](#exists) :black_small_square: [expanduser](#expanduser)
- G : [glob](#glob) :black_small_square: [group](#group)
- H : [hardlink_to](#hardlink_to) :black_small_square: [home](#home)
- I : [is_absolute](#is_absolute) :black_small_square: [is_block_device](#is_block_device) :black_small_square: [is_char_device](#is_char_device) :black_small_square: [is_dir](#is_dir) :black_small_square: [is_fifo](#is_fifo) :black_small_square: [is_file](#is_file) :black_small_square: [is_mount](#is_mount) :black_small_square: [is_relative_to](#is_relative_to) :black_small_square: [is_reserved](#is_reserved) :black_small_square: [is_socket](#is_socket) :black_small_square: [is_symlink](#is_symlink) :black_small_square: [iterdir](#iterdir)
- J : [joinpath](#joinpath)
- L : [lchmod](#lchmod) :black_small_square: [link_to](#link_to) :black_small_square: [lstat](#lstat)
- M : [match](#match) :black_small_square: [mkdir](#mkdir)
- N : [name](#name)
- O : [open](#open) :black_small_square: [owner](#owner)
- P : [parent](#parent) :black_small_square: [parents](#parents) :black_small_square: [parts](#parts)
- R : [read_bytes](#read_bytes) :black_small_square: [read_text](#read_text) :black_small_square: [readlink](#readlink) :black_small_square: [relative_to](#relative_to) :black_small_square: [rename](#rename) :black_small_square: [replace](#replace) :black_small_square: [resolve](#resolve) :black_small_square: [rglob](#rglob) :black_small_square: [rmdir](#rmdir) :black_small_square: [root](#root)
- S : [samefile](#samefile) :black_small_square: [stat](#stat) :black_small_square: [stem](#stem) :black_small_square: [suffix](#suffix) :black_small_square: [suffixes](#suffixes) :black_small_square: [symlink_to](#symlink_to)
- T : [touch](#touch)
- U : [unlink](#unlink)
- W : [with_name](#with_name) :black_small_square: [with_stem](#with_stem) :black_small_square: [with_suffix](#with_suffix) :black_small_square: [write_bytes](#write_bytes) :black_small_square: [write_text](#write_text)
- _ : [_cached_cparts](#_cached_cparts) :black_small_square: [_cparts](#_cparts) :black_small_square: [_drv](#_drv) :black_small_square: [_format_parsed_parts](#_format_parsed_parts) :black_small_square: [_from_parsed_parts](#_from_parsed_parts) :black_small_square: [_from_parts](#_from_parts) :black_small_square: [_hash](#_hash) :black_small_square: [_make_child](#_make_child) :black_small_square: [_make_child_relpath](#_make_child_relpath) :black_small_square: [_parse_args](#_parse_args) :black_small_square: [_parts](#_parts) :black_small_square: [_pparts](#_pparts) :black_small_square: [_root](#_root) :black_small_square: [_scandir](#_scandir) :black_small_square: [_str](#_str)



## Properties

### _cached_cparts


> type _cached_cparts ( = <member '_cached_cparts' of 'P...)



### _cparts


> type property ( = <property object at 0x101421e4...)



### _drv


> type _drv ( = <member '_drv' of 'PurePath' o...)



### _hash


> type _hash ( = <member '_hash' of 'PurePath' ...)



### _parts


> type _parts ( = <member '_parts' of 'PurePath'...)



### _pparts


> type _pparts ( = <member '_pparts' of 'PurePath...)



### _root


> type _root ( = <member '_root' of 'PurePath' ...)



### _str


> type _str ( = <member '_str' of 'PurePath' o...)



### anchor


> type property ( = <property object at 0x1018ad49...)



### drive


> type property ( = <property object at 0x1018ad3f...)



### name


> type property ( = <property object at 0x1018ad4e...)



### parent


> type property ( = <property object at 0x1018ad67...)



### parents


> type property ( = <property object at 0x1018ad6c...)



### parts


> type property ( = <property object at 0x1018ad62...)



### root


> type property ( = <property object at 0x1018ad44...)



### stem


> type property ( = <property object at 0x1018ad5d...)



### suffix


> type property ( = <property object at 0x1018ad53...)



### suffixes


> type property ( = <property object at 0x1018ad58...)



## Methods

### _format_parsed_parts

----------



``` python
_format_parsed_parts(cls, drv, root, parts)
```



Arguments:
- **cls**
- **drv**
- **root**
- **parts**



### _from_parsed_parts

----------



``` python
_from_parsed_parts(cls, drv, root, parts)
```



Arguments:
- **cls**
- **drv**
- **root**
- **parts**



### _from_parts

----------



``` python
_from_parts(cls, args)
```



Arguments:
- **cls**
- **args**



### _make_child

----------



``` python
_make_child(self, args)
```



Arguments:
- **self**
- **args**



### _make_child_relpath

----------



``` python
_make_child_relpath(self, part)
```



Arguments:
- **self**
- **part**



### _parse_args

----------



``` python
_parse_args(cls, args)
```



Arguments:
- **cls**
- **args**



### _scandir

----------



``` python
_scandir(self)
```



Arguments:
- **self**



### absolute

----------



``` python
absolute(self)
```

Return an absolute version of this path by prepending the current
working directory. No normalization or symlink resolution is performed.

Use resolve() to get the canonical path to a file.

Arguments:
- **self**



### as_posix

----------



``` python
as_posix(self)
```

Return the string representation of the path with forward (/)
slashes.

Arguments:
- **self**



### as_uri

----------



``` python
as_uri(self)
```

Return the path as a 'file' URI.

Arguments:
- **self**



### chmod

----------



``` python
chmod(self, mode, *, follow_symlinks=True)
```

Change the permissions of the path, like os.chmod().

Arguments:
- **self**
- **mode**
- **follow_symlinks** ( = True)



### cwd

----------



``` python
cwd(cls)
```

Return a new path pointing to the current working directory
(as returned by os.getcwd()).

Arguments:
- **cls**



### exists

----------



``` python
exists(self)
```

Whether this path exists.

Arguments:
- **self**



### expanduser

----------



``` python
expanduser(self)
```

Return a new path with expanded ~ and ~user constructs
(as returned by os.path.expanduser)

Arguments:
- **self**



### glob

----------



``` python
glob(self, pattern)
```

Iterate over this subtree and yield all existing files (of any
kind, including directories) matching the given relative pattern.

Arguments:
- **self**
- **pattern**



### group

----------



``` python
group(self)
```

Return the group name of the file gid.

Arguments:
- **self**



### hardlink_to

----------



``` python
hardlink_to(self, target)
```

Make this path a hard link pointing to the same file as *target*.

Note the order of arguments (self, target) is the reverse of os.link's.

Arguments:
- **self**
- **target**



### home

----------



``` python
home(cls)
```

Return a new path pointing to the user's home directory (as
returned by os.path.expanduser('~')).

Arguments:
- **cls**



### is_absolute

----------



``` python
is_absolute(self)
```

True if the path is absolute (has both a root and, if applicable,
a drive).

Arguments:
- **self**



### is_block_device

----------



``` python
is_block_device(self)
```

Whether this path is a block device.

Arguments:
- **self**



### is_char_device

----------



``` python
is_char_device(self)
```

Whether this path is a character device.

Arguments:
- **self**



### is_dir

----------



``` python
is_dir(self)
```

Whether this path is a directory.

Arguments:
- **self**



### is_fifo

----------



``` python
is_fifo(self)
```

Whether this path is a FIFO.

Arguments:
- **self**



### is_file

----------



``` python
is_file(self)
```

Whether this path is a regular file (also True for symlinks pointing
to regular files).

Arguments:
- **self**



### is_mount

----------



``` python
is_mount(self)
```

Check if this path is a POSIX mount point

Arguments:
- **self**



### is_relative_to

----------



``` python
is_relative_to(self, *other)
```

Return True if the path is relative to another path or False.

Arguments:
- **self**
- **other**



### is_reserved

----------



``` python
is_reserved(self)
```

Return True if the path contains one of the special names reserved
by the system, if any.

Arguments:
- **self**



### is_socket

----------



``` python
is_socket(self)
```

Whether this path is a socket.

Arguments:
- **self**



### is_symlink

----------



``` python
is_symlink(self)
```

Whether this path is a symbolic link.

Arguments:
- **self**



### iterdir

----------



``` python
iterdir(self)
```

Iterate over the files in this directory.  Does not yield any
result for the special paths '.' and '..'.

Arguments:
- **self**



### joinpath

----------



``` python
joinpath(self, *args)
```

Combine this path with one or several arguments, and return a
new path representing either a subpath (if all arguments are relative
paths) or a totally different path (if one of the arguments is
anchored).

Arguments:
- **self**
- **args**



### lchmod

----------



``` python
lchmod(self, mode)
```

Like chmod(), except if the path points to a symlink, the symlink's
permissions are changed, rather than its target's.

Arguments:
- **self**
- **mode**



### link_to

----------



``` python
link_to(self, target)
```

Make the target path a hard link pointing to this path.

Note this function does not make this path a hard link to *target*,
despite the implication of the function and argument names. The order
of arguments (target, link) is the reverse of Path.symlink_to, but
matches that of os.link.

Deprecated since Python 3.10 and scheduled for removal in Python 3.12.
Use `hardlink_to()` instead.

Arguments:
- **self**
- **target**



### lstat

----------



``` python
lstat(self)
```

Like stat(), except if the path points to a symlink, the symlink's
status information is returned, rather than its target's.

Arguments:
- **self**



### match

----------



``` python
match(self, path_pattern)
```

Return True if this path matches the given pattern.

Arguments:
- **self**
- **path_pattern**



### mkdir

----------



``` python
mkdir(self, mode=511, parents=False, exist_ok=False)
```

Create a new directory at this given path.

Arguments:
- **self**
- **mode** ( = 511)
- **parents** ( = False)
- **exist_ok** ( = False)



### open

----------



``` python
open(self, mode='r', buffering=-1, encoding=None, errors=None, newline=None)
```

Open the file pointed by this path and return a file object, as
the built-in open() function does.

Arguments:
- **self**
- **mode** ( = r)
- **buffering** ( = -1)
- **encoding** ( = None)
- **errors** ( = None)
- **newline** ( = None)



### owner

----------



``` python
owner(self)
```

Return the login name of the file owner.

Arguments:
- **self**



### read_bytes

----------



``` python
read_bytes(self)
```

Open the file in bytes mode, read it, and close the file.

Arguments:
- **self**



### read_text

----------



``` python
read_text(self, encoding=None, errors=None)
```

Open the file in text mode, read it, and close the file.

Arguments:
- **self**
- **encoding** ( = None)
- **errors** ( = None)



### readlink

----------



``` python
readlink(self)
```

Return the path to which the symbolic link points.

Arguments:
- **self**



### relative_to

----------



``` python
relative_to(self, *other)
```

Return the relative path to another path identified by the passed
arguments.  If the operation is not possible (because this is not
a subpath of the other path), raise ValueError.

Arguments:
- **self**
- **other**



### rename

----------



``` python
rename(self, target)
```

Rename this path to the target path.

The target path may be absolute or relative. Relative paths are
interpreted relative to the current working directory, *not* the
directory of the Path object.

Returns the new Path instance pointing to the target path.

Arguments:
- **self**
- **target**



### replace

----------



``` python
replace(self, target)
```

Rename this path to the target path, overwriting if that path exists.

The target path may be absolute or relative. Relative paths are
interpreted relative to the current working directory, *not* the
directory of the Path object.

Returns the new Path instance pointing to the target path.

Arguments:
- **self**
- **target**



### resolve

----------



``` python
resolve(self, strict=False)
```

Make the path absolute, resolving all symlinks on the way and also
normalizing it.

Arguments:
- **self**
- **strict** ( = False)



### rglob

----------



``` python
rglob(self, pattern)
```

Recursively yield all existing files (of any kind, including
directories) matching the given relative pattern, anywhere in
this subtree.

Arguments:
- **self**
- **pattern**



### rmdir

----------



``` python
rmdir(self)
```

Remove this directory.  The directory must be empty.

Arguments:
- **self**



### samefile

----------



``` python
samefile(self, other_path)
```

Return whether other_path is the same or not as this file
(as returned by os.path.samefile()).

Arguments:
- **self**
- **other_path**



### stat

----------



``` python
stat(self, *, follow_symlinks=True)
```

Return the result of the stat() system call on this path, like
os.stat() does.

Arguments:
- **self**
- **follow_symlinks** ( = True)



### symlink_to

----------



``` python
symlink_to(self, target, target_is_directory=False)
```

Make this path a symlink pointing to the target path.
Note the order of arguments (link, target) is the reverse of os.symlink.

Arguments:
- **self**
- **target**
- **target_is_directory** ( = False)



### touch

----------



``` python
touch(self, mode=438, exist_ok=True)
```

Create this file with the given access mode, if it doesn't exist.

Arguments:
- **self**
- **mode** ( = 438)
- **exist_ok** ( = True)



### unlink

----------



``` python
unlink(self, missing_ok=False)
```

Remove this file or link.
If the path is a directory, use rmdir() instead.

Arguments:
- **self**
- **missing_ok** ( = False)



### with_name

----------



``` python
with_name(self, name)
```

Return a new path with the file name changed.

Arguments:
- **self**
- **name**



### with_stem

----------



``` python
with_stem(self, stem)
```

Return a new path with the stem changed.

Arguments:
- **self**
- **stem**



### with_suffix

----------



``` python
with_suffix(self, suffix)
```

Return a new path with the file suffix changed.  If the path
has no suffix, add given suffix.  If the given suffix is an empty
string, remove the suffix from the path.

Arguments:
- **self**
- **suffix**



### write_bytes

----------



``` python
write_bytes(self, data)
```

Open the file in bytes mode, write to it, and close the file.

Arguments:
- **self**
- **data**



### write_text

----------



``` python
write_text(self, data, encoding=None, errors=None, newline=None)
```

Open the file in text mode, write to it, and close the file.

Arguments:
- **self**
- **data**
- **encoding** ( = None)
- **errors** ( = None)
- **newline** ( = None)


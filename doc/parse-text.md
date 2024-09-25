# Text

``` python
Text(text)
```

Implements a simple text reader.

The Text class manages a cursor on a multilines string.
It offers basic function to read around the cursor (backward and forwards).
It also implements features to move to (or after) a target and
to replace a text segment by replacement string.

Properties
----------
- cursor (int) : current position

Arguments
---------
- text (str) : the managed text


#### Arguments:
- **text** (_str_) : the managed text

## cursor

<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>

current position

## \_\_call__

``` python
__call__(start=1, count=None)
```

Read the string around the cursor

One or two argumentscan be passed:
- If only one argument is passed (**count** is None), it is used as the number of chars
  to read after the cursoor
- If two arguments are passed, they are interpreted as the starting position to read
  from and the number of characters to read

 > [!NOTE]
 > The start position is relative to the cursor

 ``` python
 # Read 3 characters from the cursor
 a = text(3)

 # Read the character preceeding the cursor
 b = text(-1, 1)

 # Note that the two following lines return the same result
 c = text()
 c = text.c
 ```

 Arguments
 ---------
 - start (int) : number of characters to read from the cursor if count is None,
   position to start to read otherwise
 - count (int) : number of characters to read, 1 is read if None

 Returns
 -------
 - str : the read characters


#### Arguments:
- **start** ( = 1)
- **count** ( = None)

## c

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

Current character

Note that an error is raised if [c](parse-text.md#c) is True.

``` python
return self.text[self.cursor]
```

Returns
-------
- str : the character at cursor

## eof

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

End of text is reached

Returns
-------
- bool : True if end of text is reached

## eol

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

End of line is reached

Returns
-------
- bool : True if current char is eol (or if eof is True)

## extract_strings

``` python
extract_strings(text)
```

Extract strings from a text and returns the extracted text and the list of extracted strings.

Arguments
---------
- text (str) : the text to extract strings from

Returns
-------
- str : text with strings replaced by 'index'
- list of strs : list of extracted strings


#### Arguments:
- **text** (_str_) : the text to extract strings from



#### Returns:
- **str** : text with strings replaced by 'index'
- **list** : list of extracted strings

## find

``` python
find(target, regex=False, halt=True)
```

Find a target into the text

> [!IMPORTANT]
> The search starts at the cursor

The target can be a single string or a tuple of strings.
The function return the target and the cursor is place just after
the target

An error is raised if the target is not found and **halt** is True.

``` python
text = Text("Search for A B C")

print(text.find("B"))
# > B

text.cursor = 0
print(text.find(("A", "B", "C")))
# > A

print(Text("Find this number: 123!").find(r"\d+"))
# > 123
```

Arguments
---------
- target (str or tuple of strs) : the string(s) to reach
- regex (bool = False) : target is a regular expression or not
- halt (bool = True) : raise an exception if not found

Returns
-------
- int : the new cursor position


#### Arguments:
- **target** (_str or tuple of strs_) : the string(s) to reach
- **regex** (_bool_ = False) : target is a regular expression or not
- **halt** (_bool_ = True) : raise an exception if not found



#### Returns:
- **int** : the new cursor position

## from_cursor

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

Return the text from the cursor.

Returns
-------
- str : text from the cursor

## move

``` python
move(offset=1)
```

Move the cursor of the given offset

Arguments
---------
- offset (int = 1) : cursor offset

Returns
-------
- int : new cursor position


#### Arguments:
- **offset** (_int_ = 1) : cursor offset



#### Returns:
- **int** : new cursor position

## move_after

``` python
move_after(target, regex=False, halt=True)
```

Move the cursor until it reaches the given target.

This function execute a [move_after](parse-text.md#move_after) on the target and places the
cursor just before the target.

``` python
self.find(target)
return self.cursor
```

``` python
text = Text("Go after TARGET: here")

text.move_after("TARGET")
print(text.from_cursor)
# > : here
```

Arguments
---------
- target (str or tuple of strs) : the string(s) to reach

Returns
-------
- int : the new cursor position


#### Arguments:
- **target** (_str or tuple of strs_) : the string(s) to reach
- **regex** ( = False)
- **halt** ( = True)



#### Returns:
- **int** : the new cursor position

## move_to

``` python
move_to(target, regex=False, halt=True)
```

Move the cursor until it reaches the given target.

This function execute a [move_to](parse-text.md#move_to) on the target and places the
cursor just before the target.

``` python
found = self.find(target)
return self.move(-len(found))
```

``` python
text = Text("Just go HERE")

text.move_to("HERE")
print(text.from_cursor)
# > HERE
```

Arguments
---------
- target (str or tuple of strs) : the string(s) to reach

Returns
-------
- int : the new cursor position


#### Arguments:
- **target** (_str or tuple of strs_) : the string(s) to reach
- **regex** ( = False)
- **halt** ( = True)



#### Returns:
- **int** : the new cursor position

## replace

``` python
replace(start, end, repl)
```

Replace the text between two positions by a replacement string.

After the operation, the cursor is placed after the replacement string.

This method return the **replaced** string.

> [!NOTE]
> The **start** and **end** position are absolute positions, note relative
> to the cursor

Typical use is given here below:

```python
line = "Line of text with a token <My Token>."

text = Text(line)
start = text.move_to('<')
end = text.move_after('>')
token = text.replace(start, end, "HERE WAS A TOKEN")

print(text.text)
# Line of text with a token HERE WAS A TOKEN.

print(token)
# <My Token>
```

Arguments
---------
- start (int) : start index of replaced part
- end (int) : end index of replace part
- repl (str) : the replacement string

Returns
-------
- str : the replaced string


#### Arguments:
- **start** (_int_) : start index of replaced part
- **end** (_int_) : end index of replace part
- **repl** (_str_) : the replacement string



#### Returns:
- **str** : the replaced string
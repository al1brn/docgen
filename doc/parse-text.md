# Text

``` python
Text(text)
```

Implements a simple text reader.

The Text class manages a cursor on a multilines string.
It offers basic function to read around the cursor (backward and forwards).
It also implements features to move to (or after) a target and
to replace a text segment by replacement string.

#### Arguments:
- **text** (_str_) : the managed text

----------
### replace

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

#### Arguments:
- **start** (_int_) : start index of replaced part
- **end** (_int_) : end index of replace part
- **repl** (_str_) : the replacement string



#### Returns:
- **str** : the replaced string

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#text) :black_small_square:  :black_small_square: [Methods](parse-text.md#methods)</sub>

## Properties



### c

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

Current character

Note that an error is raised if [c](parse-text.md#c) is True.

``` python
return self.text[self.cursor]
```

### cursor

<table><tbody>
<tr><td>type</td><td><b>int</b></td></tr>
</tbody></table>

current position

### eof

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

End of text is reached

### eol

<table><tbody>
<tr><td>type</td><td><b>bool</b></td></tr>
</tbody></table>

End of line is reached

### from_cursor

<table><tbody>
<tr><td>type</td><td><b>str</b></td></tr>
</tbody></table>

Return the text from the cursor.

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#text) :black_small_square:  :black_small_square: [Text](parse-text.md)</sub>

## Methods



----------
### extract_strings

``` python
extract_strings(text)
```

Extract strings from a text and returns the extracted text and the list of extracted strings.

#### Arguments:
- **text** (_str_) : the text to extract strings from



#### Returns:
- **str** : text with strings replaced by 'index'
- **list** : list of extracted strings

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#text) :black_small_square:  :black_small_square: [Methods](parse-text.md#methods)</sub>

----------
### find

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

#### Arguments:
- **target** (_str or tuple of strs_) : the string(s) to reach
- **regex** (_bool_ = False) : target is a regular expression or not
- **halt** (_bool_ = True) : raise an exception if not found



#### Returns:
- **int** : the new cursor position

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#text) :black_small_square:  :black_small_square: [Methods](parse-text.md#methods)</sub>

----------
### move

``` python
move(offset=1)
```

Move the cursor of the given offset

#### Arguments:
- **offset** (_int_ = 1) : cursor offset



#### Returns:
- **int** : new cursor position

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#text) :black_small_square:  :black_small_square: [Methods](parse-text.md#methods)</sub>

----------
### move_after

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

#### Arguments:
- **target** (_str or tuple of strs_) : the string(s) to reach
- **regex** ( = False)
- **halt** ( = True)



#### Returns:
- **int** : the new cursor position

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#text) :black_small_square:  :black_small_square: [Methods](parse-text.md#methods)</sub>

----------
### move_to

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

#### Arguments:
- **target** (_str or tuple of strs_) : the string(s) to reach
- **regex** ( = False)
- **halt** ( = True)



#### Returns:
- **int** : the new cursor position

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#text) :black_small_square:  :black_small_square: [Methods](parse-text.md#methods)</sub>

----------
### replace

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

#### Arguments:
- **start** (_int_) : start index of replaced part
- **end** (_int_) : end index of replace part
- **repl** (_str_) : the replacement string



#### Returns:
- **str** : the replaced string

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#text) :black_small_square:  :black_small_square: [Methods](parse-text.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#text) :black_small_square:  :black_small_square: [Text](parse-text.md)</sub>
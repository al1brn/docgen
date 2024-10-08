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

## Content

- **C** : [c](parse-text.md#c) :black_small_square: [\_\_call__](parse-text.md#__call__) :black_small_square: [cursor](parse-text.md#cursor)
- **E** : [eof](parse-text.md#eof) :black_small_square: [eol](parse-text.md#eol) :black_small_square: [extract_strings](parse-text.md#extract_strings)
- **F** : [find](parse-text.md#find) :black_small_square: [from_cursor](parse-text.md#from_cursor)
- **M** : [move](parse-text.md#move) :black_small_square: [move_after](parse-text.md#move_after) :black_small_square: [move_to](parse-text.md#move_to)
- **R** : [replace](parse-text.md#replace)

## Properties



### c

> _type_: **str**
>

Current character

Note that an error is raised if [eof](parse-text.md#eof) is True.

``` python
return self.text[self.cursor]
```

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [Text](parse-text.md#text) :black_small_square: [Content](parse-text.md#content) :black_small_square: [Properties](parse-text.md#properties)</sub>

### cursor

> _type_: **int**
>

current position

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [Text](parse-text.md#text) :black_small_square: [Content](parse-text.md#content) :black_small_square: [Properties](parse-text.md#properties)</sub>

### eof

> _type_: **bool**
>

End of text is reached

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [Text](parse-text.md#text) :black_small_square: [Content](parse-text.md#content) :black_small_square: [Properties](parse-text.md#properties)</sub>

### eol

> _type_: **bool**
>

End of line is reached

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [Text](parse-text.md#text) :black_small_square: [Content](parse-text.md#content) :black_small_square: [Properties](parse-text.md#properties)</sub>

### from_cursor

> _type_: **str**
>

Return the text from the cursor.

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [Text](parse-text.md#text) :black_small_square: [Content](parse-text.md#content) :black_small_square: [Properties](parse-text.md#properties)</sub>

## Methods



----------
### \_\_call__()

> method

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

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [Text](parse-text.md#text) :black_small_square: [Content](parse-text.md#content) :black_small_square: [Methods](parse-text.md#methods)</sub>

----------
### extract_strings()

> classmethod

``` python
extract_strings(text)
```

Extract strings from a text and returns the extracted text and the list of extracted strings.

#### Arguments:
- **text** (_str_) : the text to extract strings from



#### Returns:
- **str** : text with strings replaced by 'index'
- **list** : list of extracted strings

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [Text](parse-text.md#text) :black_small_square: [Content](parse-text.md#content) :black_small_square: [Methods](parse-text.md#methods)</sub>

----------
### find()

> method

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

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [Text](parse-text.md#text) :black_small_square: [Content](parse-text.md#content) :black_small_square: [Methods](parse-text.md#methods)</sub>

----------
### move()

> method

``` python
move(offset=1)
```

Move the cursor of the given offset

#### Arguments:
- **offset** (_int_ = 1) : cursor offset



#### Returns:
- **int** : new cursor position

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [Text](parse-text.md#text) :black_small_square: [Content](parse-text.md#content) :black_small_square: [Methods](parse-text.md#methods)</sub>

----------
### move_after()

> method

``` python
move_after(target, regex=False, halt=True)
```

Move the cursor until it reaches the given target.

This function execute a [find](parse-text.md#find) on the target and places the
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

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [Text](parse-text.md#text) :black_small_square: [Content](parse-text.md#content) :black_small_square: [Methods](parse-text.md#methods)</sub>

----------
### move_to()

> method

``` python
move_to(target, regex=False, halt=True)
```

Move the cursor until it reaches the given target.

This function execute a [find](parse-text.md#find) on the target and places the
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

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [Text](parse-text.md#text) :black_small_square: [Content](parse-text.md#content) :black_small_square: [Methods](parse-text.md#methods)</sub>

----------
### replace()

> method

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

##### <sub>:arrow_right: [docgen](index.md#docgen) :black_small_square: [Text](parse-text.md#text) :black_small_square: [Content](parse-text.md#content) :black_small_square: [Methods](parse-text.md#methods)</sub>
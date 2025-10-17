[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Hco_a0_H)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21142178)
# Activity 5: Working with Strings and Lists
For this activity, you will be writing 5 functions within the same Python code file called `activity5.py`.

Arguably one of the things Python does best is strings. It is capable of processing large strings en masse and doing operations on them. 

Today we will analyze a list of *puzzle words* that was compiled as part of the Moby lexicon project. This will also be our first example of Python working with files from our computer.

For this week you also have a text file containing all the words compiled for this project called `CROSSWD.txt`.


## Preamble: Reading files

Python lets you read files stored on your computer and use the data collected within your program. To open a file to read it, we use the `open()` function:

```python
# open takes two arguments: the first argument is the path to the file 
# to read as a string. The second argument is a string indicating what 
# mode the file is to opened in (options being 'w' for writing, 'r' for 
# reading and 'a` for appending to the file)
words_file = open('CROSSWD.txt','r')
```
We can check the type of `words_file`, which is an input/output stream:
```python
type(words_file)
```

And we can check what methods are available to us for `words_file`
```python
# The expression below is what is called a `list comprehension`. 
# In Python, you can 'select' values in a list that satisfy a criteria
# (the if condition at the end). You can see that this looks similar to
# the for loop, just a bit more elegant
print([x for x in dir(words_file) if '_' != x[0]])
```

We can use the `readline()` method to "read" a line from the file. Note that everytime you will call the method for the same file object, you will read the next line (and will return an error if there are no more):

```python
print(words_file.readline())
```

The lines contain the newline `\n` special character (not visible if you print them) in front of our word which we will not need, so we can remove them by using the `.strip()` string method:

```python
print(word.strip())
```

Even better, the file object is an iterable:  meaning we can use it in a for loop:  Note if you code and run the command that follows, you will probably have to stop your code to stop it unless you want to wait a long time.

``` python
for line in words_file:
    ## We decode each line from the file and strip the special characters.
    word = line.decode('utf-8').strip()
    print(word)
```
## Function 1: `more_than_20`

Write a function `twenty_or_more(file)` that takes in a string indicating the path to the file to consider and returns all words read from the file that have more than 20 characters as a list. Note that you will have to open the file indicated in `file` for reading, and iterate over all lines in the file. Also remember that you can add values to a list using the `.append(value)` method

## Function 2: `has_no_e`

Write a function called `has_no_e(word)` that takes a string `word`, and returns `True` if the `word` contains no `e`, otherwise it returns `False`.

## Function 3: `uses_only`

Write a function called `uses_only(word,letters)` that takes in two strings `word` and `letters` and returns `True` if `word` only uses characters from `letters`, otherwise returns `False`

## Function 4: `all_uses_only`

Write a function called `all_uses_only(file, letters)` that takes in two strings `file` representing the file to read and `letters` and returns a list of words that only use characters from `letters`

#### Hint: Your `uses_only` function will be important here




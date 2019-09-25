
# coding: utf-8

# # Libraries
# 
# **Time**
# - Teaching: 5 min
# - Exercises: 5 min
# 
# **Questions**:
# - "How can I use software that other people have written?"
# - "How can I find out what that software does?"
# 
# **Learning Objectives**:
# - "Explain what software libraries are and why programmers create and use them."
# - "Write programs that [import](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#import) and use libraries from Python's standard library."
# - "Find and read [documentation](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#documentation) for standard libraries interactively (in the interpreter) and online."
# 
# *****
# 
# ## Most of the power of a programming language is in its libraries.
# 
# *   A *library* is a collection of functions that can be used by other programs.
#     *   May also contain data values (e.g., numerical constants).
#     *   Library's contents are supposed to be related, but there's no way to enforce that.
# *   Python's [standard library](https://docs.python.org/3/library/) is installed with it.
# *   Many additional libraries are available from [PyPI](https://pypi.python.org/pypi) (the Python Package Index).
# *   We will see later how to write new libraries.
# 
# ## A program must import a library in order to use it.
# 
# *   Use `import` to load a library into a program's memory.
# *   Then refer to things from the library as `library_name.thing_name`.
#     *   Python uses `.` to mean "part of".

# In[1]:


import math

print('pi is', math.pi)
print('cos(pi) is', math.cos(math.pi))


# *   Have to refer to each item with the library's name.
#     *   `math.cos(pi)` won't work: the reference to `pi` doesn't somewhow "inherit" the function's reference to `math`.
# 
# ## Use `help` to find out more about a library's contents.
# 
# *   Works just like help for a function.

# In[ ]:


help(math)


# ## Import specific items from a library to shorten programs.
# 
# *   Use `from...import...` to load only specific items from a library.
# *   Then refer to them directly without the library name as prefix.
# 

# In[ ]:


from math import cos, pi

print('cos(pi) is', cos(pi))


# ## Create an alias for a library when importing it to shorten programs.
# 
# *   Use `import...as...` to give a library a short *alias* while importing it.
# *   Then refer to items in the library using that shortened name.

# In[ ]:


import math as m

print('cos(pi) is', m.cos(m.pi))


# *   Commonly used for libraries that are frequently used or have long names.
#     *   E.g., `matplotlib` plotting library is often aliased as `mpl`.
# *   But can make programs harder to understand,
#     since readers must learn your program's aliases.

# ## Installing a library with `pip`

# While the Anaconda distribution comes with many additional libraries beyond the standard, it may happen that you find a library online that isn't yet installed on your computer. Most of the time, this library will available in [PyPI](https://pypi.python.org/pypi) (the Python Package Index).
# 
# To install from PyPI, simply open a terminal/shell window and type:
# 
# `pip install "name of package"`
# 
# Let's install a popular fuzzy matching library by typing:
# 
# `pip install fuzzywuzzy`
# 
# Once installed, we can import the library and use the `fuzz.ratio` method to compare two strings:

# In[2]:


from fuzzywuzzy import fuzz

print(fuzz.ratio("Andy", "Andy"))


# ## Challenge 1: Locating the Right Library
# 
# You want to select a random value from your data:

# In[ ]:


ids = [1, 2, 3, 4, 5, 6]


# 1. What [standard library][stdlib]    would you most expect to help?
# 2. Which function would you select from that library? Are there alternatives?
# 
# [pypi]: https://pypi.python.org/pypi/
# [stdlib]: https://docs.python.org/3/library/

# ## Challenge 2: Exploring the Math Library
# 
#  1. What function from the `math` library can you use to calculate a square root
#     *without* using `sqrt`?
#  2. Since the library contains this function, why does `sqrt` exist?

# ## Challenge 3: When Is Help Available?
# 
# When a colleague of yours types `help(math)`,
# Python reports an error:
# 
# > ~~~
# > NameError: name 'math' is not defined
# > ~~~
# 
# What has your colleague forgotten to do?

# ## Challenge 4:  Importing With Aliases
# 
# 1. Fill in the blanks so that the program below prints `90.0`.
# 2. Rewrite the program so that it uses `import` *without* `as`.
# 3. Which form do you find easier to read?

# In[ ]:


import math as m
angle = ____.degrees(____.pi / 2)
print(____)


# ## Challenge 5: Importing Everything
# 
# We can uses the `*` character to import everything from a library, and then refer to each item by name without a prefix.

# In[ ]:


from math import *
print(pi)


# Why would't programmers always use this form of import?

# *****
# ## Keypoints
# 
# - "Most of the power of a programming language is in its libraries."
# - "A program must import a [library](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#library) in order to use it."
# - "Use `help` to find out more about a library's contents."
# - "Import specific items from a library to shorten programs."
# - "Create an alias for a library when importing it to shorten programs."

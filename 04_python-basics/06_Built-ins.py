
# coding: utf-8

# # Built-in Functions and Help
# 
# **Time**:
# - Teaching: 10 min
# - Exercises: 20 min
# 
# **Questions**
# - "How can I use built-in functions?"
# - "How can I find out what they do?"
# 
# **Learning Objectives**
# - "Explain the purpose of functions."
# - "Correctly call built-in Python functions."
# - "Correctly nest calls to built-in functions."
# - "Use help to display [documentation](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#documentation) for built-in functions."
# 
# *****

# ## A function may take zero or more arguments.
# 
# *   We have seen some functions already --- now let's take a closer look.
# *   An *argument* is a value passed into a function.
# *   `len` takes exactly one.
# *   `int`, `str`, and `float` create a new value from an existing one.
# *   `print` takes zero or more.
# *   `print` with no arguments prints a blank line.
#     *   Must always use parentheses, even if they're empty,
#         so that Python knows a function is being called.

# In[1]:


print('before')
print()
print('after')


# ## Commonly-used built-in functions include `max`, `min`, and `round`.
# 
# *   Use `max` to find the largest value of one or more values.
# *   Use `min` to find the smallest.
# *   Both work on character strings as well as numbers.
#     *   "Larger" and "smaller" use (0-9, A-Z, a-z) to compare letters.

# In[1]:


print(max(1, 2, 3))
print(min('a', 'A', '0'))


# ## Functions may only work for certain (combinations of) arguments.
# 
# *   `max` and `min` must be given at least one argument.
#     *   "Largest of the empty set" is a meaningless question.
# *   And they must be given things that can meaningfully be compared.
# 

# In[1]:


print(max(1, 'a'))


# ## Functions may have default values for some arguments.
# 
# *   `round` will round off a floating-point number.
# *   By default, rounds to zero decimal places.

# In[2]:


round(3.712)


# *   We can specify the number of decimal places we want.
# 

# In[3]:


round(3.712, 1)


# ## Use the built-in function `help` to get help for a function.
# 
# *   Every built-in function has online documentation.

# In[ ]:


help(round)


# ## The Jupyter Notebook has two ways to get help.
# 
# *   Place the cursor inside the parenthesis of the function,
#     hold down `shift`,
#     and press `tab`.
# *   Or type a function name with a question mark after it.
# 
# ## Every function returns something.
# 
# *   Every [function call](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#function-call) produces some result.
# *   If the function doesn't have a useful result to return,
#     it usually returns the special value `None`.

# In[4]:


result = print('example')
print('result of print is', result)


# ## Difference between Function, Method, Object
#   
# A **function** is a piece of code that is called by name. It can be passed data to operate on (ie. the parameters) and can optionally return data (the return value).
# 
# A **method** is a function which is tied to a particular object. Each of an object's methods typically implements one of the things it can do, or one of the questions it can answer. It is called using the dot notation: e.g. `object.method()`
# 
# An **object** is a collection of conceptually related grouping of variables (called "members") and functions using those variables (called "methods"). Every [object](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#object) is an instance of a `class`, which is like a blueprint for an object. 
# 
#   - Everything that exists is an object.
#   - Everything that happens is a function call.
#   
# Read more about objects, classes and methods [here](https://www.jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming)
# 
# Check out our Python glossary [here](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md).

# ## Challenge 1: What Happens When
# 
# 1. Explain in simple terms the order of operations in the following program:
#     when does the addition happen, when does the subtraction happen,
#     when is each function called, etc.
# 2. What is the final value of `radiance`?

# In[ ]:


radiance = 1.0
radiance = max(2.1, 2.0 + min(radiance, 1.1 * radiance - 0.5))


# ## Challenge 2: Spot the Difference
# 
# 1. Predict what each of the `print` statements in the program below will print.
# 2. Does `max(len(rich), poor)` run or produce an error message?
#    If it runs, does its result make any sense?

# In[5]:


rich = "gold"
poor = "tin"
print(max(rich, poor))
print(max(len(rich), len(poor)))


# ## Challenge 3: Why Not?
# 
# Why don't `max` and `min` return `None` when they are given no arguments?

# ## Challenge 4: Counting Text

# Below is a string of Robert Frost's "The Road Not Taken":

# In[3]:


poem = '''Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;

Then took the other, as just as fair,
And having perhaps the better claim,
Because it was grassy and wanted wear;
Though as for that the passing there
Had worn them really about the same,

And both that morning equally lay
In leaves no step had trodden black.
Oh, I kept the first for another day!
Yet knowing how way leads on to way,
I doubted if I should ever come back.

I shall be telling this with a sigh
Somewhere ages and ages hence:
Two roads diverged in a wood, and I—
I took the one less traveled by,
And that has made all the difference.'''


# Using the `len` function and the string methods, answer the following questions:
# 
# How many characters (letters) are in the poem?

# In[4]:


len(poem)


# How many words?

# In[11]:





# How many lines? (HINT: A line break is represented as  `\n`  )

# How many stanzas?

# How many unique words? (HINT: look up what `set` does)

# Remove commas and check the number of unique words again. Why is it different?

# *****
# # Keypoints:
# - "A function may take zero or more arguments."
# - "Commonly-used built-in functions include `max`, `min`, and `round`."
# - "Functions may only work for certain (combinations of) arguments."
# - "Functions may have default values for some arguments."
# - "Use the built-in function `help` to get help for a function."
# - "The Jupyter Notebook has two ways to get help."
# - "Every function returns something."


# coding: utf-8

# # Errors and Exceptions
# 
# **Time**
# - teaching: 10 min
# - exercises: 10 min
# 
# **Questions**:
# - "How do a read an error message?"
# - "What do the error messages mean?"
# - "How do a fix an error?"
# - "What if I still can't figure it out?"
# 
# **Learning Objectives**:
# 
# *   To be able to read a traceback, and determine the following relevant pieces of information:
#     * The file, function, and line number on which the error occurred
#     * The type of the error
#     * The error message
# *   To be able to describe the types of situations in which the following errors occur:
#     * `SyntaxError` and `IndentationError`
#     * `NameError`
#     * `IndexError` and `TypeError`
#     * `IOError`
# *   Debug code containing an error systematically.
# 
# *****
# 
# ## Every programmer encounters errors
# * both those who are just beginning, and those who have been programming for years.
# * Encountering errors and exceptions can be very frustrating at times
# * But understanding what the different types of errors are
# and when you are likely to encounter them can help a lot.
# * Once you know *why* you get certain types of errors,
# they become much easier to fix.
# 
# ## Errors in Python come in specific form, called a [traceback](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#traceback).
# 
# Let's examine one:

# In[1]:


import errors_01
errors_01.favorite_ice_cream()


# - This particular [traceback](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#traceback) has two levels.
# - You can determine the number of levels by looking for the number of arrows on the left hand side.
# - The last level is the actual place where the error occurred.
# - The other level(s) show what function the program executed to get to the next level down.
# 
# So, in this case, the program:
# 
# 1. first performed a [function call](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#function-call) to the function `favorite_ice_cream`.
# 
# 2. Inside this function, the program encountered an error on Line 7, when it tried to run the code `print ice_creams[3]`.
# 
# ## Long Tracebacks
# 
# > Sometimes, you might see a traceback that is very long -- sometimes they might even be 20 levels deep!
# > This can make it seem like something horrible happened,
# > but really it just means that your program called many functions before it ran into the error.
# > Most of the time,
# > you can just pay attention to the bottom-most level,
# > which is the actual place where the error occurred.
# 
# So what error did the program actually encounter?
# 
# ## Python  tells us the category or [type of error](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#type-of-error) 
# 
# In this case, it is an `IndexError`. Python then prints a more detailed error message (in this case, it says "list index out of range").
# 
# - If you encounter an error and don't know what it means, it is still important to read the traceback closely.
# - That way, if you fix the error, but encounter a new one, you can tell that the error changed.
# - sometimes just knowing *where* the error occurred is enough to fix it, even if you don't entirely understand the message.
# 
# 
# ## Python reports a [syntax error](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#syntax-error) when it can't understand the source of a program.
# 
# - People can typically figure out what is meant by text with no punctuation,
# but people are much smarter than computers.
# - If Python doesn't know how to read the program,
# it will just give up and inform you with an error.
# For example:

# In[4]:


def some_function()
    msg = "hello, world!"
    print(msg)
     return msg


# - Here, Python tells us that there is a `SyntaxError` on line 1,
# and even puts a little arrow in the place where there is an issue.
# - In this case the problem is that the function definition is missing a colon at the end.
# 
# ## Indentation is meaningful in Python
# - If we fix the problem with the colon,
# we see that there is *also* an `IndentationError`,
# which means that the lines in the function definition do not all have the same indentation:

# In[ ]:


def some_function():
    msg = "hello, world!"
    print(msg)
     return msg


# - Both `SyntaxError` and `IndentationError` indicate a problem with the syntax of your program,
# but an `IndentationError` is more specific:
# it *always* means that there is a problem with how your code is indented.
# 
# ## Tabs and Spaces
# 
# > A quick note on indentation errors:
# > they can sometimes be insidious,
# > especially if you are mixing spaces and tabs.
# > Because they are both [whitespace](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#whitespace),
# > it is difficult to visually tell the difference.
# > The IPython notebook actually gives us a bit of a hint,
# > but not all Python editors will do that.
# > In the following example,
# > the first two lines are using a tab for indentation,
# > while the third line uses four spaces:

# In[ ]:


def some_function():
    msg = "hello, world!"
    print(msg)
	return msg


# ## A `NameError`, and occurs when you try to use a variable that does not exist
# 
# For example:

# In[5]:


print(a)


# Why did you get this error?
# 
# - you might have meant to use a [string](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#string), but forgot to put quotes around it:

# In[6]:


print(hello)


# - or you just forgot to create the variable before using it.
# - In the following example,
# `count` should have been defined (e.g., with `count = 0`) before the for loop:

# In[7]:


for number in range(10):
    count = count + number
print("The count is: " + str(count))


# - or you might have made a typo when you were writing your code.

# In[ ]:


Count = 0
for number in range(10):
    count = count + number
print("The count is: " + str(count))


# ## Type and Index Errors
# 
# - Next up are errors having to do with containers (like lists and dictionaries) and the items within them. 
# - If you try to access an item in a list or a dictionary that does not exist,
# then you will get an error.

# In[ ]:


letters = ['a', 'b', 'c']
print("Letter #1 is " + letters[0])
print("Letter #2 is " + letters[1])
print("Letter #3 is " + letters[2])
print("Letter #4 is " + letters[3])


# Here, Python is telling us that there is an `IndexError` in our code, meaning we tried to access a list index that did not exist.
# 
# A similar error occurs when we confuse types; that is, when we try to use a [method](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#method) or syntax relevant to one type on another type that doesn't like it.

# In[ ]:


a_dictionary = {'beyonce', 'is', 'the', 'greatest'}
a_list = [a_dictionary]

a_list['name']


# ## File Errors
# 
# - The last type of error we'll cover today are those associated with reading and writing files: `IOError`.
# 
# - If you try to read a file that does not exist,
# you will recieve an `IOError` telling you so.

# In[ ]:


file_handle = open('myfile.txt', 'r')


# - One reason for receiving this error is that you specified an incorrect path to the file.
# - Or you could be using the "read" flag instead of the "write" flag.

# In[ ]:


file_handle = open('myfile.txt', 'w')
file_handle.read()


# ## Challenges 1: Reading Error Messages
# 
# Read the traceback below, and identify the following pieces of information about it:
# 
# 1.  How many levels does the traceback have?
# 2.  What is the file name where the error occurred?
# 3.  What is the function name where the error occurred?
# 4.  On which line number in this function did the error occurr?
# 5.  What is the type of error?
# 6.  What is the error message?

# In[ ]:


import errors_02
errors_02.print_friday_message()


# ## Challenge 2. Identifying Syntax Errors
# 
# 1. Read the code below, and (without running it) try to identify what the errors are.
# 2. Run the code, and read the error message. Is it a `SyntaxError` or an `IndentationError`?
# 3. Fix the error.
# 4. Repeat steps 2 and 3, until you have fixed all the errors.

# In[ ]:


def another_function
  print "Syntax errors are annoying."
   print"But at least python tells us about them!"
  print "So they are usually not too hard to fix."


# ## Challenge 3. Identifying Variable Name Errors
# 
# 1. Read the code below, and (without running it) try to identify what the errors are.
# 2. Run the code, and read the error message. What type of `NameError` do you think this is? In other words, is it a [string](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#string) with no quotes, a misspelled variable, or a variable that should have been defined but was not?
# 3. Fix the error.
# 4. Repeat steps 2 and 3, until you have fixed all the errors.

# In[ ]:


for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    if (Number % 3) == 0:
        message = message + a
    else:
        message = message + "b"
print(message)


# ## Challenge 4. Identifying Item Errors
# 
# 1. Read the code below, and (without running it) try to identify what the errors are.
# 2. Run the code, and read the error message. What type of error is it?
# 3. Fix the error.

# In[ ]:


seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[4])


# ## Debugging Strategies
# 
# ### Know what it's supposed to do
# 
# The first step in debugging something is to *know what it's supposed to do*. "My program doesn't work" isn't good enough: in order to diagnose and fix problems, we need to be able to tell correct output from incorrect. If we can write a test case for the failing case --- i.e., if we can assert that with *these* inputs, the function should produce *that* result --- then we're ready to start debugging. If we can't, then we need to figure out how we're going to know when we've fixed things.
# 
# ### Start with a simplified case.
# 
# If you're writing a multi-step loop or function, start with one case and get to work. Then ask what you need to do to generalize to many cases.
# 
# ### Divide and conquer
# 
# We want to localize the failure to the smallest possible region of code. The smaller the gap between cause and effect, the easier the connection is to find. Many programmers therefore use a **divide and conquer** strategy to find bugs, i.e., if the output of a function is wrong, they check whether things are OK in the middle, then concentrate on either the first or second half, and so on.
# 
# ### Change One Thing at a Time, For a Reason
# 
# Replacing random chunks of code is unlikely to do much good. (After all, if you got it wrong the first time, you'll probably get it wrong the second and third as well.) Good programmers therefore *change one thing at a time, for a reason*. They are either trying to gather more information ("is the bug still there if we change the order of the loops?") or test a fix ("can we make the bug go away by sorting our data before processing it?").
# 
# Every time we make a change, however small, we should re-run our tests immediately, because the more things we change at once, the harder it is to know what's responsible for what.
# 
# ### Outside Resources
# 
# If you've tried everything you can think of to logically fix the error and still don't understand what Python is trying to tell you, now the real searching begins. Go to Google and copy/paste the error, you're probably not the only one who has run into it!

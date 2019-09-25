
# coding: utf-8

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

# In[1]:


import errors_02
errors_02.print_friday_message()


# How many levels does the traceback have?
# <br>2
# 
# What is the file name where the error occurred?
# <br>main file
# 
# What is the function name where the error occurred?
# <br>errors_02.print_friday_message()
# 
# On which line number in this function did the error occurr?
# <br>1
# 
# What is the type of error?
# <br>ImportError
# 
# What is the error message?
# <br>No module named 'errors_02'

# ## Challenge 2. Identifying Syntax Errors
# 
# 1. Read the code below, and (without running it) try to identify what the errors are.
# 2. Run the code, and read the error message. Is it a `SyntaxError` or an `IndentationError`?
# 3. Fix the error.
# 4. Repeat steps 2 and 3, until you have fixed all the errors.

# In[2]:


def another_function():
    print("Syntax errors are annoying.")
    print("But at least python tells us about them!")
    print("So they are usually not too hard to fix.")


# `SyntaxError`

# ## Challenge 3. Identifying Variable Name Errors
# 
# 1. Read the code below, and (without running it) try to identify what the errors are.
# 2. Run the code, and read the error message. What type of `NameError` do you think this is? In other words, is it a [string](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#string) with no quotes, a misspelled variable, or a variable that should have been defined but was not?
# 3. Fix the error.
# 4. Repeat steps 2 and 3, until you have fixed all the errors.

# In[3]:


for number in range(10):
    # use a if the number is a multiple of 3, otherwise use b
    message = ""
    if (number % 3) == 0:
        message = message + "a"
    else:
        message = message + "b"
print(message)


# Number is not defined because Number != number

# ## Challenge 4. Identifying Item Errors
# 
# 1. Read the code below, and (without running it) try to identify what the errors are.
# 2. Run the code, and read the error message. What type of error is it?
# 3. Fix the error.

# In[4]:


seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[3])


# Python starts index at 0!

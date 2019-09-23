
# coding: utf-8

# # Functions
# 
# **Time**
# 
# - Teaching: 10 min
# - Exercises: 15 min
# 
# **Questions**:
# 
# - "How can I avoid rewriting code that I will use again?"
# 
# **Learning Objectives**:
# 
# - "Understand what a function is and why it's helpful."
# - "Understand how to define a function and its arguments."
# - "Understand what `return` does."
# - "Write a basic function."
# * * * * *

# ## Functions are the basic building blocks of programs.
# 
# * Functions are the basic building blocks that we use to store chunks of code we'll want to use again later. 
# * Specifically, they do three things:
#     1. They name pieces of code the way variables name strings and numbers.
#     2. They take arguments, or data that you want to do something on.
#     3. Using 1 and 2 they let you make your own "mini-scripts" or "tiny commands."
# * The details are pretty simple, but this is one of those ideas where it's good to get lots of practice!
#     
# 
# ## Define a function using `def` with a name, parameters, and a block of code.
# 
# *   Begin the definition of a new function with `def`.
# *   Followed by the name of the function.
#     *   Must obey the same rules as variable names.
# *   The *parameters* are defined in parentheses.
#     *   Empty parentheses if the function doesn't take any inputs.
#     *   We will discuss this in detail in a moment.
# *   Then a colon.
# *   Then an indented block of code.

# In[5]:


def print_greeting():
    print('Hello!')


# ## Defining a function does not run it!!!
# 
# *   Defining a function does not run it.
#     *   Like assigning a value to a variable.
# *   Must call the function to execute the code it contains.
# 

# In[6]:


print_greeting()


# ## Arguments in call are matched to parameters in definition.
# 
# *   Functions are most useful when they can operate on different data.
# *   Specify *parameters* when defining a function.
#     *   These become variables when the function is executed.
#     *   Are assigned the arguments in the call (i.e., the values passed to the function).
# 

# In[7]:


def print_date(year, month, day):
    joined = str(year) + '/' + str(month) + '/' + str(day)
    print(joined)

print_date(1871, 3, 19)


# *   Via [Twitter](https://twitter.com/minisciencegirl/status/693486088963272705):
#     `()` contains the ingredients for the function
#     while the [body](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#body) contains the recipe.
# 
# ## Functions may return a result to their caller using `return`.
# 
# *   Use `return ...` to give one (and only one) value back to the caller.
# *   May occur anywhere in the function.
# *   But functions are easier to understand if `return` occurs:
#     *   At the start to handle special cases.
#     *   At the very end, with a final result.
# 

# In[2]:


def average(values):
    if len(values) == 0:
        return None
    return sum(values) / len(values)


# In[3]:


a = average([1, 3, 4])
print('average of actual values:', a)


# In[4]:


print('average of empty list:', average([]))


# *   Remember: [every function returns something](https://github.com/dlab-berkeley/python-intensive/blob/master/Day_1/06_Built-ins.ipynb).
# *   A function that doesn't explicitly `return` a value automatically returns `None`.
# 

# In[ ]:


result = print_date(1871, 3, 19)
print('result of call is:', result)


# ## Challenge 1: Definition and Use
# 
# What does the following program print?

# In[9]:


def report(pressure):
    print('pressure is', pressure)
    
print('calling', report, 22.5)


# ## Challenge 2: Change the Names
# 
# Fill in the blanks to create a function that takes a name like "Rochelle Terman" and returns that name in uppercase and reversed, like "TERMAN, ROCHELLE"

# In[ ]:


def long_function(name_string):
    upper_case = name_string.____ # make upper
    upper_case_list = upper_case._____ # turn into a list
    first_name = ______ # take first name
    last_name = _______ # take last name
    reversed_name = ________ # reverse and separate by a comma and space
    return(reversed_name)


# ## Challenge 3: Order of Operations
# 
# See what the following programs prints

# In[ ]:


result = print_date(1871, 3, 19)
print('result of call is:', result)


# Explain why the two lines of output appeared in the order they did.

# ## Challenge 4: Calling by Name
# 
# What does this short program print?

# In[ ]:


def print_date(year, month, day):
    joined = str(year) + '/' + str(month) + '/' + str(day)
    print(joined)

print_date(day=1, month=2, year=2003)


# When and why is it useful to call functions this way?

# ## Challenge 5: Find the substring
# 
# In our project, we'll be dealing with texts like this (from Djibouti's 2013 review):

# In[ ]:


rec_1 = "143.1 Pursue efforts to ratify international human rights instruments (Kuwait);" 
rec_2 = "143.2 Ratify the international human rights instruments to which Djibouti is not yet party (Niger);" 
rec_3 = "143.3 Carry on with the ratification of international conventions (Democratic Republic of Congo);" 
rec_4 = "143.4 Speed up measures aimed at ratifying the Optional Protocol to CEDAW (Republic of Moldova);" 


# As you see, the recommending country is always at the end of the line in parentheses.
# 
# Write a function that accepts a recommendation (a string) and returns the recommending country (also a string)

# In[ ]:


def get_country:
    # your code here

# uncomment to test your code
get_country(rec_1)


# Modify the function above to return a [`tuple`](http://www.tutorialspoint.com/python/python_tuples.htm) with element 0 being the country name, and element 1 being the recommendation as a string:

# In[ ]:


def get_country_rec:
    # your code here


# uncomment to test your code
get_country_rec(rec_1)


# *****
# ## Keypoints
# 
# 1. Functions are the basic building blocks of programs.
# 2. Define a function using `def` with a name, parameters, and a block of code.
# 3. Defining a function does not run it
# 4. Arguments in call are matched to parameters in definition.
# 5. Functions may return a result to their caller using return.

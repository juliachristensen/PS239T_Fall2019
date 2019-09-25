
# coding: utf-8

# ## Challenge 1: Locating the Right Library
# 
# You want to select a random value from your data:

# In[1]:


ids = [1, 2, 3, 4, 5, 6]


# 1. What [standard library][stdlib]    would you most expect to help?
# 2. Which function would you select from that library? Are there alternatives?
# 
# [pypi]: https://pypi.python.org/pypi/
# [stdlib]: https://docs.python.org/3/library/

# In[2]:


import random
print(random.choice(ids))


# ## Challenge 2: Exploring the Math Library
# 
#  1. What function from the `math` library can you use to calculate a square root
#     *without* using `sqrt`?
#  2. Since the library contains this function, why does `sqrt` exist?

# In[3]:


import math
print(math.pow(4, .5))
print(math.sqrt(4))


# `sqrt` is faster, more optimized for computers

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

# In[4]:


import math  # import!
help(math)


# ## Challenge 4:  Importing With Aliases
# 
# 1. Fill in the blanks so that the program below prints `90.0`.
# 2. Rewrite the program so that it uses `import` *without* `as`.
# 3. Which form do you find easier to read?

# In[5]:


import math as m
angle = m.degrees(m.pi / 2)
print(angle)


# In[6]:


import math
angle = math.degrees(math.pi / 2)
print(angle)


# ## Challenge 5: Importing Everything
# 
# We can uses the `*` character to import everything from a library, and then refer to each item by name without a prefix.

# In[7]:


from math import *
print(pi)


# Why would't programmers always use this form of import?

# Cluttered namespace!

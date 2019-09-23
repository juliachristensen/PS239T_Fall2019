
# coding: utf-8

# # Lists
# 
# **Time**
# - teaching: 10 min
# - exercises: 15 min
# 
# **Questions**:
# - "How do I organize several data types in an ordered manner?"
# - "How can I modify this collection of data?"
# 
# **Learning Objectives**:
# - "Understand how to create and modify a list"
# - "Understand what a list can and can't do"
# - "Become familiar with common list methods"
# * * * * *
# 
# A list is an ordered, indexable collection of data. Lets say you're doing a study on the following countries:
# 
#     country:
#     
#     "Afghanistan"
#     "Canada"
#     "Sierra Leone"
#     "Denmark"
#     "Japan"
# 
# You could put that data into a list 
# 
# * contain data in square brackets `[...]`, 
# * each value is separated by a comma `,`.

# In[1]:


country_list = ["Afghanistan", "Canada", "Sierra Leone", "Denmark", "Japan"]
type(country_list)


# * Use `len` to find out how many values are in a list.

# In[2]:


len(country_list)


# ## Use an item’s [index](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#index) to fetch it from a list.
# 
# * Each value in a list is stored in a particular location.
# * Locations are numbered from 0 rather than 1.
# * Use the location’s index in square brackets to access the value it contains.

# In[3]:


print('the first item is:', country_list[0])
print('the fourth item is:', country_list[3])


# * Lists can be indexed from the back using a negative index. 

# In[4]:


print(country_list[-1])
print(country_list[-2])


# ## "Slice" a list using `[ : ]`
# 
# * Just as with strings, we can get multiple items from a list using splicing
# * Note that the first index is included, while the second is excluded

# In[ ]:


print(country_list[1:4])


# * Leave an index blank to get everything from the beginning / end

# In[ ]:


print(country_list[:4])


# In[ ]:


print(country_list[2:])


# ## Lists’ values can be replaced by assigning to specific indices.

# In[5]:


country_list[0] = "Iran"
print('Country List is now:', country_list)


# * This makes lists different from strings. 
# * You cannot change the characters in a [string](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#string) after it has been created.
#     *   *Immutable*: cannot be changed after creation.
#     *   In contrast, lists are *mutable*: they can be modified in place.

# In[6]:


mystring = "Donut"
mystring[0] = 'C'


# Mutable also means that any other variables pointing to a list will be changed accordingly:

# In[4]:


new_list = country_list
print("new_list: ", new_list)

country_list[0] = "India"
print("new_list: ", new_list)


# ## Lists have Methods
# 
# * Just like strings have methods, lists do too. 
#    * Remember that a [method](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#method) is like a function, but tied to a particular object.
#    * Use `object_name.method_name` to call methods.
#    * IPython lets us do tab completion after a dot ('.') to see what an object has to offer.

# In[11]:


country_list.sort()
country_list


# * If you want to append items to the end of a list, use the `append` method.

# In[ ]:


country_list.append("United States")
print(country_list)


# ## Use del to remove items from a list entirely.
# 
# * `del list_name[index]` removes an item from a list and shortens the list.
# * Not a function or a method, but a statement in the language.
# 

# In[5]:


print("original list was:", country_list)
del country_list[3]
print("the list is now:", country_list)


# ## Lists may contain values of different types.
# 
# *   A single list may contain numbers, strings, and anything else.

# In[ ]:


complex_list = ['life', 42, 'the universe', [1,2,3]]
print(complex_list)


# * Notice that we put a list inside of a list, which has its own index: 

# In[ ]:


print(complex_list[3])


# 
# ## The empty list contains no values.
# 
# *   Use `[]` on its own to represent a list that doesn't contain any values.
#     *   "The zero of lists."
# *   Helpful as a starting point for collecting values
#     (which we will see in the next episode.)
#     
# ## Indexing beyond the end of the collection is an error.
# 
# *   Python reports an `IndexError` if we attempt to access a value that doesn't exist.
#     *   This is a kind of [runtime error](https://github.com/dlab-berkeley/python-intensive/blob/master/Day_3/15_Errors.ipynb).
#     *   Cannot be detected as the code is parsed
#         because the index might be calculated based on data.

# In[12]:


print(country_list[99])


# ## Challenge 1: Splice It
# 
# If `thing` is a list and `low` and `high` are both non-negative integers:
# 
# 1. What does `thing[low:high]` do?
# 2. What does `thing[low:]` (without a value after the colon) do?
# 3. What does `thing[:high]` (without a value before the colon) do?
# 4. What does `thing[:]` (just a colon) do?
# 5. How long is the list `thing[low:high]`?

# In[14]:


thing=['low','high']
thing[low:]


# ## Challenge 2: Making Strides
# 
# What does the following program print?

# In[15]:


city = 'Berkeley'
print(city[::2])
print(city[::-1])


# 1. If we write a [slice](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#slice) as low:high:stride, what does stride do?
# 2. What expression would select all of the even-numbered items from a collection?

# ## Challenge 3: Append vs. Extend
# 
# Using the program below, can you tell the difference between the `append` method and the `extend` method?

# In[6]:


pantry_1 = ['bread', 'pasta', 'beans', 'cereal']
pantry_2 = ['bread', 'pasta', 'beans', 'cereal']
new_items = ['granola bars', 'cookies']
pantry_1.append(new_items)
pantry_2.extend(new_items)
print('append does this:', pantry_1)
print('extend does this:', pantry_2)


# ## Challenge 4: Index
# 
# I've created a (long) list for you below. Use the `.index()` method to find out what the index number is for `Waldo`

# In[ ]:


Wheres_Waldo = ["Anna", "Shad", "Rachel", "Maura", "Jason", "Matt", "Konrad", "Justine", "Sarah", "Laura",                 "Chelsea", "Nina", "Dierdre", "Julian", "Waldo", "Naniette", "Melissa", "Biz", "Elsa", "Demetria",                "Liz", "Olivia", "Will", "Ogi", "Melanie", "Jessica"]


# ## Challenge 5:  join
# 
# Read the help file for the `join` method. 
# 
# Using the join method, concatenate all the values in this list into one string:

# In[ ]:


letters = ['s', 'p', 'a', 'm']


# Now use the `join` method to make one string with all the names from the list `Wheres_Waldo`, which prints each name on a separate line. (HINT: Remember a new line is represented by `\n`

# Reverse the order of the names:

# # Keypoints
# 
# 1. A list stores many values in a single structure.
# 2. Use an item’s index to fetch it from a list.
# 3. Lists’ values can be replaced by assigning to them.
# 4. Appending items to a list lengthens it.
# 5. Use del to remove items from a list entirely.
# 6. The empty list contains no values.
# 7. Lists may contain values of different types.
# 8. Character strings are immutable.
# 9. Indexing beyond the end of the collection is an error.

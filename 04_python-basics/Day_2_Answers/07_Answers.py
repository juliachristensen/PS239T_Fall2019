
# coding: utf-8

# ## Challenge 1: Splice It
# 
# If `thing` is a list and `low` and `high` are both non-negative integers:
# 
# 1. What does `thing[low:high]` do?
# 2. What does `thing[low:]` (without a value after the colon) do?
# 3. What does `thing[:high]` (without a value before the colon) do?
# 4. What does `thing[:]` (just a colon) do?
# 5. How long is the list `thing[low:high]`?

# In[1]:


thing = [1, 4, 3, 6, 3, 6, 7]

low = 2
high = 5

print(thing[low:high])
print(thing[low:])
print(thing[:high])
print(thing[:])
print(len(thing[low:high]))


# ## Challenge 2: Making Strides
# 
# What does the following program print?

# In[30]:


city = 'Berkeley'
print(city[:-2])


print(city[::-2])
print(city[::-1])


# 1. If we write a [slice](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#slice) as low:high:stride, what does stride do?
# 2. What expression would select all of the even-numbered items from a collection?

# In[3]:


numbers = list(range(1,51))
print(numbers)


# In[4]:


print(numbers[1::2])


# ## Challenge 3: Append vs. Extend
# 
# Using the program below, can you tell the difference between the `append` method and the `extend` method?

# In[1]:


pantry_1 = ['bread', 'pasta', 'beans', 'cereal']
pantry_2 = ['bread', 'pasta', 'beans', 'cereal']
new_items = ['granola bars', 'cookies']
pantry_1.append(new_items)
pantry_2.extend(new_items)
print('append does this:', pantry_1)
print('extend does this:', pantry_2)


# In[6]:


pantry_1[4][0]


# ## Challenge 4: Index
# 
# I've created a (long) list for you below. Use the `.index()` method to find out what the index number is for `Waldo`

# In[6]:


Wheres_Waldo = ["Anna", "Shad", "Rachel", "Maura", "Jason", "Matt", "Konrad", "Justine", "Sarah", "Laura",                 "Chelsea", "Nina", "Dierdre", "Julian", "Waldo", "Naniette", "Melissa", "Biz", "Elsa", "Demetria",                "Liz", "Olivia", "Will", "Ogi", "Melanie", "Jessica"]


# In[7]:


Wheres_Waldo.index("Waldo")


# ## Challenge 5:  join
# 
# Read the help file for the `join` method. 
# 
# Using the join method, concatenate all the values in this list into one string:

# In[8]:


letters = ['s', 'p', 'a', 'm']


# In[9]:


print(''.join(letters))


# Now use the `join` method to make one string with all the names from the list `Wheres_Waldo`, which prints each name on a separate line. (HINT: Remember a new line is represented by `\n`

# In[10]:


print('\n'.join(Wheres_Waldo))


# Reverse the order of the names:

# In[11]:


print('\n'.join(Wheres_Waldo[::-1]))


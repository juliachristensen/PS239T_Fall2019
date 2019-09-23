
# coding: utf-8

# ## Challenge 1: Reversing a String
# 
# Fill in the blanks in the program below so that it prints "nit"
# (the reverse of the original character string "tin").

# In[4]:


original = "tin"
result = ""
for char in original:
    result = char + result
    print(char)
    print(result)
print(result)


# ### BONUS: How can you do this in one line with stride?

# In[2]:


original[::-1]


# ## Challenge 2: Practice Accumulating
# 
# Fill in the blanks in each of the programs below
# to produce the indicated result.

# In[7]:


# Total length of the strings in the list: ["red", "green", "blue"] => 12
total = 0
for word in ["red", "green", "blue"]:
    total = total + len(word)
print(total)


# In[8]:


# List of word lengths: ["red", "green", "blue"] => [3, 5, 4]
lengths = []
for word in ["red", "green", "blue"]:
    lengths.append(len(word))
print(lengths)


# In[9]:


# Concatenate all words: ["red", "green", "blue"] => "redgreenblue"
words = ["red", "green", "blue"]
result = ""
for c in words:
    result = ''.join(words)
print(result)


# In[10]:


# Create acronym: ["red", "green", "blue"] => "RGB"
# write the whole thing

ac = ""
for c in words:
    ac += c[0].upper()
print(ac)


# ## Challenge 3: Multiple Operations
# 
# Below is a list of presidents. Create a new list that contains only the last name of each president.
# 
# (HINT: Look at string methods!)

# In[11]:


presidents_full = ["George Washington", "John Adams", "Thomas Jefferson", "James Madison", "James Monroe",         "John Quincy Adams", "Andrew Jackson", "Martin Van Buren", "William Henry Harrison", "John Tyler",         "James K. Polk", "Zachary Taylor", "Millard Fillmore", "Franklin Pierce", "James Buchanan",         "Abraham Lincoln", "Andrew Johnson", "Ulysses S. Grant", "Rutherford B. Hayes", "James A. Garfield",         "Chester A. Arthur", "Grover Cleveland", "Benjamin Harrison", "Grover Cleveland", "William McKinley",         "Theodore Roosevelt", "William Howard Taft", "Woodrow Wilson", "Warren G. Harding", "Calvin Coolidge",         "Herbert Hoover", "Franklin D. Roosevelt", "Harry S. Truman", "Dwight D. Eisenhower", "John F. Kennedy",         "Lyndon B. Johnson", "Richard Nixon", "Gerald Ford", "Jimmy Carter", "Ronald Reagan", "George H. W. Bush",         "Bill Clinton", "George W. Bush", "Barack Obama"]


# In[12]:


last_names = []
for p in presidents_full:
    l_name = p.split()[-1]
    last_names.append(l_name)


# In[13]:


last_names


# Now sort the list alphabetically by last name (HINT: look up `sorted`):

# In[14]:


sorted(last_names)


# In[15]:


sorted(presidents_full, key=lambda x: x.split()[-1])


# ## Challenge 4: Range
# 
# Using `range` and a for loop, calculate the factorial of 42 (the product of all integers up to and including 42).

# In[12]:


factorial = 1
for num in range(1, 43):
    factorial *= num

print(factorial)


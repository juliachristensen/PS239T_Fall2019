
# coding: utf-8

# ## Challenge 1: Trimming Values
# 
# Fill in the blanks so that this program creates a new list
# containing zeroes where the original list's values were negative
# and ones where the origina list's values were positive.
# 

# In[1]:


original = [-1.5, 0.2, 0.4, 0.0, -1.3, 0.4]
result = []
for value in original:
    if value < 0:
        result.append(0)
    else:
        result.append(1)
print(result)


# ## Challenge 2: String Conditionals
# 
# Here are our presidents again. Create a list of all the presidents whose last name starts with the letter B.
# 

# In[2]:


presidents_full = ["George Washington", "John Adams", "Thomas Jefferson", "James Madison", "James Monroe",         "John Quincy Adams", "Andrew Jackson", "Martin Van Buren", "William Henry Harrison", "John Tyler",         "James K. Polk", "Zachary Taylor", "Millard Fillmore", "Franklin Pierce", "James Buchanan",         "Abraham Lincoln", "Andrew Johnson", "Ulysses S. Grant", "Rutherford B. Hayes", "James A. Garfield",         "Chester A. Arthur", "Grover Cleveland", "Benjamin Harrison", "Grover Cleveland", "William McKinley",         "Theodore Roosevelt", "William Howard Taft", "Woodrow Wilson", "Warren G. Harding", "Calvin Coolidge",         "Herbert Hoover", "Franklin D. Roosevelt", "Harry S. Truman", "Dwight D. Eisenhower", "John F. Kennedy",         "Lyndon B. Johnson", "Richard Nixon", "Gerald Ford", "Jimmy Carter", "Ronald Reagan", "George H. W. Bush",         "Bill Clinton", "George W. Bush", "Barack Obama"]


# In[3]:


b_pres = []

for p in presidents_full:
    if p.split()[-1][0] == "B":
        b_pres.append(p)

print(b_pres)


# ## Challenge 3: Find the rhyming words

# Below are the first two stanzas of "row, row, row your boat":

# In[2]:


song = '''Row, row, row your boat
Gently down the stream,
Merrily merrily, merrily, merrily
Life is but a dream.

Row, row, row your boat
Gently down the brook,
If you catch a little fish 
Let it off the hook.'''


# Using string methods, for loops, and conditionals, write some code to `print` only the rhyming words (HINT: we'll be simplistic and assume it rhymes if the last 3 characters are the same)

# In[14]:


for char in ".,":
    song = song.replace(char, "")

song.split()[13][3:]


# In[4]:


for w in song.split():
    for other_w in song.split():
        if w[-3:] == other_w[-3:] and w.lower() != other_w.lower():
            print(w)


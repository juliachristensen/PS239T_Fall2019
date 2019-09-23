
# coding: utf-8

# # Loops
# 
# **Time**
# - Teaching: 10 min
# - Exercises: 15 min
# 
# **Questions**:
# - "How can I make a program do many things?"
# 
# **Learning Objectives**:
# - "Explain what for loops are normally used for."
# - "Trace the execution of a simple (unnested) loop and correctly state the values of variables in each iteration."
# - "Write for loops that use the Accumulator pattern to aggregate values."
# * * * * *

# ## A *for loop* executes commands once for each value in a collection.
# 
# *   Doing calculations on the values in a list one by one
#     is as painful as working with `pressure_001`, `pressure_002`, etc.
# *   A *for loop* tells Python to execute some statements once for each value in a list,
#     a character string,
#     or some other collection.
# *   "for each thing in this group, do these operations"
# 

# In[ ]:


for number in [2, 3, 5]:
    print(number)


# *   This `for` loop is equivalent to:

# In[ ]:


print(2)
print(3)
print(5)


# ## The first line of the `for` loop must end with a colon, and the [body](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#body) must be indented.
# 
# *   The colon at the end of the first line signals the start of a *block* of statements.
# *   Python uses indentation rather than `{}` or `begin`/`end` to show *nesting*.
#     *   Any consistent indentation is legal, but almost everyone uses four spaces.

# In[ ]:


for number in [2, 3, 5]:
print(number)


# ## A `for` loop is made up of a collection, a loop variable, and a body.

# In[ ]:


for number in [2, 3, 5]:
    print(number)


# *   The collection, `[2, 3, 5]`, is what the loop is being run on.
# *   The body, `print(number)`, specifies what to do for each value in the collection.
# *   The loop variable, `number`, is what changes for each *iteration* of the loop.
#     *   The "current thing".
# 
# ## Loop variables can be called anything!!!
# 
# *   As with all variables, loop variables are:
#     *   Created on demand.
#     *   Meaningless: their names can be anything at all.
#     *   Placeholders for the loop

# In[ ]:


for kitten in [2, 3, 5]:
    print(kitten)


# ## The body of a loop can contain many statements.
# 
# *   But no loop should be more than a few lines long.
# *   Hard for human beings to keep larger chunks of code in mind.

# In[ ]:


primes = [2, 3, 5]
for p in primes:
    squared = p ** 2
    cubed = p ** 3
    print(p, squared, cubed)


# 
# ## Use `range` to iterate over a [sequence](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#sequence) of numbers.
# 
# *   The built-in function `range` produces a sequence of numbers.
#     *   *Not* a list: the numbers are produced on demand
#         to make looping over large ranges more efficient.
# *   `range(N)` is the numbers 0..N-1
#     *   Exactly the legal indices of a list or character [string](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#string) of length N
# 

# In[ ]:


print('a range is not a list:', range(3))
for number in range(3):
    print(number)


# ## The Accumulator pattern turns many values into one.
# 
# *   A common pattern in programs is to:
#     1.  Initialize an *accumulator* variable to zero, the empty string, or the empty list.
#     2.  Update the variable with values from a collection.
#     
# If only one [argument](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#argument) is given to `range`, the minimum will default to 0. But two arguments may also be given:
# 

# In[ ]:


# Sum the first 10 integers.
total = 0
for number in range(1, 11): # start at one, end at 10
   total = total + number
print(total)


# *   Read `total = total + number` as:
#     *   Add the current value of the [loop variable](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#loop-variable) `number` to the current value of the accumulator variable `total`.
#     *   Assign this new value to to `total`, replacing the current value.
#     
# Instead of writing `total = total + number`, this can be simplified to `total += number`. This will reassign total to the current value of total plus the current value of number:

# In[ ]:


# Sum the first 10 integers.
total = 0
for number in range(1, 11): # start at one, end at 10
   total += number
print(total)


# # The Accumulator pattern works on lists, too

# In[1]:


values = [1, 2, 3, 4, 8, 9, 10]

squared_values = []
for x in values:
    squared_values.append(x**2)

print(squared_values)


# ## Challenge 1: Reversing a String
# 
# Fill in the blanks in the program below so that it prints "nit"
# (the reverse of the original character string "tin").

# In[ ]:


original = "tin"
result = ____
for char in original:
    result = ____
print(result)


# ### BONUS: How can you do this in one line with stride?

# ## Challenge 2: Practice Accumulating
# 
# Fill in the blanks in each of the programs below
# to produce the indicated result.

# In[ ]:


# Total length of the strings in the list: ["red", "green", "blue"] => 12
total = 0
for word in ["red", "green", "blue"]:
    ____ = ____ + len(word)
print(total)


# In[ ]:


# List of word lengths: ["red", "green", "blue"] => [3, 5, 4]
lengths = ____
for word in ["red", "green", "blue"]:
    lengths = lengths.____(____)
print(lengths)


# In[ ]:


# Concatenate all words: ["red", "green", "blue"] => "redgreenblue"
words = ["red", "green", "blue"]
result = ____
for ____ in ____:
    ____
print(result)


# In[ ]:


# Create acronym: ["red", "green", "blue"] => "RGB"
# write the whole thing


# ## Challenge 3: Multiple Operations
# 
# Below is a list of presidents. Create a new list that contains only the last name of each president.
# 
# (HINT: Look at string methods!)

# In[ ]:


presidents_full = ["George Washington", "John Adams", "Thomas Jefferson", "James Madison", "James Monroe",         "John Quincy Adams", "Andrew Jackson", "Martin Van Buren", "William Henry Harrison", "John Tyler",         "James K. Polk", "Zachary Taylor", "Millard Fillmore", "Franklin Pierce", "James Buchanan",         "Abraham Lincoln", "Andrew Johnson", "Ulysses S. Grant", "Rutherford B. Hayes", "James A. Garfield",         "Chester A. Arthur", "Grover Cleveland", "Benjamin Harrison", "Grover Cleveland", "William McKinley",         "Theodore Roosevelt", "William Howard Taft", "Woodrow Wilson", "Warren G. Harding", "Calvin Coolidge",         "Herbert Hoover", "Franklin D. Roosevelt", "Harry S. Truman", "Dwight D. Eisenhower", "John F. Kennedy",         "Lyndon B. Johnson", "Richard Nixon", "Gerald Ford", "Jimmy Carter", "Ronald Reagan", "George H. W. Bush",         "Bill Clinton", "George W. Bush", "Barack Obama"]


# Now sort the list alphabetically by last name (HINT: look up `sorted`):

# ## Challenge 4: Range
# 
# Using `range` and a for loop, calculate the factorial of 42 (the product of all integers up to and including 42).

# *****
# # Keypoints:
# - "A *for loop* executes commands once for each value in a collection."
# - "The first line of the `for` loop must end with a colon, and the body must be indented."
# - "A `for` loop is made up of a collection, a loop variable, and a body."
# - "Loop variables can be called anything."
# - "The body of a loop can contain many statements."
# - "Use `range` to iterate over a sequence of numbers."
# - "The Accumulator pattern turns many values into one."

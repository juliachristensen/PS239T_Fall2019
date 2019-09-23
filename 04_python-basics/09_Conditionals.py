
# coding: utf-8

# # Conditionals
# 
# **Time**
# 
# - Teaching: 10 min
# - Exercises: 15 min
# 
# **Questions**:
# 
# - "How can programs do different things for different data?"
# 
# **Learning Objectives**:
# 
# - "Correctly write programs that use if and else statements and simple [Boolean expressions](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#boolean-operators) (without logical operators)."
# - "Trace the execution of unnested conditionals and conditionals inside loops."
# keypoints:
# - "Use `if` statements to control whether or not a block of code is executed."
# - "Conditionals are often used inside loops."
# - "Use `else` to execute a block of code when an `if` condition is *not* true."
# - "Use `elif` to specify additional tests."
# - "Conditions are tested once, in order."
# * * * * *

# ## Use `if` statements to control whether or not a block of code is executed.
# 
# *   An `if` statement (more properly called a *conditional* statement)
#     controls whether some block of code is executed or not.
# *   Structure is similar to a `for` statement:
#     *   First line opens with `if` and ends with a colon
#     *   Body containing one or more statements is indented (usually by 4 spaces)
# 

# In[ ]:


age = 84
if age > 60:
    print(age, 'is old')

age = 20
if age > 60:
    print (age, 'is large')


# 
# ## Conditionals are often used inside loops.
# 
# *   Not much point using a conditional when we know the value (as above).
# *   But useful when we have a collection to process.

# In[ ]:


ages = [20, 43, 12, 88, 67]
for age in ages:
    if age > 60:
        print(age, 'is old')


# ## Use `else` to execute a block of code when an `if` condition is *not* true.
# 
# *   `else` is always attached to `if`.
# *   Allows us to specify an alternative to execute when the `if` *branch* isn't taken.
# 

# In[ ]:


ages = [20, 43, 12, 88, 67]
for age in ages:
    if age > 60:
        print(age, 'is old')
    else:
        print(age, 'is not old')


# ## Use `elif` to specify additional tests.
# 
# *   May want to provide several alternative choices, each with its own test.
# *   Use `elif` (short for "else if") and a condition to specify these.
# *   Always associated with an `if`.
# *   Must come before the `else` (which is the "catch all").

# In[ ]:


ages = [20, 43, 12, 88, 67]
for age in ages:
    if age > 60:
        print(age, 'is old')
    elif age > 40:
        print(age, 'is middle-aged')
    else:
        print(age, 'is young')


# # Use [boolean operators](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#boolean-operators) to make complex statements
# 
# I can also generate more complex conditional statements with boolean operators
# like **and** and **or**, and use comparators like "<", ">"

# In[ ]:


ages = [20, 43, 12, 88, 67]
for age in ages:
    if age > 65 or age < 16:
        print(age, 'is outside the labor force')
    else:
        print(age, 'is in the labor force')


# ## Conditions are tested once, in order.
# 
# *   Python steps through the branches of the conditional in order, testing each in turn.
# *   So ordering matters.

# In[ ]:


grade = 85
if grade >= 70:
    print('grade is C')
elif grade >= 80:
    print('grade is B')
elif grade >= 90:
    print('grade is A')


# *   Conditionals do *not* automatically go back and re-evaluate if values change.

# In[ ]:


population = 10000
if population > 200000:
    print('large city')
else:
    print('small city')
    population = 500000


# *   Often use conditionals in a loop to "evolve" the values of variables.
# 

# In[ ]:


population = 10000
for i in range(5): # execute the loop 5 times
    print(i, ':', population)
    if population > 200000:
        print('large city')
        population -= 5000
    else:
        print('small city')
        population += 75000

print('final population:', population)


# ## Challenge 1: Trimming Values
# 
# Fill in the blanks so that this program creates a new list
# containing zeroes where the original list's values were negative
# and ones where the original list's values were positive.
# 

# In[ ]:


original = [-1.5, 0.2, 0.4, 0.0, -1.3, 0.4]
result = ____
for value in original:
    if ____:
        result.append(0)
    else:
        ____
print(result)


# ## Challenge 2: String Conditionals
# 
# Here are our presidents again. Create a list of all the presidents whose last name starts with the letter B.
# 

# In[ ]:


presidents_full = ["George Washington", "John Adams", "Thomas Jefferson", "James Madison", "James Monroe",         "John Quincy Adams", "Andrew Jackson", "Martin Van Buren", "William Henry Harrison", "John Tyler",         "James K. Polk", "Zachary Taylor", "Millard Fillmore", "Franklin Pierce", "James Buchanan",         "Abraham Lincoln", "Andrew Johnson", "Ulysses S. Grant", "Rutherford B. Hayes", "James A. Garfield",         "Chester A. Arthur", "Grover Cleveland", "Benjamin Harrison", "Grover Cleveland", "William McKinley",         "Theodore Roosevelt", "William Howard Taft", "Woodrow Wilson", "Warren G. Harding", "Calvin Coolidge",         "Herbert Hoover", "Franklin D. Roosevelt", "Harry S. Truman", "Dwight D. Eisenhower", "John F. Kennedy",         "Lyndon B. Johnson", "Richard Nixon", "Gerald Ford", "Jimmy Carter", "Ronald Reagan", "George H. W. Bush",         "Bill Clinton", "George W. Bush", "Barack Obama"]


# ## Challenge 3: Find the rhyming words

# Below are the first two stanzas of "row, row, row your boat":

# In[ ]:


song = '''Row, row, row your boat
Gently down the stream,
Merrily merrily, merrily, merrily
Life is but a dream.

Row, row, row your boat
Gently down the brook,
If you catch a little fish 
Let it off the hook.'''


# Using string methods, for loops, and conditionals, write some code to `print` only the rhyming words (HINT: we'll be simplistic and assume it rhymes if the last 3 characters are the same)

# *****
# 
# ## Keypoints
# 
# 1. Use `if` statements to control whether or not a block of code is executed.
# 2. Conditionals are often used inside loops.
# 3. Use `else` to execute a block of code when an `if` condition is *not* true.
# 4. Use `elif` to specify additional tests.
# 5. Use boolean operators to make complex statements.
# 6. Conditions are tested once, in order.

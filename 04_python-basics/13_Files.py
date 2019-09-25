
# coding: utf-8

# # Files 
# 
# **Time**
# - Teaching: 10 min
# - Exercises: 5 min
# 
# **Questions**:
# - "How do a open a file and read its contents?"
# - "How do I write a file with the variables I generated?"
# 
# **Learning Objectives**:
# - "Learn the Pythonic way of reading in files."
# - "Understand how to read/write text files and csv files."
# - "Understand how to use pandas to read a csv file"
# * * * * *
# 
# In this lesson we will cover how to read and write files.

# ## Reading from a file
# 
# Reading a file requires three steps:
# 
# 1. Opening the file
# 2. Reading the file
# 3. Closing the file

# In[6]:


my_file = open("example.txt")
text = my_file.read()
my_file.close()

print(text)


# - However, use the `with open` syntax and this will automatically close files for you. 

# In[ ]:


# better code
with open('example.txt') as my_file:
    text = my_file.read()
    
print(text)


# `with` will keep the file open as long as the program is still in the indented block, once outside, the file is no longer open, and you can't access the contents, only what you have saved to a variable.

# ## Reading a file as a list
# 
# - Very often we want to read in a file line by line, storing those lines as a list.
# - To do that, we can use the `for line in my_file` syntax:

# In[ ]:


stored = []
with open('example.txt') as my_file:
    for line in my_file:
        stored.append(line)


# In[ ]:


stored


# - We can use the `strip` [method](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#method) to get rid of those line breaks at the end

# In[ ]:


stored = []
with open('example.txt') as my_file:
    for line in my_file:
        stored.append(line.strip())


# In[ ]:


stored


# ## Writing to a file
# 
# We can use the `with open` syntax for writing files as well.

# In[ ]:


# this is okay...
new_file = open("example2.txt", "w")
bees = ['bears', 'beats', 'Battlestar Galactica']
for i in bees:
    new_file.write(i + '\n')
new_file.close()


# In[ ]:


# but this is better...
bees = ['bears', 'beats', 'Battlestar Galactica']
with open('example2.txt', 'w') as new_file:
    for i in bees:
        new_file.write(i + '\n')


# In[ ]:


cat example2.txt


# ## Using the CSV Module
# 
# A common task in programming is reading a csv file. 
# - In python, a common way to do that is to read a csv as a list of dictionaries. 
# - For this, we use the `csv` module

# In[1]:


import csv


# In[2]:


#read csv and read into a list of dictionaries
capitals = [] # make empty list
with open('capitals.csv', 'r') as csvfile: # open file
    reader = csv.DictReader(csvfile) # create a reader
    for row in reader: # loop through rows
        capitals.append(row) # append each row to the list


# In[3]:


capitals[:5]


# - Writing a list of dictionaries as a CSV is similar:

# In[4]:


# get the keys in each dictionary
keys = capitals[1].keys()
keys


# # with open('capitals2.csv', 'w') as output_file:
#     dict_writer = csv.DictWriter(output_file, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(capitals)

# ## Challenge 1: Read in a list
# 
# The file `counties.txt` has a column of counties in California. Read in the data into a list called `counties`.

# ## Challenge 2: Writing a CSV file
# 
# Below is a list of dictionaries representing US states. Write this [object](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#object) as a CSV file called `states.csv`

# In[ ]:


states = [{'state': 'Ohio', 'population': 11.6, 'year in union': 1803, 'state bird': 'Northern cardinal', 'capital': 'Columbus'},
          {'state': 'Michigan', 'population': 9.9, 'year in union': 1837, 'capital': 'Lansing'},
          {'state': 'California', 'population': 39.1, 'year in union': 1850, 'state bird': 'California quail', 'capital': 'Sacramento'},
          {'state': 'Florida', 'population': 20.2, 'year in union': 1834, 'capital': 'Tallahassee'},
          {'state': 'Alabama', 'population': 4.9, 'year in union': 1819, 'capital': 'Montgomery'}]


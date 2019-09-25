
# coding: utf-8

# ## Challenge 1: Read in a list
# 
# The file `counties.txt` has a column of counties in California. Read in the data into a list called `counties`.

# In[1]:


with open("../counties.txt", "r") as f:  # from Answers folder must cd up one level
    counties = f.read()
    
print(counties)


# ## Challenge 2: Writing a CSV file
# 
# Below is a list of dictionaries representing US states. Write this [object](https://github.com/dlab-berkeley/python-intensive/blob/master/Glossary.md#object) as a CSV file called `states.csv`

# In[2]:


states = [{'state': 'Ohio', 'population': 11.6, 'year in union': 1803, 'state bird': 'Northern cardinal', 'capital': 'Columbus'},
          {'state': 'Michigan', 'population': 9.9, 'year in union': 1837, 'capital': 'Lansing'},
          {'state': 'California', 'population': 39.1, 'year in union': 1850, 'state bird': 'California quail', 'capital': 'Sacramento'},
          {'state': 'Florida', 'population': 20.2, 'year in union': 1834, 'capital': 'Tallahassee'},
          {'state': 'Alabama', 'population': 4.9, 'year in union': 1819, 'capital': 'Montgomery'}]


# In[3]:


import csv
keys = states[2].keys()  # have to index one without state bird, or add for all
with open('states.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(states)



# coding: utf-8

# ## Challenge 1: Definition and Use
# 
# What does the following program print?

# In[1]:


def report(pressure):
    print('pressure is', pressure)
    
print('calling', report, 22.5)


# ## Challenge 2: Change the Names
# 
# Fill in the blanks to create a function that takes a name like "Rochelle Terman" and returns that name in uppercase and reversed, like "TERMAN, ROCHELLE"

# In[3]:


def long_function(name_string):
    upper_case = name_string.upper() # make upper
    upper_case_list = upper_case.split() # turn into a list
    first_name = upper_case_list[0] # take first name
    last_name = upper_case_list[1] # take last name
    reversed_name = last_name + ", " + first_name # reverse and separate by a comma and space
    return(reversed_name)

long_function("John Doe")
long_function("John Doe Agnihotri")


# In one line:

# In[5]:


def long_function(name_string):
    return ', '.join(name_string.upper().split()[::-1])


long_function("Rochelle Terman Agnihotri")


# ## Challenge 3: Order of Operations
# 
# See what the following programs prints

# In[4]:


def print_date(year, month, day):
    joined = str(year) + '/' + str(month) + '/' + str(day)
    print(joined)

result = print_date(1871, 3, 19)
print('result of call is:', result)


# Explain why the two lines of output appeared in the order they did.

# ## Challenge 4: Calling by Name
# 
# What does this short program print?

# In[5]:


def print_date(year, month, day):
    joined = str(year) + '/' + str(month) + '/' + str(day)
    print(joined)

print_date(day=1, month=2, year=2003)


# When and why is it useful to call functions this way?

# ## Challenge 5: Find the substring
# 
# In our project, we'll be dealing with texts like this (from Djibouti's 2013 review):

# In[6]:


rec_1 = "143.1 Pursue efforts to ratify international human rights instruments (Kuwait);" 
rec_2 = "143.2 Ratify the international human rights instruments to which Djibouti is not yet party (Niger);" 
rec_3 = "143.3 Carry on with the ratification of international conventions (Democratic Republic of Congo);" 
rec_4 = "143.4 Speed up measures aimed at ratifying the Optional Protocol to CEDAW (Republic of Moldova);" 


# In[12]:


rec = "143.1 Pursue efforts to ratify international human rights instruments (Kuwait);" 
pieces = rec.split("(")
pieces
end = pieces[-1]
end[:-2]


# As you see, the recommending country is always at the end of the line in parentheses.
# 
# Write a function that accepts a recommendation (a string) and returns the recommending country (also a string)

# In[7]:


def get_country(rec):
    pieces = rec.split("(")
    end = pieces[-1]
    country = end[:-2]
    return country

get_country(rec_3)


# In one line:

# In[8]:


def get_country(rec):
    return rec.split("(")[-1][:-2]

get_country(rec_3)


# Modify the function above to return a [`tuple`](http://www.tutorialspoint.com/python/python_tuples.htm) with element 0 being the country name, and element 1 being the recommendation as a string:

# In[9]:


def get_country_rec(rec):
    pieces = rec.split("(")
    end = pieces[-1]
    front = pieces[0]
    country = end[:-2]
    
    front_words = front.split()[1:]
    front_rec = ' '.join(front_words)

    return (country, front_rec)

country_and_rec = get_country_rec(rec_3)


# In[10]:


print(country_and_rec[0])
print(country_and_rec[1])


# In one line--**DON'T EVER WRITE CODE LIKE THIS**:

# In[11]:


def get_country_rec(rec):
    return (rec.split("(")[-1][:-2], ' '.join(rec.split("(")[0].split()[1:]))

get_country_rec(rec_3)


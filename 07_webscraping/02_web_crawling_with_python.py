
# coding: utf-8

# # Web crawling
# 
# The following content heavily draws on [Web Scraping with Python](https://proquest.safaribooksonline.com/book/programming/python/9781491985564) (2018) by Ryan Mitchell.
# 
# - First, we learn how create a list of URLs from a webpage.
# - Second, we learn how to crawl through the list of these URLs.

# ## Web crawling 
# 
# The idea behind web scrawling is recursion. Instead of scraping one web page, we do the same process over and over different web pages (or websites) using Uinform Resource locations (or URLs). Since web crawling substantially increases work load of the target's server, do this very carefully again within *technical*, *legal*, and *ethical* boundaries.  

# ### Create a list of URLs
# 
# Since we're studying computational methods, let's look at the list of past winners of Turing Award -- the computer science equivalent to Nobel prizes and collect links from the URL.
# 

# To begin with, let's find out whether we can gain access to the web page.

# In[1]:


from urllib.request import urlopen 
from urllib.error import HTTPError
from urllib.error import URLError

try:
    page = urlopen('https://en.wikipedia.org/wiki/Turing_Award')
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server is broken")
else:
    print("The site is working")





# Then, let's scrap the table and the find the element (the URLs of the prize winners) we need.

# In[2]:


from bs4 import BeautifulSoup

soup = BeautifulSoup(page, "html.parser")


wiki_table = soup.find('table',{'class':'wikitable'})


# Find some patterns we can exploit.

# In[3]:


import re

wiki_table.find_all('tr')[1].find_all('td')[0].find('a').get('href') # first winner
wiki_table.find_all('tr')[2].find_all('td')[0].find('a').get('href') # second winner


# Calculate the total number of prize winners. Remember each row in the table contains information about a prize winner.

# In[4]:


winners=len(wiki_table.find_all('tr')) 


# In[5]:


links = []

for i in range(0,winners-1):
    if i <= winners:
        links.append(wiki_table.find_all('tr')[i+1].find_all('td')[0].find('a').get('href'))
        print(links[i]) # to check whether we get the right list
    else:
        print("Something is wrong") # for debugging


# **Challenge**
# 
# But we have one problem. The links are not the full URLs we look for. We want "https://en.wikipedia.org/wiki/Alan_Perlis" not "wiki/Alan_Perlis". How can you fix this?

# In[6]:


''.join(["https://en.wikipedia.org",links[0]]) # using join method


# In[7]:


new_links = []

for i in range(0,winners-1):
    if i <= winners-1:
        new_links.append(''.join(["https://en.wikipedia.org",links[i]]))
        print(new_links[i]) # to check whether we get the right list
    else:
        print("Something is wrong") # for debugging


# ### Crawl through the list

# Let's extract the birth information from each of the prize winner's Wikipage.

# In[8]:


try:
    test_page = urlopen(new_links[0])
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server is broken")
else:
    print("The site is working")
    
test_soup = BeautifulSoup(test_page, "html.parser")
test_infobox = test_soup.find("table",{"class":"vcard"})

test_infobox.find(text = re.compile("Born")).find_next().text


# Now we loop the code over the list.

# In[9]:


birth_list = []

for url in new_links:
    req = urlopen(url)
    page = BeautifulSoup(req, 'html.parser')
    birth = page.find("table",{"class":"vcard"}).find(text = re.compile("Born")).find_next().text
    birth_list.append(birth)


# In[10]:


birth_list[0:winners-1]

##birth list cleaned
##regular expressions

birth_list_cleaned=[]

for element in birth_list:
    birth_list_cleaned.append(re.findall('[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]',element))


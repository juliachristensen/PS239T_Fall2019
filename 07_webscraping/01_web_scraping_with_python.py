
# coding: utf-8

# # Web scraping 
# 
# The following content heavily draws on [Web Scraping with Python](https://proquest.safaribooksonline.com/book/programming/python/9781491985564) (2018) by Ryan Mitchell.
# and pythonprogramming.net 
 
# ## Definition
# 
# Web scraping collects data from Web other than using API. You can do that by writing a simple program to query a web server, request data, and parse the HTML data to extract information you need.
# 
# 
# In most cases, collecting data from API is more convenient and legally safe. But when API does not exist, you have to do web scraping within *technical*, *legal*, and *ethical* boundaries. The issues around web scraping are complex because they are tied to Internet security, intellectual property, as well as knowledge as commons.
# 
# I'm only covering the very basics of web scraping. Jaren Haber who's coming to the class on next Weds as a guest lecturer will cover more sophisticated tools (`scrapy` and `selenium`).

# ## Request and respond
# 
# In this tutorial, we use with the wikipedia entry of [List of countries ranked by ethnic and cultural diversity level](https://en.wikipedia.org/wiki/List_of_countries_ranked_by_ethnic_and_cultural_diversity_level). The main idea behind web scraping is to write code that mimics what web browser does. So, we start by learning how to make a request to a website.
# 
# ![Diversity Index](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/List_of_countries_ranked_by_ethnic_and_cultural_diversity_level%2C_List_based_on_Fearon%27s_analysis.png/330px-List_of_countries_ranked_by_ethnic_and_cultural_diversity_level%2C_List_based_on_Fearon%27s_analysis.png)
# List of countries ranked by ethnic and cultural diversity level. List based on Fearon's analysis
# 
# Also, before doing any web scraping, check the website's terms and agreements or [robots.txt](https://en.wikipedia.org/robots.txt) to avoid legal ramifications. In case, if you want to use Python code to extract information from robots.txt, look at [this code](https://stackoverflow.com/questions/43085744/parsing-robots-txt-in-python).
# 
# The below is a simple guideline for reading robots.txt. For more information, please read [this blog post](https://www.promptcloud.com/blog/how-to-read-and-respect-robots-file/#).
# 
# 1. Full access
# ``User-agent:*
# Disallow: ``
# 
# 2. 
# ``User-agent:*
# Disallow:/ ``

# In[1]:


# urlib is a standard Python library and contains functions for requesting data across the web 
from urllib.request import urlopen 
from urllib.error import HTTPError
from urllib.error import URLError

try:
    page = urlopen('https://en.wikipedia.org/wiki/List_of_countries_ranked_by_ethnic_and_cultural_diversity_level')
except HTTPError as e:
    print(e) # The HTTP error: "404 Page Not Found (you messd up)" or 500 Internal Server Error (I messed up)"
except URLError as e:
    print("The server is broken") # No server could be reached 
else:
    print("The site is working") 


# You can read the requested document by  `page.read() `. It shows something. But it's not very informative especially for those who are less familiar with HTML and CSS.

# In[2]:


import requests 

page = requests.get('https://en.wikipedia.org/wiki/List_of_countries_ranked_by_ethnic_and_cultural_diversity_level')

print(page.status_code) # to check whether the down was successful; 200 is a okay sign


# ## Parse
# 
# Python is a great tool for web scraping because its [beautiful soup](https://www.crummy.com/software/BeautifulSoup/) library makes parsing HTML so easy. You can install beautiful soup library in several ways.
# 
# - 1. Unix/Linux: type `sudo apt-get install python-bs4` in terminal. This is same for Windows OS, though you should do it in bash.
# - 2. Mac: `sudo easy_install pip` (in case, you havent't installed pip already) then `pip install beautifulsoup4`
# 

# ### HTML parser

# The most popular parser is html.parser. For malformed HTML documents, lxml and html5lib parsers work better.   

# In[3]:


from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, "html.parser")


# ### Parsing HTML
# 
# You can inspect the document using `print(soup.prettify())`. After exploring the web site of interest, you can extract parts of the document by identifying specific HTML/CSS tags or attributes. 

# In[4]:


print(soup) # Not very informative


# In[5]:


print(soup.prettify()) # Better

# ### Title of the page can be displayed by .title
# ### is it text? 
print(soup.title)
type(soup.title)

# ### You can get text by adding .text
print(soup.title.text)
type(soup.title.text)


##paragraph
print(soup.find('p'))

##all paragraphs?
all_paragraphs=[]
for par in soup.find_all('p'):
    all_paragraphs.append(par.text)

##The syntax of find and find all has a lot of features 
## see web scraping with python for examples    
##find_all(tag, attributes, recursive, text, limit, keywords)
##find(tag, attributes, recursive, text, keywords)

# ### Extracing all urls
all_urls=[]    
for url in soup.find_all('a'):
    all_urls.append(url.get('href'))


# regular expression -- string matching method
##regular expressions?
##modify the search based on a known pattern
import re 

re.search('[a-z]+',all_urls[1])

all_urls_regex=[]    
for url in soup.find_all('a',
                         {'href':re.compile(r'/+')}):
    all_urls_regex.append(url.get('href'))



# In[6]:
# ### Extracing a table
#Pattern find_all(tagName, tagAttributes)
    
wiki_table = soup.find('table', # find element  
                       {'class':'wikitable sortable'}) # find class attribute


# #### Specific solution

# Now, let's learn how to save the country information from the table using a particular attribute.

# In[7]:


country_list = wiki_table('a') # by a (hyperlink)


# In[8]:


country_list[10]


# In[9]:


countries = [] # list container (placeholder)

for country in country_list:
    countries.append(country.get('title')) # we need get('title') to get only title information not 
    # the other elements of beautiful soup objects
    
print(countries)


# #### General solution

# We can scrap the entire table using looping.

# In[10]:


wiki_table.find_all('th') # heading 
#wiki_table.find_all('tr')[1].find_all('td') # to get some ideas about how looping would work 
#len(wiki_table.find_all('tr')[1].find_all('td'))


# We use regular expressions (e.g., `[A-Z]+`) to differentiate strings from numbers (or some other tasks). Regular expressions (regex) are a collection of symbols that replace a long line of searching and sequencing functions with one line-line code. But at the beginning they look so strange. We get to them in more detail when we start talking about text analysis.
# 
# In this tutorial, we just touch the surface:
# 
# 1. +: Matches the preceding character, subexpression, or bracketed character, 1 or more times. a+b+ = aaaab, aaabbb, abbbbb,
# 2. [a-z]: matches any character within the bracket

# In[11]:


 

# create empty lists
rank = []  
country = []
frac_index = []
div_index = []  

for row in wiki_table.find_all('tr'): # for rows 
    cells = row.find_all(['th','td']) # to iterater through each row
    if len(cells) == 4: # no heading
        rank.append(cells[0].find(text=True)) # there's only string 
        country.append(cells[1].find_all(text=re.compile('[A-Z]+')))
        frac_index.append(cells[2].find(text=re.compile('[0-9]+')))
        div_index.append(cells[3].find(text=re.compile('[0-9]+')))
    else:
        print("something is wrong") # for debugging


# ## Turn into a data frame

# Combine these lists as parts of the same data frame.

# In[37]:


import pandas as pd # convention

div_pd = pd.DataFrame() # create a data frame
 
div_pd['rank'] = rank
div_pd['country'] = country
div_pd['ethnic_fractionalization_index'] = frac_index
div_pd['cultural_diversity_index'] = div_index


# In[38]:


div_pd # Oops, I don't like first row 


# In[40]:


div_pd = div_pd.drop(0) # drop the first row


# ## Export the file

# In[36]:


div_pd.to_csv("div_index.csv")

# A different Approach same result?

table = soup.find('table', {'class' : 'wikitable sortable'})
rows = table.findAll('tr')
data_header = []
                            
for row in rows:
    cols = row.find_all(['td','th'])
    cols = [ele.text.strip() for ele in cols]
    print(cols)
    data_header.append(cols) 



import csv

myfile=open('div_index_2.csv', 'w')  
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
wr.writerows(data_header)
myfile.close()
        
###Directly get tables using pandas?

dfs=pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_ranked_by_ethnic_and_cultural_diversity_level')

dfs=pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_ranked_by_ethnic_and_cultural_diversity_level',header=0, attrs={"class":"wikitable sortable"})

dfs[0].to_csv("div_index_3.csv")


###short introduction to plotting in python
import matplotlib.pyplot as plt
plt.scatter(div_pd.ethnic_fractionalization_index, div_pd.cultural_diversity_index)
plt.xlabel('Ethnic Fractionalization')
plt.ylabel('Cultural Diversity')

plt.savefig('First_plot.png')

###Exercise get the table of turing award winners from 
## https://en.wikipedia.org/wiki/Turing_Award

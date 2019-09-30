
# coding: utf-8

# # Accessing Databases via Web APIs: Lecture Code
# * * * * *

# Import required libraries
from __future__ import division
import requests
import urllib
import json
import math


# ## 1. Constructing API GET Request
# 
# In the first place, we know that every call will require us to provide a) a base URL for the API, b) some authorization code or key, and c) a format for the response. So let's put store those in some variables.

# In[14]:

# set key
key="[ADD YOUR KEY HERE]"
key="7iJ3lTTEh7wao3Jr1HR8BUr9D6RQwACA"

# set base url
base_url="http://api.nytimes.com/svc/search/v2/articlesearch"

# set response format
response_format=".json"


# You often want to send some sort of data in the URL’s query string. This data tells the API what information you want. In our case, we want articles about Prince. Requests allows you to provide these arguments as a dictionary, using the `params` keyword argument. In addition to the search term `q`, we have to put in the `api-key` term.

# In[15]:

# set search parameters
search_params = {"q":"Prince",
                 "api-key":key}       


# Now we're ready to make the request. We use the `.get` method from the `requests` library to make an HTTP GET Request.

# In[16]:

# make request
r = requests.get(base_url+response_format, params=search_params)

# Now, we have a [response](http://docs.python-requests.org/en/latest/api/#requests.Response) object called `r`. We can get all the information we need from this object. For instance, we can see that the URL has been correctly encoded by printing the URL. Click on the link to see what happens.

# In[17]:

print(r.url)


# Click on that link to see what it returns!

# Hmm - looks like we're getting a lot of junk unrelated to the musical artist in here. Let's make it a little more specific:

# In[18]:

# set search parameters
search_params = {"q":"Prince music",
                 "api-key":key}  
# make request
r = requests.get(base_url+response_format, params=search_params)

print(r.url)


# Better!

# ### Challenge 1:  Adding a date range
# 
# What if we only want to search within a particular date range? The NYT Article API allows us to specify start and end dates.
# 
# Alter the `search_params` code above so that the request only searches for articles in the year 2005.
# 
# You're gonna need to look at the documentation [here](http://developer.nytimes.com/docs/read/article_search_api_v2) to see how to do this.

# In[19]:

#YOUR CODE HERE

# Uncomment to test
# r = requests.get(base_url+response_format, params=search_params)
# r.url


# ### Challenge 2:  Specifying a results page
# 
# The above will return the first 10 results. To get the next ten, you need to add a "page" parameter. Change the search parameters above to get the second 10 resuls. 

# In[20]:

search_params = {"q":"Prince music",
                 "begin_date": "20050101",
                 "end_date": "20050131",
                 "page": "1",
                 "api-key":key}  
# make request
r = requests.get(base_url+response_format, params=search_params)

print(r.url)

# Uncomment to test
# r = requests.get(base_url+response_format, params=search_params)
# r.url


# ## 2. Parsing the response text

# We can read the content of the server’s response using `.text`

# In[21]:

# Inspect the content of the response, parsing the result as text
response_text= r.text
print(response_text[:1000])


# What you see here is JSON text, encoded as unicode text. JSON stands for "Javascript object notation." It has a very similar structure to a python dictionary -- both are built on key/value pairs. This makes it easy to convert JSON response to a python dictionary.

# In[22]:

# Convert JSON response to a dictionary
data=json.loads(response_text)
# data


# That looks intimidating! But it's really just a big dictionary. Let's see what keys we got in there.

# In[23]:

data.keys()


# In[24]:

# this is boring
data['status']


# In[25]:

# so is this
data['copyright']


# In[26]:

# this is what we want!
# data['response']


# In[27]:

data['response'].keys()


# In[28]:

data['response']['meta'].keys()


# In[29]:

data['response']['meta']['hits'] # whoa - that's a lot of hits!


# In[30]:

# data['response']['docs']
type(data['response']['docs'])


# That looks what we want! Let's put that in it's own variable.

# In[31]:

docs = data['response']['docs']


# In[32]:

docs[1]


# ## 3. Putting everything together to get all the articles.

# ### That's great. But we only have 10 items. The original response said we had 30528 hits! Which means we have to make 30528 /10, or 3053 requests to get them all.*
# #### *Note - in general, most free APIs have limits on how often you can "call" them, i.e., how many requests you can send. For the NYT, the daily limit is 1000, and you are limited to 5 calls/sec. At first, this might sound like plenty--but in general, it's not. You'll want to be creative with your search terms and date restrictions to ensure that you have a manageable number of calls to the API. Going forward, we're just going to look at the 2016 results - a much more manageable 523 (53 calls). 
# 
# ### Sounds like a job for a loop! 
# 
# But first, let's review what we've done so far.

# In[33]:

# set key
# key="XXX"

# set base url
base_url="http://api.nytimes.com/svc/search/v2/articlesearch"

# set response format
response_format=".json"

# set search parameters
search_params = {"q":"Prince music",
                 "api-key":key,
                 "begin_date":"20150101", # date must be in YYYYMMDD format
                 "end_date":"20150131"}

# make request
rr = requests.get(base_url+response_format, params=search_params)
    
# convert to a dictionary
data=json.loads(rr.text)
    
# get number of hits
hits = data['response']['meta']['hits']
print("number of hits: " + str(hits))
    
# get number of pages
pages = int(math.ceil(hits/10))


# In[ ]:

# make an empty list where we'll hold all of our docs for every page
all_docs = [] 
    
# now we're ready to loop through the pages
for i in range(pages):
    print("collecting page " + str(i))
        
    # set the page parameter
    search_params['page'] = i
        
    # make request
    rr = requests.get(base_url+response_format, params=search_params)
    
    # get text and convert to a dictionary
    data=json.loads(rr.text)
        
    # get just the docs
    docs = data['response']['docs']
        
    # add those docs to the big list
    all_docs = all_docs + docs


# In[ ]:

print(data)


# In[ ]:

len(all_docs)


# ### Challenge 3: Make a function
# 
# Turn the code above into a function that inputs a search term, and returns all the documents containing that search term in 2014.

# In[ ]:

def apisearch(q, begin):
    # set key
    key="[ADD KEY HERE]"
    key="7iJ3lTTEh7wao3Jr1HR8BUr9D6RQwACA"
    # set base url
    base_url="http://api.nytimes.com/svc/search/v2/articlesearch"
    # set response format
    response_format=".json" 
    search_params = {"q": q,
                 "begin_date": begin,
                 "end_date": "20141231",
                 "page": "1",
                 "api-key":key}  
    # make request
    r = requests.get(base_url+response_format, params=search_params)
    print(r.url)


# In[ ]:

apisearch("Clinton", "20140101")


# ## 4. Formatting and Exporting
# 
# Let's take another look at one of these documents.

# In[ ]:

all_docs[0]


# This is all great, but it's pretty messy. What we’d really like to to have, eventually, is a CSV, with each row representing an article, and each column representing something about that article (header, date, etc). As we saw before, the best way to do this is to make a lsit of dictionaries, with each dictionary representing an article and each dictionary representing a field of metadata from that article (e.g. headline, date, etc.) We can do this with a custom function:

# In[ ]:

def format_articles(unformatted_docs):
    '''
    This function takes in a list of documents returned by the NYT api 
    and parses the documents into a list of dictionaries, 
    with 'id', 'header', and 'date' keys
    '''
    formatted = []
    for i in unformatted_docs:
        dic = {}
        dic['id'] = i['_id']
        dic['headline'] = i['headline']['main'].encode("utf8")
        dic['date'] = i['pub_date'][0:10] # cutting time of day.
        formatted.append(dic)
    return(formatted) 


# In[ ]:

all_formatted = format_articles(all_docs)


# In[ ]:

all_formatted[:5]


# ### Challenge 4: Export the data to a CSV.

# In[ ]:

import csv
keys = all_formatted[0].keys()
with open('article_API.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_formatted)
    


# In[ ]:




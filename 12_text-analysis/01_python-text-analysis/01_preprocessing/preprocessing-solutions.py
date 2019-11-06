
# coding: utf-8

# # Preprocessing
# 
# Like other data types, text data never comes clean. Moreover, most of our downstream methods only accept data structured in a particular way. Because of this, before we do any computational text analysis techniques, we will always need to perform some level of preprocessing. Text data has its own unique kind of preprocessing. In this notebook, we will cover the core preprocessing methods in preparation for our next two weeks:
# 
# - Reading in files
# - Character encoding
# - Tokenization
# - Sentence segmentation
# - Removing punctuation
# - Stripping whitespace
# - Text normalization
# - Stop words
# - Stemming/Lemmatizing
# - POS tagging
# - DTM/TF-IDF
# 
# ### Time
# - Teaching: 50 minutes
# - Exercises: 60 minutes

# ## Reading in files
# 
# The first step is to read in the files containing the data. As we discussed last week, the most common file types for text data are: `.txt`, `.csv`, `.json`, `.html` and `.xml`.
# 
# #### Reading in `.txt` files
# 
# Python has built-in support for reading in `.txt` files.
# 
# - What type of object is `raw`?
# - How many characters are in `raw`?
# - Get the first 1000 characters of `raw`?

# In[4]:


import os
DATA_DIR = '../data'
fname = 'pride-and-prejudice.txt'
fname = os.path.join(DATA_DIR, fname)
with open(fname, encoding='utf-8') as f:
    raw = f.read()


# #### Reading in `.csv`
# 
# Python has a built-in module called `csv` for reading in csv files.
# 
# - What type is `tweets`?
# - How many entries are in `raw`?
# - Which entry is the header row?
# - How can we get the text of the first question?
# - How can we get a list of the texts of all questions?

# In[5]:


import csv
fname = 'trump-tweets.csv'
fname = os.path.join(DATA_DIR, fname)
tweets = []
with open(fname) as f:
    reader = csv.reader(f)
    tweets = list(reader)


# #### Reading in `.csv` with `pandas`
# 
# `pandas` is a third-party library that makes working with tabular data much easier. This is the recommended way to read in a `.csv` file.
# 
# - How many tweets are there?
# - What happened to the header row?

# In[6]:


import pandas as pd
fname = 'trump-tweets.csv'
fname = os.path.join(DATA_DIR, fname)
tweets = pd.read_csv(fname)


# In[5]:


tweets.head(3)


# In[7]:


tweet_text = list(tweets['Tweet_Text'])
tweet_text[:4]


# #### Reading in `.json` files
# 
# Python has built-in support for reading in `.json` files.
# 
# - How many questions are there in the dataset?
# - What data type is each question?
# - How can we access the question text of the first question?
# - How can we get a list of the texts of all questions?

# In[8]:


import json
fname = 'jeopardy.json'
fname = os.path.join(DATA_DIR, fname)
with open(fname) as f:
    data = json.load(f)


# In[8]:


data[:3]


# #### Reading in `.html` files
# 
# The best way to read in `.html` files in Python is with the `BeautifulSoup` package.

# In[9]:


from bs4 import BeautifulSoup
fname = 'time.html'
fname = os.path.join(DATA_DIR, fname)
with open(fname,encoding='utf-8') as f:
    html = f.read()
    soup = BeautifulSoup(html)


# In[12]:


texts = soup.findAll(text=True)
#texts = soup.getText()
texts[:5]


# #### Reading in `.xml` files
# 
# We read in `.xml` files using the `ElementTree` module of Python's standard library. We can think of `.xml` files as trees where each branch has a tag name. We can find all the branches with a certain name as follows:

# In[13]:


from xml.etree import ElementTree as ET
fname = 'books.xml'
fname = os.path.join(DATA_DIR, fname)
e = ET.parse(fname)
root = e.getroot()


# In[14]:


descriptions = root.findall('*/description')
text = [d.text for d in descriptions]
text[:3]


# #### Reading in multiple files
# 
# Often, our text data is split across multiple files in a folder. We want to be able to read them all into a single variable.
# 
# - What type is `austen`?
# - What type is `fnames` after it is first assigned a value?
# - What type is `fnames` after it is assigned a second value?
# - How 

# In[18]:


import glob
fnames = os.path.join(DATA_DIR, 'austen', '*.txt')
fnames = glob.glob(fnames)
austen = ''
for fname in fnames:
    with open(fname, encoding='utf-8') as f:
        text = f.read()
        austen += text


# ### Challenge
# 
# Read in all the `.csv` files in the folder `amazon`. Extract out only the text column from each file and store them all in a list called `reviews`.

# In[22]:


fnames = os.path.join(DATA_DIR, 'amazon', '*.csv')
fnames = glob.glob(fnames)
reviews = []
column_names = ['id', 'product_id', 'user_id', 'profile_name', 'helpfulness_num', 'helpfulness_denom',
               'score', 'time', 'summary', 'text']
for fname in fnames[:2]:
    df = pd.read_csv(fname, names=column_names)
    text = list(df['text'])
    reviews.extend(text)


# ## Character encoding
# 
# Character encoding was more of a problem in Python 2 and early years in general. With Python 3 and most text files being encoded in `UTF-8`, we don't often need to think about it. If you're getting nonsense when reading in a file, try adding `encoding='utf-8'` to the `open` function.

# In[13]:


fname = 'dante.txt'
fname = os.path.join(DATA_DIR, fname)
with open(fname) as f:
    text = f.read()


# In[14]:


text[5000:6000]


# In[15]:


fname = 'akutagawa.txt'
fname = os.path.join(DATA_DIR, fname)
with open(fname) as f:
    text = f.read()


# In[16]:


text[5000:6000]


# ## Tokenization
# 
# Once we've read in the data, our next step is often to split it into words. This step is referred to as "tokenization". That's because each occurrence of a word is called a "token". Each distinct word used is called a word "type". So the word type "the" may correspond to multiple tokens of "the" in a text.
# 
# #### Tokenizing by whitespace
# 
# - What problems do you notice with tokenizing by whitespace?
# - What type is `text`?
# - What type is `tokens`?
# - What type is each element of `tokens`?

# In[13]:


import os
fname = 'example1.txt'
fname = os.path.join(DATA_DIR, fname)
with open(fname) as f:
    text = f.read()


# In[18]:


text.split()[:10]


# #### Tokenizing with regular expressions

# In[14]:


import re
word_pattern = r'\w+'
tokens = re.findall(word_pattern, text)
tokens[:10]


# #### Tokenizing with `nltk`
# 
# [Just a bunch of regular expressions under the hood](https://github.com/nltk/nltk/blob/develop/nltk/tokenize/treebank.py)

# In[15]:


from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
tokens[:10]


# #### Challenge
# 
# A while ago you read in a bunch of Jane Austen books into a variable called `austen`. Tokenize that using a method of your choice. Find all the unique words types (you might want the `set` function). Sort the resulting set object to create a vocabulary (you might want to use the `sorted` function).

# In[16]:


tokens = word_tokenize(austen)


# In[20]:


vocab = sorted(set(tokens))
vocab[0:100]


# ## Sentence segmentation
# 
# Sentence segmentation involves identifying the boundaries of sentences.
# 
# #### Sentence segmentation by splitting on punctuation

# In[66]:


text.split('.')


# We could improve on this by using regular expressions. They'll allow us to split strings based on a number of characters.

# In[67]:


sent_boundary_pattern = r'[.?!]'
re.split(sent_boundary_pattern, text)


# ### Challenge
# 
# The file `example2.txt` has more punctuation problems. Read it in and see what the problems are. Try your best to modify the code from above to work for as many cases as you can.

# In[31]:


fname = 'example2.txt'
fname = os.path.join(DATA_DIR, fname)
with open(fname) as f:
    text = f.read()


# In[36]:


# Simply looking for certain characters gives us problems, as you'll see below. There's no notion of context in the
# regular expression below.
sent_enders = r'[\.\?!]'
re.split(sent_enders, text)


# #### Sentence segmentation by `nltk`

# In[68]:


from nltk.tokenize import sent_tokenize
fname = 'example2.txt'
fname = os.path.join(DATA_DIR, fname)
with open(fname) as f:
    text = f.read()
sent_tokenize(text)


# ## Removing punctuation
# 
# Sometimes (although admittedly less frequently than tokenizing and sentence segmentation), you might want to keep only the alphanumeric characters (i.e. the letters and numbers) and ditch the punctuation. Here's how we can do that.
# 
# - What type is `punctuation`?

# In[70]:


from string import punctuation
punctuation


# In[26]:


no_punct = ''.join([ch for ch in text if ch not in punctuation])
no_punct


# ## Strip whitespace
# 
# This is an extremely common step. It's simple to perform and nicely pre-packaged in Python. It's particularly common for user-generated text (think survey forms).

# In[71]:


fname = 'example3.txt'
fname = os.path.join(DATA_DIR, fname)
with open(fname) as f:
    text = f.read()


# In[73]:


print(text)


# In[74]:


stripped_text = text.strip()
print(stripped_text)


# In[75]:


whitespace_pattern = r'\s+'
clean_text = re.sub(whitespace_pattern, ' ', text)
clean_text


# ## Text normalization
# 
# Text normalization means making our text fit some standard patterns. Lots of steps come under this wide umbrella, but the most common are:
# 
# - case folding
# - removing URLs, digits, hashtags
# - OOV (removing infequent words)
# 
# #### Case folding
# 
# Case folding means dealing with upper and lower cases characters. This is usually done by making all characters lower cased.

# In[21]:


fname = 'example4.txt'
fname = os.path.join(DATA_DIR, fname)
with open(fname) as f:
    text = f.read()
text


# In[24]:


text.lower()


# ### Challenge
# 
# The `lower` method we used above is a string method, that is, it works on strings. But what if you want to lowercase every word in a list (say you've already tokenized the text). Take the list of tokens below and make each one lower case.

# In[25]:


tokens = word_tokenize(text)
lowercase_tokens = []
for token in tokens:
    lowercased_version = token.lower()
    lowercase_tokens.append(lowercased_version)


# In[26]:


lowercase_tokens = [token.lower() for token in tokens]


# ### Removing URLs, digits and hashtags
# 
# We rarely care about the exact URL used in a tweet, or the exact number. We could remove them completely (think about how we'd do that), but it's often informative to know that there is a URL or a digit in the text. So we want to replace individual URLs asnd digits with a symbol that preserves the fact that a URL was there. It's standard to just use the strings "URL" and "DIGIT".
# 
# How do we do this? Once again, regular expressions save the day.

# In[34]:


url_pattern = r'https?:\/\/.*[\r\n]*'
single_tweet = tweet_text[0]
single_tweet


# In[35]:


URL_SIGN = ' URL '
re.sub(url_pattern, URL_SIGN, single_tweet)


# #### Challenge
# 
# Above we replaced the URL in a single tweet. Now replace all the URLs in all tweets in `tweet_text`.

# In[50]:


url_pattern = r'https?:\/\/.*[\r\n]*'
URL_SIGN = ' URL '
list_of_url_less_tweets = []
for facebook_post in tweet_text:
    url_less_tweet = re.sub(url_pattern, URL_SIGN, facebook_post)
    list_of_url_less_tweets.append(url_less_tweet)


# In[93]:


list_of_url_less_tweets = [re.sub(url_pattern, URL_SIGN, facebook_post) for facebook_post in tweet_text]


# In[94]:


list_of_url_less_tweets


# #### Challenge
# 
# Use the regular expression for hashtags below to replace all hashtags in all tweets in `tweet_text`.

# In[38]:


hashtag_pattern = r'(?:^|\s)[＃#]{1}(\w+)'
HASHTAG_SIGN = ' HASHTAG '
digit_pattern = '\d+'
DIGIT_SIGN = ' DIGIT '


# In[39]:


no_hashtags = [re.sub(hashtag_pattern, HASHTAG_SIGN, tweet) for tweet in tweet_text]


# #### OOV words
# 
# Sometimes it's best for us to remove infrequent words (sometimes not!). When we do remove infrequent words, it's often for a downstream method (like classification) that is sensitive to rare words.

# In[37]:


all_tweets = ' '.join(tweet_text)
clean = re.sub(url_pattern, URL_SIGN, all_tweets)
clean = re.sub(hashtag_pattern, HASHTAG_SIGN, clean)
clean = re.sub(digit_pattern, DIGIT_SIGN, clean)
tokens = word_tokenize(clean)
tokens = [token for token in tokens if token not in punctuation]
tokens[:20]


# We can count the frequency of each word type with the built-in `Counter` in Python. This basically just takes the set of word types (we calculated this above as `vocabularly`) and makes a special Python dictionary with each value being the number of times it appears in the list. We can ask that dictionary for the most common words, or for the frequency of individual word types.

# In[38]:


from collections import Counter
freq = Counter(tokens)
freq.most_common(10)


# In[39]:


freq['unleashed']


# In[40]:


OOV = 'OOV'
new_tokens = []
for token in tokens:
    if freq[token] == 1:
        new_tokens.append(OOV)
    else:
        new_tokens.append(token)


# In[41]:


new_tokens[:20]


# ### Challenge
# 
# I've read in some Amazon reviews from earlier into a list called `reviews`. Each element of the list is a string, representing the text of a single review. Try to:
# - Tokenize each review
# - Separate each review into sentences
# - Strip all whitespace
# - Make all characters lower case
# - Replace any URLs and digits
# 
# Then find the most common 50 words.

# In[42]:


fnames = os.path.join(DATA_DIR, 'amazon', '*.csv')
fnames = glob.glob(fnames)
reviews = []
column_names = ['id', 'product_id', 'user_id', 'profile_name', 'helpfulness_num', 'helpfulness_denom',
               'score', 'time', 'summary', 'text']
for fname in fnames[:2]:
    df = pd.read_csv(fname, names=column_names)
    text = list(df['text'])
    reviews.extend(text)


# In[52]:


lowercase_reviews = [review.lower() for review in reviews]
no_whitespace = [review.strip() for review in lowercase_reviews]
no_urls = [re.sub(url_pattern, URL_SIGN, review) for review in no_whitespace]
no_digits = [re.sub(digit_pattern, DIGIT_SIGN, review) for review in no_urls]
tokenized = [word_tokenize(review) for review in no_digits[:50]]


# In[53]:


tokenized[:2]


# ## Removing stop words
# 
# You might have noticed that the most common words above aren't terribly exciting. They're words like "am", "i", "the" and "a": stop words. These are rarely useful to us in computational text analysis, so it's very common to remove them completely.
# 
# - What other stop words do you think there are?

# In[54]:


from nltk.corpus import stopwords
stop = stopwords.words('english')
stop


# ### Challenge
# 
# Use the list `stop` of English stopwords to remove stopwords from our dataset of Tweets.

# In[56]:


from string import punctuation
all_tweets = ' '.join(tweet_text)
clean = re.sub(url_pattern, URL_SIGN, all_tweets)
clean = re.sub(hashtag_pattern, HASHTAG_SIGN, clean)
clean = re.sub(digit_pattern, DIGIT_SIGN, clean)
tokens = word_tokenize(clean)
tokens = [token for token in tokens if token not in punctuation]
tokens[:20]


# In[57]:


no_stopwords = [token for token in tokens if token not in stop]


# ## Stemming/lemmatization
# 
# Stemming and lemmatization both refer to remove morphological affixes on words. For example, if we stem the word "grows", we get "grow". If we stem the word "running", we get "run". We do this because often we care more about the core content of the word (i.e. that it has something to do with growth or running, rather than the fact that it's a third person present tense verb, or progressive participle).
# 
# NLTK provides many algorithms for stemming. For English, a great baseline is the [Porter](https://github.com/nltk/nltk/blob/develop/nltk/stem/porter.py) algorithm, which is in spirit isn't that far from a bunch of regular expressions.

# In[58]:


from nltk.stem import PorterStemmer
stemmer = PorterStemmer()


# In[59]:


stemmer.stem('grows')


# In[60]:


stemmer.stem('running')


# In[49]:


stemmer.stem('leaves')


# In[61]:


from nltk.stem import SnowballStemmer, WordNetLemmatizer
snowballer_stemmer = SnowballStemmer('english')
lemmatizer = WordNetLemmatizer()


# In[62]:


print(snowballer_stemmer.stem('running'))
print(snowballer_stemmer.stem('leaves'))


# In[52]:


print(lemmatizer.lemmatize('leaves'))


# ### Challenge
# 
# Use the Porter stemmer to stem each word in the tweet dataset after having removed stop words.

# In[67]:


tokenized_tweets = [word_tokenize(tweet) for tweet in tweet_text]
all_stemmed = []
for tweet in tokenized_tweets:
    stemmed = [stemmer.stem(t) for t in tweet]
    all_stemmed.append(stemmed)


# ## POS tagging
# 
# POS tagging means assigning each token a part-of-speech (e.g. noun, verb, adjective, etc.). Again, there are many different [alternatives](https://github.com/nltk/nltk/tree/develop/nltk/tag), but NLTK keeps its recommended POS tagger available through the function `pos_tag`. The tagger expects a list of tokens as input.When doing POS tagging, it is advisable **not** to remove stop words beforehand (although you are free to do it afterwards).

# In[69]:


from nltk import pos_tag
single_review = reviews[3]
single_review


# In[54]:


tokens = word_tokenize(single_review)
tagged_review = pos_tag(tokens)
tagged_review


# ### Challenge
# 
# Below I've read in the text of Austen's _Pride and Prejudice_ into a variable called `pride`. Preprocess using the following steps:
# 
# - Strip whitespace
# - Replace all numbers with '0'
# - Tokenize
# - Tag each token with a POS tag
# 
# Make sure you know:
# - What type is the result?
# - What type is each element of the result?
# - What type are the elements of the elements of the result?

# In[70]:


fname = 'pride-and-prejudice.txt'
fname = os.path.join(DATA_DIR, fname)
with open(fname, encoding='utf-8') as f:
    raw = f.read()
pride = raw[679:684814]


# In[71]:


pride = pride.strip()
pride = re.sub(digit_pattern, '0', pride)
tokenized = word_tokenize(pride[:1000]) # Just tokenize the first 1000 characters to speed things up


# In[73]:


tagged = pos_tag(tokenized)


# ## DTM/TF-IDF
# 
# Document term matrix and Term Frequency-Inverse Document Frequency are common preprocessing steps for taking tokenized texts and turning them into numerical features, ready for supervised machine learning models. Scikit-learn is the standard method of using DTM and TF-IDF in Python. They have two main classes for this: [CountVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) and [TfidfVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer).

# In[56]:


clean = [re.sub(url_pattern, URL_SIGN, t) for t in tweet_text]
clean = [re.sub(hashtag_pattern, HASHTAG_SIGN, t) for t in clean]
clean = [re.sub(digit_pattern, DIGIT_SIGN, t) for t in clean]
clean = [re.sub(whitespace_pattern, ' ', t) for t in clean]
clean[:4]


# In[57]:


from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
count = CountVectorizer()
X = count.fit_transform(clean)
X


# In[58]:


X.toarray()[:5,:5]


# In[59]:


tfidf = TfidfVectorizer()
X = tfidf.fit_transform(clean)
X


# In[60]:


X.toarray()[:5,:5]


# ## Things we didn't cover
# 
# - Named entity recognition
# - Syntactic parsing
# - Information extraction
# - Removing markup from HTML
# - Extracting numerical features
# - SpaCy

# Accessing Databases via Web APIs

> ### Learning objectives
> 
> * Explain purpose of API 
> * Explain how API used for data science
> * Explain basic syntax and concepts for using APIs (for data science)



## What is an API?

API stands for **Application Programming Interface**. They are sets of rules and procedures that facilitate interactions between computers and their applications. 

In other words, APIs standardize how information is communicated electronically. 

### Web APIs

Web APIs are a type of API that...
* allows users to query a remote database over the internet
* take on a variety of formats 

### "RESTful" APIs

We will focus on web APIs that adhere to the REST standard: 
* majority of web APIs adhere to a particular style known as **Representational State Transfer** or **REST**. 
* "RESTful" APIs are convenient because we can use them to query databases using URLs 


## RESTful Web APIs are All Around You

Consider a simple Google search (go ahead and search something). Ever wonder what all that extra stuff in the address bar was all about?  

> **Mini-challenge:** search for the URL `https://www.google.com/search?q=API`. Note that this is equivilent to searching 'API' using google search. 

It looks like Google makes its query by taking the search terms, separating each of them with a "`+`", and appending them to the link: `https://www.google.com/#q=`. So that we have `https://www.google.com/#q=search1+search2`

Notice that we can change our Google search by adding some terms to the URL.

> **Mini-challenge:** modify your 'API' search to include both 'API' and 'definition' by changing the URL (don't type anything new in the search box).  


## Some Basic Terminology

### URL

URL stands for Uniform Resource Location. URLs are strings of characters that, when interpreted via the Hypertext Transfer Protocol (HTTP), point to a data resource, notably files written in Hypertext Markup Language (HTML) or a subset of a database.

### HTTP Methods / Verbs

Developers use a number of common methods including `GET`, `HEAD`, `POST`, `PUT`, and `DELETE` to query, modify, etc. data in a database. 

Only one of these is relevant for our purposes: `GET`. 

The *GET* method requests a representation of a data resource corresponding to a particular URL.  The process of executing the GET method is often referred to as a **GET request** and is the main method used for querying RESTful databases.


## How Do GET Requests Work?  A Web Browsing Example

Surfing the Web = Making a bunch of GET Requests
* For instance, I open my web browser and type in http://www.wikipedia.org.  Once I hit return, I'd see a webpage.
* Several different processes occured, however, between me hitting "return" and the page finally being rendered. 

### Step 1: The GET Request

* web browser took the entered character string 
* used the command-line tool "Curl" to write a properly formatted HTTP GET request 
* submitted it to the server that hosts the Wikipedia homepage.

### STEP 2: The Response

* Wikipedia's server receives this request
* send back an HTTP response
* from which Curl extracted the HTML code for the page

```
[1] "<!DOCTYPE html>\n<html lang=\"mul\" class=\"no-js\">\n<head>\n<meta charset=\"utf-8\">\n<title>Wikipedia</title>\n<meta name=\"description\" content=\"Wikipedia is a free online encyclopedia, created and edited by volunteers around the world and hosted by the Wikimedia Foundation.\">\n<![if gt IE 7]>\n<script>\ndocum"
```

### STEP 3: The Formatting

* raw HTML code was formatted and executed by the web browser
* rendering the page as seen in the window.


## RESTful Database Querying

### The GET Request

URL we supply must be constructed so that the resulting request can be interpreted and succesfully acted upon by the server.  

Likely that the character string must encode **search terms and/or filtering parameters**, as well as one or more **authentication codes**.  

While the terms are often similar across APIs, most are API-specific.


### The Response

Unlike web browsing, the content of the server's response that is extracted by Curl is unlikely to be HTML code. 
* will likely be **raw text** response that can be parsed into one of a few file formats commonly used for data storage.  
* usual suspects include .csv, .xml, and .json files.


### The Formatting

Web browser parsed the HTML code, but **we need R, Python, or other programming languages** to parse the server response and convert it into a format for local storage (e.g. matrices, dataframes, databases, lists, etc.).

## Example: 

Characterize the volume of coverage of impeachment over the past few weeks. Specifically, what trends do you see?

### STEP 1: Finding Data Resources

* Popularity = How frequently or widely something is referenced over time
* Popularity = Frequency in Newspapers
* Popularity = Frequency in New York Times

[NYT Article API](http://developer.nytimes.com/)

### STEP 2: Getting API Access

* For most APIs, a key or other user credentials are required
* Most APIs are set up for developers, so you’ll likely be asked to register an "application"
* rate limits = total number of calls / time
* NYT API = 10 calls per second and 10,000 calls per day

[NYT Article API Keys](http://developer.nytimes.com/apps/mykeys)

### STEP 3: Constructing API GET Request

Most GET request URLs for API querying have three or four components:

1. **Base URL**: a link stub that will be at the beginning of all calls

2. **Authenication Key/Token**: a user-specific character string

3. **Response Format**: a character string indicating how the response should be formatted; usually one of .csv, .json, or .xml

4. **Search Parameters**: a character string telling the server what to extract from the database; basically a series of filters used to point to specific parts of a database

Documentation: 

* Common architectures, but each API has its own unique quirks.
* Carefully reviewing the API documentation is critical!!
* Fortunately, the NYT Article API is [very well documented!](http://developer.nytimes.com/docs/read/article_search_api_v2)

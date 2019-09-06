# Introduction to R

## What is R

R is an open source programming/scripting language used primarily for statistics and data science. 


### Base R and Packages

R automatically comes with a set of packages (functions and datasets) that are collectively referred to as **Base R.** 

Typically, we download additional packages because Base R isn't sufficient. Instead of trying to centrally write and distribute code, R relies on its users to identify and write packages to provide added functionality. This system contrasts with rival software like Stata or Excel where one centralized entity writes all of the underlying code for Stata. 

**Tidyverse** is a set of packages that have revolutionized how people program in R. The creator of tidyverse, Hadley Wickham, is probably the most famous person in the R community today. He is also good at explaining things, which is why he is quoted so many times here. 


### RStudio 

We will be interacting with R using RStudio.

RStudio is an integrated development environment (IDE) for the R software package. An IDE is software that helps computer programmers develop software by combining tools and improving user interface. RStudio is the most popular IDE for R.


## Why R is good

1. Open source 
	* Free to download (for non-commercial use) 
	* Available on all platforms (Unix, Windows, Linux).
	* If you do your analysis in R, anyone can easily replicate it.

2. Widely used in academia and industry 
	* As of January 2019, R ranks 12th in the TIOBE index, which measures the popularity of programming languages. 
	* Superior (if not just comparable) to commercial alternatives. 
	* Active community 

3. Designed for data analysis and statistics 
	* "R is a weird language but it is weird for good reasons, and it’s a really good fit for data science." - [Hadely Wickam](https://qz.com/1661487/hadley-wickham-on-the-future-of-r-python-and-the-tidyverse/)
	* Faster to learn: "I think you are going to get up and running faster with R...there’s just a bunch more stuff built in and you don’t have to learn as many programming concepts." - [Hadely Wickam](https://www.r-bloggers.com/advice-to-young-and-old-programmers-a-conversation-with-hadley-wickham/)
	* Community developing R is made up of people who are also doing data science

4. Flexible
	* R can do anything whereas Stata can do only things allowed to do.

5. Visualization
	* Some of the best data visualization tools available. 
	* Much better than python. 

6. General programming features 
	* Not just for statistics, but also general purpose programming.
	* Object oriented (R has objects) and functional (you can write functions).


## Why R is annoying

R is a quirky language -- Some quirks are really useful but others are annoying. 
	* R is inconsistent 
		* Lots of special cases where syntax deviates from the normal pattern 
		* A popular set of packages called tidyverse adds to this challenge by using different (generally better) syntax. At this point, tidyverse is so extensive that it often feels like a seperate language.  
	* R is slow at doing some important things 
		* Writing fast code in R is an advanced topic 
	* R is not great for big data 
		* parallel processing not well implemented 
		* bad at managing memory 

R users and developers have less computer science training. 
	* Code and packages are often badly written 
	* Quality control practices not widespread  


## R ~~vs.~~ and Python

### Hadely Wickam's thoughts

> Generally, there are a lot of people who talk about R versus Python like it’s a war that either R or Python is going to win. I think that is not helpful because it is not actually a battle. These things exist independently and are **both awesome in different ways.**
>
> A pattern that I see is that the data science team in a company uses R and the data engineering team uses Python. The Python people tend to have a background in software engineering and are very confident about their programming skills. They see R and it looks very weird, and say with a lot of certainty these facts about R [not being as good].
>
> The R users are generally not as confident in their programming skills. They really like R, but can’t argue with the engineering team, because they don’t have the language to make that argument. People using R tend to have these backgrounds in biology or marketing and they don’t have the vocabulary. R is a weird language but it is weird for good reasons, and it’s a really good fit for data science. It’s not a general purpose programming language, but there are good reasons for a lot of the things it does.
>
> -Hadley Wickam in an [August 2019 interview](https://qz.com/1661487/hadley-wickham-on-the-future-of-r-python-and-the-tidyverse/)



***************************************************************************

## More Information

### A1: Using R and Python together 

As long as you save the file at the end of a script, you can run a sequence of python and R scripts seperately. 

1. Run sequence of python and R scripts seperately

	* Can be done manually using RStudio and a python IDE
	* Use function to evaluate script written in other langage (i.e. `reticulate::source_python()` in R)
	* Use command line and write Bash script to run R and python scripts in the correct order

2. Blend R and Python in a single script

See [this article](https://towardsdatascience.com/from-r-vs-python-to-r-and-python-aa25db33ce17) for more information. 


### A2: Bonus: More about R

From [Hadley Wickham](http://adv-r.had.co.nz/Introduction.html):

If you are new to R, you might wonder what makes learning such a quirky language worthwhile. In my opinion, R's some of the best features are:

* It's free, open source, and available on every major platform. As a result, if you do your analysis in R, anyone can easily replicate it.

* A massive set of packages for statistical modeling, machine learning, visualization, and importing and manipulating data. Whatever model or graphic you're trying to do, the chances are that someone has already tried to do it. At a minimum, you can learn from their efforts.

* Cutting edge tools. Researchers in statistics and machine learning will often publish an R package to accompany their articles. This means immediate access to the very latest statistical techniques and implementations.

* Deep-seated language support for data analysis. This includes features likes missing values, data frames, and subsetting.

* A fantastic community. It is easy to get help from experts on the
  [R-help mailing list](https://stat.ethz.ch/mailman/listinfo/r-help), [stackoverflow](http://stackoverflow.com/questions/tagged/r), or subject-specific mailing lists like [R-SIG-mixed-models](https://stat.ethz.ch/mailman/listinfo/r-sig-mixed-models) or [ggplot2](https://groups.google.com/forum/#!forum/ggplot2). You can also connect with other R learners via [twitter](https://twitter.com/search?q=%23rstats), [linkedin](http://www.linkedin.com/groups/R-Project-Statistical-Computing-77616), and through many local [user groups](http://blog.revolutionanalytics.com/local-r-groups.html).

* Powerful tools for communicating your results. R packages make it easy to produce HTML or PDF [reports](http://yihui.name/knitr/), or create [interactive websites](http://www.rstudio.com/shiny/).

* A strong foundation in functional programming. The ideas of functional programming are well suited to solving many of the challenges of data analysis. R provides a powerful and flexible toolkit which allows you to write concise yet descriptive code.

* An [IDE](http://www.rstudio.com/ide/) tailored to the needs of interactive data analysis and statistical programming.

* Powerful metaprogramming facilities. R is not just a programming language; it is also an environment for interactive data analysis. Its metaprogramming capabilities allow you to write magically succinct and concise functions and provide an excellent environment for designing domain-specific languages.

* Designed to connect to high-performance programming languages like C, FORTRAN, and C++.

Of course, R is not perfect. R's biggest challenge is that most R users are not programmers. This means that:

* Much of the R code you'll see in the wild is written in haste to solve a pressing problem. As a result, code is not very elegant, fast, or easy to understand. Most users do not revise their code to address these shortcomings.

* Compared to other programming languages, the R community tends to be more focused on results instead of processes. Knowledge of software engineering best practices is patchy: for instance, not enough R programmers use source code control or automated testing.

* Metaprogramming is a double-edged sword. Too many R functions use tricks to reduce the amount of typing at the cost of making code that is hard to understand and that can fail in unexpected ways.

* Inconsistency is rife across contributed packages, even within base R. You are confronted with over 20 years of evolution every time you use R. Learning R can be tough because there are many special cases to remember.

* R is not a particularly fast programming language, and poorly written R code can be terribly slow. R is also a profligate user of memory. 
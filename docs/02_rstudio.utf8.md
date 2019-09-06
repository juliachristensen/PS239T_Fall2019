---
title: "RStudio"
---



# RStudio and RMarkdown 

## 1. RStudio 

We will be interacting with R using RStudio. 

RStudio is an **integrated development environment (IDE)** for the R software package. An **IDE** is software that helps computer programmers develop software by combining tools and improving user interface. RStudio is the most popular IDE for R. 

### 1.1. Tour of RStudio 

For a detailed describtion of RStudio features and keyboard shortcuts, see the [RStudio Cheatsheet](https://github.com/rstudio/cheatsheets/blob/master/rstudio-ide.pdf).

Four display windows:  

1. Source
2. Console/Terminal 
3. Environment/History Connections
4. Files/Plots/Packages/Help/Viewer

Some hidden features:

- Outline button in top right corner of source window 
- Tools > Global Options
  - Change font colors, size, etc. 
  - Wrap text 
- Zoom one pane (see View tab or keyboard shortcuts)


### 1.2. Running Code

There are two main ways of interacting with R: using the console or by using script files (plain text files that contain your code).

The console window (in RStudio, the bottom left panel) is the place where R is waiting for you to tell it what to do, and where it will show the results of a command.  You can type commands directly into the console, but they will be forgotten when you close the session. It is better to enter the commands in the script editor, and save the script. This way, you have a complete record of what you did, you can easily show others how you did it and you can do it again later on if needed. You can copy-paste into the R console, but the RStudio script editor allows you to 'send' the current line or the currently selected text to the R console using the `Ctrl-Enter` shortcut.

At some point in your analysis, you may want to check the content of variable or the structure of an object, without necessarily keep a record of it in your script. You can type these commands directly in the console. RStudio provides the `Ctrl-1` and `Ctrl-2` shortcuts allow you to jump between the script and the console windows.

If R is ready to accept commands, the R console shows a `>` prompt. If it receives a command (by typing, copy-pasting or sent from the script editor using `Ctrl-Enter`; `Command-Enter` will also work on Macs), R will try to execute it, and when ready, show the results and come back with a new `>`-prompt to wait for new commands. This is the equivalent of the `$` in your terminal. 

If R is still waiting for you to enter more data because it isn't complete yet, the console will show a `+` prompt. It means that you haven't finished entering a complete command. This is because you have not 'closed' a parenthesis or quotation. If you're in RStudio and this happens, click inside the console window and press `Esc`; this should help you out of trouble.


**********************************************************

## 2. RMarkdown 

This is an R Markdown document. Markdown is a simple formatting syntax for authoring HTML, PDF, and MS Word documents. For more details on using R Markdown see <http://rmarkdown.rstudio.com>.

When you click the **Knit** button a document will be generated that includes both content as well as the output of any embedded R code chunks within the document. You can embed an R code chunk like this:


```r
summary(cars)
```

```
##      speed           dist       
##  Min.   : 4.0   Min.   :  2.00  
##  1st Qu.:12.0   1st Qu.: 26.00  
##  Median :15.0   Median : 36.00  
##  Mean   :15.4   Mean   : 42.98  
##  3rd Qu.:19.0   3rd Qu.: 56.00  
##  Max.   :25.0   Max.   :120.00
```

You can also embed plots, for example:

<img src="02_rstudio_files/figure-html/pressure-1.png" width="672" />

Note that the `echo = FALSE` parameter was added to the code chunk to prevent printing of the R code that generated the plot.

### 2.1. Julia's thoughts

RMarkdown is fantastic but it is also buggy. 

If you plan to knit a file, try knitting it periodically so that you catch any errors and bugs early.

Kitting to PDF is buggier than knitting to html (usually). 

Embedding LaTeX equations is particularly buggy. 

Resources for using RMarkdown. 

- [R Markdown cheat sheet](https://github.com/rstudio/cheatsheets/blob/master/rmarkdown-2.0.pdf).
- [R Markdown: The Definitive Guide](https://bookdown.org/yihui/rmarkdown/) by Yihui Xie, J. J. Allaire, Garrett Grolemund.


**********************************************************

## 3. Exercises

1. Open the original R program. How does RStudio improve your quality of life?  

2. Create two new documents in RStudio (you don't need to save them). One document should be an R script file and the other should be an RMarkdown file. Run `getwd()` in each to see the default working directory. What is the difference? Why does this matter? 













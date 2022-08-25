## Homework 5
You must submit your GitHub username to Canvas. You must have a _private_ repository with the name specified. You must also add me (edkrueger) and the TAs (ericschulman, mynameisphatcao) as collaborators.  

## Problem 0 - (0 points)

You'll clone a repo that has the datasets, some structure and some (very minimal) starter code.

a) Go to the repo: https://github.com/edkrueger/eco395m-homework-5   

b) Select "Use this template" and create a _private_ repository with the name "eco395m-homework-5".  

c) Select "Settings>Collaborators>" and add "edkrueger", "ericschulman" and "mynameisphatcao" as collaborators.    

## Problem 1 - (100 points)
You'll analyze the word frequencies of the complete works of William Shakespeare.

When grading this problem, we'll execute the code by cloning your repo, running `cd eco395m-homework-5` to open your repository and running `python3 code/shakespeare.py`. This will execute the code on the `main` branch.  
Depending on your Python installation, you may need to run it with `python3 code/shakespeare.py`.  
Because Python paths are relative to the location the _script is executed from_, it is essential to follow this instruction for execution.  
If your code does not execute properly with this command, it will be considered incomplete.  
We'll check for a CSV file called `shakespeare_report.csv` at the location, relative to the top level of the repo, of `artifacts/shakespeare_report.csv`.  

The expectation is that your code generates the output when we run it, not just that the file exists. This means that if the code does not run, you will recieve a 0.  

You'll get 40 points if the code runs and the generated CSV follows the format specified in `artifacts/example_shakespeare_report.csv`. In particular, this means that the CSV must have the same header as the example. If it does not, you will receive a 0.  

You'll get 20 points if the list of words _does not_ include any of the stopwords.  
We'll spot-check your CSV's word counts for the 3 words in the example. If their counts all match the example within +/- 5% of the example's counts, you'll get 20 points. Otherwise, if they are all within +/- 20% of the example's counts, you'll get 10 points.  
We'll spot-check your CSV's word counts for 3 withheld words. If their counts all match the example within +/- 5% of the example's counts, you'll get 20 points. Otherwise, if they are within +/- 20% of the withheld counts, you'll get 10 points.  
We won't use any word with a frequency of less than 500 to check.  

Do not import any modules _other than modules found in the [Python Standard Library](https://docs.python.org/3/library/)_; if you do, You will receive a 0 for this homework.  
In particular, do not use Pandas for this assignment.  
The point of these exercises is to learn Python and some of its standard library.  

_For more realistic problems like this one, there are often many different ways to implement the same requirements.
There is some starter code in the template that you can decide to use entirely, partially, or not at all.  
In any case, if you follow the instructions, you should get the same results I do._

a) Read in the Shakespeare corpus ignoring the header lines, skipping the attribution lines and ignoring the ending line.

b) Import the `re` module. The `re` module is a Python module for Regular Expressions or Regex.
Regex is a language used to find text, extract text and make substitutions efficiently. Its a very useful skill to have for NLP, text analytics and programming in general.
I've used it for many things, including preparing text for NLP models, validating URLs, extracting text while web scraping and parsing terminal output.
I'd encourage you to understand how it works if you are interested, but I'll give you the patterns I used in my solution.

c) Convert to lowercase.  

d) Remove punctuation by running `clean_text = re.sub('[^A-Za-z\s]', '', dirty_text)` with the variables substituted as nescessesary.  

e) Normalize all whitespace to single spaces with `text_with_only_spaces = re.sub("\s+", " ", text_with_arbitrary_whitespace)` with the variables substituted as nescessesary.  

f) Convert your cleaned text into a list of one-word strings.  

g) Read in the stopwords and apply the same cleaning to them as you did to the other text.  

h) Count the number of times that each word _that is not a stopword_ appears.  Don't count the stopwords.  

i) Sort your words by their counts in descending order.
(Hint: Dictionaries are unordered, so you'll want to use the `.items()` method to convert to a list of tuples.
You can then use the `sorted` function to sort your list in descending order using the second index of each tuple as the sort key.)  

j) Write to a CSV file to `artifacts/shakespeare_report.csv` with one column called "word" and one called "count". For an example, see `artifacts/example_shakespeare_report.csv`  

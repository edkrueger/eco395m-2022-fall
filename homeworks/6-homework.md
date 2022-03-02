## Homework 6
You must submit your GitHub username to Canvas. You must have a _private_ repository with the name specified. You must also add me (edkrueger) and the TAs (ericschulman, mynameisphatcao) as collaborators.  

## Problem 0 - (0 points)

You'll clone a repo that has the datasets, some structure and some (very minimal) starter code.  

a) Go to the repo: https://github.com/edkrueger/eco395m-homework-6   

b) Select "Use this template" and create a _private_ repository with the name "eco395m-homework-6".  

c) Select "Settings>Collaborators>" and add "edkrueger", "ericschulman" and "mynameisphatcao" as collaborators.    

## Problem 1 - (50 points)
You'll aggregate 2020 county-level election results into state-level results.

When grading this problem, we'll execute the code by cloning your repo, running `cd eco395m-homework-6` repository and running `python3 code/election_2020.py`.  

Depending on your Python installation, you may need to run it with `python3 code/election_2020.py`.  
Because Python paths are relative to the location the _script is executed from_, it is essential to follow this instruction for execution.  
If your code does not execute properly with this command, it will be considered incomplete.  
We'll check for a CSV file called `election_report.csv` at the location, relative to the top level of the repo, of `artifacts/election_report.csv`.  
The expectation is that your code generates the output when we run it, not just that the file exists.  

You'll get 20 points if the generated CSV follows the format specified in `artifacts/example_election_report.csv`.  
You'll get 10 points if the CSV is in the correct order.
We'll spot-check your CSV's word counts for 3 state/candidate combinations. If their counts all match the example exactly, you'll get 20 points. Otherwise, if they are all within +/- 20% of the example's counts, you'll get 10 points, but we'll have to have a recount. Data is real election data, so you can verify your results against the actual outcomes.

Do not import any modules _other than modules found in the [Python Standard Library](https://docs.python.org/3/library/)_ for this problem; if you do, You will receive a 0 for this problem.  
In particular, do not use Pandas for this problem.  
The point of this problem is to learn Python and some of its standard library.  

_For more realistic problems like this one, there are often many different ways to implement the same requirements.
There is some starter code in the template that you can decide to use entirely, partially, or not at all.  
In any case, if you follow the instructions, you should get the same results I do._

a) Count the votes for each combination of year, state code and candidate while ignoring years that aren't 2020. (Hint: Any immutable type can be a dictionary key in Python; in particular, this means that tuples can be dictionary keys.)  
b) Convert your Dictionary to a list of rows containing year, state code, candidate and total votes so that it is ready to sort.  
c) Sort your list of rows such that the results are in alphabetical order by state code and, for each state, the row are ordered by descending number of votes. In other words, for each state, the candidate with the most votes should appear first. (Hint: There are essentially two approaches to this part. One approach to this problem is to take advantage of the fact that the sort that the `sorted` function uses is a stable sort. A stable sort is a sort that preserves the order of elements where the values of a sort key are the same. Therefore we can sort the list twice, with different keys, to achieve our goal. Another more challenging but potentially more performant option is to create a function that ranks the rows in the correct order and use this as the sort key. This approach is essentially the same as making a utility function that represents safety-first or lexicographical preferences. If you take this approach, note that you can access character codes (which are ordered) for a character with the `ord` function.)  
d) Write to a CSV file to `artifacts/election_report.csv` with columns "year", "state_code", "candidate" and "votes". For an example, see `artifacts/example_election_report.csv`  


## Problem 2 - (50 points)
You'll aggregate 2020 county-level election results into state-level results. But this time with Pandas.  pecifically Pandas 1.3.5, which is on GCP Vertex AI Notebook and we'll use this version to grade.  

When grading this problem, we'll execute the code by cloning your repo, running `cd eco395m-homework-6` repository and running `python3 code/pandas_election_2020.py `.  
Depending on your Python installation, you may need to run it with `python3 code/pandas_election_2020.py`.  
Because Python paths are relative to the location the _script is executed from_, it is essential to follow this instruction for execution.  
If your code does not execute properly with this command, it will be considered incomplete.  
We'll check for a CSV file called `election_report_pandas.csv` at the location, relative to the top level of the repo, of `artifacts/election_report_pandas.csv`.  
The expectation is that your code generates the output when we run it, not just that the file exists.  

You'll get 20 points if the generated CSV follows the format specified in `artifacts/example_election_report.csv`.  
You'll get 10 points if the CSV is in the correct order.
We'll spot-check your CSV's word counts for 3 state/candidate combinations. If their counts all match the example exactly, you'll get 20 points. Otherwise, if they are all within +/- 20% of the example's counts, you'll get 10 points, but we'll have to have a recount. Data is real election data, so you can verify your results against the actual outcomes.

Use Pandas for this problem!

_For more realistic problems like this one, there are often many different ways to implement the same requirements. That said, it is possible to solve this problem as a single method chain pipe. You are encouraged to do so._

a) Count the votes for each year, state code, candidate combination while ignoring years that aren't 2020.  
b) Sort your list of rows such that the results are in alphabetical order by state code and, for each state, the row are ordered by descending number of votes. In other words, for each state, the candidate with the most votes should appear first.  
c) Write to a CSV file to `artifacts/election_report_pandas.csv
` with columns "year", "state_code", "candidate" and "votes". For an example, see `artifacts/example_election_report.csv`  
d) You can check that the CSV from this problem is identical to the last one by running `python3 code/compare.py`  

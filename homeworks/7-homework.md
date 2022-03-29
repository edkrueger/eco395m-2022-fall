## Homework 7
You must submit your GitHub username to Canvas. You must have a _private_ repository with the name specified. You must also add me (edkrueger) and the TAs (ericschulman, mynameisphatcao) as collaborators.  

## Problem 0 - (0 points)

You'll clone a repo that has the datasets, some structure and some (very minimal) starter code.  

a) Go to the repo: https://github.com/edkrueger/eco395m-homework-7

b) Select "Use this template" and create a _private_ repository with the name "eco395m-homework-7".  

c) Select "Settings>Collaborators>" and add "edkrueger", "ericschulman" and "mynameisphatcao" as collaborators.  

## Problem 1 - (100 points)
You'll scrape the website http://books.toscrape.com/, collecting the following fields: 

| Field | Type | Example |
| - | - | - | - |
| "upc" | str | "a897fe39b1053632" |
| "title" | str | "A Light in the Attic" |
| "category" | str | "Poetry" |
| "description" | str | "It's hard to imagine a world" (trimmed here) |
| "price_gbp" | float | 51.77 |
| "stock" | int | 22 |

The example comes from this [book](http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html).  

You'll write the data to a CSV and a JSONL. See [this](https://jsonlines.org/) for the JSONL specification.  

When grading this problem, we'll execute the code by cloning your repo, running `cd eco395m-homework-7` repository and running `python code/scrape.py`.  
Your code will be executed in a Python environment containing only the Standard Library and the packages specified in `requirements.txt`.  

Because Python paths are relative to the location the _script is executed from_, it is essential to follow this instruction for execution.  
If your code does not execute properly with this command, it will be considered incomplete.  
We'll check for a CSV file called `results.csv` at the location, relative to the top level of the repo, of `artifacts/results.csv`.
We'll also check for a JSONL file called `results.jsonl` at the location, relative to the top level of the repo, of `artifacts/results.jsonl`.

The expectation is that your code generates the output when we run it, not just that the file exists. This means that if the code does not run, you will receive a 0.  
We also expect that your code executes in under 5 minutes, if it does not, you will receive a 0.  

You'll get 10 points if the generated CSV follows the format specified in `artifacts/example_results.csv`. In particular, this means that the CSV must have the same header as the example. If it does not, you will receive a 0 for this part.  
You'll get 10 points if the generated JSONL follows the format specified in `artifacts/example_results.jsonl`. In particular, this means that the CSV must have the same fieldnames as the example. If it does not, you will receive a 0 for this part. Note, that since JSONL lines are JSON Objects, they are considered unstructured, so the order in which the key-value pairs appear does not matter.  

You'll get 20 points if your CSV contains all 1000 books and 0 points otherwise.  
You'll get 20 points if your JSONL contains all 1000 books and 0 points otherwise.  

We'll spot-check 3 of your CSV's books for an exact match on all values for all fields _except_ "description". If all of the fields checked match exactly for all 3 book, you'll receive 30 points and 0 points otherwise.  
We'll spot-check 3 of your JSONL's books for an exact match on all values for all fields _except_ "description". If all of the fields checked match exactly for all 3 book, you'll receive 30 points and 0 points otherwise.  

_For more realistic problems like this one, there are often many different ways to implement the same requirements. You are not required to use the starter code, but if you do, the steps will follow the order below._

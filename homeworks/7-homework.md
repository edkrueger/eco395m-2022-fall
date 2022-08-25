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
| - | - | - |
| "upc" | str | "a897fe39b1053632" |
| "title" | str | "A Light in the Attic" |
| "category" | str | "Poetry" |
| "description" | str | "It's hard to imagine a world" (trimmed here) |
| "price_gbp" | float | 51.77 |
| "stock" | int | 22 |

The example comes from this [book](http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html).  

You'll write the data to a CSV and a JSONL. See [this](https://jsonlines.org/) for the JSONL specification.  

When grading this problem, we'll execute the code by cloning your repo, running `cd eco395m-homework-7` to open your repository and running `python code/scrape.py`.

Your code will be executed in a Python environment containing only the Standard Library and the packages specified in `requirements.txt`. Install them with `pip install -r requirements.txt`.   

Because Python paths are relative to the location the _script is executed from_, it is essential to follow this instruction for execution.  
If your code does not execute properly with this command, it will be considered incomplete.  
We'll check for a CSV file called `results.csv` at the location, relative to the top level of the repo, of `artifacts/results.csv`.
We'll also check for a JSONL file called `results.jsonl` at the location, relative to the top level of the repo, of `artifacts/results.jsonl`.

The expectation is that your code generates the output when we run it, not just that the file exists. This means that if the code does not run, you will receive a 0.  
We also expect that your code executes in under 5 minutes, if it does not, you will receive a 0.  

You'll get 10 points if the generated CSV follows the format specified in `artifacts/example_results.csv`. In particular, this means that the CSV must have the same header as the example. If it does not, you will receive a 0 for this part.  
You'll get 10 points if the generated JSONL follows the format specified in `artifacts/example_results.jsonl`. In particular, this means that the CSV must have the same fieldnames as the example. If it does not, you will receive a 0 for this part. Note, that since JSONL lines are JSON Objects, they are considered unstructured, so the order in which the key-value pairs appear does not matter.  

You'll get 10 additional points if your CSV contains all 1000 books and 0 points otherwise.  
You'll get 10 additional points if your JSONL contains all 1000 books and 0 points otherwise.  

We'll spot-check 3 of your CSV's books for an exact match on all values for all fields _except_ "description". If all of the fields checked match exactly for all 3 book, you'll receive 30 points and 0 points otherwise.  
We'll spot-check 3 of your JSONL's books for an exact match on all values for all fields _except_ "description". If all of the fields checked match exactly for all 3 book, you'll receive 30 points and 0 points otherwise.  

_For more realistic problems like this one, there are often many different ways to implement the same requirements. You are not required to use the starter code, but if you do, the steps will follow the order below._

A function called `get_soup` is already implemented for you in the starter code. It takes a URL and returns a `bs4.BeautifulSoup` instance representing the webpage at the URL.  
a) Write `scrape_page`, a function to scrape all of the book URLs from a page. There is a test to check if this function works properly. You can execute it by running `python code/scrape_pages.py`. (Hint: If there is no page with the given number, have this function return an empty list.)  
b) Write `scrape_all_pages`, a function to scrape all of the book URLs from all pages using `scrape_page`. (Hint: This function should end when it encounters a page that has no books.  I.e. then scrape_page returns an empty list.)  
c) Implement `extract_price` and `extract_stock` to clean the strings in the format that appears on the books. There are tests to check if this function works properly. You can execute them by running `python code/scrape_books.py`.  
d) Implement `get_category`, `get_title`, `get_description` and `get_product_information` that take a soup object that represents a book. There are tests for these; run them as in (c). 
e) Implement `scrape_book` which uses the functions from (d) to scrape a book given its URL. There is a test for this; run it as in (c).  
f) Implement `scrape_books` which uses `scrape_book` to scrape a list of books given their URLs.
e) Implement `scrape` which uses `scrape_all_pages` and `scrape_books` to scrape all books.  
f) Write `write_books_to_csv` to save the books to CSV.  
g) Write `write_books_to_jsonl` to save the books to JSONL. Be sure to use `encoding="utf-8"`.  




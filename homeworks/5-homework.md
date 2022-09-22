## Homework 5
You must have a _private_ repository with the name specified. You must also add me (edkrueger) and the TAs ([Click here for TA GitHub usernames](/ta-githubs.txt)) as collaborators.  

## Problem 0 - (0 points)

You'll request data about groundwater from the USGS's groundwater REST service for the summer of 2022. Click (here)[https://waterservices.usgs.gov/rest/GW-Levels-Service.html] for the documentation -- you'll need it.

You'll clone a repo some starter code.  

a) Go to the repo: https://github.com/edkrueger/eco395m-homework-groundwater  

b) Select "Use this template" and create a _private_ repository with the name "eco395m-homework-groundwater".  

c) Select "Settings>Collaborators>" and add "edkrueger" and the TAs as collaborators.

## Problem 1 - (100 points)
You'll scrape the endpoint mentioned above, collecting the following fields: 

| Field | Type | Example |
| - | - | - |
| "variable_name" | str | "Depth to water level, ft below land surface" |
| "site_name" | str | "AS-69-23-402 (Hondo Canyon)" |
| "datetime" | str) (ISO 8601 datetime ) | "2022-07-27 14:40:00" |
| "value" | float | 247.68 |
| "longitude" | float | -98.5955556 |
| "latitude" | float | 29.49527778 |

You'll request the data from the endpoint for the state of Texas for the Summer of 2022 in a JSON format. Summer 2022 is between June 21st and September 22nd, inclusive.

You'll extract the fields referenced and create rows for each value.

You'll sort the rows lexicographically by `variable_name`, `site_name`, and then `datetime`.
 
You'll write the data to a CSV.

When grading this problem, we'll execute the code by cloning your repo, running `cd eco395m-homework-groundwater` to open your repository and running `python code/scrape.py`.

Your code will be executed in a Python environment containing only the Standard Library and the packages specified in `requirements.txt`. Install them with `pip install -r requirements.txt`.   

Because Python paths are relative to the location the _script is executed from_, it is essential to follow this instruction for execution.  
If your code does not execute properly with this command, it will be considered incomplete.  
We'll check for a CSV file called `results.csv` at the location, relative to the top level of the repo, of `artifacts/results.csv`.

The expectation is that your code generates the output when we run it, not just that the file exists. This means that if the code does not run, you will receive a 0.  

We also expect that your code executes in under 1 minute; if it does not, you will receive a 0. For context, my code executes in under 1/5th of a second.  

You'll get 20 points if the generated CSV follows the format specified in `artifacts/example_results.csv`. In particular, the CSV must have the same header as the example. If it does not, you will receive a 0 for this part.  

You'll get 20 additional points if your CSV contains at least as many rows as mine does.  

We'll spot-check 3 of your CSV's rows for an exact match on all values. If all of the fields checked match exactly for all 3 rows, you'll receive 60 points and 0 points otherwise.  

_You are required to use the starter code. If you don't we will not help you. You don't necessarily need to complete the steps in the order below, but you should follow all of the steps._

a) Figure out the request you have to make in Postman. To minimize USGS's egress costs, allow compression in transit. See the endpoint documentation for more details.  

b) Have a look at the response in Postman to understand the structure.  

c) Look at `clean_data.py` and notice that I've left in tests for many of the functions under `if __name__ == "__main__"`. You can also use the sample data in this section to understand what the raw data looks like and what is expected for each function's output.  

d) Implement `extract_metadata_from_timeseries`, `extract_metadata_from_timeseries` and `extract_data_from_timeseries` in `clean_data.py`. There is an assertion for each of these functions that will act as a test under `if __name__ == "__main__"`. You can execute them by running `python code/clean_data.py`. If they return an assertion error, then the test failed, and you need to figure out why. This time around, feel free to modify code under `if __name__ == "__main__"` in particular, you may want to add some print statements or some additional tests. When implementing `extract_data_from_timeseries`, note that the dates that come in a response are in a special string format called ISO format. There is a constructor for `datetime` objects that can read this format. You don't need to write your own parser. See the docs for `datetime` (here)[https://docs.python.org/3/library/datetime.html].

e) Take your work in (a) and use it to implement `request_raw_data` in `scrape.py`.   

f) Implement the other functions in `clean_data.py`.  

g) Implement the other functions in `scrape.py`. Note that one way to sort lexicographically is to use a stable sort and start the innermost column sort by it, then sort by the next innermost column, etc. Then, stop when you reach the outermost column. Also, note that the `csv` module knows how to serialize `datetime` objects, so you won't have to do any conversion.

# Homework 8
You must have a _private_ repository with the name specified. You must also add me (edkrueger) and the TAs ([Click here for TA GitHub usernames](/ta-githubs.txt)) as collaborators.  

## Problem 0 - (0 points)
You'll clone a repo with several SQL exercises.

a) Go to the repo: https://github.com/edkrueger/eco395m-homework-chinook  

b) Select "Use this template" and create a _private_ repository with the name "eco395m-homework-chinook".  

c) Select "Settings>Collaborators>" and add "edkrueger"and the TA(s) as collaborators.  

## Problem 1 - (0 points)

You'll make a database instance and a database, then you will connect to it with DBeaver (or another SQL client of your choice) and run a script to create and load the tables. You'll also configure the environmental variables so that the checker, written in Python, can execute SQL against your database.

a) Make a database instance as we did in class. If you've already done this, you can use the one you already have. Go to GCP SQL and create a PostgreSQL 13 database instance. Make sure that you whitelist the IPs in block 0.0.0.0/0. Picking the lowest spec for this instance will be sufficient for this problem. Save your password!  

b) Use GCP SQL to create a database called `chinook`. You can do this in the "Databases" tab.

c) Connect to your database with DBeaver. Your host can be found in GCP SQL on the "Overview" tab. The port will be the default Postgres port: `5432`. You can use the default postgres username, `postgres`, and the password you set in the last step. Connect with database as `chinook`.

d) In DBeaver, Navigate to "chinook" > "Databases" > "chinook". Right-click the database `chinook` -- its the one that looks like a silo. Then select "SQL Editor" > "New SQL Script".

f) Copy the code in `setup/chinook.sql` into you SQL editor and execute it.

e) Before you can run the checker, you must give it the right credentials to connect to your database. Copy the file `demo.env` to `.env` and modify it by providing the credentials you found in step (c). An easy way to do this is to run `cp demo.env .env` and then modify the file.  

f) Run the checker by running `python code/checker.py`. If you've configured everything properly, you'll see an error like `can't execute an empty query` because your queries haven't been written yet. If your connection configuration is incorrect you receive an error message like `connection to server at "123.456.789.101", port 5432 failed: FATAL:  password authentication failed for user "postgres"`.

## Problem 2 - (100 points)
You'll solve the SQL problems in `code/queries.py`. You can check your answers by running `python code/check.py`.

When grading this problem...  

When grading this problem, we'll execute the code by cloning your repo, running `cd eco395m-homework-chinook` to open your repository and running `python3 code/queries.py`. This will execute the code on the `main` branch.  

100 points will be awarded in proportion to the number of exercises you successfully solve. An exercise will be successfully solved if your solution passes all of the cases. A solution that does not pass all of the cases will not be considered successfully solved.  

_You are allowed to skip up to 2 exercises. There are 12 exercises in total. So, submissions with at least 10 successfully solved exercises will receive all 100 points._  

a) For each exercise in `queries.py`. Develop your solution in DBeaver and when you believe it is correct, copy it and paste it into the triple-quoted string under the exercise in `queries.py`. Check your solution by running `python code/check.py`, modify your code as needed and try again. (Hint: If you are confused about a test case, feel free to _read_ the test code -- just don't modify the test code!)  
b) Repeat for the other exercises.

_Do not modify the code in `check.py`. Do not hard code solutions to test cases in your queries. These will be considered academic dishonesty, and you will receive a 0 for this homework._  
_Do not import anything or write any code other than the SQL in the query strings in `query.py`. You will receive a 0 for this homework if you do. The point of these exercises is to learn SQL._  

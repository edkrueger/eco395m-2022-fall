# Homework 8
You must submit your GitHub username to Canvas. You must have a _private_ repository with the name specified. You must also add me (edkrueger) and the TAs (ericschulman, mynameisphatcao) as collaborators.  

## Problem 0 - (0 points)
You'll clone a repo with several SQL exercises.

a) Go to the repo: https://github.com/edkrueger/eco395m-homework-8

b) Select "Use this template" and create a _private_ repository with the name "eco395m-homework-8".  

c) Select "Settings>Collaborators>" and add "edkrueger", "ericschulman" and "mynameisphatcao" as collaborators.    

## Problem 1 - (0 points)

You'll make a database instance and a database, then you will connect to it with DBeaver (or another SQL client of your choice) and run a script to create and load the tables. You'll also configure the environmental variables so that the checker, written in Python, can execute SQL against your database.

a) Make a database instance as we did in class. If you've already done this, you can use the one you already have. Go to GCP SQL and create a PostgreSQL 13 database instance. Make sure that you whitelist the IPs in block 0.0.0.0/0. Picking the lowest spec for this instance will be sufficient for this problem. Save your password!  

b) Use GCP SQL to create a database called `chinook`. You can do this in the "Databases" tab.

c) Connect to your database with DBeaver. Your host can be found in GCP SQL on the "Overview" tab. The port will be the default Postgres port: `5432`. You can use the default postgres username, `postgres`, and the password you set in the last step. Connect with database as `chinook`.

d) In DBeaver, Navigate to "chinook" > "Databases" > "chinook". Right-click the database `chinook` -- its the one that looks like a silo. Then select "SQL Editor" > "New SQL Script".

f) Copy the code in `setup/chinook.sql` into you SQL editor and execute it.

e) Before you can run the checker, you must give it the right credentials to connect to your database. Copy the file `demo.env` to `.env` and modify it by providing the credentials you found in step (c).

f) Run the checker by running `python code/checker.py`. If you've configured everything properly, you'll see an error like `can't execute an empty query` because your queries haven't been written yet. If your connection configuration is incorrect you receive an error message like `connection to server at "123.456.789.101", port 5432 failed: FATAL:  password authentication failed for user "postgres"`.


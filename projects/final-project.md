# Final Project 

You’ll work in self-assigned groups with 3-10 members. (If there are too many small groups, I may have to merge them or adjust presentation times.)

You'll use a database. You'll select a topic and data sources to load into a database. This may take the form of ETL with a Python, Pandas, or other script, directly loading CSVs or other files into Postgres or BigQuery, or using a database to store results of web or API scraping. Other uses could be acceptable, such as building an app to load data into and from a database or using a database as a way of caching scientific computations.

You'll include an analysis and visualization element in your project.

You'll have to use at least one significant technology or pattern that we haven't covered in homework. Some examples of variable difficulty could include:
* Using GCP Data Studio to connect to a Database and produce visualizations
* Using Big Query
* Making an interactive dashboard in Streamlit
* Making an application or dashboard in Flask
* Making and deploying a dashboard as a static site
* Using the ORM part of SQLAlchemy
* Use Dask or Spark to process larger datasets
* Take advantage of Postgres' Full-text search
* Take advantage of Postgres' GIS capabilities
* Schedule scraper to run periodically by deploying
* Use an ML model to make predictions on demand
* Using a noSQL database

You’ll use a public GitHub repository to organize, record and document your work and your findings. This project will become part of your portfolio – it's public, so you are welcome and encouraged to share it when you are done. You’ll present your work to the class.

## Use of a Database - (10 points)
* You'll use a database to perform meaningful tasks
* You'll leverage your databases' querying capabilities appropriately (i.e. you won't simply dump your entire database into a dataframe to analyze it.)

## Use of new technology or pattern - (10 points)
* You'll use a new technology or pattern to perform meaningful tasks
* You'll discuss your choice with me to set group-specific goals which you'll be graded according to

## The Report in README.md - (15 points)

The report should cover your data source and your analysis.  

Requirements for reporting your analysis:
* The goal of the analysis is must be clearly articulated
* The report must include your methodology
* The report must include a description of your project and its findings (or lack of findings)
* Your findings (or non-findings) must be clearly documented
* Your findings must be supported by your analysis
* The limitations of the analysis must be clearly outlined
* Extensions of your analysis or areas for more research must be included in your report
* You should not include analysis, plots, discoveries, that aren’t directly related to your findings – you can put them as an appendix in another file if you like

Requirements for reporting about the data:
* Source(s) of dataset(s) must be clearly documented
* Data collection methods must be understood and clearly documented. You should read and summarize the documentation of the data, make sure that you understand and document all columns/features that are relevant to your analysis. You should understand and summarize what isn’t in the data too.
* Limitations of the data must be clearly outlined
* A discussion of extensions of data that would be required to improve the analysis should be included

## Reproducibility - (20 points)

Your work must be reproducible. This means that anyone should be able to follow your instructions to run your code on your data and get the same results you do.  

Requirements for reproducibility:
* Instructions to rerun that analysis must be included in the README.md
* The analysis must run in a GCP Vertex AI Notebook (unless not applicable -- ask me before)
* Additional packages should be included in `requirements.txt`
* All data cleaning must be reproducible through code – data must not be manually modified (i.e. no modifications in Excel)
* Must use relative paths
* Data should be included in the repository if the dataset is small enough, otherwise, instructions for downloading the datasets and placing them in the right locations are required

## Code Quality - (15 points)

Requirements for formatting:
* Your code should use double and single quotes consistently
* Long lines, pipes or method chains must be broken into smaller lines
* (Note: Formatting can be automated using [black](https://black.readthedocs.io/en/stable/) for .py files or [nb-black](https://pypi.org/project/nb-black/) for notebooks)

Requirements for clean code:
* You should remove unused imports
* You should delete functions that are no longer used
* You should remove code that isn’t used
* You should not have any commented out code

Requirements for comments and docstrings:
* Functions should have simple docstrings explaining their inputs and outputs
* Comments should be used sparingly either to clarify difficult to understand, unintuitive or otherwise surprising code or to add structure (Note: In most cases, a function with a docstring will be a better option than a comment)

Software design:
* Use appropriate tools for appropriate tasks, don't use tools when you don't need them (i.e. don't use Pandas dataframes as an unnecessary replacement for dictionaries and lists)
* Use tools appropriately (i.e. use method chaining in Pandas)
* Consistency in the use of tools (i.e. using just one graphing library or visualization tool with consistent styling)
* Use of functions to produce modular code

Security:
* You won't leak credentials (you _really_ do not want to do this in a public repo, but you shouldn't do it in a private one either -- ask me why)
* You'll use some method of sanitizing database commands where appropriate (i.e. don't use f-string or string concatenation to template database commands)

## Repo - (5 points)

Requirements for the repo:
* Your group must collaborate in a single repository
* When you submit your project, all of your code and documentation should be on the main branch
* You should use GitHub Issues to organize your work and allow for collaboration
* You should make a branch for each issue
* Your repo should have at least 60 commits as a group

## Presentation - (5 points)

Presentations will be in class on Friday, May 13, 2:00pm-5:00pm CT.  

Requirements for the presentation:
* You should try to test your setup in <location TBD> before the day of presentations if possible, problems during the setup will cut into your presentations and affect your grade.
* The presentation must be around 10 minutes – we’ll cut you off if it isn’t.
* The presentation should primarily focus on your goal, methodology, findings, limitations and potential extensions.
* You should limit your discussion of packages or techniques, whether related to the code or otherwise, to things that your classmates would not already know either from in class or in their training as Economists.
* Your whole group should collaborate in designing and rehearsing the presentation. With additional time, I recommend having more than one member speak, but it is acceptable if one person wishes to take the presentation.
* You’ll have 5 minutes of Q&A with the class and me.

## Individual Requirements - (20 points)
* You must solve at least two meaningful issues
* You make at least 10 meaningful commits
* You must attend your group’s presentation and all others

# Midterm Project

You’ll work in self assigned groups with 3-5 members. You’ll create a dataset by combining other datasets or scraping data. Unless you come to me for a specific exemption, don't use only a Kaggle dataset, similarly clean data or a toy dataset. Then you’ll perform an analysis on that dataset. You’ll use a public GitHub repository to organize, record and document your work and your findings. This project will become part of your portfolio – it's public, so you are welcome and encouraged to share it when you are done. You’ll present your work to the class.

## The Report in README.md - (30 points)

The report should cover your data source and your analysis.  

Requirements for reporting about the data:
* Source(s) of dataset(s) must be clearly documented
* Data collection methods must be understood and clearly documented. You should read and summarize the documentation of the data, make sure that you understand and document all columns/features that are relevant to your analysis. You should understand and summarize what isn’t in the data too.
* Limitations of the data must be clearly outlined
* A discussion of extensions of data that would be required to improve the analysis should be included

Requirements for reporting your analysis:
* The goal of the analysis is must be clearly articulated
* The report must include your methodology
* The report must include a description of your project and its findings (or lack of findings)
* Your findings (or non-findings) must be clearly documented
* The limitations of the analysis must be clearly outlined
* Extensions of your analysis or areas for more research must be included in your report
* You should not include analysis, plots, discoveries, that aren’t directly related to your findings – you can put them as an appendix in another file if you like

## Reproducibility - (20 points)

Your work must be reproducible. This means that anyone should be able to follow your instructions to run your code on your data and get the same results you do.  

Requirements for reproducibility:
* Instructions to rerun that analysis must be included in the README.md
* ~The analysis must run in a GCP Vertex AI Notebook~ (removed for Fall 2022)
* Additional packages should be included in `requirements.txt`
* All data cleaning must be reproducible through code – data must not be manually modified (i.e. no modifications in Excel)
* Must use relative paths
* Data should be included in the repository if the dataset is small enough, otherwise instructions for downloading the datasets and placing them in the right locations is required.

## Code Quality - (10 points)

Requirements for formatting:
* Your code should use double and single quotes consistently
* Long lines, pipes or method chains must be broken into smaller lines
* (Note: Formatting can be automated using [black](https://black.readthedocs.io/en/stable/) for .py files or [nb-black](https://pypi.org/project/nb-black/) for notebooks)

Requirements for clean code:
* You should remove unused imports
* You should delete functions that are no longer used
* Your should remove code that isn’t used
* Your should not have any commented out code

Requirements for comments and docstrings:
* Functions should have simple docstrings explaining their inputs and outputs
* Comments should be used sparingly either to clarify difficult to understand, unintuitive or otherwise surprising code or add structure. (Note: In most cases a function with a docstring will be a better option than a comment.)


## Repo - (10 points)

Requirements for the repo:
* You group must collaborate in a single repository
* When you submit your project, all of your code and documentation should be on the main branch
* You should use GitHub Issues to organize your work and allow for collaboration
* You should make a branch for each issue
* Your repo should have at least 30 commits as a group

## Presentation - (10 points)

Presentations will be in class on the day specified in the syllabus.  

Requirements for the presentation:
* You must test your setup in BRB 1.118 before the day of presentations, problems during the setup will cut into your presentations and affect your grade.
* The presentation must be around 6 minutes – we’ll cut you off if it isn’t.
* The presentation should primarily focus on your goal, methodology, findings, limitations and potential extensions.
* You should limit your discussion of packages or techniques, whether related to the code or otherwise, to things that your classmates would not already know either from in class or their training as Economists.
* You may delegate a single person to present – you whole group should collaborate in designing and rehearsing the presentation.
* You’ll have 6 minutes of Q&A with the class and I.

## Individual Requirements - (20 points)
* You must solve at least two meaningful (GitHub) issues
* You make at least 5 meaningful commits that contribute _code_ to the repo
* You must attend your group’s presentation and all others

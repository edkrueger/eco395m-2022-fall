## Homework 1
You must submit a URL to your _private_ GitHub repository called `eco395m-homework-1` to receive credit. You must also add me (edkrueger) and the TAs (ericschulman, mynameisphatcao) as collaborators.  
You will not submit your fork in Problem 3. We'll be able to grade that problem by looking at your PR (pull request) to the class repo.  

## Problem 0 - (0 points)
Some initial setup.  
a) Create a new private repository called `eco395m-homework-1` on GitHub  
b) Select "Settings>Collaborators>" and add "edkrueger", "ericschulman" and "mynameisphatcao" as collaborators  
c) Clone the repository locally  

## Problem 1 - (10 points)
You'll commit your first file to GitHub.  

We'll grade this problem by checking if the file exists on GitHub and if it was added with a commit through the git CLI.  

a) Create a file at the top of your repository with "Hello World" in it by running: `echo "Hello World" > hello.txt`  

b) Have git track the file by running:  `git add hello.txt`  

c) Commit the file by running: `git commit -m "Say Hello."`  

d) Push the file to GitHub by running: `git push`  

## Problem 2 - (60 points)
You'll get used to using bash and git in this problem. You'll create files and folders representing your home. You'll create a shell script to make your "home" automatically. You'll push the results to GitHub in stages.  

We'll grade this problem by:
* Checking if your "home" exists
* Checking if your script generates your "home"
* Checking for the absence of extraneous files.
* Checking for at least 2 commits

a) Create a folder in your repository called `home`  

b) Using `mkdir`, `cd`, `ls`, `pwd`, `touch`, etc. Make a representation of your home inside the home folder. Folders represent rooms or areas in your home. Make a few files representing things in those rooms/areas. There is no need to make this too complex; make sure you get the hang of it.  
_(Note: that git doesn't track folders; it tracks files. So make sure to have at least one file in each folder.)_  

c) Run `git status -u`. Do you see any files that you didn't intentionally create? If you do, create a `.gitignore` file in your repository top directory and have it ignore the extra files. Commit the `.gitignore` file and run `git status -u` again. You should no longer see these files.  
_(Note: Operating systems, text editors, IDEs and many other applications create hidden files that store their configuration in files. These files all relate to your local machines, and it's considered bad practice to commit these to git. In this and future homeworks, you will lose points for having these files in your GitHub repos.)_  

d) Commit the files you created and push them to the GitHub repository.  

e) Take some of the commands you ran to make your "home" and make them into the script called `make_home.sh` in the `home` directory. Run the script by running `sh make_home.sh` to ensure it works.  

f) Commit the script and push it to the GitHub repository.  

## Problem 3 (30 points)

You'll fork the class repository and add a text file introducing yourself. Then you will make a Pull Request to merge in your file.  

We'll grade this problem by checking for the existence of the Pull Request.  

a) Navigate to the class repository and make a fork.  
b) Clone your fork locally.  
c) Make a folder called `introductions`.  
d) In that folder, make a file in the format `<first name>-<last name>.txt`. For example, for me, the fill would be called `edward-krueger.txt`.  
e) In that file, introduce yourself. Be sure to mention your interests in economics, programming and data. Feel free to include whatever else you like. You won't be graded on the contents, but you may wish to look at other students' responses to get to know your classmates and find common interests for group projects.  
_(Note: this is a public repository, so your response will be visible to anyone.)_  

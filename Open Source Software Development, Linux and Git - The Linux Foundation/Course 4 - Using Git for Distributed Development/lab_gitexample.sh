#!/bin/bash
#/* **************** Coursera/lab_gitexample.sh **************** */
#/*
# * The code herein is: Copyright the Linux Foundation, 2018
# *
# * This Copyright is retained for the purpose of protecting free
# * redistribution of source.
# *
# *     URL:    http://training.linuxfoundation.org
# *     email:  trainingquestions@linuxfoundation.org
# *
# * This code is distributed under Version 2 of the GNU General Public
# * License, which you should have received with the source.
# *
# */
#!/bin/bash 

# Set up the directory we are going to work in 

rm -rf git-test ; mkdir git-test ; cd git-test

# initialize the repository and put our name and email in the .config file

echo -e "\n\n*************   CREATING THE REPOSITORY AND CONFIGURING IT\n\n"

git init
git config user.name "A Smart Guy"
git config user.email "asmartguy@linux.com"

echo -e "\n\n*************   CREATING A COUPLE OF FILES AND ADDING THEM TO THE PROJECT AND COMMITTING\n\n"

# create a couple of files and add them to the project
# we'll do this as two commits, although we could do it as one

echo file1 > file1
git add file1
git commit file1 -m "This is the first commit"

echo file2 > file2
git add file2
git commit . -m "This is the second commit"

# modify one of the files and then see the difference with the repository

echo -e "\n\n*************   MODIFYING ONE OF THE FILES AND THEN DIFFING\n\n"

echo This is another line for file2 >> file2
git diff

# now stage it and diff again
git add file2
git diff

echo -e "\n\n*************   ADDING THE MODIFIED FILE AND THEN DIFFING AGAIN\n\n"

echo -e "\n\n*************   RECOMITTING FOR THE THIRD TIME\n\n"

# now get it all in with another commit

git commit . -m "This is the third commit"

echo -e" \n\n*************   LOOKING AT THE HISTORY OF THE PROJECT\n\n"

# look at the history

git log

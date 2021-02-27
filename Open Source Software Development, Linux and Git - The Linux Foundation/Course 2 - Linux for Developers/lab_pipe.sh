#!/bin/bash
#/* **************** LFD201:2018-05-21 s_11/lab_pipe.sh **************** */
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

# Lab: Redirection
     
# Try a command such as the following:

#      $ ls /etc/passwd /etc/passwd_not

# where one file exists and the other does not.

# 1) Get the 'stdout' output of the command in one file and the
#    'stderr' output in another.

ls /etc/passwd /etc/passwd_not > stdout_out 2> stderr_out

echo stdout_out contains: 
cat stdout_out

echo stderr_out contains:
cat stderr_out

# 2) Now get them both to go to the same file.

ls /etc/passwd /etc/passwd_not >& stdout_and_stderr_out            
# 
ls /etc/passwd /etc/passwd_not >  stdout_and_stderr_out 2>&1 

echo stdout_and_stderr_out contains:
cat stdout_and_stderr_out

# 3) Now get the 'stderr' output to go away to '/dev/null'

ls /etc/passwd /etc/passwd_not 2> /dev/null
echo was the output on the terminal

# 4) Now pipe the result of the 'ls' command into 'sort' and get the
# 'stderr' output into a separate file.

ls /etc/passwd /etc/passwd_not  2> stderr_out | sort > stdout_out

echo stdout_out now contains:
cat stdout_out
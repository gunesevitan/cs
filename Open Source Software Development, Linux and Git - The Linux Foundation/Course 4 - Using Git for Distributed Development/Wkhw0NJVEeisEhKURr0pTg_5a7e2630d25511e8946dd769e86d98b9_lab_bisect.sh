#!/bin/bash
#/* **************** Coursera/lab_bisect.sh **************** */
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

# initialize the repository and put our name and email in the .config file

echo -e "\n\n*************   CREATING THE REPOSITORY AND CONFIGURING IT\n\n"

rm -rf git-test ; mkdir git-test ; cd git-test
git init
git config user.name "A Smart Guy"
git config user.email "asmartguy@linux.com"

echo -e "\n\n*************   CREATING A NUMBER OF  FILES AND ADDING"
echo -e "                    THEM TO THE PROJECT AND COMMITTING\n\n"

n=0
while [ $n -lt 64 ] ; do
    n=$(($n+1))
    file=file$n
    echo file > $file
    if [ "$n" == "19" ] ; then 
	echo BAD >> $file  
    fi
    git add $file
    git commit $file -m"$file"
    git tag $file
    echo I added and commmitted $file
done

echo -e "\n\n************* I PUT THE BAD LINE IN file19\n\n"

echo -e "\n\n************* STARTING THE BISCETION\n\n"

git bisect start 
git bisect bad 
git bisect good file1

echo -e "\n\n************* SEARCHING FOR THE BAD FILE\n\n"

echo -e "\n\n************* DOING TH BISECTION MANUALLY\n\n"

over=0
while [ "$over" == "0" ] ; do
    if [ "$(grep BAD file*)" == "" ] ; then
	git bisect good | tee gitout
    else
	git bisect bad  | tee  gitout
    fi

    if [ "$(grep 'revisions left' gitout)" == "" ] ; then
	over=1
	echo "****************** FOUND THE BUG!"
    fi
done

echo -e "\n\n*************** SETTING UP A TESTING SCRIPT\n\n"

cat <<EOF >> my_script.sh
#!/bin/bash

if [ "\$(grep BAD file*)" == "" ] ; then
    exit 0
fi
exit 1
EOF
chmod +x my_script.sh

# reset to original state

git reset

git bisect start
git bisect bad  file64
git bisect good file1

# do automated script

git bisect run ./my_script.sh

# check log

git bisect log




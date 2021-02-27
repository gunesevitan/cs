#!/bin/bash
#/* **************** Coursera: lab_stress.sh **************** */
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

set -x

tar zxvf stress-1.0.4.tar.gz

cd stress-1.0.4

./configure

make

sudo make install


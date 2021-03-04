#!/bin/bash
#/* **************** Coursera/build_rpm.sh **************** */
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

RROOT=$HOME/rpmbuild
PATCHFILE=my_app-1.0.0.patch

# just for in testing:
# rm -rf $RROOT

for names in SOURCES SPECS BUILD RPMS SRPMS ; do
    [[ ! -d $RROOT/$names ]] &&  mkdir -p $RROOT/$names
done 
# construct patch file
diff -Naur my_app-1.0.0 my_app-1.0.0_PATCHED > $PATCHFILE
# produce unpatched source tar ball
tar zcvf $RROOT/SOURCES/my_app-1.0.0.tar.gz my_app-1.0.0

# copy specfile and tar ball to the rpmbuild directories
cp $PATCHFILE $RROOT/SOURCES/
cp my_app-1.0.0.spec $RROOT/SPECS
cd $RROOT/SPECS
# ok construct binary and source rpms!
rpmbuild  -ba my_app-1.0.0.spec

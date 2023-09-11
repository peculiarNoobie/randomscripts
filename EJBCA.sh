#!/bin/bash

###################################################################################
#        Download the new configdumpresult.tgz - configdumpresult.tgz             #
#        Download the old configdumpresult.tgz - configdumpresult (1).tgz         #
#                                                                                 #
##################################################################################
###JRG###

homedir=~

#put your own directory
mydir=~/Documents/Godmode/PHInfrascripts
dl=$homedir"/Downloads"
## variable ex is for extracting the configdumpresult using tar command
ex='tar -xvf'
folcompare=$mydir"/EJBCA/foldercompare.py"
oldConfig=$dl"/configdumpresult (1).tgz"
oldConfig0=$dl"/configdumpresult.tgz"
oldConfig1=$dl"/configdumpresult(1).tgz"
oldConfig2=$dl"/configdumpresult.tar.gz"
oldConfig3=$dl"/configdumpresult (1).tar.gz"

config=$dl"/configdumpresult.tar.gz"
config1=$dl"/configdumpresult.tgz"



	

##### Commands belows will delete the existing configdumpresult old and new
tput setaf 1;echo -e "###############  Deleting old configdumpresult #####################\n"
tput setaf 7;echo -e "###############       pls donate thanks        #####################\n\n\n"
sleep 2s;
rm -rf $mydir"/EJBCA/confDump/configdumpresult"
sleep 2s;
rm -rf $mydir"/EJBCA/confDump/configdumpresult-old"
sleep 2s;

#####  Commands below will extract the configdumpresult old and new
tput setaf 2;echo -e "###############  Extracting configdumpresult to mydir/EJBCA/confDump #####################\n\n\n"
sleep 2s;

if [ -a "$config1"  ]
then
	$ex $dl"/configdumpresult.tgz" -C $mydir"/EJBCA/confDump" 
elif [ -a "$config"  ]
then
	$ex $dl"/configdumpresult.tar.gz" -C $mydir"/EJBCA/confDump" 
else
	echo "Error during checking of configdumpresult" > $mydir"/EJBCA/result.txt"
	echo "No configdumpresult file found" 2>&1 | tee -a $mydir"/EJBCA/result.txt"
	exit
fi

echo -e "\n\n\nDeleting config file in Downloads\n\n\n"
sleep 2s;

if [ -a "$config"  ]
then
	rm -rf $dl"/configdumpresult.tar.gz" 
elif [ -a "$config1"  ]
then
	rm -rf $dl"/configdumpresult.tgz" 
else
	echo "Error during checking of configdumpresult" > $mydir"/EJBCA/result.txt"
	echo "No configdumpresult file found" 2>&1 | tee -a $mydir"/EJBCA/result.txt"
	exit
fi
sleep 2s;

tput setaf 2;echo -e "###############  Extracting configdumpresult-old to $mydir/EJBCA/confDump #####################\n\n\n"
sleep 2s;

##Condition checking the file for old configdumpresult with or without space in name in Downloads
if [ -a "$oldConfig"  ]
then
	$ex $dl"/configdumpresult (1).tgz" -C $mydir"/EJBCA/confDump" --one-top-level=configdumpresult-old --strip-components 1
elif [ -a "$oldConfig0"  ]
then
	$ex $dl"/configdumpresult.tgz" -C $mydir"/EJBCA/confDump" --one-top-level=configdumpresult-old --strip-components 1
elif [ -a "$oldConfig1"  ]
then
	$ex $dl"/configdumpresult(1).tgz" -C $mydir"/EJBCA/confDump" --one-top-level=configdumpresult-old --strip-components 1
elif [ -a "$oldConfig2"  ]
then
	$ex $dl"/configdumpresult.tar.gz" -C $mydir"/EJBCA/confDump" --one-top-level=configdumpresult-old --strip-components 1
elif [ -a "$oldConfig3"  ]
then
	$ex $dl"/configdumpresult (1).tar.gz" -C $mydir"/EJBCA/confDump" --one-top-level=configdumpresult-old --strip-components 1
else
	echo "Error during checking of old configdumpresult" > $mydir"/EJBCA/result.txt"
	echo "No Old configdumpresult file found" 2>&1 | tee -a $mydir"/EJBCA/result.txt"
	exit
fi

echo -e "\n\n\nDELETING oldconfig in Downloads\n\n\n"
sleep 2s;

if [ -a "$oldConfig"  ]
then
	rm -rf $dl"/configdumpresult (1).tgz" 
elif [ -a "$oldConfig0"  ]
then
	rm -rf $dl"/configdumpresult.tgz" 
elif [ -a "$oldConfig1"  ]
then
	rm -rf $dl"/configdumpresult(1).tgz" 
elif [ -a "$oldConfig2"  ]
then
	rm -rf $dl"/configdumpresult.tar.gz" 
elif [ -a "$oldConfig3"  ]
then
	rm -rf $dl"/configdumpresult (1).tar.gz" 
else
	echo "Error during removing of old configdumpresult" > $mydir"/EJBCA/result.txt"
	echo "No Old configdumpresult file found" 2>&1 | tee -a $mydir"/EJBCA/result.txt"
	exit
fi
sleep 2s;

#####  Commands below will execute the python ReviewFull3.py and oldercompare_orig.py
tput setaf 3;echo -e "ReviewFull #####################\n\n\n" > $mydir"/EJBCA/result.txt"
sleep 2s;
python $mydir"/EJBCA/ReviewFull3.py" 2>&1 | tee -a $mydir"/EJBCA/result.txt"

tput setaf 5;echo -e "\nFolder Compare #####################\n\n" >> $mydir"/EJBCA/result.txt"
sleep 2s;
# python $mydir"/EJBCA/foldercompare.py" >> $mydir"/EJBCA/result.txt"
#get the difference in folder comapre.
compare=$(python $mydir/EJBCA/foldercompare.py)

sleep 2s;

##Check the differences from yesterday's and today's dump
if [[ "$compare" = "" ]] ; then
	tput setaf 5;echo -e "Hi Paul\n\n No difference found in Yesterday's and Today's dumps. \n For your review." | tee -a $mydir"/EJBCA/result.txt"
else
	tput setaf 5;echo -e "Hi Paul,\n\nDifference found in Yesterday's and Today's dumps.\n\n" | tee -a $mydir"/EJBCA/result.txt"
	echo "$compare" | tee -a $mydir"/Ejbca/result.txt" 
fi
echo "$compare"

tput setaf 2;echo "FILE DELETED"
start tosend
tput setaf 3;echo "Press ok to continue"
cat result.txt|clip
sleep 2s;

#notify
ps='powershell -File'
$ps alertCopy.ps1

exit
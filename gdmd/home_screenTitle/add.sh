#!/bin/bash

clear

echo -e "\nType your keyword for your script [REMEMBER THIS keyword]:\n" ; read kw
echo -e "\nPython or Bash | Type py for python script and bash for Bash script\n" ; read sc
echo -e "\nDirectory path, start from PHInfrascripts/...\n" ; read dp
echo -e "\nLink of its stash repository\n" ; read repo

if [[ $kw != "" ]] && [[ $sc != "" ]] && [[ $dp != "" ]] && [[ $repo != "" ]]
then
      # Append the text by using '>>' symbol
      echo -e "$kw:$sc:$dp:$repo" >> $godmodetxt/dbitems.txt
      echo -e "Adding your input"
      sleep 3

else 
        echo -e "YOU ADDED SOMETHING NULL!!!"
        sleep 5

fi

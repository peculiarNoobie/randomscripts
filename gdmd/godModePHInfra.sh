#!/bin/bash

##################################################################################
#                   Welcome to PH INFRA GOD MODE Bash script                     #
#                  Compilation of everyscripts infra/soc needs                   #
##################################################################################
###JRG###
mytitle="God Mode(PHInfra)"
echo -e '\033]2;'$mytitle'\007'
printf '\033[8;45;79t'

homedir=~


####################### v You Can fix the directory path here v ###########################

#General file directory folder of godmode text folders and necessary scripts folder
#export scriptdirectoryPATH="$homedir/Documents/Godmode/PHInfrascripts/"
#export godmode="$homedir/Documents/Godmode/home_screenTitle/"


# Making it more flexible              CAUTION on editing this

export dir_path=$(dirname $(readlink -f "${BASH_SOURCE:-$0}")) #directory path from the root of this bash script
export godmode=$dir_path/PHInfrascripts
export godmodetxt=$dir_path/home_screenTitle #textfiles are here



####################### v how things are working in the prog v  ###########################

conditions() {
    
    #Main user input determine what to do in the godmode
    read -p 'Number: ' ans

    case $ans in

    0) #others help you to add, delete, and look for other scripts other than the default and most used scripts in the home page.
        bash $godmodetxt/others.sh
        ;;
    
    1) #run PH Infra script (created by Lester)
        cd $godmode'/ph_infra_report/'
        start python 'PH Infra v0.2.py'
        sleep 3s
        ;;
    
    2) #run PHSocTeam script (created by Josh) Opens necessary tabs for SOC in googlechrome 
        cd $godmode'/PhSOC/'

        start python PHSocTeam.py
        cd $dir_path
        sleep 3s
        ;;
    
    3) #run HVCA Blacklisting tool (created by JC)
        cd $godmode'/hvca-blacklisting-tool/HVCA Blacklisting Tool/'

        start python HVCABlackListScript.py
        cd $dir_path
        sleep 3s
        ;;
    
    4) #run EJBCA script

        cd $godmode'/Ejbca/'

        start sh 'EJBCA.sh'
        sleep 5s;
        cd $dir_path
        sleep 3s
        ;;
       
    5) #exiting the godmode script for good   
        clear
        tput setaf 3; echo -e "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t    Thank you goodbye"
        sleep 3s
        exit
        ;;
    
    *) #wrong input 0,1,2,3,4,5 only. 
        clear
        tput setaf 1; echo -e "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t       Invalid input!!! Please try again."
        sleep 3s
        ;;
    esac
}



####################### v txt files needed for user interface v ###########################

home() {

    clear
    cd $dir_path
    tput setaf 3; cat "$godmodetxt/titlename.txt"
    tput setaf 1; echo -e "\n\tProject Note: " ; 
    tput setaf 7; cat "$godmodetxt/note.txt"
    tput setaf 3; echo -e "\n\tScripts: "
    tput setaf 2; cat "$godmodetxt/choices.txt"
    tput setaf 7; echo -e "\t[0] Others"
    tput setaf 3; echo -e "\n\nHello! What do you need for today?"
    
    tput setaf 7
}


########### v make the program run continuously calling all functions v ##################

while true
do 
    ans=0
    home
    conditions
done




sleep 5;
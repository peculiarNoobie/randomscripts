#!/bin/bash
#cd ~/Documents/Godmode
#echo $(pwd)
#export dir_path=~/Documents/Godmode #$(dirname $(readlink -f "${BASH_SOURCE:-$0}")) #directory path from the root of this bash script
#export godmode=$dir_path/PHInfrascripts
#export godmodetxt=$dir_path/home_screenTitle
#################### Initialization ##############################
clear
tput setaf 3; cat "$godmodetxt/titlename.txt"
tput setaf 1; echo -e "\n\tProject Note: " ; 
tput setaf 7; cat "$godmodetxt/note.txt"
tput setaf 3; echo -e "\n\tChoose: "
tput setaf 2; cat "$godmodetxt/choice2.txt"
tput setaf 3; echo -e "\n\nHello! What do you need for today?"
#echo $(pwd) for debuging purposes
tput setaf 7
read -p "> " x 
#sleep 5;

################## how things works ##############################
case $x in 

    #update 
    0)

        tput setaf 3; echo -e "\n\nHello! What do you need to edit? "
        tput setaf 3; echo -e "\n\tChoose: "
        tput setaf 7
        read -p "> " y

        case $y in
            all)
                clear
                git pull --recurse-submodules
                echo -e "\n\nCheck if scripts are updated\n\n"
                git pull origin master
                sleep 10
                bash godModePHInfra.sh
                ;;

            *)
                clear 
                scp=$(grep -w -i $y $godmodetxt/dbitems.txt | cut -d: -f3 | cut -d/ -f1-2)
                echo "\n $scp \n"
                cd "$scp"
                git pull origin
                git status
                sleep 5
                bash godModePHInfra.sh
                ;;
        esac
        ;;
    
    #find        
    1)
        #sleep 5;
        echo "keywords: "
        cut -d: -f1 $godmodetxt/dbitems.txt
        tput setaf 7; echo -e "Enter keyword: "
        read kw 
        scp=$(grep -w -i $kw $godmodetxt/dbitems.txt | cut -d: -f3)
        prg=$(grep -w -i $kw $godmodetxt/dbitems.txt | cut -d: -f2)
        case $scp in
            "")
                echo "none found" ; sleep 3;
                ;;
            *)
                echo "found it" ; sleep 3;
                case $prg in
                    "bash")
                        echo "bash"
                        sleep 3
                        start sh "$dir_path/$scp"
                        ;;
                    "py")
                        echo "python"
                        start python "$dir_path/$scp"
                        sleep 5
                        ;;
                    *)
                        echo -e "language is stated in dbitems.txt is not recognizable, please change the language [Python/Bash]"
                        sleep 10;
                        ;;
                esac

                ;;
        esac
        bash others.sh
        ;;

    2) 
        bash $godmodetxt/add.sh #add
        ;;
    
    3)
        echo "nothing to see here yet" ; sleep 3; bash godModePHInfra.sh #delete
        ;;

    4)
        bash godModePHInfra.sh
        ;;

    *) 
        clear
        tput setaf 1; echo -e "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t      Invalid input!!! Going back now."
        sleep 10s;
        ;;
    esac

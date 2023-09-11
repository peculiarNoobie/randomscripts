# PHInfra Tool kit - GODMODE
![GitHub Logo](https://intranet.internal.globalsign.com/stash/users/joshua.garcia/repos/projectgodmode/browse/docimg/GODMode.png?raw=true) <br />
A one time run script to run necessary scripts that we needed in Infra or Soc.<br />

### Caution: Edit the scripts with caution 


## Table of Contents

- [Getting Started](#getting-started) <br />
  - [Project Features](#project-features) <br />
  - [Overview](#overview) <br />
  - [Requirements](#requirements) <br />
  	- [Definitions, Acronyms, and Abbreviations](#definitions,-acronyms,-and-abbreviations)</br>
    - [First time running Godmode](#first-time) <br />
    - [Directory path and Variables](#directory-path) <br />
    - [Database text file](#dbtext) <br />
 - [User Manual](#user-manual) <br />
    -[Adding your Scripts as submodules](#add-directory-submodules)<br />
 - [Target Audience](#target-audience) <br />
 - [Focus Areas](#focus-areas) <br />
    - [Scenarios](#scenarios) <br />
    - [Languages](#languages) <br />
 - [Troubleshooting](#troubleshooting)</br>
 - [Authors](#authors) <br />

<a name="getting-started"></a>
## Getting Started
Project that can help PHInfra team to run their necessary scripts in one BASH Script. An all in one script that can run, update, and help the team to locate their scripts. 

**Keywords: PHInfra, EJBCA, BASH Shell, Submodule, Repositories, Blacklisting.**
<a name="project-features"></a>
### Project Features
This repository contains a program that has features, listed as follows:
  1. [In EJBCA] No need to go to Result.txt to copy the text file. Result.txt will automatically be in your clipboard, ready to be pasted in the comment,
  2. Pull/update your scripts. The code only rely on your local repository,
  3. Add/Delete and Find your scripts using a keyword you set and run it,
  4. Dedicated [.env](https://intranet.internal.globalsign.com/stash/users/joshua.garcia/repos/projectgodmode/browse/.env) file for directories and variables that are usually change,
  5. [run-me-first.sh](https://intranet.internal.globalsign.com/stash/users/joshua.garcia/repos/projectgodmode/browse/run%20me%20first.sh) script which clones necessary scripts as submodules, and
  6. [dbitems.txt](https://intranet.internal.globalsign.com/stash/users/joshua.garcia/repos/projectgodmode/browse/home_screenTitle/dbitems.txt) for manually adding and deleting scripts and its following directory path and clone link 


<a name="overview"></a>
### Overview
Created specifically for PHInfra team connecting each of their scripts in one. Utilize submodules in git to pull from each specific repositories. Necessary scripts that we needed in Infra or Soc including EJBCA, Phinfra script, HVCA, etc. By this, you just need to run godmode script and choose what script you needed. No need to find your script every single time you need to run that script.

<a name="requirements"></a>
### Requirements
* **Any IDE (Integrated Development Enviroment Software)**, in this case, the developers used Visual Studio (VS) Code. <br />
To download, open your browser, head over to https://code.visualstudio.com/, and choose the software appropriate for your platform (Windows, Mac, or Linux).

* **BASH Shell** <br />
  is a Unix shell and command language written by Brian Fox for the GNU Project as a free software replacement for the Bourne shell. 
  User are recommended to use GitBash application to run the GodMode Bash script.

<a name="definitions,-acronyms,-and-abbreviations"></a>
### Definitions, Acronyms, and Abbreviations
* **EJBCA** or Enterprise JavaBeans Certificate Authority) is a free software public key infrastructure (PKI) certificate authority software package maintained and sponsored by the Swedish for-profit company PrimeKey Solutions AB, which holds the copyright to most of the codebase.
* **PHInfra** tool created by Lester Javier that automatically opens necessary monitoring tool and reminding the user to screenshot the monitoring tool every 2hrs.
* **Submodule** or a git submodule is a record within a host git repository that points to a specific commit in another external repository.
* **HVCA** is a tool taht PHInfra uses to add a website in the blacklist repo.
* **Repositories** a place where scripts were stored in stash/repo of each programmer.
* **Blacklisting** is a list of things that are identified as deceitful and should be kept away from.

<a name="first-time"></a>
##### First time to run Godmode:
* **Just run the run me first** <br />
  	simply click the script [run me first](https://intranet.internal.globalsign.com/stash/users/joshua.garcia/repos/projectgodmode/browse/run%20me%20first.sh)
  - To install all the submodules including (EJBCA, HVCA, and PHInfra tool):
    ```
    $ git submodule list
    $ git submodule update
    ```

<a name="directory-path"></a>
#### Directory path and Variables:
* **[.env](https://intranet.internal.globalsign.com/stash/users/joshua.garcia/repos/projectgodmode/browse/.env)** <br />
  Usually you just need to configure this whenever you needed to reconfigure your Path in Chrome(x86/none) and testfile in HVCA
  - To configure, open the file .env open the file in notepad:
    ```
	chromeS=
	chrome_path=
    feature_HVCA=
	domain_HVCA=
    ```
    **Make sure to contact John Carlo Conchas or Lester Javier even Joshua Ron Garcia before reconfiguring .env file**

<a name="dbtext"></a>
#### Database text file:
* **[dbitems.txt](https://intranet.internal.globalsign.com/stash/users/joshua.garcia/repos/projectgodmode/browse/home_screenTitle/dbitems.txt)** <br />
  For adding, deleting, reconfiguring, and updating scripts to be find by Godmode. Each keys are separated by semicolon (:) that will help the program search for necessary scripts and repo to pull.<br />
  You may edit this but proceed with caution. Avoid editing default scripts. Semi-colon (:) are use as delimeter
	- Format of the dbtext file
    ```
    [keyword to search]:[py or bash script]:[file path of the script]:[link of the repository to be pull]
    ```

<a name="user-manual"></a>
## User Manual
![Godmode Script](https://intranet.internal.globalsign.com/stash/users/joshua.garcia/repos/projectgodmode/browse/docimg/godmoderun.png?raw=true)</br>

The User manual present the step-by-step procedure on how to use the Godmode.

**Instructions:**<br />
  Note: Skip 1-2 if it isn't your first time using This script.

  1. Clone Godmode to your Computer.</br>
    ```
    $ git clone https://intranet.internal.globalsign.com/stash/scm/~joshua.garcia/projectgodmode.git
    ```
  2. Run the **[run me first.sh](https://intranet.internal.globalsign.com/stash/users/joshua.garcia/repos/projectgodmode/browse/run%20me%20first.sh)** To clone every submodule needed and install necessary modules to run the script. <br />
  3. Run the **[godModePHInfra.sh](https://intranet.internal.globalsign.com/stash/users/joshua.garcia/repos/projectgodmode/browse/godModePHInfra.sh)** <br />
  <br />
   **YOU'RE GOOD TO GO** 
  4. [OPTIONAL] Press Others to see other choices (pull/update scripts, find)
  	4a. When pulling a scripts from a repo, godmode script will pull it based on the link added in the [dbitems.txt](https://intranet.internal.globalsign.com/stash/users/joshua.garcia/repos/projectgodmode/browse/home_screenTitle/dbitems.txt).
  		**please refer in [Database text file](#dbtext) section** 
    4b. Adding, Deleting, and finding scripts. (Adding and deleting the script is still brewing by the programmer.) After choosing find option, you need to put the exact keyword written in the [dbitems.txt](https://intranet.internal.globalsign.com/stash/users/joshua.garcia/repos/projectgodmode/browse/home_screenTitle/dbitems.txt)
  		- Default Scripts cannot be remove in the choices. They SHOULD NOT be removed in the dbitems.txt, but you can add and delete other scripts in the [dbitems.txt](https://intranet.internal.globalsign.com/stash/users/joshua.garcia/repos/projectgodmode/browse/home_screenTitle/dbitems.txt) when searching/finding a script.</br>
  
  ![Default Scripts](https://intranet.internal.globalsign.com/stash/users/joshua.garcia/repos/projectgodmode/browse/docimg/defaultScripts.png?raw=true) </br>
  
  **Default Scripts**<br />
  
  5. Exit if you must
  
  --Kindly contact Joshua Ron Garcia for any bug in the program--
  
 * **Home** <br />
   The Home page serves as the starting point of the program. When a user start the script, this is the first thing they will see. It presents the default scripts that are commonly used by PHInfra team and there is others below the exit. </br>
   * PH Infra Script<br /> 
	 Created by Lester Arvin Javier. Use to open all necessary infra-monitoring tool sites in chrome. You just first need to know what your shift is (APAC, EMEA, or US). Choose depending on your shift. **note: ** Keep this running since this notifies you to screenshot PH monitoring tool.  
   * PHSOC<br />
   	 Created by Joshua Garcia. This opens all necessary and related in SOC. This automatically exits after it opens every website SOC needed.
   * HVCABlacklistingScript<br />
   	 Created by John Conchas. Use in automating blacklisting.
   * EJBCA<br />
   	 An improved version of EJBCA. This helps the user to just run the script and automatically copy everything in Requirement.txt and opens the folder "tosend" for the user to attatch every file inside the folder "tosend" in the ticket.
   * exit<br />
   	 Close the Godmode
   * Others<br />
   	 -- Refer below --<br />
* **Others** <br />
   Others is where the user can update/pull repositories to keep their scripts updated. You can also find other scripts even the default scripts in the find option with the right KEYWORD written in the [dbitems.txt](https://intranet.internal.globalsign.com/stash/users/joshua.garcia/repos/projectgodmode/browse/home_screenTitle/dbitems.txt).
   ```
   **Some default keywords you may try**
   - starwars (this is just for test purposes you cannot update this)
   - ejbca
   - hvca
   - phinfra
   ```   
	
   * Update/pull scripts offers the user to update a specific script or all the scripts even GodMode script. 
  	 After choosing this option the user will be ask to type what to update:
     ```
     - all
     - [keyword]
     ```

   ![Default Scripts](https://intranet.internal.globalsign.com/stash/users/joshua.garcia/repos/projectgodmode/browse/docimg/others.png?raw=true){height=500 width=400} </br>

<a name="add-directory-submodules"></a>
### **Adding your Scripts as submodule**<br />
    
Note: You can or you may not put your scripts in PHInfra folder. BUT it is **advisable** to copy paste your script folder inside the [PHInfrascripts](https://intranet.internal.globalsign.com/stash/users/joshua.garcia/repos/projectgodmode/browse/PHInfrascripts) folder to avoid future confusion. The folder is created to organize and compile all the scripts in one folder. 

  * **Case 1: You already have your local repository in your computer**<br />
      1. Copy paste your local-repo inside PHInfrascripts folder. <br />
      2. Open Gitbash inside your Godmode folder
      3. Then, type the following command in your gitbash <br />
        ```
        git submodule add <url> PHInfrascripts/[foldername of repo]
        ```
        This should be the output of your gitbash <br />
        ![Default Scripts](https://intranet.internal.globalsign.com/stash/users/joshua.garcia/repos/projectgodmode/browse/docimg/localrepodone.png?raw=true)<br />

      4. Double check the .gitmodule if your script path is added. <br />
              **Caution: Avoid editing the .gitmodule manually.**<br />

  * **Case 1.2: You still haven't clone your new script yet**<br />
      1. Open Gitbash inside your Godmode folder<br />
      2. Type the following command in gitbash<br />
      ```
      git submodule add <url> PHInfrascripts/[foldername of repo]
      ```
      This should be the output of your gitbash<br />
      ![Default Scripts](https://intranet.internal.globalsign.com/stash/users/joshua.garcia/repos/projectgodmode/browse/docimg/cloningrepodone.png?raw=true)<br />

      3. Double check the .gitmodule if your script path is added. <br />
        **Caution: Avoid editing the .gitmodule manually.**<br />

  * **3.** Open godmode script
  * **4.** Choose "Others"
  * **5.** ADD
           - When adding your script follow the instructions. Remember the keyword you put. If you mistakenly enter wrong keyword or anything that is needed. You can edit it in dbitems. Refer in [Dbtext Manual](#dbtext)
  * **6.** Test it by choosing "Others" after returning to Home
  * **7.** Choose Find, then type your keyword



<a name="target-audience"></a>
## Target Audience
For this repository, our target audience is PHInfra/SOC Team or any IT person that may use the scripts. As our content in this repository, the necessary scripts.

<a name="focus-areas"></a>
## Focus Areas
This repository aims to give an ease to our team. <br />Help to compile every script that the team needed.<br />A one time run to run everything else.

<a name="scenarios"></a>
### Scenarios
We aim to have scenarios that helps the users to avoid losing their necessary scripts and help to keep their scripts updated from the repository of the creator.

<a name="languages"></a>
### Languages
The language that our program uses is BASH Scripting. A Unix command line interface responsible for interacting with a computer's operating system. 
<br /><br />
<a name="troubleshooting"></a>
## Troubleshooting
* **Default scripts fail to be cloned/ Missing file**</br>

	User can *temporarily* get the folder/file of the script from the owners repository or move your copy of the script that is missing in [PHInfrascripts](https://intranet.internal.globalsign.com/stash/users/joshua.garcia/repos/projectgodmode/browse/PHInfrascripts) folder. Some scripts like ph-infra tool can't be pulled for some reason. Note that if you copy pasted a repository inside the PHInfra folder, the script will may not determine the pathfolder and repository link.</br></br>

* **There's an update in the script but the script tells its updated**</br>

	Right click the folder of the specific script (e.g. hvca-blacklisting-tool, ph_infra_report) open in gitbash and type</br>
    ```
    git remote -v
    ```
  	The git link must be the repository link of the repository. Contact the owner of the repository of the script or contact the author of this script for fixing the submodule.</br></br>
    
* **ALWAYS PUT THE SCRIPT in its right folder**</br>

	put it in PHInfrascripts checkout the default scripts (ejbca, hvca, phinfra, and phsoc) there are respective folders inside the [PHInfrascripts](https://intranet.internal.globalsign.com/stash/users/joshua.garcia/repos/projectgodmode/browse/PHInfrascripts) folder.</br></br>

<a name="authors"></a>
## Authors
   *Garcia, Joshua Ron G.* (https://intranet.internal.globalsign.com/stash/users/joshua.garcia, https://github.com/peculiarNoobie)
* **Contributors** <br />
  * *John Carlo Conchas* (https://intranet.internal.globalsign.com/stash/users/john.conchas)
  * *Lester Arvin Javier* (https://intranet.internal.globalsign.com/stash/users/lester.javier)

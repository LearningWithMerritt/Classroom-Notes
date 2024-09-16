

# Filesystem Lab Directions

Welcome to the Filesystem Lab: CLI Navigation Maze
The goal of this lab is to familiarize you with the command line interface and navigation through the file system. 

1. Navigate to this directory in your local copy of the Classroom-Notes repository. 
```
Classroom-Notes/4-Operating-Systems/2-General/file_system_lab
```

<br> 

2. If you are on Windows Powershell run the following commands:
```
> cmd
> run.bat
> powershell
> cd ~\Desktop
> dir
```

<br> 


3. If you are on Windows Command Prompt commands:
```
> run.bat
> cd %USERPROFILE%\Desktop
> dir
```

<br> 


4. If you are on Linux Bash,fsh,zsh,etc. commands:
```
$ sh run.sh
$ cd ~/Desktop
$ ls
```

<br> 


5. On the first run of the program navigate through the directory structure to find the "exit". The correct "exit" will tell you how to get out of the maze. 
    1. You may also find a "treasure map" that will tell you the correct path to the exit.


<br> 

6. After you find the exit the first time, navigate back to  
```
Classroom-Notes/4-Operating-Systems/2-General/file_system_lab
```

<br> 


7. Run the program again. The maze will be recreated and the exit will change. This time you should be faster at finding the exit since you have become familiar with the commands. 


<br> 


8. After you find the exit the first time, navigate back to  
```
Classroom-Notes/4-Operating-Systems/2-General/file_system_lab
```

<br> 

9. For the final run, it is time to use more advanced commands, try using the following commands to help you find the "exit".

<br> 

`Windows Command Prompt or Powershell`
```
> findstr /s /i "search string" *.*
```
* findstr : search for text
* /s : recursively (go through all file and folders)
* /i : ignore case
* \* : wildcard 

<br> 


`Linux bash, fsh, zsh, etc.` 
```
grep -ri "search string" /path/to/directory
``` 
* grep: search  
* -r : recursively (go through all files and folders)  
* -i : ignore case  



Command Line Interface

Shell: program that interprets commands entered by the user at the command line. 
It is responsible for executing the commands and displaying the results to the user.

Command line: text-based interface that allows users to interact with a computer by typing in commands. 
It is the oldest and most basic type of user interface.

Terminal: software application that provides a command line interface. 
It is often used to access and manage servers, but it can also be used on desktop computers.

Prompt: symbol or sequence of symbols that appears at the command line, indicating that the system is ready to receive a command.
The prompt typically looks like a dollar sign ($) or greater than sign (>).

Console: physical device that provides a text-based interface to a computer. 
It is typically a monitor and keyboard.

A CLI interface command is typically made up of the following parts:

Command name: 
    This is the name of the command that you want to execute.

Flags: 
    optional parameters, but they are typically used to enable or disable certain features of the command.

Arguments: 
    optional parameters that you can use to modify the behavior of the command.


Help Flag:
    /? - help with the command

File Commands
    help - displays a list of possible commands
	help <command> - list help for a specific command
    systeminfo - displays information about the computer, such as the operating system version, processor, and memory.
    cls - clears the screen
    dir - displays the files and folders in the current directory
	dir /a - a for attributes but shows all files even hidden
    cd  - change directory
    echo - display text on the command line
    type - read file contents on the command line
    > - redirect command
    notepad - open notepad
    tree - display the directory structure of a folder
	tree /f - include files in the tree
    move - move a file or directory
    ren - rename a file or directory
    del - delete a file
    mkdir - make a new directory
    rmdir - remove a directory
	rmdir /s /q 
    find - locate file, directory or text
    more - displays file contents one page at a time.
    tasklist - lists the running processes (programs)
    taskkill - terminates a process 
    shutdown - shuts down the computer


Keyboard Shortcut:
    Ctrl + C - keyboard interrupt 



### **PowerShell Commands**

| **Command**                            | **Description**                                      | **Alias**                               |
|----------------------------------------|------------------------------------------------------|-----------------------------------------|
| `pwd`                                  | Displays the current directory                       | `Get-Location`                          |
| `cd [path]`                            | Changes the current directory                        | `Set-Location`                          |
| `ls`                                   | Lists files and directories                          | `Get-ChildItem`                         |
| `dir`                                  | Lists files and directories                          | Same as `ls`                            |
| `cp [source] [destination]`            | Copies a file or directory                           | `Copy-Item`                             |
| `mv [source] [destination]`            | Moves a file or directory                            | `Move-Item`                             |
| `rm [path]`                            | Deletes a file or directory                          | `Remove-Item`                           |
| `mkdir [name]`                         | Creates a new directory                              | `New-Item -ItemType Directory`          |
| `rmdir [path]`                         | Deletes a directory                                  | `Remove-Item -Recurse`                  |
| `cat [file]`                           | Displays the content of a file                       | `Get-Content`                           |
| `echo [text] > [file]`                 | Writes text to a file                                |                                         |
| `echo [text] >> [file]`                | Appends text to a file                               |                                         |
| `more [file]`                          | Displays file content one page at a time             |                                         |
| `sort [file]`                          | Sorts the contents of a file                         |                                         |
| `select-string [pattern] [file]`       | Searches for a pattern in a file                     |                                         |
| `ps`                                   | Lists running processes                              | `Get-Process`                           |
| `kill [pid]`                           | Stops a process by its ID                            | `Stop-Process`                          |
| `start [program]`                      | Starts a program or process                          | `Start-Process`                         |
| `stop-process -name [processname]`     | Stops a process by name                              |                                         |
| `systeminfo`                           | Displays detailed system information                 |                                         |
| `get-service`                          | Lists all services on the system                     |                                         |
| `get-process`                          | Displays information about running processes         |                                         |
| `get-date`                             | Displays the current date and time                   |                                         |
| `ipconfig`                             | Displays IP configuration                            |                                         |
| `ping [hostname]`                      | Tests network connectivity to a host                 |                                         |
| `tracert [hostname]`                   | Traces the route packets take to a host              |                                         |
| `netstat`                              | Displays network connections and statistics          |                                         |
| `nslookup [hostname]`                  | Queries DNS for domain name or IP address mapping    |                                         |
| `?`                                    | Alias for `Where-Object`                             |                                         |
| `%`                                    | Alias for `ForEach-Object`                           |                                         |
| `gci`                                  | Alias for `Get-ChildItem`                            |                                         |
| `gi`                                   | Alias for `Get-Item`                                 |                                         |
| `ni`                                   | Alias for `New-Item`                                 |                                         |
| `ri`                                   | Alias for `Remove-Item`                              |                                         |
| `sl`                                   | Alias for `Set-Location`                             |                                         |
| `clc`                                  | Clears the content of the clipboard                  |                                         |
| `cls` or `clear`                       | Clears the screen                                    |                                         |


### **CMD Commands**

| **Command**                   | **Description**                                          |
|-------------------------------|----------------------------------------------------------|
| `cd [path]`                   | Changes the current directory                            |
| `dir`                         | Lists files and directories in the current directory     |
| `copy [source] [destination]` | Copies files from one location to another                |
| `move [source] [destination]` | Moves files from one location to another                 |
| `del [file]`                  | Deletes a file                                           |
| `mkdir [name]`                | Creates a new directory                                  |
| `rmdir [path]`                | Deletes a directory                                      |
| `type [file]`                 | Displays the contents of a file                          |
| `echo [text] > [file]`        | Writes text to a file                                    |
| `echo [text] >> [file]`       | Appends text to a file                                   |
| `findstr [pattern] [file]`    | Searches for a pattern in a file                         |
| `tasklist`                    | Lists all running processes                              |
| `taskkill /PID [pid] /F`      | Stops a process by its ID forcefully                     |
| `start [program]`             | Starts a new program                                     |
| `systeminfo`                  | Displays detailed system information                     |
| `hostname`                    | Displays the computer's hostname                         |
| `date`                        | Displays or sets the system date                         |
| `time`                        | Displays or sets the system time                         |
| `ipconfig`                    | Displays IP configuration                                |
| `ping [hostname]`             | Tests network connectivity to a host                     |
| `tracert [hostname]`          | Traces the route packets take to a host                  |
| `netstat`                     | Displays active network connections                      |
| `nslookup [hostname]`         | Queries DNS for domain name or IP address mapping        |
| `if`                          | Performs conditional processing in batch scripts         |
| `for`                         | Runs a specified command for each file in a set          |
| `goto [label]`                | Directs batch script execution to a labeled line         |
| `pause`                       | Suspends the execution of the script and shows a message |

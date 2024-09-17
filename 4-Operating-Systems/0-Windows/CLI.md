# `Windows: The Command Line Interface`

___


`Shell`: program that interprets commands entered by the user at the command line. 
> * It is responsible for executing the commands and displaying the results to the user.

<br>

`Command line`: text-based interface that allows users to interact with a computer by typing in commands. 
> * It is the oldest and most basic type of user interface.

<br>

`Terminal`: software application that provides a command line interface. 
> * It is often used to access and manage servers, but it can also be used on desktop computers.

<br>

`Prompt`: symbol or sequence of symbols that appears at the command line, indicating that the system is ready to receive a command.
> * The prompt typically ends with a dollar sign (`$`) or greater than sign (`>`).

`Windows Command Prompt`
```
C:\Users\%USERNAME%\Desktop> _ 
```
`Windows Powershell Prompt`
```
PS C:\Users\$env:USERNAME\Desktop> _
```
> %USERNAME%, and $env:USERNAME, are variables that represent the username of the currently logged in user. 


<br>

`Console`: physical device that provides a text-based interface to a computer. 
> * It is typically a monitor and keyboard.

<br>

___

<br>

# `CLI Command Interface`
A CLI command is typically made up of three parts: command, flags, and arguments.   
syntax:
```
command flags arguments
```
example:
```
dir /a C:\home\%USERNAME%\Desktop
```

`Command Name`: This is the name of the command that you want to execute.

`Flags`: optional parameters, but they are typically used to enable or disable certain features of the command.

`Arguments`: optional parameters that you can use to modify the behavior of the command.

<br>

___

<br>

# `Command Prompt (CMD)`
The `Windows Command Prompt`, often referred to as cmd, is a command-line interpreter application available in most Windows operating systems. 
> * It provides a text-based interface for users to interact with the operating system by executing various commands and running scripts.

<br> 

`CMD Prompt Syntax:`   
*Note: '`>`' indicates the prompt and should not be typed as part of the command* 
```
> [command] [flags] [arguments]
```
Example:
```
> tree /f C:\Users\%USERNAME%\Desktop
```
<br> 

___

<br>

# `General CMD Prompt Commands`

Help Flag:  
* `/?` - help with the command

Keyboard Shortcut:  
* `Ctrl + C` - keyboard interrupt (use this to stop the currently running command and return the prompt)

| **Command**                   | **Description**                                          | **Example**                                                |
|-------------------------------|----------------------------------------------------------|------------------------------------------------------------|
| `help`                        | Displays a list of possible commands                     | `help`                                                     |
| `help [command]`              | Lists help for a specific command                        | `help dir`                                                 |
| `cd [path]`                   | Changes the current directory                            | `cd C:\Users\%USERNAME%\Documents`                         |
| `dir`                         | Lists files and directories in the current directory     | `dir`                                                      |
| `dir /a`                      | Lists all files and directories, including hidden ones   | `dir /a`                                                   |
| `tree`                        | Displays the directory structure of a folder             | `tree`                                                     |
| `tree /f`                     | Includes files in the directory structure display        | `tree /f`                                                  |
| `cls`                         | Clears the screen                                        | `cls`                                                      |
| `notepad`                     | Opens Notepad                                            | `notepad`                                                  |
| `copy [source] [destination]` | Copies files from one location to another                | `copy file.txt D:\Backup\file.txt`                         |
| `move [source] [destination]` | Moves files from one location to another                 | `move file.txt D:\Backup\file.txt`                         |
| `del [file]`                  | Deletes a file                                           | `del file.txt`                                             |
| `mkdir [name]`                | Creates a new directory                                  | `mkdir new_folder`                                         |
| `rmdir [path]`                | Deletes a directory                                      | `rmdir old_folder`                                         |
| `rmdir /s /q [path]`          | Deletes a directory and all its contents quietly         | `rmdir /s /q old_folder`                                   |
| `type [file]`                 | Displays the contents of a file                          | `type file.txt`                                            |
| `echo [text] > [file]`        | Writes text to a file                                    | `echo Hello World > file.txt`                              |
| `echo [text] >> [file]`       | Appends text to a file                                   | `echo Appended Text >> file.txt`                           |
| `findstr [pattern] [file]`    | Searches for a pattern in a file                         | `findstr "error" logfile.txt`                              |
| `tasklist`                    | Lists all running processes                              | `tasklist`                                                 |
| `taskkill /PID [pid] /F`      | Stops a process by its ID forcefully                     | `taskkill /PID 1234 /F`                                    |
| `start [program]`             | Starts a new program                                     | `start notepad.exe`                                        |
| `systeminfo`                  | Displays detailed system information                     | `systeminfo`                                               |
| `hostname`                    | Displays the computer's hostname                         | `hostname`                                                 |
| `date`                        | Displays or sets the system date                         | `date`                                                     |
| `time`                        | Displays or sets the system time                         | `time`                                                     |
| `ipconfig`                    | Displays IP configuration                                | `ipconfig`                                                 |
| `ping [hostname]`             | Tests network connectivity to a host                     | `ping google.com`                                          |
| `tracert [hostname]`          | Traces the route packets take to a host                  | `tracert google.com`                                       |
| `netstat`                     | Displays active network connections                      | `netstat`                                                  |
| `nslookup [hostname]`         | Queries DNS for domain name or IP address mapping        | `nslookup google.com`                                      |
| `if`                          | Performs conditional processing in batch scripts         | `if exist file.txt echo File exists!`                      |
| `for`                         | Runs a specified command for each file in a set          | `for %i in (*.txt) do echo %i`                             |
| `goto [label]`                | Directs batch script execution to a labeled line         | `goto :start`                                              |
| `pause`                       | Suspends the execution of the script and shows a message | `pause`                                                    |
| `find`                        | Locates a file, directory, or text                       | `find "Hello" file.txt`                                    |
| `more`                        | Displays file contents one page at a time                | `type file.txt \| more`                                    |
| `shutdown`                    | Shuts down the computer                                  | `shutdown /s /t 0`                                         |


<br>

___

<br>

# `Powershell`
`Windows PowerShell` is a command-line shell with a scripting language and is designed to automate the administration of Windows operating systems and applications. 
> * It is a task automation framework and scripting language developed by Microsoft. 
> * PowerShell provides a more advanced and flexible environment compared to the traditional Command Prompt.

<br>

___

# `Powershell Prompt Syntax` 
*Note: '`>`' indicates the prompt and should not be typed as part of the command*
```
> [command] [flags] [arguments]
```
Example:
```
> New-Item -Name file.txt
```

<br>

___

# `General PowerShell Commands`

Keyboard Shortcut:  
    `Ctrl + C` - keyboard interrupt 

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
| `cls` or `clear`                       | Clears the screen                                    |                                         |


## `Examples`
| **Command**                            | **Example**                               |
|----------------------------------------|-------------------------------------------|
| `pwd`                                  | `pwd` or `Get-Location`                   |
| `cd [path]`                            | `cd C:\Users\$env:USERNAME\Documents`     |
| `ls`                                   | `ls` or `Get-ChildItem`                   |
| `dir`                                  | `dir` or `Get-ChildItem`                  |
| `cp [source] [destination]`            | `cp file.txt C:\Backup\file.txt`          |
| `mv [source] [destination]`            | `mv file.txt C:\Backup\file.txt`          |
| `rm [path]`                            | `rm file.txt` or `Remove-Item file.txt`   |
| `mkdir [name]`                         | `mkdir new_folder`                        |
| `rmdir [path]`                         | `rmdir new_folder`                        |
| `cat [file]`                           | `cat file.txt`                            |
| `echo [text] > [file]`                 | `echo "Hello, World!" > file.txt`         |
| `echo [text] >> [file]`                | `echo "Additional text" >> file.txt`      |
| `more [file]`                          | `more file.txt`                           |
| `sort [file]`                          | `sort file.txt`                           |
| `select-string [pattern] [file]`       | `select-string "error" logfile.txt`       |
| `ps`                                   | `ps` or `Get-Process`                     |
| `kill [pid]`                           | `kill 1234` or `Stop-Process -Id 1234`    |
| `start [program]`                      | `start notepad`                           |
| `stop-process -name [processname]`     | `stop-process -name notepad`              |
| `systeminfo`                           | `systeminfo`                              |
| `get-service`                          | `get-service`                             |
| `get-process`                          | `get-process`                             |
| `get-date`                             | `get-date`                                |
| `ipconfig`                             | `ipconfig`                                |
| `ping [hostname]`                      | `ping google.com`                         |
| `tracert [hostname]`                   | `tracert google.com`                      |
| `netstat`                              | `netstat`                                 |
| `nslookup [hostname]`                  | `nslookup google.com`                     |
| `?`                                    | `Get-Process \| ? {$_.CPU -gt 100}`       |
| `%`                                    | `Get-Process \| % { $_.ProcessName }`     |
| `gci`                                  | `gci`                                     |
| `gi`                                   | `gi file.txt`                             |
| `ni`                                   | `ni newfile.txt -ItemType File`           |
| `ri`                                   | `ri file.txt`                             |
| `sl`                                   | `sl C:\`                                  |
| `cls` or `clear`                       | `cls` or `clear`                          |


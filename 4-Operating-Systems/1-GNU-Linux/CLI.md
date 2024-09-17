# `Linux Command Line`

`Console`: physical device that provides a text-based interface to a computer. 
It is typically a monitor and keyboard.

<br>

`Command line`: text-based interface that allows users to interact with a computer by typing in commands. 
It is the oldest and most basic type of user interface.

<br>

`Shell`: program that interprets commands entered by the user at the command line. 
It is responsible for executing the commands and displaying the results to the user.

<br>

Linux has multiple shells that can be used, but the default shell is `bash`. 
The Bash shell (Bourne-Again Shell) is a Unix shell and command language written by Brian Fox for the GNU Project 
    as a free software replacement for the Bourne shell. 
First released in 1989, it has been used as the default login shell for most Linux distributions. 
Bash was one of the first programs Linus Torvalds ported to Linux, alongside GCC.

<br>

`Bash` is also a popular programming language for writing shell scripts. 
Shell scripts are text files that contain a series of commands that are executed by the Bash shell. 
Shell scripts can be used to automate tasks, such as backing up files, installing software, or deploying a web application.

<br>

`Terminal`: software application that provides a command line interface. 
It is often used to access and manage servers, but it can also be used on desktop computers.

<br>

`Prompt`: symbol or sequence of symbols that appears at the command line, indicating that the system is ready to receive a command.
The prompt typically looks like a dollar sign (`$`) or greater than sign (`>`).

GNU/Linux Bash Prompt 
```
username@hostname:/home/USER/Desktop $ _
```

<br>

# `CLI Command Syntax`

A CLI command is typically made up of three parts: command, flags, and arguments.   
syntax:
```
command flags arguments
```
example:
```
ls -la /home/$USER/Desktop
```

`Command name`: This is the name of the command that you want to execute.

`Flags`: optional parameters, but they are typically used to enable or disable certain features of the command.

`Arguments`: optional parameters that you can use to modify the behavior of the command.



<br>



# `Linux CLI Common Commands`:

| Command | Description | Example|
|:-:|:-|:-|
| `compgen` | Generates a list of all the commands that can be executed.| `compgen -c`|
| `man` | Display the manual (documentation) for a command. | `man ls` for the manual on the `ls` command. |
| `whoami`| Display the current user. | `whoami`|
| `pwd` | Print the working directory (displays your current location in the file system). | `pwd`|
| `ls`| List files and directories in the current directory.| `ls`<br>`ls -la`|
| `cd`| Change directory. | `cd <directory>` to navigate to a different directory. |
| `mkdir` | Create a new directory. | `mkdir my_directory` |
| `rmdir` | Remove a directory (only if it's empty).| `rmdir my_directory` |
| `touch` | Create an empty file. | `touch my_file.txt`|
| `rm`| Remove files or directories. Use with caution, as it's irreversible. | `rm my_file.txt` or `rm -r my_directory` |
| `cp`| Copy files or directories.| `cp file.txt /path/to/destination` or `cp -r directory/ /path/to/destination` |
| `mv`| Move or rename files or directories.| `mv file.txt new_name.txt` or `mv file.txt /path/to/destination`|
| `>` | Redirects output to a file. | `echo "hello world" > file.txt`|
| `>>`| Redirects output and appends to file. | `echo "hello world" >> file.txt`|
| `<` | Redirects file contents to input. | `sort < unsorted_list.txt` - Sorts the contents of unsorted_list.txt.|
| `2>`| Redirects error messages to file. | `ls non_existent_file 2> error_log.txt` - Redirects the error output to error_log.txt.|
| `2>>` | Redirects error messages and appends to file. | `ls non_existent_file 2>> error_log.txt` - Appends error messages to error_log.txt.|
| `&>`| Redirects error and output to file. | `echo "Hello" &> output_log.txt` - Redirects both output and errors to output_log.txt.|
| `\|` | Redirects the output of one command to the input of another.| `cat file.txt \| grep "search_term"` - Passes the output of cat to grep to search for a term.|
| `< <()` | Use the output of a command as if it were a file. | `diff <(cat file1.txt) <(cat file2.txt)` - Compares the output of cat file1.txt and cat file2.txt as if they were files.|
| `cat` | Display the contents of a file. | `cat file.txt` |
| `less`| View the contents of a file one page at a time. Use arrow keys to navigate, and press "q" to exit.| `less file.txt`|
| `head`| Display the beginning of a file.| `head file.txt`|
| `tail`| Display the end of a file.| `tail file.txt`|
| `nano`| Built-in CLI text editor. | `nano file.txt`|
| `grep`| Search for a specific pattern in files. | `grep "search_term" file.txt`|
| `find`| Search for files and directories. | `find /path/to/search -name "file.txt"`|
| `df -h` | Show disk space usage on the system in human-readable format. | `df -h`|
| `du -h` | Display the size of directories and files in human-readable format. | `du -h`|
| `ps -ef`| List running processes. | `ps -ef`|
| `kill`| Terminate processes.| `kill <process_id>`|
| `top` | Display a dynamic view of system processes. | `top`|
| `sudo`| Run a command with superuser privileges. Use with caution.| `sudo apt update`|
| `chmod` | Change file permissions.| `chmod +x file.sh` to make a file executable |
| `chown` | Change the owner of a file or directory.| `chown new_owner:new_group file.txt` |
| `tar` | Create or extract tar archives. | `tar -xvf archive.tar` to extract a tar file.|
| `wget`| Download files from the internet. | `wget http://example.com/file.zip` |


<br>

# `CLI Keyboard Shortcuts`
| Shortcut           | Description                      |
|--------------------|----------------------------------|
| `Ctrl + Alt + T`   | Open the Terminal Emulator.      |


## Basic Navigation
| Shortcut           | Description                                      |
|--------------------|--------------------------------------------------|
| `Ctrl + C`         | Terminate the currently running command.         |
| `Ctrl + D`         | Log out or exit the current shell.               |
| `Ctrl + Z`         | Suspend a running process (put it in the background). |
| `Ctrl + L`         | Clear the terminal screen.                       |


## Text Manipulation
| Shortcut           | Description                                      |
|--------------------|--------------------------------------------------|
| `Ctrl + A`         | Move the cursor to the beginning of the line.    |
| `Ctrl + E`         | Move the cursor to the end of the line.          |
| `Ctrl + U`         | Delete from the cursor to the beginning of the line. |
| `Ctrl + K`         | Delete from the cursor to the end of the line.   |
| `Ctrl + Y`         | Paste the text that was cut using `Ctrl + U` or `Ctrl + K`. |


## Tab Completion
| Shortcut           | Description                                      |
|--------------------|--------------------------------------------------|
| `Tab`              | Auto-complete file and directory names.          |


## History
| Shortcut           | Description                                      |
|--------------------|--------------------------------------------------|
| `Up Arrow`         | Access previous commands in your command history. |
| `Down Arrow`       | Access next commands in your command history.    |
| `Ctrl + R`         | Search through command history.                  |
| `!!`               | Re-run the last command.                         |
| `!n`               | Re-run the nth command from your history (e.g., `!5` to run the fifth command). |


## File and Directory Operations
| Shortcut           | Description                                      |
|--------------------|--------------------------------------------------|
| `Ctrl + T`         | Swap the last two characters before the cursor.  |
| `Ctrl + W`         | Delete the word before the cursor.               |
| `Alt + .`          | Insert the last argument from the previous command. |

### **CMD Prompt Commands**

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
| `cls`                         | Clears the screen                                        |

Useful Examples:  
Search all files and folders in the current directory: `findstr /s /i "search_string" *.*`






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
| `select-string [pattern] [file]`       | Searches for a pattern in a file                     |                                         |
| `gci`                                  | Alias for `Get-ChildItem`                            |                                         |
| `gi`                                   | Alias for `Get-Item`                                 |                                         |
| `ni`                                   | Alias for `New-Item`                                 |                                         |
| `ri`                                   | Alias for `Remove-Item`                              |                                         |
| `sl`                                   | Alias for `Set-Location`                             |                                         |
| `cls` or `clear`                       | Clears the screen                                    |                                         |




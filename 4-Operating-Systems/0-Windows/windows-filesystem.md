# `Windows Filesystem`

The `file system` is a component of the operating system kernel that manages how data is organized and stored on physical storage devices (SSDs, HDDs).
|Filesystem| Abbreviation| OS|
|:-|:-:|:-|
|New Technology File System|NTFS|Default for `Windows`|
|Fourth Extended File System|Ext4|Default for `GNU/Linux` (most distros)|
|Apple File System|APFS|Default for `macOS`|
|File Allocation Table|FAT|cross platform|
|File Allocation Table 32|FAT32|cross platform|
|Extended File Allocation Table|exFAT|cross platform|

<br>

___

<br>

# `Files`


A `file` is a collection of data that is stored on a computer storage device.
* Files can contain any type  of data, such as text, images, videos, music, and programs. 

* Files are identified by their `filename`, which is a unique name that is assigned to the file when it is created. 

* Files are organized into folders (directories), which are containers that can contain other files and folders.

<br>

A `file extension` is a suffix that is added to the end of a filename to indicate the type of data the file stores. 
syntax:
```
<filename>.<extension>
```
example
```
file.txt
```

<br>

___

<br>

# `File Paths`

A `file path` is a string of characters that identifies the location of a file on a computer storage device. 

`C:\Users\$env:USERNAME\Desktop`

`File paths` in Windows are typically composed of a drive letter (C), a volume separator(:), a directory structure (separated with backslashes), and/or a filename. 


| **Component**| **Description**| **Example**|
|------------------------|--------------------------------------------------------|--------------------------|
| `Drive letter`| The letter assigned to a drive (optional). | `C`, `D`, `E`|
| `Volume separator`| A colon used to separate the drive letter from the path. | `:`|
| `Directory structure` | The folders or directories leading to the file, separated by backslashes (`\`). | `\Users\John\Documents` |
| `Filename`| The name of the file (can include an extension). | `file.txt` |

<br>

Filepath examples:
```
C:\Users\John\Documents\file.txt
```
```
C:\Users\Alice\Pictures\Vacation\beach.jpg
```
```
C:\Program Files\Adobe\Reader\AcroRd32.exe
```
```
E:\Backup\2023\financial_data.xlsx
```
```
"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
```
Network filepath example:
```
\\Server\SharedFolder\Projects\Report.docx
```

<br>

___

<br>

# `Absolute File Paths`
File paths can be `absolute` or `relative`. 

An `absolute file path` specifies the complete location(address) of a file, starting from the root directory. 

example:
```
C:\Windows\System32
```
```
C:\Users\$env:USERNAME\Desktop\My-Folder\myfile.txt
```
```
"D:\My Documents\myfile.txt"
```
Network file path example:
```
\\SERVER\SHARE\myfile.txt
```
```
\\?\UNC\SERVER\SHARE\myfile.txt
```

<br>

___

<br>

# `Relative File Paths`
File paths can be `absolute` or `relative`.

A `relative file path` specifies the location of a file relative to the current working directory (current location). 

* `.` is a reference to the current working directory

* `..` is a reference to the parent directory of the current working directory

example:
```
.\myfile.txt
```
```
"..\My Documents\myfile.txt"
```
```
.\subdir\myfile.txt
```
```
..\..\..\
```
```
..\Desktop
```

<br>

___

<br>

# `Tips for Working with Windows File Paths`
* Use backslashes `\` to separate directory components.
```
C:\Users\$env:USERNAME\Desktop\My-Folder\myfile.txt
```

<br> 

* Enclose file paths in double quotes if they contain spaces.
```
"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
```

<br>

* To use a relative file path, start with a period `.` to indicate the current working directory or `..` to indicate the parent directory.

<br>

___

<br>

# `Windows Filesystem Structure`
`Below %USERNAME% represents the username of a specific user.`

```
C:\Program Files        - contains all of the programs that are installed on your computer.  
C:\Program Files (x86)  - contains 32-bit programs that are installed on your computer.  
C:\ProgramData          - contains files that are used by applications that are installed for all users on the computer.  
C:\PerfLogs             - contains performance logs and reports.   

C:\Windows              - contains all of the Windows operating system files.  
|-- C:\Windows\System32 - contains important system files that are necessary for Windows to run.  
|-- C:\Windows\SysWOW64 - contains 64-bit versions of system files that are necessary for Windows to run.  

C:\Users                                    - contains subfolders for each user account on your computer.  
|--	C:\Users\%USERNAME%                     - The folder contains the files and folders specific to a user account  
|	|--	C:\Users\%USERNAME%\.cache          - This file contains temporary files that are created by applications.   
|	|--	C:\Users\%USERNAME%\Desktop         - contains shortcuts to files and folders that you use frequently.  
|   |-- C:\Users\%USERNAME%\Documents       - contains your personal documents, such as Word documents, Excel spreadsheets, and Powerpoint presentations.  
|   |-- C:\Users\%USERNAME%\Downloads       - contains files that you have downloaded from the internet.  
|   |-- C:\Users\%USERNAME%\Music           - contains your music files.  
|   |-- C:\Users\%USERNAME%\Pictures        - contains your image files.  
|   |-- C:\Users\%USERNAME%\Videos          - contains your video files.  
|   |-- C:\Users\%USERNAME%\Favorites       - contains shortcuts to websites that you have bookmarked.  
|   |-- C:\Users\%USERNAME%\Links           - contains shortcuts to files and folders that you have shared with other users.  
|   |-- C:\Users\%USERNAME%\AppData         - contains application data, such as settings and preferences.  
|   |-- C:\Users\%USERNAME%\Local           - contains application data that is specific to your user account.  
|   |-- C:\Users\%USERNAME%\Roaming         - contains application data that is shared across all user accounts.  
|   |-- C:\Users\%USERNAME%\Searches        - contains a list of the most recent searches that you have performed in File Explorer.   
|   |-- C:\Users\%USERNAME%\Saved Games     - contains saved games for games that you have installed on your computer.   
|   |-- C:\Users\%USERNAME%\OneDrive        - contains files that are stored in your OneDrive cloud storage account.   
|   |-- C:\Users\%USERNAME%\Contacts        - contains your contacts, such as your email addresses, phone numbers, and addresses.   
|   |-- C:\Users\%USERNAME%\3D Objects      - contains 3D objects that you have created or downloaded.   
|  
|-- C:\tmp           - stores temporary files that are created by Windows and by applications.  
|-- C:\Recovery      - contains snapshots of files, and a folder used to restore the Operating System if it becomes corrupted or infected with malware.   
|-- C:\$Recycle.Bin  - contains deleted files that have not yet been permanently deleted.  
|-- C:\Drivers       - contains device drivers. (software that communicates with the hardware of your computer)  
|-- C:\$WINDOWS.~BT  - hidden folder that is created on your computer when you upgrade to Windows 10.   
|-- C:\Intel         - contains files related to the Intel hardware on the computer. (software, drivers, logs)  
|-- C:\OneDriveTemp  - contains temporary files related to the OneDrive application  
|-- C:\inetpub       - contains files that are used by the Internet Information Services (IIS) web server.  
```
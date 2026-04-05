# `Windows Filesystem`

The `file system` is a component of the operating system kernel that manages how data is organized and stored on physical storage devices (SSDs, HDDs).

<br>

___

<br>

Covered in this file:
1. [`File System Types`](#file-system-types)
1. [`Files`](#files)
1. [`File Extensions`](#file-extensions)
1. [`File Paths`](#windows-file-paths)
1. [`Absolute File Paths`](#absolute-file-paths)
1. [`Relative File Paths`](#relative-file-paths)
1. [`Tips for Working with Windows File Paths`](#tips-for-working-with-windows-file-paths)
1. [`Windows File System Structure`](#windows-filesystem-structure)


<br>

___

<br>

# `File System Defined`
A `filesystem` is a a component of the OS kernel that defines how the OS organizes, stores, and manages files on a storage device.
* filesystems define how data is named, stored, retrieved, and managed, including the hierarchy of directories (folders) and the metadata associated with files (like size, permissions, and timestamps).

# `File System Types`
|Filesystem| Abbreviation| OS|
|:-|:-:|:-|
|New Technology File System|NTFS|Default for `Windows`|
|Fourth Extended File System|Ext4|Default for `GNU/Linux` (most distros)|
|Apple File System|APFS|Default for `macOS`|
|File Allocation Table|FAT|cross platform|
|File Allocation Table 32|FAT32|cross platform|
|Extended File Allocation Table|exFAT|cross platform|

<br>

[Back to Top](#windows-filesystem)
___

<br>

# `Files`


A `file` is a collection of `binary data` that is stored on a computer storage device.
* Files can represent any type of data, such as text, images, videos, music, and programs. 

* Files are identified by their `filename`, which is a unique name that is assigned to the file when it is created. 

* Files are organized into `folders (directories)`, which are containers that can contain other files and folders.

<br>

---


## `Binary Data`
`Binary data` is any information that is represented in binary form, meaning stored or transmitted using only two possible values (states). 
* Computers use binary because their hardware (transistors) can easily represent two states: on (1) and off (0).

<br>

[Back to Top](#windows-filesystem)
___

<br>

# `File Extensions`

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

[Back to Top](#windows-filesystem)
___

<br>

# `Windows File Paths`

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

[Back to Top](#windows-filesystem)
___

<br>

# `Absolute File Paths`
File paths can be `absolute` or `relative`. 

An `absolute file path` specifies the complete location(address) of a file, starting from the root directory. 

<br>

The `root directory` is the topmost directory in a file system hierarchy. It serves as the starting point or base from which all other directories and files branch out. `It is the folder that contains all other folders.` 

<br>

`Windows:` The root directory is specific to each drive and represented by a backslash `\` following the drive letter `C:`.

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

[Back to Top](#windows-filesystem)
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

[Back to Top](#windows-filesystem)
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

[Back to Top](#windows-filesystem)
___

<br>

# `Windows Filesystem Structure`
`Below %USERNAME% represents the username of a specific user.`

```
C:\
├── C:\Program Files
├── C:\Program Files (x86)
├── C:\ProgramData
├── C:\PerfLogs
├── C:\Windows
│   ├── C:\Windows\System32
│   └── C:\Windows\SysWOW64
├── C:\Users
│   └── C:\Users\%USERNAME%
│       ├── C:\Users\%USERNAME%\.cache
│       ├── C:\Users\%USERNAME%\Desktop
│       ├── C:\Users\%USERNAME%\Documents
│       ├── C:\Users\%USERNAME%\Downloads
│       ├── C:\Users\%USERNAME%\Music
│       ├── C:\Users\%USERNAME%\Pictures
│       ├── C:\Users\%USERNAME%\Videos
│       ├── C:\Users\%USERNAME%\Favorites
│       ├── C:\Users\%USERNAME%\Links
│       ├── C:\Users\%USERNAME%\AppData
│       │   ├── C:\Users\%USERNAME%\AppData\Local
│       │   └── C:\Users\%USERNAME%\AppData\Roaming
│       ├── C:\Users\%USERNAME%\Searches
│       ├── C:\Users\%USERNAME%\Saved Games
│       ├── C:\Users\%USERNAME%\OneDrive
│       ├── C:\Users\%USERNAME%\Contacts
│       └── C:\Users\%USERNAME%\3D Objects
├── C:\tmp
├── C:\Recovery
├── C:\$Recycle.Bin
├── C:\Drivers
├── C:\$WINDOWS.~BT
├── C:\Intel
├── C:\OneDriveTemp
└── C:\inetpub
```

| Path| Description|
|:-|:-|
| C:\ | The root directory. The folder that contains all other folders|
| C:\Program Files                  | Contains all of the programs that are installed on your computer.                                    |
| C:\Program Files (x86)           | Contains 32-bit programs that are installed on your computer.                                       |
| C:\ProgramData                    | Contains files that are used by applications that are installed for all users on the computer.      |
| C:\PerfLogs                       | Contains performance logs and reports.                                                               |
| C:\Windows                        | Contains all of the Windows operating system files.                                                 |
| C:\Windows\System32               | Contains important system files that are necessary for Windows to run.                               |
| C:\Windows\SysWOW64               | Contains 64-bit versions of system files that are necessary for Windows to run.                     |
| C:\Users                          | Contains subfolders for each user account on your computer.                                          |
| C:\Users\\%USERNAME%               | The folder contains the files and folders specific to a user account.                                |
| C:\Users\\%USERNAME%\\.cache        | Contains temporary files that are created by applications.                                          |
| C:\Users\\%USERNAME%\Desktop       | Contains shortcuts to files and folders that you use frequently.                                     |
| C:\Users\\%USERNAME%\Documents     | Contains your personal documents, such as Word documents, Excel spreadsheets, and PowerPoint presentations. |
| C:\Users\\%USERNAME%\Downloads     | Contains files that you have downloaded from the internet.                                          |
| C:\Users\\%USERNAME%\Music         | Contains your music files.                                                                            |
| C:\Users\\%USERNAME%\Pictures      | Contains your image files.                                                                            |
| C:\Users\\%USERNAME%\Videos        | Contains your video files.                                                                            |
| C:\Users\\%USERNAME%\Favorites     | Contains shortcuts to websites that you have bookmarked.                                             |
| C:\Users\\%USERNAME%\Links         | Contains shortcuts to files and folders that you have shared with other users.                      |
| C:\Users\\%USERNAME%\AppData       | Contains application data, such as settings and preferences.                                       |
| C:\Users\\%USERNAME%\Local         | Contains application data that is specific to your user account.                                     |
| C:\Users\\%USERNAME%\Roaming       | Contains application data that is shared across all user accounts.                                  |
| C:\Users\\%USERNAME%\Searches      | Contains a list of the most recent searches that you have performed in File Explorer.               |
| C:\Users\\%USERNAME%\Saved Games   | Contains saved games for games that you have installed on your computer.                           |
| C:\Users\\%USERNAME%\OneDrive      | Contains files that are stored in your OneDrive cloud storage account.                             |
| C:\Users\\%USERNAME%\Contacts      | Contains your contacts, such as your email addresses, phone numbers, and addresses.                |
| C:\Users\\%USERNAME%\3D Objects    | Contains 3D objects that you have created or downloaded.                                           |
| C:\tmp                            | Stores temporary files that are created by Windows and by applications.                              |
| C:\Recovery                       | Contains snapshots of files and a folder used to restore the Operating System if it becomes corrupted or infected with malware. |
| C:\$Recycle.Bin                   | Contains deleted files that have not yet been permanently deleted.                                   |
| C:\Drivers                        | Contains device drivers (software that communicates with the hardware of your computer).             |
| C:\$WINDOWS.~BT                  | Hidden folder created on your computer when you upgrade to Windows 10.                             |
| C:\Intel                          | Contains files related to the Intel hardware on the computer (software, drivers, logs).             |
| C:\OneDriveTemp                   | Contains temporary files related to the OneDrive application.                                       |
| C:\inetpub                        | Contains files that are used by the Internet Information Services (IIS) web server.                |


<br>

[Back to Top](#windows-filesystem)
___

<br>

*Created and maintained by Mr. Merritt*
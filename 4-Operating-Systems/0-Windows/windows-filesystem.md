

A file path is a string of characters that identifies the location of a file on a computer storage device. 
File paths are typically composed of the following components:
    >> Drive letter (optional)
    >> Volume separator (":")
    >> Directory structure (separated by backslashes)
    >> Filename

C:\My Documents\myfile.txt
Windows file paths can be absolute or relative. 
    >> An absolute file path specifies the complete location of a file, starting from the root directory. 
    >> A relative file path specifies the location of a file relative to the current working directory.

Absolute file paths:
    C:\Windows\System32
    D:\My Documents\myfile.txt
    \\?\UNC\SERVER\SHARE\myfile.txt

Relative file paths:
    .\myfile.txt
    ..\My Documents\myfile.txt
    .\subdir\myfile.txt

Tips for working with Windows File paths
    >> Use backslashes (\) to separate directory components.
    >> Enclose file paths in double quotes if they contain spaces.
    >> To use a relative file path, start with a period (".") to indicate the current working directory.

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




A file is a collection of data that is stored on a computer storage device. 

Files can contain any type of data, such as text, images, videos, music, and programs. 
        
Files are identified by their filename, which is a unique name that is assigned to the file when it is created.

Files are organized into folders, which are directories that can contain other files and folders. 

A file extension is a suffix that is added to the end of a filename to indicate the type of file. 
        It is typically separated from the rest of the filename by a period (.)


File System: a component of the kernel that manages how data is organized and stored on storage devices.
    Ext4 (Fourth Extended File System) Default for Linux (most distros)
    NTFS (New Technology File System) Default for Windows
    APFS (Apple File System) Default for macOS 

    Other common systems: 
    FAT (File Allocation Table):
    FAT32
    exFAT (Extended File Allocation Table)


A file manager or file browser is an application that provides a user interface to manage files and folders. 





















Directories are folders that contain other directories and files. 

A parent directory or superdirectory is a directory that contains one or more child directories. 
A child directory or subdirectory is a directory that is contained within another directory.

A file path is a string of characters that identifies the location of a file on a computer storage device. 

File paths are typically composed of the following components:
    >> Directory structure (separated by forward slashes / )
    >> Filename

Linux file paths can be absolute or relative. 
    >> An absolute file path specifies the complete location of a file, starting from the root directory. 
    >> A relative file path specifies the location of a file relative to the current working directory.

Absolute file path examples:
    /home/<USER>/Desktop/myfile.txt
    /usr/bin/bash
    /etc/passwd
    /var/log/syslog
    /opt/mysql/bin/mysqld

Relative file paths examples:
    myfile.txt 
    ./myfile.txt 
    ../myfile.txt 
    ./subdir/myfile.txt 
    ../subdir/myfile.txt 
    ../../../myfile.txt

    .  : represents the current working directory
    .. : represents the parent directory of the current working directory

Tips for working with Linux File paths
    >> Use forward slashes (/) to separate directory components
    >> To use a relative file path, start with a period (".") to indicate the current working directory.
    >> To indicate the parent directory use a double period ("..")





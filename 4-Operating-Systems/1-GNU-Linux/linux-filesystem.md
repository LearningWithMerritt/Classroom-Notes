# `Linux Filesystem`

The `file system` is a component of the operating system kernel that manages how data is organized and stored on physical storage devices (SSDs, HDDs).

<br>

___

<br>

Covered in this file:
1. [`File System Types`](#file-system-types)
1. [`Files`](#files)
1. [`File Extensions`](#file-extensions)
1. [`File Mangers`](#file-managers)
1. [`File Paths`](#linux-file-paths)
    1. [`Absolute File Paths`](#absolute-file-paths)
    1. [`Relative File Paths`](#relative-file-paths)
    1. [`Tips for Working with Linux File Paths`](#tips-for-working-with-linux-file-paths)
1. [`Linux File System Structure`](#linux-filesystem-structure)


<br>

___

<br>

# `File System Types`
|Filesystem| Abbreviation| OS|
|:-|:-:|:-|
|Fourth Extended File System|Ext4|Default for `GNU/Linux` (most distros)|
|New Technology File System|NTFS|Default for `Windows`|
|Apple File System|APFS|Default for `macOS`|
|File Allocation Table|FAT|cross platform|
|File Allocation Table 32|FAT32|cross platform|
|Extended File Allocation Table|exFAT|cross platform|

<br>

[Back to Top](#linux-filesystem)
___

<br>

# `Files`


A `file` is a collection of data that is stored on a computer storage device.
* Files can contain any type  of data, such as text, images, videos, music, and programs. 

* Files are identified by their `filename`, which is a unique name that is assigned to the file when it is created. 

* Files are organized into `folders (directories)`, which are containers that can contain other files and folders.


<br>

[Back to Top](#linux-filesystem)
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

[Back to Top](#linux-filesystem)
___

<br>

# `File Managers`

A `file manager` or `file browser` is an application that provides a user interface to manage files and folders. 

<br>

| File Manager| Desktop Environment | Description |
|--|--|--|
| `Nautilus`| GNOME | The default file manager for GNOME, known for its simplicity and ease of use.|
| `Nemo`| Cinnamon| A fork of Nautilus, providing additional features and a more traditional desktop experience.|
| `Dolphin` | KDE Plasma| Highly customizable file manager with advanced features like split views and tabs. |
| `Thunar`| Xfce| Lightweight file manager, ideal for older hardware, with a simple interface. |
| `Caja`| MATE| Continuation of Nautilus with a focus on providing a traditional desktop experience. |
| `PCManFM` | LXDE/LXQt | Lightweight and user-friendly file manager for LXDE and LXQt desktop environments. |
| `Ranger`| Terminal| A text-based file manager operating in the terminal, offering powerful navigation shortcuts.|
| `Midnight Commander` | Terminal | Classic text-based file manager with a two-pane interface for easy file operations.|


<br>

[Back to Top](#linux-filesystem)
___

<br>


# `Linux File Paths`

A `file path` is a string of characters that identifies the location of a file on a computer storage device. 

`/home/$USER/Desktop`

`File paths` in Linux are typically composed of  a directory structure (separated with forwardslashes), and/or a filename. 


<br>

Filepath examples:
```
/home/John/Documents/file.txt
```
```
/home/Alice/Pictures/Vacation/beach.jpg
```
```
/var/log/syslog
```
```
/media/usb/
```
Network share example:
```
/mnt/network_drive/
```

<br>

[Back to Top](#linux-filesystem)
___

<br>

## `Absolute File Paths`
File paths can be `absolute` or `relative`. 

An `absolute file path` specifies the complete location(address) of a file, starting from the root directory. 

example:
```
/sys/kernel
```
```
/home/$USER/Desktop/My-Folder/myfile.txt
```
```
"/mnt/d/My Documents/myfile.txt"
```
Network file path example:
```
/mnt/share/myfile.txt
```


<br>

[Back to Top](#linux-filesystem)
___

<br>

## `Relative File Paths`
File paths can be `absolute` or `relative`.

A `relative file path` specifies the location of a file relative to the current working directory (current location). 

* `.` is a reference to the current working directory

* `..` is a reference to the parent directory of the current working directory

example:
```
./myfile.txt
```
```
"../My Documents/myfile.txt"
```
```
./subdir/myfile.txt
```
```
../../../
```
```
../Desktop
```

<br>

[Back to Top](#linux-filesystem)
___

<br>

## `Tips for Working with Linux File Paths`
* Use backslashes `/` to separate directory components.
```
/home/$USER/Desktop/My-Folder/myfile.txt
```

<br> 

* Enclose file paths in double quotes if they contain spaces.
```
"/home/$USER/Desktop/My Folder"
```

<br>

* To use a relative file path, start with a period `.` to indicate the current working directory or `..` to indicate the parent directory.

```
./myfile.txt
```
```
../Desktop
```

<br>

[Back to Top](#linux-filesystem)
___

<br>

# `Linux Filesystem Structure`
`Below $USER represents the username of a specific user.`

Linux Distributions will contain, most if not all of these directories in the `root` `/` directory. 

`In linux, root is the folder that contains all other folders and is represented with a single forward slash /`

Simplified Filesystem Tree Structure
```
/
├── /bin                            
├── /boot                           
├── /cdrom                          
├── /dev                            
├── /etc                            
├── /home                           
│   └── /home/$USER                 
│       ├── /home/$USER/Desktop     
│       ├── /home/$USER/Documents   
│       ├── /home/$USER/Downloads   
│       ├── /home/$USER/Music       
│       ├── /home/$USER/Pictures    
│       ├── /home/$USER/Public      
│       ├── /home/$USER/Templates   
│       └── /home/$USER/Videos      
├── /lib                            
│   ├── /lib/lib32                  
│   ├── /lib/lib64                  
│   └── /lib/libx32                 
├── /media                          
├── /mnt                            
├── /opt                            
├── /proc                           
├── /root                           
├── /run                            
├── /sbin                           
├── /srv                            
├── /sys                            
├── /tmp                            
├── /usr                            
└── /var                            
```
| **Directory**| **Description**|
|:-|:-|
| `/`                   | Root directory, the starting point of the filesystem.                                         |
| `/bin`                | `(binaries)` contains command binaries or the commands you run in Linux.                       |
| `/boot`               | Contains files the system needs to boot.                                                     |
| `/cdrom`              | `(compact disk read only memory)` mount point for CD-ROMs.                                    |
| `/dev`                | `(devices)` consists of files that represent the devices that are attached to the local system.|
| `/etc`                | (pronounced et-see) or `(etcetera)` is the directory where Linux system configuration files live.|
| `/home`               | Where the folders for the users on the system are kept.                                      |
| `/home/$USER`         | User's home directory.                                                                         |
| `/home/$USER/Desktop` | Contains shortcuts, files, and folders that you use frequently.                               |
| `/home/$USER/Documents` | Stores personal documents.                                                                    |
| `/home/$USER/Downloads` | Stores downloaded files and directories.                                                    |
| `/home/$USER/Music`   | Stores music.                                                                                 |
| `/home/$USER/Pictures` | Stores pictures.                                                                               |
| `/home/$USER/Public`   | Used to share files with other users.                                                         |
| `/home/$USER/Templates`| Contains user-made templates for creating new files and folders.                             |
| `/home/$USER/Videos`   | Stores videos.                                                                                |
| `/lib`                | Where shared library files are stored that are required for system boot.                     |
| `/lib/lib32`          | `(library)` directory for software using the x86 instruction set.                               |
| `/lib/lib64`          | `(library)` directory for software using the x86-64 instruction set.                           |
| `/lib/libx32`         | `(library)` directory for software using the x86-64 instruction set but with the 32-bit point size.|
| `/media`              | Where external removable devices such as USB drives are mounted.                             |
| `/mnt`                | `(mount)` temporary mount point for regular file systems like old school floppy disks and CD-ROMs.|
| `/opt`                | `(optional)` where optional files such as third-party tools are saved.                        |
| `/proc`               | `(processes)` contains information specific to the processes on the system.                    |
| `/root`               | Home directory for the root (admin) user.                                                    |
| `/run`                | Stores volatile runtime data such as info about the running system since last boot.          |
| `/sbin`               | `(super user binaries)` contains root (admin) binaries. These are super user commands.        |
| `/srv`                | `(service)` contains server-specific and service-related files.                                |
| `/sys`                | `(system)` interface to the kernel that acts as a virtual filesystem.                          |
| `/tmp`                | `(temporary)` where temporary files are stored and will typically be deleted upon system boot. |
| `/usr`                |  contains all the user binaries, their documentation (man pages), libraries, header files, etc. |
| `/var`                | `(variable)` where files that are likely to change (log files, web files, email, cron files, etc.) are stored. |

<br>

[Back to Top](#linux-filesystem)
___

<br>

*Created and maintained by Mr. Merritt*























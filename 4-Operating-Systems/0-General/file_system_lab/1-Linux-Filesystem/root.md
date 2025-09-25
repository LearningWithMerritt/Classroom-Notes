# `Filesystem Root: /`

In Linux, the root directory is the topmost directory in the filesystem hierarchy.
It is denoted by a single forward slash (/). All other directories, files, and
devices are organized under this root directory, forming a tree-like structure.

Key Points about the Root Directory (/):

1. Top of the Hierarchy:
   The root directory is the starting point of the entire filesystem. All other
   directories branch out from this point, making it the parent directory of all
   other directories and files on the system.

2. Absolute Paths:
   In Linux, an absolute path always starts with a '/', indicating that it begins
   from the root directory. For example, /home/user/documents refers to then
   documents directory inside the user directory, which is inside the home directory,
   starting from the root.

3. System Directories:
   Several important system directories reside directly under the root directory.
   These directories store system files, user data, configuration files, libraries,
   binaries, and more. Some common subdirectories include:
   - /bin: Contains essential binary executables (e.g., ls, cp, mv).
   - /boot: Contains files needed to boot the system, including the Linux kernel.
   - /dev: Contains device files, which represent hardware devices (e.g., hard drives, printers).
   - /etc: Contains system-wide configuration files.
   - /home: Contains home directories for all users (e.g., /home/username).
   - /lib: Contains shared libraries and kernel modules.
   - /media and /mnt: Temporary mount points for removable media like USB drives and other filesystems.
   - /opt: Contains optional software packages.
   - /proc: A virtual filesystem that provides information about running processes.
   - /root: The home directory for the root (superuser) account.
   - /sbin: Contains system binaries, typically for administrative tasks.
   - /tmp: A temporary directory for storing transient files.
   - /usr: Contains user utilities and applications.
   - /var: Contains variable data files, such as logs, databases, and spool files.

4. Root User vs. Root Directory:
   It's important not to confuse the 'root directory' (/) with the 'root user.' The root user
   is the superuser with administrative privileges, while the root directory is the top-level
   directory of the filesystem.

5. Mount Points:
   In Linux, filesystems from different storage devices (like hard drives, SSDs, and removable
   media) are mounted at specific directories within the root filesystem. For example, a separate
   partition might be mounted at /home, or a USB drive might be mounted at /media/usb.

Example of a Linux Filesystem Structure:
Try typing 'tree -L 2' to see the first two levels of your filesystem.
If tree is not installed --> 'sudo apt install tree'
/
|-- bin
|-- boot
|-- dev
|-- etc
|-- home
│   |-- user1
│   |-- user2
|-- lib
|-- media
|-- mnt
|-- opt
|-- proc
|-- root
|-- sbin
|-- tmp
|-- usr
|-- var 
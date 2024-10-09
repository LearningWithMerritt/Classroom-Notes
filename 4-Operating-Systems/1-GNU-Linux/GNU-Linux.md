# `The GNU/Linux Operating System`

Covered in this file:
1. [`What an OS is made of`](#what-an-os-is-made-of)
1. [`GNU/Linux`](#gnulinux)
1. [`The Linux Kernel`](#the-linux-kernel)
1. [`The Shell`](#the-shell)
1. [`The User Interface`](#the-user-interface-gui-and-cli)
    1. [`Graphical User Interface`](#graphical-user-interface-gui)
    1. [`Command Line Interface`](#command-line-interface-cli)
1. [`Some Popular Linux Distros`](#some-popular-linux-distros)


<br>

___

<br>

# `What an OS is made of:`
An OS is made of 4 major parts:
1. `Kernel`: Manages hardware resources and provides low-level services.
1. `Shell`: Acts as an intermediary, allowing users or applications to communicate with the kernel.
1. `User Interface`: Provides a direct way for users to interact with the system, either through a GUI or CLI.
1. `Applications`: Run on top of the OS, requesting resources from the kernel to perform user-driven tasks.

```
+---------------------------------------+
|            Applications               |
+---------------------------------------+----------+
|       User Interface (GUI/CLI)        |  <-- OS  |
+---------------------------------------+          |
|               Shell                   |  <-- OS  |
+---------------------------------------+          |
|               Kernel                  |  <-- OS  |
+---------------------------------------+----------+
|     Hardware (CPU, Memory, etc.)      |
+---------------------------------------+
```

<br>

[Back To Top](#the-gnulinux-operating-system)
___

<br>

# `GNU/Linux`



`Linux` is a family of open-source Unix-like operating systems based on the Linux kernel, an 
operating system kernel first released on September 17, 1991, by Linus Torvalds.

<br>

`GNU/Linux` is a term used by the Free Software Foundation (FSF) to refer to the operating system 
that combines the GNU operating system with the Linux kernel. 

* The FSF argues that the Linux kernel is only one component of a complete operating system, and that the GNU Project has contributed many more essential components, such as the GNU Compiler Collection (GCC),the GNU C Library (glibc), and the GNU Bash shell.

<br>

`Linux distributions` aka `distros` are operating systems made from a software collection that includes the Linux kernel, 
and often a package management system. 

* A Linux distribution may also be described as a particular assortment of application and utility software (various GNU tools and libraries, for example), packaged with the Linux kernel in such a way that its capabilities meet many users' needs.

<br>


`Open source software` (OSS) is computer software that is released under a license in which the copyright holder grants users the rights to use, study, change, and distribute the software and its source code to anyone and for any purpose.


<br>

[Back To Top](#the-gnulinux-operating-system)
___

<br>

# `The Linux Kernel`

The `Linux kernel` is the core of the Linux operating system and is responsible for managing the system’s resources and hardware. It operates in the background and interacts directly with the hardware components, making it the foundation of all Linux-based systems.

The Linux kernel is `monolithic`, meaning that all core functionality runs in a single large process in kernel space. However, it’s also modular, so additional features (such as device drivers) can be loaded or removed dynamically as modules.

<br> 

Key Functions of the Kernel:

1. `Process Management`: The kernel manages running processes, including process scheduling, creation, and termination. It ensures multiple processes can run simultaneously (multitasking) by sharing CPU resources.

1. `Memory Management`: The kernel allocates and manages the system’s RAM, ensuring each process has access to memory while preventing memory leaks or conflicts between processes.

1. `Device Management`: The kernel interacts with device drivers to manage input/output devices like disks, network interfaces, and peripherals.

1. `File System Management`: It handles reading and writing data to disk, managing files and directories through various file systems (e.g., ext4, XFS).

1. `Networking`: The kernel includes a networking stack that handles data transfer between devices, enabling communication over networks using protocols like TCP/IP.

<br>

[Back To Top](#the-gnulinux-operating-system)
___

<br>

# `The Shell`

The `shell` is a command-line interpreter that provides an interface between the user and the kernel. It allows users to execute commands, scripts, and programs by typing text commands. The shell takes user input, interprets it, and passes it on to the kernel for execution.

`The default shell in most linux distros is bash.` 

<br>

Common GNU/Linux Shells:
* `Bash (Bourne Again Shell)`: The default shell in most Linux distributions. It's widely used due to its powerful scripting capabilities and extensive built-in commands.

* `Zsh (Z Shell)`: An extended shell with advanced features like customizable prompts and powerful auto-completion. It’s popular among power users.

* `Fish (Friendly Interactive Shell)`: Known for its user-friendliness and features like syntax highlighting, Fish is designed to be more intuitive for new users.

* `Dash (Debian Almquist Shell)`: A lightweight, POSIX-compliant shell that’s faster than Bash but lacks some of Bash's advanced features.

<br>

[Back To Top](#the-gnulinux-operating-system)
___

<br>

# `The User Interface: GUI and CLI`

The `User Interface (UI)` in Linux can be either a `Graphical User Interface (GUI)` or a `Command Line Interface (CLI)`. Both offer ways for users to interact with the operating system and perform tasks like running programs, managing files, or configuring system settings.

<br>

`GUI`: User-friendly, intuitive, and visually oriented. Ideal for everyday tasks like browsing the web, managing files, or using multimedia applications.

<br>

`CLI`: Provides greater control, efficiency, and automation capabilities through typed commands and scripts. Preferred by system administrators, developers, and power users.

<br>

## `Graphical User Interface GUI`

A `GUI` provides a visual environment where users can interact with the system through `windows, icons, menus, and pointers (WIMP)`. GUIs are popular for their ease of use and accessibility for new users or those coming from Windows/macOS environments.

<br>

Common `Desktop GUI` environments for `GNU/Linux`:

| **Desktop Environment** | **Description** |
|:-:|:-|
|`GNOME` | A widely-used desktop environment, known for its clean, minimalistic design. It’s used by popular distros like Ubuntu. |
|`KDE Plasma` | A highly customizable and feature-rich desktop environment. It offers a traditional desktop layout with a focus on flexibility and productivity. |
|`Xfce`| A lightweight desktop environment designed for speed and low resource usage, making it ideal for older hardware or users seeking performance. |
|`Cinnamon`| Based on GNOME but with a more traditional desktop feel, Cinnamon is the default desktop for Linux Mint and focuses on simplicity and ease of use. |
|`MATE`| A continuation of the old GNOME 2 interface, MATE provides a classic desktop experience with modern features. |

<br>

## `Command Line Interface CLI`
The `CLI` allows users to interact with the shell via typed commands, often through a `terminal emulator`. The CLI is especially powerful for system administration, scripting, and direct control of system processes.

<br>

Common `Terminal Emulators` in `GNU/Linux`:

| **Terminal Emulator**    | **Description** |
|:-|:-|
| `GNOME Terminal`       | The default terminal for the GNOME desktop environment, providing access to the shell in a graphical window. |
| `Konsole`              | The default terminal for KDE Plasma, known for its extensive customization options. |
| `xterm`                | A basic terminal emulator that is lightweight and fast, often used in minimalistic setups. |


<br>

[Back To Top](#the-gnulinux-operating-system)
___

<br>

# `Some Popular Linux Distros`

| **Distribution** | **Description** |
|------------------|-----------------|
| `Ubuntu`       | One of the most popular Linux distributions, known for its user-friendly interface and strong community support. Based on Debian, it’s ideal for beginners and widely used on desktops and servers. |
| `Debian`       | A stable and versatile Linux distribution known for its robust package management system (APT) and commitment to open-source software. It serves as the foundation for many other distributions, including Ubuntu. |
| `Fedora`       | A cutting-edge Linux distribution sponsored by Red Hat, aimed at developers and users who want the latest features. It is known for shipping with the newest software and technologies, including the GNOME desktop environment. |
| `Mint`         | A beginner-friendly distribution based on Ubuntu (and sometimes Debian), with a focus on ease of use and a traditional desktop layout. It’s particularly known for its Cinnamon desktop environment. |
| `Manjaro`      | A user-friendly Arch-based distribution that offers an easy installation process and various desktop environments. It provides the power of Arch Linux with a simplified experience. |
| `OpenSUSE`     | A stable and secure Linux distribution, available in two forms: Tumbleweed (a rolling release) and Leap (a regular release). It is popular for both desktop and server environments, and offers powerful administration tools like YaST. |
| `Elementary OS`| A visually appealing, macOS-like distribution based on Ubuntu, focused on providing a polished and minimalist user experience with its Pantheon desktop environment. Ideal for users looking for a sleek and simple interface. |
| `Pop!_OS`      | Developed by System76, Pop!_OS is based on Ubuntu and tailored for developers, engineers, and gaming enthusiasts. It includes features like automatic tiling and a focus on productivity out of the box. |
| `Zorin OS`     | A distribution aimed at new Linux users, particularly those switching from Windows. It provides a familiar desktop experience with a focus on ease of use and customization. Based on Ubuntu. |
| `Solus`        | A rolling-release distribution built from scratch, known for its Budgie desktop environment. It’s focused on desktop use and aims to provide a modern, clean, and fast experience. |
| `Void Linux`   | An independent distribution with a focus on simplicity and minimalism. It uses the runit init system instead of systemd, making it unique among Linux distros. Void also supports both glibc and musl as C libraries. |
| `Alpine Linux` | A lightweight, security-focused Linux distribution often used for containers due to its small size and minimal dependencies. It uses musl instead of glibc and OpenRC for init. Commonly found in Docker containers. |

<br>

[Back To Top](#the-gnulinux-operating-system)
___

<br>


*Created and maintained by Mr. Merritt*


import os
from pathlib import * 
import subprocess

# Define the maze structure as a nested dictionary
maze_structure = {
    "maze": {
        "left": {
            "east": {
                "north": {},
                "south": {
                    "up": {},
                    "down": {
                        "straight": {},
                        "turn-around": {
                            "straight": {}
                        }
                    }
                }
            },
            "west": {
                "north": {},
                "south": {
                    "up": {},
                    "down": {
                        "straight": {
                            "east": {
                                "north": {},
                                "south": {
                                    "up": {},
                                    "down": {
                                        "straight": {},
                                        "turn-around": {}
                                    }
                                }
                            },
                            "west": {
                                "north": {},
                                "south": {
                                    "up": {},
                                    "down": {
                                        "straight": {},
                                        "turn-around": {}
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "right": {
            "east": {
                "down": {
                    "north": {},
                    "south": {
                        "up": {},
                        "down": {
                            "straight": {},
                            "turn-around": {}
                        }
                    }

                }
            },
            "west": {
                "north": {},
                "south": {}
            }
        }
    }
}


def create_directories(base_path, structure):
    for dir_name, sub_dirs in structure.items():
        # Create the directory
        new_path = os.path.join(base_path, dir_name)
        os.makedirs(new_path, exist_ok=True)
        with open(os.path.join(base_path, "file.txt"), "a") as f:
            f.write("DEAD END.........")
        
        # Recursively create sub-directories
        create_directories(new_path, sub_dirs)

    print("Maze directory structure created successfully!")


def hide_files():
    path =  Path(__file__).parent.resolve()
    try:
        with open(path / "maze" / "left" / "west" / "south" / "down" / "straight" / "west" / "south" / "down" / "turn-around"/ "exit.txt", "w") as file:
            if os.name == "posix":
                file.write("cd ~/Desktop")
            elif os.name == "nt":
                file.write("cd ~\Desktop")
    except FileNotFoundError as e:
        print(f"The file path could not be found, check your path.\n{e}")

    

    # path = Path().resolve().root
    path = Path("/")
    filename = "HIDDEN_FILE.txt"


    if(os.name == "nt"):
        user = os.getenv("USERPROFILE")

        with open(path / filename, "a") as f:
            f.write(
                "This file is in the root directory, or the folder that contains all other folders.\n"
                "In Windows the root directory is typically written as C:\\ \n\n"
                "In Windows, the root directory is the top-level directory in a drive.\n"
                "It is denoted by the drive letter followed by a colon and a backslash (e.g., C:\\, D:\\).\n\n"
                "The root directory is where the directory structure of a drive begins,\n"
                "and all other directories and files are nested within this root.\n\n"
                "Below is the basic structure of C:\\ and the folders it contains.\n"
                "Try typing 'tree /F /A /L 2' on your terminal to see your actual folder structure.\n"
                '''
                C:\\
                ├── Program Files
                │   ├── Common Files
                │   ├── WindowsApps
                │   └── ...
                ├── Program Files (x86)
                │   ├── Common Files
                │   └── ...
                ├── Users
                │   ├── Default
                │   ├── Public
                │   ├── %USERNAME%
                │   │   ├── Desktop
                │   │   ├── Documents
                │   │   ├── Downloads
                │   │   └── ...
                │   └── ...
                ├── Windows
                │   ├── System32
                │   ├── WinSxS
                │   ├── Temp
                │   └── ...
                ├── ProgramData
                ├── PerfLogs
                ├── $Recycle.Bin
                └── ...
                '''
            )
        
        with open(path / "Users" /  filename, "a") as f:
            f.write(
                "In Windows, the 'Users' directory is a key part of the filesystem hierarchy.\n"
                "It is located at 'C:\\Users' by default and contains individual directories for each user account.\n\n"
                
                "Key Points about the 'Users' Directory:\n\n"
                
                "1. User Directories:\n"
                "   Each user account on the system has a corresponding directory within the 'Users' folder.\n"
                "   These directories typically have names corresponding to the usernames. For example:\n"
                "   - 'C:\\Users\\Default': A default profile used when creating new user accounts.\n"
                "   - 'C:\\Users\\Public': A public profile that provides access to common files for all users.\n"
                "   - 'C:\\Users\\YourUsername': A personal directory for the individual user 'YourUsername'.\n\n"
                
                "2. User Profile Contents:\n"
                "   Each user's directory contains personal files and folders, including:\n"
                "   - 'Desktop': Contains files and shortcuts that appear on the user's desktop.\n"
                "   - 'Documents': A folder for storing documents and other personal files.\n"
                "   - 'Downloads': The default folder for files downloaded from the internet.\n"
                "   - 'Pictures': A folder for storing image files.\n"
                "   - 'Videos': A folder for storing video files.\n"
                "   - 'AppData': A hidden folder for application-specific data, including settings and cache.\n\n"
                
                "3. Special Folders:\n"
                "   - 'Default': This is a template profile used by the system when creating new user accounts.\n"
                "   - 'Public': Contains files and folders accessible by all users of the computer.\n\n"
                
                "4. Access Permissions:\n"
                "   Each user's directory is generally accessible only by the respective user and system administrators.\n"
                "   The permissions ensure privacy and security of user data.\n\n"
                
                "Example of the 'Users' Directory Structure:\n\n"
                "C:\\Users\\\n"
                "├── Default\n"
                "├── Public\n"
                "└── YourUsername\n"
                "    ├── Desktop\n"
                "    ├── Documents\n"
                "    ├── Downloads\n"
                "    ├── Pictures\n"
                "    ├── Videos\n"
                "    └── AppData\n\n"

            )

        with open(user / filename, "a") as f:
            f.write(
                "Since usernames vary %USERNAME% is used to represent any username. %USERNAME% represents your actual username on the computer.\n"
                "In Windows, the %USERNAME% directory refers to the personal directory for a specific user account.\n"
                "It is located under the 'Users' folder, typically found at 'C:\\Users\\%USERNAME%'.\n\n"
                
                "Key Points about the %USERNAME% Directory:\n\n"
                
                "1. Location:\n"
                "   The %USERNAME% directory is located at 'C:\\Users\\%USERNAME%', where %USERNAME% is the actual name of the user.\n\n"
                
                "2. Contents:\n"
                "   This directory contains personal files and folders specific to the user. Common subdirectories include:\n"
                "   - 'Desktop': Contains files and shortcuts that appear on the user's desktop.\n"
                "   - 'Documents': A folder for storing personal documents and files.\n"
                "   - 'Downloads': The default folder for files downloaded from the internet.\n"
                "   - 'Pictures': A folder for storing image files and photo collections.\n"
                "   - 'Videos': A folder for storing video files and media.\n"
                "   - 'Music': A folder for storing audio files and music collections.\n"
                "   - 'AppData': A hidden folder containing application-specific data, such as settings and cache.\n\n"
                
                "3. User Profile Information:\n"
                "   - 'AppData': Contains subdirectories like 'Local', 'LocalLow', and 'Roaming', used by applications to store user-specific data.\n\n"
                
                "4. Access Permissions:\n"
                "   The %USERNAME% directory is typically accessible only by the user and system administrators.\n"
                "   This ensures that personal files and settings are kept private and secure.\n\n"
                
                "5. Example of %USERNAME% Directory Structure:\n\n"
                "C:\\Users\\%USERNAME%\\\n"
                "├── Desktop\n"
                "├── Documents\n"
                "├── Downloads\n"
                "├── Pictures\n"
                "├── Videos\n"
                "├── Music\n"
                "└── AppData\n"
                "    ├── Local\n"
                "    ├── LocalLow\n"
                "    └── Roaming\n\n"
            )
    
        with open(user / "Desktop" / filename, "a") as f:
            f.write(
                "In Windows, the 'Desktop' directory is a special folder within a user's profile directory.\n"
                "It is located at 'C:\\Users\\%USERNAME%\\Desktop', where '%USERNAME%' is the actual name of the user.\n\n"
                
                "Key Points about the 'Desktop' Directory:\n\n"
                
                "1. Location:\n"
                "   The 'Desktop' directory is part of the user's profile folder. Its full path is typically 'C:\\Users\\%USERNAME%\\Desktop'.\n\n"
                
                "2. Contents:\n"
                "   The 'Desktop' directory contains files and shortcuts that are displayed on the user's desktop screen. Common contents include:\n"
                "   - **Files:** Documents, images, and other files that the user places on their desktop for easy access.\n"
                "   - **Shortcuts:** Links to applications, folders, or files that the user frequently uses.\n\n"
                
                "3. Purpose:\n"
                "   - The desktop provides a convenient place for users to access frequently used files and applications.\n"
                "   - It acts as a workspace where users can organize their most important or frequently accessed items.\n\n"
                
                "4. Customization:\n"
                "   - Users can customize the appearance of their desktop, including background images and icon arrangement.\n"
                "   - The desktop environment can be personalized to suit individual preferences.\n\n"
                
                "5. Example Path:\n\n"
                "C:\\Users\\%USERNAME%\\Desktop\n\n"
                
                "Summary:\n"
                "The 'Desktop' directory in Windows is a user-specific folder that contains files and shortcuts visible on the desktop screen.\n"
                "It provides a central location for organizing and accessing frequently used items and can be customized according to user preferences."
            )

        with open(user / "Downloads" / filename, "a") as f:
            f.write(
                "In Windows, the 'Downloads' directory is the default location where files\n"
                "downloaded from the internet are saved. It is located at 'C:\\Users\\%USERNAME%\\Downloads',\n"
                "where '%USERNAME%' represents the name of the current user.\n\n"
                
                "Key Points about the 'Downloads' Directory:\n\n"
                
                "1. Location:\n"
                "   The 'Downloads' folder is part of the user's profile and is usually found at:\n"
                "   'C:\\Users\\%USERNAME%\\Downloads'.\n\n"
                
                "2. Purpose:\n"
                "   The 'Downloads' directory is used as the default destination for files downloaded via web browsers,\n"
                "   email clients, and other programs. It helps keep the system organized by providing a central place\n"
                "   for all downloads.\n\n"
            )

    elif(os.name == "posix"):
        user = Path.home()

        commands = [
            ["sudo", "touch", f"/{filename}"],
            ["sudo","chmod","777", f"/{filename}"],
            ["sudo", "touch", f"/home/{filename}"],
            ["sudo","chmod","777", f"/home/{filename}"]
        ]

        for command in commands:
            result = subprocess.run(command, capture_output=True, text=True)

        with open(path / filename, "a") as f:
            f.write(
                "In Linux, the root directory is the topmost directory in the filesystem hierarchy.\n"
                "It is denoted by a single forward slash (/). All other directories, files, and\n"
                "devices are organized under this root directory, forming a tree-like structure.\n\n"
                
                "Key Points about the Root Directory (/):\n\n"
                
                "1. Top of the Hierarchy:\n"
                "   The root directory is the starting point of the entire filesystem. All other\n"
                "   directories branch out from this point, making it the parent directory of all\n"
                "   other directories and files on the system.\n\n"
                
                "2. Absolute Paths:\n"
                "   In Linux, an absolute path always starts with a '/', indicating that it begins\n"
                "   from the root directory. For example, /home/user/documents refers to then\n"
                "   documents directory inside the user directory, which is inside the home directory,\n"
                "   starting from the root.\n\n"
                
                "3. System Directories:\n"
                "   Several important system directories reside directly under the root directory.\n"
                "   These directories store system files, user data, configuration files, libraries,\n"
                "   binaries, and more. Some common subdirectories include:\n"
                "   - /bin: Contains essential binary executables (e.g., ls, cp, mv).\n"
                "   - /boot: Contains files needed to boot the system, including the Linux kernel.\n"
                "   - /dev: Contains device files, which represent hardware devices (e.g., hard drives, printers).\n"
                "   - /etc: Contains system-wide configuration files.\n"
                "   - /home: Contains home directories for all users (e.g., /home/username).\n"
                "   - /lib: Contains shared libraries and kernel modules.\n"
                "   - /media and /mnt: Temporary mount points for removable media like USB drives and other filesystems.\n"
                "   - /opt: Contains optional software packages.\n"
                "   - /proc: A virtual filesystem that provides information about running processes.\n"
                "   - /root: The home directory for the root (superuser) account.\n"
                "   - /sbin: Contains system binaries, typically for administrative tasks.\n"
                "   - /tmp: A temporary directory for storing transient files.\n"
                "   - /usr: Contains user utilities and applications.\n"
                "   - /var: Contains variable data files, such as logs, databases, and spool files.\n\n"
                
                "4. Root User vs. Root Directory:\n"
                "   It's important not to confuse the 'root directory' (/) with the 'root user.' The root user\n"
                "   is the superuser with administrative privileges, while the root directory is the top-level\n"
                "   directory of the filesystem.\n\n"
                
                "5. Mount Points:\n"
                "   In Linux, filesystems from different storage devices (like hard drives, SSDs, and removable\n"
                "   media) are mounted at specific directories within the root filesystem. For example, a separate\n"
                "   partition might be mounted at /home, or a USB drive might be mounted at /media/usb.\n\n"
                
                "Example of a Linux Filesystem Structure:\n\n"
                "Try typing 'tree -L 2' to see the first two levels of your filesystem.\n"
                "If tree is not installed --> 'sudo apt install tree'\n"
                "/\n"
                "├── bin\n"
                "├── boot\n"
                "├── dev\n"
                "├── etc\n"
                "├── home\n"
                "│   ├── user1\n"
                "│   └── user2\n"
                "├── lib\n"
                "├── media\n"
                "├── mnt\n"
                "├── opt\n"
                "├── proc\n"
                "├── root\n"
                "├── sbin\n"
                "├── tmp\n"
                "├── usr\n"
                "└── var\n\n" 
            )
            
        with open(path / "home" / filename, "a") as f:

            f.write(
                "In Linux, the 'home' directory is a special directory that stores personal files and settings\n"
                "for each user on the system. It is located at '/home/$USER', where '$USER' represents the name\n"
                "of the current user.\n\n"
                
                "Key Points about the 'Home' Directory:\n\n"
                
                "1. Location:\n"
                "   The 'home' directory is typically found at '/home', and each user has a subdirectory within it.\n"
                "   For example, a user named 'john' will have their files located at '/home/john'.\n\n"
                
                "2. Purpose:\n"
                "   The 'home' directory serves as the main workspace for users, containing their personal files,\n"
                "   settings, and data. It is where users store documents, downloads, and application configuration files.\n\n"
                
                "3. Contents:\n"
                "   A typical 'home' directory contains various subdirectories, including:\n"
                "   - **Desktop:** Files and shortcuts visible on the user's desktop.\n"
                "   - **Documents:** Personal documents and files.\n"
                "   - **Downloads:** Files downloaded from the internet.\n"
                "   - **Pictures:** Images and photo collections.\n"
                "   - **Music:** Audio files and music collections.\n"
                "   - **Videos:** Video files and media content.\n"
                "   - **.config and .local:** Hidden directories that store application settings and user-specific configurations.\n\n"
                
                "4. Permissions:\n"
                "   Each user's 'home' directory is generally only accessible by that user and the system administrator.\n"
                "   This ensures privacy and separation of data between users on the same machine.\n\n"
                
                "5. Example Path:\n\n"
                "/home/$USER\n\n"
                
                "Summary:\n"
                "The 'home' directory in Linux is the central location for a user's personal files and settings.\n"
                "It provides a private workspace for each user, ensuring a structured and organized environment\n"
                "for managing personal data."
            )
            
        with open(user / filename, "a") as f:
            f.write(
                "In Linux, the '$USER' directory refers to the personal home directory of the current user.\n"
                "The '$USER' environment variable represents the username of the person logged into the system.\n"
                "The home directory for the user is located at '/home/$USER'.\n\n"
                
                "Key Points about the '$USER' Directory:\n\n"
                
                "1. Location:\n"
                "   The home directory for each user is typically found at '/home/$USER', where '$USER' is the name\n"
                "   of the current user. For example, if the user's name is 'john', their home directory will be\n"
                "   '/home/john'.\n\n"
                
                "2. Purpose:\n"
                "   The '$USER' directory is a private space for the user to store personal files, documents, and configurations.\n"
                "   Each user has their own separate directory to ensure privacy and separation of data from other users on the system.\n\n"
                
                "3. Contents:\n"
                "   The '$USER' directory typically contains several important subdirectories, including:\n"
                "   - **Desktop:** Files and shortcuts that appear on the user's desktop.\n"
                "   - **Documents:** A folder for storing personal documents and files.\n"
                "   - **Downloads:** A folder where files downloaded from the internet are stored.\n"
                "   - **Pictures, Music, Videos:** Folders for organizing personal media files.\n"
                "   - **.config, .local, .cache:** Hidden directories that store application settings and user-specific configurations.\n\n"
                
                "4. Permissions:\n"
                "   Each user's home directory is generally only accessible by that user and the system administrator.\n"
                "   This ensures that files and configurations remain private and secure.\n\n"
                
                "5. Example Path:\n\n"
                "/home/$USER\n\n"
                
                "Summary:\n"
                "The '$USER' directory in Linux refers to the user's personal home directory. It contains the user's\n"
                "files, settings, and configurations, ensuring a private workspace for each individual on the system."
            )
        
        with open(user / "Desktop" / filename, "a") as f:
                f.write(
                    "In Linux, the 'Desktop' directory is a special folder located within a user's home directory.\n"
                    "It is typically found at '/home/$USER/Desktop', where '$USER' respresents the name of the user.\n"
                    "The 'Desktop' directory is used to store files, shortcuts, and folders that are visible on the\n"
                    "graphical desktop environment (GUI) of the system.\n\n"
                    
                    "Key Points about the 'Desktop' Directory:\n\n"
                    
                    "1. Location:\n"
                    "   The 'Desktop' directory is a subdirectory of the user's home directory and is located at\n"
                    "   '/home/$USER/Desktop'.\n\n"
                    
                    "2. Purpose:\n"
                    "   The 'Desktop' directory is used to store files and shortcuts that are visually represented on the\n"
                    "   user's desktop in graphical environments like GNOME, KDE, or Xfce. This provides easy access to frequently\n"
                    "   used items right on the desktop screen.\n\n"
                    
                    "3. Contents:\n"
                    "   The 'Desktop' directory can contain a variety of items, including:\n"
                    "   - **Files:** Documents, images, and other files that the user wants quick access to.\n"
                    "   - **Shortcuts:** Links to applications, files, or folders.\n"
                    "   - **Folders:** Additional subdirectories that the user may create for organization.\n\n"
                    
                    "4. Customization:\n"
                    "   - Users can customize the appearance of their desktop by adding or removing items from the 'Desktop' directory.\n"
                    "   - The desktop environment will reflect any changes made to this folder in real-time, showing or hiding files accordingly.\n\n"
                    
                    "5. Example Path:\n\n"
                    "/home/$USER/Desktop\n\n"
                
                )
                
        with open(user / "Downloads" / filename, "a") as f:
            f.write(
                "In Linux, the 'Downloads' directory is the default location where files downloaded from the\n"
                "internet are saved. It is located at '/home/$USER/Downloads', where '$USER' is the environment variable\n"
                "representing the current user's name.\n\n"
                
                "Key Points about the 'Downloads' Directory:\n\n"
                
                "1. Location:\n"
                "   The 'Downloads' directory is a subdirectory within the user's home folder, typically found at:\n"
                "   '/home/$USER/Downloads'.\n\n"
                
                "2. Purpose:\n"
                "   The 'Downloads' directory is used as the default destination for files downloaded from web browsers,\n"
                "   email clients, and other applications. It helps keep the system organized by providing a central location\n"
                "   for all downloaded content.\n\n"
                
                "3. Contents:\n"
                "   The 'Downloads' folder typically contains a variety of file types such as:\n"
                "   - **Documents:** PDFs, text files, and word processing documents.\n"
                "   - **Media Files:** Images, videos, and audio files.\n"
                "   - **Software:** Installation packages (.deb, .tar.gz, or executable files).\n"
                "   - **Compressed Files:** ZIP or TAR archives.\n\n"
                
                "4. Organization:\n"
                "   Users can organize the 'Downloads' directory by moving files to other folders or deleting unnecessary\n"
                "   files to free up space. It's important to periodically clean this folder to prevent clutter.\n\n"
                
                "5. Example Path:\n\n"
                "/home/$USER/Downloads\n\n"
                
                "Summary:\n"
                "The 'Downloads' directory in Linux is a user-specific folder where downloaded files are stored.\n"
                "It provides a centralized location for managing downloaded content, making it easy to access\n"
                "and organize files."
            )

    else:
        print("File system not recognized.\nExiting...")
        exit()

    print("Files hidden successfully!")


# Set the base path where the maze structure will be created
base_path = "."

# Create the maze directory structure
create_directories(base_path, maze_structure)

hide_files()





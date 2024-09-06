# `Operating Systems`

# `Terms`

`Hardware` refers to the physical components of a computer system or electronic device. 
> * This includes the central processing unit (CPU), memory (RAM), storage devices (hard drives, SSDs), input devices (keyboard, mouse), output devices (monitor, printer), and other physical parts that are integral to the operation of the device.

<br>

`Firmware` is specialized software that is embedded into hardware devices to control their functions. 
> * It is stored in non-volatile memory, such as ROM or flash memory, and provides low-level control for the hardware. 
> * Firmware is essential for the basic operation of the device and is often updated to fix bugs or add functionality.
> * Typically found on the motherboard.

- `BIOS (Basic Input/Output System)`: The traditional firmware that initializes and tests hardware during the boot process, and provides an interface for the operating system to interact with the hardware.  
- `UEFI (Unified Extensible Firmware Interface)`: The modern replacement for BIOS, offering more advanced features and a graphical interface. UEFI handles the initial hardware initialization and boot process and provides an environment for managing hardware and system settings.


<br>

`Software` refers to a collection of programs and operating information used by a computer or electronic device. 
> * It encompasses all the non-hardware components, including operating systems, applications, and utilities that perform tasks and manage hardware resources.

<br>

`Device Drivers` are specialized software programs that allow the operating system and software applications to communicate with hardware devices. 
> * They act as intermediaries between the operating system and hardware components, such as printers, graphics cards, or network adapters, enabling the hardware to function correctly.
> * Device drivers are integrated into the kernel or loaded as kernel modules. They operate in kernel space, which is a protected area of memory with higher privileges compared to user space.
>   - Drivers translate operating system commands into device-specific instructions
>   - Drivers handle input/output operations
>   - Drivers manage device-specific functions

<br>

`Kernel` is the core component of an operating system that manages system resources and hardware interactions. 
> * It provides essential services such as process management, memory management, hardware abstraction, and system calls. 
> * The kernel operates in a privileged mode to ensure efficient and secure communication between hardware and software.

<br>

`Shell (CLI)`, or Command Line Interface, is a text-based interface used to interact with the operating system. 
> * Users enter commands in a terminal or command prompt to perform various tasks, such as file management, system configuration, and program execution. 
> * The CLI allows for powerful and precise control over the system.

<br>

`Applications (GUI)`, or Graphical User Interface applications, are software programs designed to provide users with an intuitive and visually interactive way to perform tasks. 
> * They use graphical elements such as windows, icons, buttons, and menus to facilitate user interaction, making complex operations easier to manage through visual representation.

<br>


# `Defining Operating System`


An **Operating System (OS)** is a software system that manages and controls the hardware and software resources of a computer or electronic device. 
> It provides a user interface and acts as an intermediary between users, applications, and the hardware.

## Components of an Operating System

1. `Kernel`: The central component of the OS that manages system resources and hardware interactions.
- **Functions**:
  - Manages CPU, memory, and device drivers.
  - Handles process and memory management.
  - Provides system calls for applications to interact with hardware.
  - `File System`: Manages files and directories on storage devices.
  - `Device Drivers`: Software components that enable the OS to communicate with hardware devices.

<br>

2. `Shell`: A command-line interface that allows users to interact with the kernel.
- **Functions**:
  - Executes commands and scripts.
  - Provides a text-based interface for file management and system operations.
  - Supports automation and scripting.

<br>

3. `System Libraries`: Collections of pre-written code that applications can use.
- **Functions**:
  - Provide standard functions and routines for applications.
  - Facilitate communication between applications and the OS.
  - Include libraries for handling tasks like input/output, networking, and graphics.

<br>

4. `Applications` : (often referred to as apps or software applications) are programs designed to perform specific tasks or functions for end users. 
- **Functions**:
    - `User Interface`: Facilitates user interaction with the OS and applications.
        - Provides graphical (GUI) or command-line (CLI) interfaces.
    - `System Utilites`: Tools and programs that perform system maintenance and configuration tasks.
    - `Security Mechanisms`: Components that enforce security policies and protect the system.









Perfect — I’ll continue building out the rest of the `Batch scripting notes` in the same structured Markdown style you showed me.

---

# `Batch Scripting Introduction`

*Use CTRL + F to search for keywords in this file*
*You are encouraged to copy and alter the code in this file to understand how it works*

---

Covered in this file:

1. [`What is Batch Scripting?`](#what-is-batch-scripting)
2. [`Creating a Batch File`](#creating-a-batch-file)
3. [`Running a Batch File`](#running-a-batch-file)
4. [`Basic Syntax`](#basic-syntax)
   1. [`The ECHO Command`](#the-echo-command)
   2. [`The REM Command (Comments)`](#the-rem-command-comments)
   3. [`Using Variables`](#using-variables)
5. [`Control Flow`](#control-flow)
   1. [`IF Statements`](#if-statements)
   2. [`GOTO and Labels`](#goto-and-labels)
   3. [`FOR Loops`](#for-loops)
6. [`Working with Files and Directories`](#working-with-files-and-directories)
7. [`Useful Tips`](#useful-tips)

<br>  

---

<br>  

# `What is Batch Scripting?`

Basically: A `Batch script` is a text file containing a series of commands that are executed by the Windows Command Prompt (`cmd.exe`).

Specifically: Batch scripting provides a way to `automate tasks` in Windows by writing command-line instructions in a `.bat` or `.cmd` file.

* Batch files are executed line-by-line in sequence.
* They can automate repetitive actions like file management, program launching, or system configuration.
* While simple compared to other scripting languages, Batch scripts are still powerful for system tasks.


example:
```batch
@echo off
echo Hello, World!
pause
```

Output when run:

```
Hello, World!
Press any key to continue . . .
```

<br>  

[Back to Top](#batch-scripting-introduction)

---

<br>  

# `Creating a Batch File`

1. Open `Notepad` (or any text editor).
2. Type your Batch commands (example below).
3. Save the file with the extension `.bat` or `.cmd`.

Example:

```batch
@echo off
echo This is my first batch file!
pause
```

Double-clicking the file will execute it in the Command Prompt.

<br>  

[Back to Top](#batch-scripting-introduction)

---

<br>  

# `Running a Batch File`

There are several ways to run a Batch script:

* `Double-click` the `.bat` file in File Explorer.
* Run it from the `Command Prompt` by typing the filename:

  ```cmd
  myscript.bat
  ```
* Place it in system startup folders or schedule it with `Task Scheduler` for automation.

<br>  

[Back to Top](#batch-scripting-introduction)

---

<br>  

# `Basic Syntax`

Batch files are made up of `commands` that are executed in sequence. Let’s start with the most essential ones:

<br>  

## `The ECHO Command`

The `ECHO` command displays text on the screen.

```batch
@echo off
echo This text will appear in the console.
```

* `@echo off` hides the command itself from being printed.
* Without it, each command is shown before execution.

<br>  

[Back to Top](#batch-scripting-introduction)

---

<br>  

## `The REM Command (Comments)`

`REM` adds comments inside a Batch file. Comments are ignored by the interpreter.

```batch
@echo off
REM This is a comment
echo Hello World
```

Alternatively, `::` can also be used as a shorthand for comments:

```batch
:: Another way to write comments
```

<br>  

[Back to Top](#batch-scripting-introduction)

---

<br>  

## `Using Variables`

Batch variables are defined using `SET` and accessed with `%` signs.

```batch
@echo off
set name=Alice
echo Hello %name%
pause
```

Output:

```
Hello Alice
```

* Variables are always strings (no strict data types).
* You can use `SET /A` for arithmetic:

```batch
set /a sum=5+10
echo %sum%
```

Output:

```
15
```

<br>  

[Back to Top](#batch-scripting-introduction)

---

<br>  

# `Control Flow`

Batch scripting supports simple logic structures:

<br>  

## `IF Statements`

```batch
@echo off
set /a number=10
if %number%==10 echo Number is 10
```

Conditional checks with operators:

* `==` Equal
* `NEQ` Not equal
* `LSS` Less than
* `LEQ` Less than or equal
* `GTR` Greater than
* `GEQ` Greater than or equal

```batch
if %number% GTR 5 echo Number is greater than 5
```

<br>


## `Multi-line IF Statements`

Normally, `IF` runs a single command. To execute **multiple commands**, enclose them in parentheses:

```batch
@echo off
set /a number=5

if %number% LSS 10 (
    echo The number is less than 10
    echo Doing multiple things...
    set /a doubled=%number%*2
    echo Doubled value: %doubled%
)
```

Output:

```
The number is less than 10
Doing multiple things...
Doubled value: 10
```

*Important:*

* Commands inside the parentheses must be indented (recommended for readability).
* Parentheses must open on the same line as the `IF` statement.


<br>

## `GOTO and Labels`

You can jump to different parts of a script using labels.

```batch
@echo off
goto skip
echo This will be skipped.
:skip
echo This will be shown.
```

<br>  

## `FOR Loops`

The `FOR` command repeats actions for a list of values or files.

```batch
@echo off
for %%i in (1 2 3 4 5) do echo Number: %%i
```

Output:

```
Number: 1  
Number: 2  
Number: 3  
Number: 4  
Number: 5  
```

<br>  

## `Multi-line FOR Loops`

Like `IF`, `FOR` can also execute multiple commands with parentheses:

```batch
@echo off
for %%i in (1 2 3) do (
    echo Processing number %%i
    set /a squared=%%i*%%i
    echo %%i squared is %squared%
)
```

**Important Note About Variables:**
When using variables inside loops, `%` expansion happens **before** the loop runs.
This means `%squared%` will not update as expected unless you use **delayed expansion**.

Enable delayed expansion with:

```batch
setlocal enabledelayedexpansion
```

Then use `!var!` instead of `%var%`.

Corrected example with delayed expansion:

```batch
@echo off
setlocal enabledelayedexpansion
for %%i in (1 2 3) do (
    set /a squared=%%i*%%i
    echo %%i squared is !squared!
)
endlocal
```

Output:

```
1 squared is 1
2 squared is 4
3 squared is 9
```

<br>  

[Back to Top](#batch-scripting-introduction)

---

<br>  

# `Working with Files and Directories`

Some useful commands:

* `DIR` – list files in a directory
* `COPY` – copy files
* `DEL` – delete files
* `MKDIR` – create a folder
* `RMDIR` – remove a folder

Example:

```batch
@echo off
mkdir testfolder
cd testfolder
echo This is inside testfolder > file.txt
dir
pause
```

This will create a folder, write a file, and show its contents.

<br>  

[Back to Top](#batch-scripting-introduction)

---

<br>  

# `Useful Tips`

* Always start scripts with `@echo off` to make output cleaner.
* Use `pause` to keep the window open until a key is pressed.
* Use `call` when running another batch file from within one.
* Test scripts in a safe directory before using them on important files.

<br>  

[Back to Top](#batch-scripting-introduction)

---

<br>  



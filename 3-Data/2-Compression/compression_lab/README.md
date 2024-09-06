

# `Compression Lab`

Directions:
1. Read through the 'compress-this.txt' file and enjoy the AI generated, funny computer story entitled "The Great Computer Conspiracy". 
1. Design your own lossless algorithm to compress the data in this story to the smallest size you can. 
    1. *It must be possible to completely restore the orginal data from your compressed format*
1. Apply your algorithm to the data in the text file. Write this data to the currently empty 'my_compression.txt' file.
1. Compare the size of the two files in bytes. (See below if you need help)
1. Using the provided 'compress-it.py' file, compress the data using the 4 common algorithms in the script.
    1. *Read the compress-it.py file to get an idea of how the script works*

1. Compare the size of your compression to the size of these compressed files.
1. BONUS: Impliment your compression algorithm in a Python script.


<br>

To compare sizes on Windows:

    dir

When reading the output of dir or ls on poweshell the Length column lists the size of a file in bytes.
```
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          9/2/2024  22:10 PM           5298 compress-it.py
-a----          9/2/2024  21:34 PM           4149 compress-this.txt
-a----          9/2/2024  22:22 PM              0 my_compression.txt
-a----          9/2/2024  22:38 PM            886 README.md
```

<br>


To compare sizes on linux:

    $ ls -la

Output:
When reading the output of ls -la on bash the columns are not listed, however they have been added below to help you find the size of the files in bytes.
```
Permissions Links Owner Group Size Date   Time  Name

-rw-r--r--    1    user user  5298 Sep  2 22:10 compress-it.py
-rw-r--r--    1    user user  4149 Sep  2 21:34 compress-this.txt
-rw-r--r--    1    user user     0 Sep  2 22:22 my_compression.txt
-rw-r--r--    1    user user   886 Sep  2 22:38 README.md
```



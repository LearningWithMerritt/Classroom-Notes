# File Signatures
> * File signatures, also known as magic numbers, are unique sequences of bytes found at the beginning of a file that help to identify its format or type.  
> * These signatures are used by software to determine how to interpret or process the file's data. Each file format has a distinct signature, allowing programs to recognize and handle various file types correctly.  

> * Location: File signatures are typically located at the very start of a file, often in the first few bytes.  
> * Purpose: They help identify the file type regardless of its extension, making it easier for programs to process the file correctly.  
> * Format: File signatures are expressed in hexadecimal format and represent a specific sequence of bytes.  
>* Usage: Software, such as file readers or operating systems, use file signatures to verify file types and ensure proper handling or decoding.  

| **File Type**   | **File Extension(s)** | **File Signature (Hexadecimal)**  | **Description** |
|:-:|:-:|:-:|:-:|
| Portable Document Format| .pdf| 25 50 44 46 2D 31 2E 34 0A | PDF document|
| Microsoft Word (Older)| .doc | D0 CF 11 E0 A1 B1 1A E1 | Older Microsoft Word document|
| Microsoft Word (Open XML)| .docx| 50 4B 03 04 14 00 06 00 08 00| Microsoft Word Open XML document|
| Microsoft Excel (Older) | .xls | D0 CF 11 E0 A1 B1 1A E1 | Older Microsoft Excel spreadsheet|
| Microsoft Excel (Open XML) | .xlsx| 50 4B 03 04 14 00 06 00 08 00| Microsoft Excel Open XML spreadsheet |
| Portable Network Graphics| .png | 89 50 4E 47 0D 0A 1A 0A | PNG image file|
| Joint Photographic Experts Group | .jpg, .jpeg | FF D8 FF E0 00 10 4A 46 49 46 | JPEG image file |
| Graphics Interchange Format| .gif | 47 49 46 38  | GIF image file|
| Tagged Image File Format| .tiff| 49 49 2A 00 or 4D 4D 00 2A| TIFF image file |
| Audio Interchange File Format| .wav | 52 49 46 46 xx xx xx xx 57 41 56 41| WAV audio file|
| MPEG-4 Video| .mp4 | 00 00 00 xx 66 74 79 70 | MP4 video file|
| Moving Picture Experts Group | .mpg, .mpeg| 00 00 01 BA or 00 00 01 B3| MPEG video file |
| Compressed Archive | .zip | 50 4B 03 04 | ZIP archive file|
| Compressed Archive | .rar | 52 61 72 21 1A 07 00 00 00| RAR archive file|
| Unix Executable File| .out, (varies)| 7F 45 4C 46 | Executable file on Unix/Linux systems|
| ELF Executable| .elf | 7F 45 4C 46 | Executable file on Unix/Linux systems|
| Windows Executable | .exe | 4D 5A| Executable file on Windows systems |
| Rich Text Format| .rtf | 7B 5C 72 74 66 31 2E 30 | Rich Text Format file |
| Hypertext Markup Language| .html, .htm| 3C 68 74 6D 6C 3E| HTML document |
| Extensible Markup Language | .xml | 3C 3F 78 6D 6C 20 | XML document|
| Apple Pages| .pages| 50 4B 03 04 14 00 06 00 08 00| Apple Pages document|
| Apple Numbers | .numbers| 50 4B 03 04 14 00 06 00 08 00| Apple Numbers spreadsheet |
| Adobe Photoshop Document| .psd | 38 42 50 53 00 00 00 00 | Adobe Photoshop file|
| Autodesk AutoCAD Drawing | .dwg | 41 43 31 30 30 0A | AutoCAD drawing file|
| Windows Media Audio| .wma | 30 26 B2 75 8E 66 CF 11 A6 D9 00 00| Windows Media Audio file|
| Advanced Video Coding | .avc | 00 00 00 01 67| H.264/AVC video file|
| JavaScript Object Notation | .json| 7B 0A| JSON data file|
| PostScript | .ps| 25 21 50 53 2D 31 2E 30 | PostScript file |
| MATLAB| .mat | 4D 54 4C 42 00 00 00 00 | MATLAB data file|
| TrueType Font | .ttf | 00 01 00 00 00 00 00 00 | TrueType font file |
| OpenType Font | .otf | 4F 54 54 4F 00 00 00 00 | OpenType font file |
| Flash Video| .flv | 46 4C 56 01 00 00 00| Flash video file|
| RealAudio| .ra, .ram | 2E 52 41 4D 00 00 00 00 | RealAudio file|
| Microsoft Access Database| .mdb | 00 01 00 00 00 00 00 00 | Microsoft Access database file|
| SQLite Database | .sqlite, .db | 53 51 4C 69 74 65 00 00 | SQLite database file|
| Java Class File | .class| CA FE BA BE | Java class file |
| Android Package | .apk | 4C 50 00 00 00 00 00 00 | Android application package|


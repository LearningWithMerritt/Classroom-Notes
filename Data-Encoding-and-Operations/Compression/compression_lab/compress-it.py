'''Hey! I see you reading my code.'''

import os
import sys
import pathlib
import shutil

ROOT = pathlib.Path(__file__).parent.resolve()
COMPRESSED_DIR = ROOT / "compressed"
DECOMPRESS_DIR = ROOT / "decompressed"

path = [COMPRESSED_DIR, DECOMPRESS_DIR]



def zip_it(file_in, file_out = "compressed.zip"):
    import zipfile

    try:
        if ".zip" in file_in:

            with zipfile.ZipFile(COMPRESSED_DIR / file_in, 'r') as zip:
                zip.extractall(DECOMPRESS_DIR)
        
        else:
            with zipfile.ZipFile(COMPRESSED_DIR / file_out, 'w') as zip:
                zip.write(file_in)
            
    

    except FileNotFoundError as e:
        print(f"File {file_in} could not be found. You might check your path.\n{e}")

    except Exception as e:
        print(e)
        
def gunzip_it(file_in, file_out):
    import gzip

    try:
        if ".gz" in file_in:
                            
            with gzip.open(COMPRESSED_DIR / file_in, "rb") as file:
                content = file.read()

            with open(DECOMPRESS_DIR / file_out, "wb") as file:
                file.write(content)
        
        else:
            with open(file_in, "rb") as file:
                content = file.read()
                
            with gzip.open(COMPRESSED_DIR / file_out, "wb") as file:
                file.write(content)

    

    except FileNotFoundError as e:
        print(f"File {file_in} could not be found. You might check your path.\n{e}")

    except Exception as e:
        print(e)
        

def bzip2_it(file_in, file_out):
    import bz2

    try:
        if ".bz2" in file_in:
                            
            with bz2.open(COMPRESSED_DIR / file_in, "rb") as file:
                content = file.read()

            with open(DECOMPRESS_DIR / file_out, "wb") as file:
                file.write(content)
        
        else:
            with open(file_in, "rb") as file:
                content = file.read()
                
            with bz2.open(COMPRESSED_DIR / file_out, "wb") as file:
                file.write(content)


    except FileNotFoundError as e:
        print(f"File {file_in} could not be found. You might check your path.\n{e}")

    except Exception as e:
        print(e)


def lzma_it(file_in, file_out):
    import lzma

    try:
        if ".xz" in file_in:
                            
            with lzma.open(COMPRESSED_DIR / file_in, "rb") as file:
                content = file.read()

            with open(DECOMPRESS_DIR / file_out, "wb") as file:
                file.write(content)
        
        else:
            with open(file_in, "rb") as file:
                content = file.read()
                
            with lzma.open(COMPRESSED_DIR / file_out, "wb") as file:
                file.write(content)

    

    except FileNotFoundError as e:
        print(f"File {file_in} could not be found. You might check your path.\n{e}")

    except Exception as e:
        print(e)



if __name__ == "__main__":


    if not os.path.exists(COMPRESSED_DIR):
        os.mkdir(COMPRESSED_DIR)

    if not os.path.exists(DECOMPRESS_DIR):
        os.mkdir(DECOMPRESS_DIR)

    if len(sys.argv) > 1:
        if sys.argv[1] == "compress":

            #Compress
            zip_it("compress-this.txt", "compressed.zip")
            gunzip_it("compress-this.txt","compressed.txt.gz")
            bzip2_it("compress-this.txt","compressed.txt.bz2")
            lzma_it("compress-this.txt","compressed.txt.xz")

        elif sys.argv[1] == "decompress":

            #Decompress
            zip_it("compressed.zip")
            gunzip_it("compressed.txt.gz", "gz-decompress.txt")
            bzip2_it("compressed.txt.bz2","bz2-decompress.txt")
            lzma_it("compressed.txt.xz", "xz-decompress.txt")

        elif sys.argv[1] == "clear":
            for dir in path:
                if os.path.exists(dir):
                    shutil.rmtree(dir)

        elif sys.argv[1] == "help":
            print("compress-it.py arguments list:\n\n"
                  "compress : compresses the 'compress-this.txt file using DEFLATE(.zip), gunzip (.gz), bzip2 (.bz2), and lzma (.xz) formats. Stored in the compressed directory.\n"
                  "decompress: decompresses the files in the compressed directory, and stores them in the decompressed directory. This is the reverse of compress.\n"
                  "clear : resets the lab. This removes the compressed and decompressed directories and thier files.\n"
                  "help : display this help menu.\n\n"
                  "To run a command:\n"
                  "Windows > python compress-it.py <argument>\n"
                  "Linux $ python3 compress-it.py <argument>"
                  )

        
        else:
            print("Command Not Recognized.\nTry 'Windows > python compress-it.py help' or 'Linux $ python3 compress-it.py help' for a list of arguments")
    else:
        print("Expected 1 command line argument, but got none.\nTry 'Windows > python compress-it.py help' or 'Linux $ python3 compress-it.py help' for a list of arguments")
       



    
'''Generate your own unicode tables with the code below.'''


def gen_unicode_table(start = 1, stop = 1024, print_out = False, write_to_md = False):
    """
    Generates a table of Unicode characters along with their corresponding Unicode code point,
    decimal, hexadecimal, binary, and octal representations.

    Parameters:
    -----------
    start : int, optional
        The starting Unicode code point to generate the table from (default is 1).
    stop : int, optional
        The stopping Unicode code point to generate the table up to (default is 1024).
    print_out : bool, optional
        If True, prints the generated table in markdown format to the console (default is False).
    write_to_md : bool, optional
        If True, writes the generated table in markdown format to a file named "table.md" (default is False).

    Returns:
    --------
    dict
        A dictionary where the keys are characters and the values are tuples of the following encodings:
        - Unicode Code Point (e.g., "U+0041")
        - Decimal (e.g., 65)
        - Hexadecimal (e.g., "0x41")
        - Binary (e.g., "0b1000001")
        - Octal (e.g., "0o101")

    Notes:
    ------
    - The table is initialized with headers and alignment symbols for markdown table formatting.
    - If `print_out` is True, the table will be printed to the console with markdown syntax.
    - If `write_to_md` is True, the table will be written as a markdown file with UTF-8 encoding.
    - Surrogate pairs and some special characters may not render properly in certain environments.

    Example:
    --------
    # Generate a table for Unicode characters from U+0041 (A) to U+0044 (D) and print it out
    gen_unicode_table(65, 68, print_out=True)

    Output:
    -------
    |Character|Unicode Code Point|Decimal|Hexadecimal|Binary|Octal|
    |:-:|:-:|:-:|:-:|:-:|:-:|
    |A|U+0041|65|0x41|0b1000001|0o101|
    |B|U+0042|66|0x42|0b1000010|0o102|
    |C|U+0043|67|0x43|0b1000011|0o103|
    |D|U+0044|68|0x44|0b1000100|0o104|
    """
        
    table = {"Character" : ("Unicode Code Point", "Decimal", "Hexadecimal","Binary","Octal")}
    table[":-:"] = (":-:",":-:",":-:",":-:",":-:")
    for num in range(start,stop+1):
        if(chr(num) == "\\"):
            char = "\\"
        else:
            char = chr(num)
    
        table[char] =(f"U+{num:04x}",num,hex(num),bin(num), oct(num))

    if(print_out):
        # print(str(table).replace("),","),\n"))
        for char,encodings in table.items():
           print(f"|{char}|{encodings[0]}|{encodings[1]}|{encodings[2]}|{encodings[3]}|{encodings[4]}|")

    if(write_to_md):
        md_table = []
        for char,encodings in table.items():
           md_table.append((f"|{char}|{encodings[0]}|{encodings[1]}|{encodings[2]}|{encodings[3]}|{encodings[4]}|\n").encode("utf-8", errors="replace"))
        
        with open("table.md", "wb") as f:
            f.writelines(md_table)
        

    return table




if __name__ == "__main__":

    gen_unicode_table(print_out=True, write_to_md=True)


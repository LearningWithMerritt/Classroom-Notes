## `Defining a Character`
___
`Characters:`  
> * Basically: a basic unit of information that represents a letter, number, symbol, or control code
> * Specifically: a binary value mapped to a specific symbol as defined by ASCII or UTF

<br>

`American Standard Code for Information Interchange (ASCII)`  
> * a character encoding standard used to represent text in computers and other devices that use text.
> * defines a set of 128 characters, where each character is represented by a unique 7-bit binary number.
> * forms the basis for more extensive character encoding schemes like Unicode.

<br>

`Unicode`   
> *  a universal character encoding standard designed to represent and handle text in most of the world's writing systems.
> * The Unicode standard assigns a unique code point to every character, regardless of platform, program, or language
> * These code points are hexadeximal values prefixed with 'U+'

<br>

`Unicode Transformation Format (UTF)`  
> * a family of character encoding schemes used to represent Unicode characters. 
> * The most common encodings are UTF-8, UTF-16, and UTF-32. These encoding transform unicode code points into sequences of bytes.

<br>

***NOTE: 1 byte equals 8 bits***  
***NOTE: The prefix 0b indicates a binary value***  
***NOTE: The prefix 0x indicates a hexadecimal value***  

<br>

|Encoding Scheme|Size|Range|Character|Encoding|Unicode Code Point|
|:-:|:-:|:-:|:-:|:-:|:-:|
|ASCII|7 bits|128 possible values| "a"|0b01100001| U+0065 |
|UTF-8|1 to 4 bytes|1,112,064 possible values| "a"|0x65|U+0065|
|UTF-16|2 or 4 bytes|1,112,064 possible values| "a"|0x0065|U+0065|
|UTF-32|4 bytes|4,294,967,296 possible values| "a" |0x00000065|U+0065|

For more on Unicode and character encodings: [https://home.unicode.org/](https://home.unicode.org/)

<br>

## Character Examples:
```python
"a"
"b"
"@"
"$"
"1"
"0"
```

**American Standard Code for Information Interchange (ASCII)**
> * 7 bit ASCII defines 128 characters including all alphanumeric characters
> * In many cases this is the only table we will need to interact with characters

In many cases it can help to memorize 3 character values: 0, A, and a:
> * These three numbers allow you to determine the other encodings for all alphanumeric characters.

|Character|Decimal|
|:-:|:-:|
|0| 48|
|A| 65|
|a| 97|

<br>

***NOTE: You may notice that this table does not include all 128 characters, this is because the omitted codes are control codes and have been omitted for simplicity.***

|**Character**|**Unicode Code Point**|**Decimal**|**Hexadecimal**|**Binary**|**Octal**|
|:-:|:-:|:-:|:-:|:-:|:-:|
| SPACE |U+0020|32|0x20|0b100000|0o40|
|!|U+0021|33|0x21|0b100001|0o41|
|"|U+0022|34|0x22|0b100010|0o42|
|#|U+0023|35|0x23|0b100011|0o43|
|$|U+0024|36|0x24|0b100100|0o44|
|%|U+0025|37|0x25|0b100101|0o45|
|&|U+0026|38|0x26|0b100110|0o46|
|'|U+0027|39|0x27|0b100111|0o47|
|(|U+0028|40|0x28|0b101000|0o50|
|)|U+0029|41|0x29|0b101001|0o51|
|*|U+002a|42|0x2a|0b101010|0o52|
|+|U+002b|43|0x2b|0b101011|0o53|
|,|U+002c|44|0x2c|0b101100|0o54|
|-|U+002d|45|0x2d|0b101101|0o55|
|.|U+002e|46|0x2e|0b101110|0o56|
|/|U+002f|47|0x2f|0b101111|0o57|
|**Character**|**Unicode Code Point**|**Decimal**|**Hexadecimal**|**Binary**|**Octal**|
|0|U+0030|48|0x30|0b110000|0o60|
|1|U+0031|49|0x31|0b110001|0o61|
|2|U+0032|50|0x32|0b110010|0o62|
|3|U+0033|51|0x33|0b110011|0o63|
|4|U+0034|52|0x34|0b110100|0o64|
|5|U+0035|53|0x35|0b110101|0o65|
|6|U+0036|54|0x36|0b110110|0o66|
|7|U+0037|55|0x37|0b110111|0o67|
|8|U+0038|56|0x38|0b111000|0o70|
|9|U+0039|57|0x39|0b111001|0o71|
|**Character**|**Unicode Code Point**|**Decimal**|**Hexadecimal**|**Binary**|**Octal**|
|:|U+003a|58|0x3a|0b111010|0o72|
|;|U+003b|59|0x3b|0b111011|0o73|
|<|U+003c|60|0x3c|0b111100|0o74|
|=|U+003d|61|0x3d|0b111101|0o75|
|>|U+003e|62|0x3e|0b111110|0o76|
|?|U+003f|63|0x3f|0b111111|0o77|
|@|U+0040|64|0x40|0b1000000|0o100|
|**Character**|**Unicode Code Point**|**Decimal**|**Hexadecimal**|**Binary**|**Octal**|
|A|U+0041|65|0x41|0b1000001|0o101|
|B|U+0042|66|0x42|0b1000010|0o102|
|C|U+0043|67|0x43|0b1000011|0o103|
|D|U+0044|68|0x44|0b1000100|0o104|
|E|U+0045|69|0x45|0b1000101|0o105|
|F|U+0046|70|0x46|0b1000110|0o106|
|G|U+0047|71|0x47|0b1000111|0o107|
|H|U+0048|72|0x48|0b1001000|0o110|
|I|U+0049|73|0x49|0b1001001|0o111|
|J|U+004a|74|0x4a|0b1001010|0o112|
|K|U+004b|75|0x4b|0b1001011|0o113|
|L|U+004c|76|0x4c|0b1001100|0o114|
|M|U+004d|77|0x4d|0b1001101|0o115|
|N|U+004e|78|0x4e|0b1001110|0o116|
|O|U+004f|79|0x4f|0b1001111|0o117|
|P|U+0050|80|0x50|0b1010000|0o120|
|Q|U+0051|81|0x51|0b1010001|0o121|
|R|U+0052|82|0x52|0b1010010|0o122|
|S|U+0053|83|0x53|0b1010011|0o123|
|T|U+0054|84|0x54|0b1010100|0o124|
|U|U+0055|85|0x55|0b1010101|0o125|
|V|U+0056|86|0x56|0b1010110|0o126|
|W|U+0057|87|0x57|0b1010111|0o127|
|X|U+0058|88|0x58|0b1011000|0o130|
|Y|U+0059|89|0x59|0b1011001|0o131|
|Z|U+005a|90|0x5a|0b1011010|0o132|
|**Character**|**Unicode Code Point**|**Decimal**|**Hexadecimal**|**Binary**|**Octal**|
|[|U+005b|91|0x5b|0b1011011|0o133|
|\\ |U+005c|92|0x5c|0b1011100|0o134|
|]|U+005d|93|0x5d|0b1011101|0o135|
|^|U+005e|94|0x5e|0b1011110|0o136|
|_|U+005f|95|0x5f|0b1011111|0o137|
|`|U+0060|96|0x60|0b1100000|0o140|
|**Character**|**Unicode Code Point**|**Decimal**|**Hexadecimal**|**Binary**|**Octal**|
|a|U+0061|97|0x61|0b1100001|0o141|
|b|U+0062|98|0x62|0b1100010|0o142|
|c|U+0063|99|0x63|0b1100011|0o143|
|d|U+0064|100|0x64|0b1100100|0o144|
|e|U+0065|101|0x65|0b1100101|0o145|
|f|U+0066|102|0x66|0b1100110|0o146|
|g|U+0067|103|0x67|0b1100111|0o147|
|h|U+0068|104|0x68|0b1101000|0o150|
|i|U+0069|105|0x69|0b1101001|0o151|
|j|U+006a|106|0x6a|0b1101010|0o152|
|k|U+006b|107|0x6b|0b1101011|0o153|
|l|U+006c|108|0x6c|0b1101100|0o154|
|m|U+006d|109|0x6d|0b1101101|0o155|
|n|U+006e|110|0x6e|0b1101110|0o156|
|o|U+006f|111|0x6f|0b1101111|0o157|
|p|U+0070|112|0x70|0b1110000|0o160|
|q|U+0071|113|0x71|0b1110001|0o161|
|r|U+0072|114|0x72|0b1110010|0o162|
|s|U+0073|115|0x73|0b1110011|0o163|
|t|U+0074|116|0x74|0b1110100|0o164|
|u|U+0075|117|0x75|0b1110101|0o165|
|v|U+0076|118|0x76|0b1110110|0o166|
|w|U+0077|119|0x77|0b1110111|0o167|
|x|U+0078|120|0x78|0b1111000|0o170|
|y|U+0079|121|0x79|0b1111001|0o171|
|z|U+007a|122|0x7a|0b1111010|0o172|
|**Character**|**Unicode Code Point**|**Decimal**|**Hexadecimal**|**Binary**|**Octal**|
|{|U+007b|123|0x7b|0b1111011|0o173|
|\||U+007c|124|0x7c|0b1111100|0o174|
|}|U+007d|125|0x7d|0b1111101|0o175|
|~|U+007e|126|0x7e|0b1111110|0o176|

<br>
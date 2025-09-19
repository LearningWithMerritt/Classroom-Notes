# `Data Encoding: Hexadecimal`
___

<br>

# `The Decimal System (Base 10)`
The decimal system, also known as the base-10 system, is a positional numeral system that uses ten distinct digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9.     
> * Each digit's position in a number determines its value, which is a power of 10. 
> * The decimal system is the most widely used numeral system globally, especially for everyday counting and arithmetic.   
> * It is believed to be so prevalent due to the fact that humans have ten fingers, making it a natural choice for counting and calculations.  

*deci- from the latin decimus meaning "tenth"*

<br>

## `The Decimal System uses 10 digits`
10 Digits: 0 to 9 → (0,1,2,3,4,5,6,7,8,9) 

<br>

## `Places in the decimal (base 10) system`

||||||||||||||||||
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|10,000,000|1,000,000|100,000|10,000|1,000|100|10|1|**.**|1/10|1/100|1/1000|1/10000|1/100,000|1/1,000,000|1/10,000,000|
|10<sup>7</sup>|10<sup>6</sup>|10<sup>5</sup>|10<sup>4</sup>|10<sup>3</sup>|10<sup>2</sup>|10<sup>1</sup>|10<sup>0</sup>|**.**|10<sup>-1</sup>|10<sup>-2</sup>|10<sup>-3</sup>|10<sup>-4</sup>|10<sup>-5</sup>|10<sup>-6</sup>|10<sup>-7</sup>|

Example:

156 meaning 1 hundred, 5 tens, and 6 ones

This is the number system we are all used to using, but it is not the only number system. 

<br>

___

<br>

# `Floating Points (aka decimal points)`

* Floating points are used to seperate the whole part of a number from the fractional part of the number.
* Floating Points are generally refered to as decimal points, however this can cause some confusion as the use of the term results in an incorrect meaning of "decimal number"

**"Decimal number" is a reference to any number in the base 10 system and is not limited to only numbers that contain a floating point.** 

Therefore when we refer to numbers with a floating point, they will be called floating point numbers or "floats".


<br>

___

<br>

# `The Hexadecimal System (Base 16)`
The hexadecimal system, also known as base-16, is a positional numeral system that uses 16 distinct symbols to represent values.  
> * These symbols include the digits 0 through 9 to represent values 0 to 9, and the letters A through F to represent values 10 to 15.

<br>

## `Structure of the Hexadecimal System:`
* Base: The system is base-16, meaning each digit's place represents a power of 16.  
* Digits: The digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.  
>   * A represents 10.  
>   * B represents 11.  
>   * C represents 12.  
>   * D represents 13.  
>   * E represents 14.  
>   * F represents 15.  

`2 hexadecimal digits equals 1 byte --> #00 or 0x00`

*Greek hexa-  meaning “six”*  
*deci- from the latin decimus meaning “tenth”*

<br>

## `Hexadecimal uses 16 digits`
16 digits: 0 to 9 and A to F -->(0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F)  
The letters can be uppercase or lowercase

|Hexadecimal|0|1|2|3|4|5|6|7|8|9|`A`|`B`|`C`|`D`|`E`|`F`|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Decimal|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|

<br>

## `Hexadecimal Notation (#, 0x, 0h, $, &H)`
You will often see hexadecimal numbers written with a `0x`, `#`, `0h`, `$` or  `&H`  in front of them. 

| Prefix | Usage Description                                        | Example   |
|--------|----------------------------------------------------------|-----------|
| `0x`     | Used in many programming languages like C, C++, Python, and JavaScript | `0x1A3F`  |
| `#`      | Used in some variations of assembly or macro languages    | `#1A3F`   |
| `0h`     | Occasionally used in assembly languages or other specific contexts | `0h1A3F`  |
| `$`      | Common in older assembly languages and some dialects of BASIC | `$1A3F`   |
| `&H`     | Used in Visual Basic and similar languages                | `&H1A3F`  |




> * Python uses “0x”

## Examples

|Decimal|Hexadecimal|Hexadecimal|
|:-:|:-:|:-:|
|0|#00|0x00|
|1|#01|0x01|
|5|#05|0x05|
|10|#0a|0x0a|
|42|#2a|0x2a|
|100|#64|0x64|
|128|#80|0x80|
|255|#FF|0xFF|


<br>

___

<br>

# `Converting from Decimal to Hexadecimal`

Steps:
1. Divide the decimal number by 16 and write down the remainder.
1. Use the quotient from the previous division, divide by 16, and write down the remainder. 
1. Convert the remainder to the letter if necessary.
1. Repeat until the quotient is 0, writing the remainders from right to left. 


example:    
## `Convert decimal 24 to hexadecimal.`   
24 / 16 = 1 remainder 8  → 8  
1 / 16 = 0 remainder 1 → 18  

Decimal 24 in hexadecimal is #18 or 0x18  


## `Convert decimal 255 to hexadecimal. `  
255 / 16 = 15 remainder 15 → F  
15 / 16 = 0 remainder 15 → FF  

Decimal 255 in hexadecimal is #FF or 0xFF



<br>

___

<br>

# `Converting Hexadecimal to Decimal`
Steps:
1. Starting from the right multiply the digit by 16<sup>0</sup>.
1. Move to the left and multiply the digit by 16<sup>1</sup>.
1. Repeat while increasing the power of 16 by 1 until you have reached the end of the hexadecimal number. 
1. Add all of the answers together. 


## `Convert 0xA3 to decimal.`

|( 3 * 16<sup>0</sup> )| + |( A * 16<sup>1</sup> )| = 163|
|:-:|:-:|:-:|:-:|
|3| + |160|  = 163| 

0xA3 in decimal is 163


## `Convert 0x1C90 to decimal`
|( 0 * 16<sup>0</sup> )| + |( 9 * 16<sup>1</sup> )| + |( C * 16<sup>2</sup> )| + |( 1 * 16<sup>3</sup> )|= 7312|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|0|+|144|+|3072|+|4096| = 7312|

0x1C90 in decimal is 7312






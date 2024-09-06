
# Data Encoding: Binary
---

# `The Decimal System (Base 10)`
> * The decimal system, also known as the base-10 system, is a positional numeral system that uses ten distinct digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9.     
> * Each digit's position in a number determines its value, which is a power of 10.The decimal system is the most widely used numeral system globally, especially for everyday counting and arithmetic.   
> * It is believed to be so prevalent due to the fact that humans have ten fingers, making it a natural choice for counting and calculations.  

*deci- from the latin decimus meaning "tenth"*

## The Decimal System uses 10 digits
10 Digits: 0 to 9 → (0,1,2,3,4,5,6,7,8,9) 

## Places in the decimal (base 10) system

||||||||||||||||||
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|10,000,000|1,000,000|100,000|10,000|1,000|100|10|1|**.**|1/10|1/100|1/1000|1/10000|1/100,000|1/1,000,000|1/10,000,000|
|10<sup>7</sup>|10<sup>6</sup>|10<sup>5</sup>|10<sup>4</sup>|10<sup>3</sup>|10<sup>2</sup>|10<sup>1</sup>|10<sup>0</sup>|**.**|10<sup>-1</sup>|10<sup>-2</sup>|10<sup>-3</sup>|10<sup>-4</sup>|10<sup>-5</sup>|10<sup>-6</sup>|10<sup>-7</sup>|

Example:

156 meaning 1 hundred, 5 tens, and 6 ones

This is the number system we are all used to using, but it is not the only number system. 
---

# `Floating Points (aka decimal points)`

* Floating points are used to seperate the whole part of a number from the fractional part of the number.
* Floating Points are generally refered to as decimal points, however this can cause some confusion as the use of the term results in an incorrect meaning of "decimal number"

**"Decimal number" is a reference to any number in the base 10 system and is not limited to only numbers that contain a floating point.** 

Therefore when we refer to numbers with a floating point, they will be called floating point numbers or "floats".

---

# `The Binary System (Base 2)`
> * The binary system, also known as the base-2 numeral system, is a method of representing numbers using only two symbols: 0 and 1. 
> * It is the foundational system used in computing and digital electronics because it aligns naturally with the binary logic of digital circuits, which have two states: on (1) and off (0).

## Structure of the Binary System:
> * Base: The system is base-2, meaning each digit's place represents a power of 2.
> * Digits: The digits are 0 and 1.
>   * 0 represents the value zero.
>   * 1 represents the value one.

*latin bi- meaning "twice, double or two"*

## The binary system uses 2 digits 
2 Digits: 0 or 1 → (0,1)

## Places in the Binary (base 2) System

||||||||||||||||||
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|128|64|32|16|8|4|2|1|**.**|1/2|1/4|1/8|1/16|1/32|1/64|1/128|
|2<sup>7</sup>|2<sup>6</sup>|2<sup>5</sup>|2<sup>4</sup>|2<sup>3</sup>|2<sup>2</sup>|2<sup>1</sup>|2<sup>0</sup>|**.**|2<sup>-1</sup>|2<sup>-2</sup>|2<sup>-3</sup>|2<sup>-4</sup>|2<sup>-5</sup>|2<sup>-6</sup>|2<sup>-7</sup>|

> As humans we easily understand the decimal system, but computers operate in bits, each bit with two states on or off, powered or unpowered, 0 or 1. 

[**bit**]: the smallest unit a data a computer can process or store. Represented as a 0/1, yes/no, True/False, or on/off
* 1 bit of binary data → 0
* 1 bit of binary data → 1

[**byte**]: a unit consisting of 8 bits of binary data.
* 8 bits or 1 byte of binary data → 0000 0000
* 8 bits or 1 byte of binary data → 0010 1010

## Examples

|decimal|binary (bits)|binary (byte)|
|:-:|:-:|:-:|
|0|0|0000 0000|
|1|1|0000 0001|
|5|101|0000 0101|
|10|1010|0000 1010|
|42|101010|0010 1010|
|100|1100100|0110 0100|
|128|1000000|1000 0000|
|255|11111111|1111 1111|

---

# `Converting decimal to binary`

Steps:
1. Divide the decimal number by 2 and write down the remainder.
1. Use the quotient from the previous division, divide by 2, and write down the remainder. 
1. Repeat until the quotient is 0, writing the remainders from right to left. 


## Convert decimal 13 to binary.
|||
|:-:|:-:| 
|13 / 2  =  6 remainder 1|→ 1|  
|6 / 2 =  3 remainder 0|→ 01|  
|3 / 2 =  1 remainder 1|→ 101|  
|1 / 2 =  0 remainder 1|→ 1101|  

**13 in binary is → 1101 or 0000 1101**

---

# `Converting binary to decimal`

Steps:
1. Find the leftmost bit equal to 1 and multiply by 2, then add the next leftmost digit. 
1. Take the answer and multiply by 2, then add the next leftmost digit. 
1. Repeat until you are at the end of the binary number.




## Convert binary 101 to decimal.  
101 → 1 * 2 + 0 = 2  
101 →  2 * 2 + 1 = 5   

101 in decimal is → 5  

Convert 1101 to decimal  
1 * 2 + 1 = 3  
3 * 2 + 0 = 6  
6 * 2 + 1 = 13  

1101 in decimal is → 13

---

# `First 32 Powers of 2`
| Power (n) | 2^n            |
|-----------|----------------|
| 0         | 1              |
| 1         | 2              |
| 2         | 4              |
| 3         | 8              |
| 4         | 16             |
| 5         | 32             |
| 6         | 64             |
| 7         | 128            |
| 8         | 256            |
| 9         | 512            |
| 10        | 1,024          |
| 11        | 2,048          |
| 12        | 4,096          |
| 13        | 8,192          |
| 14        | 16,384         |
| 15        | 32,768         |
| 16        | 65,536         |
| 17        | 131,072        |
| 18        | 262,144        |
| 19        | 524,288        |
| 20        | 1,048,576      |
| 21        | 2,097,152      |
| 22        | 4,194,304      |
| 23        | 8,388,608      |
| 24        | 16,777,216     |
| 25        | 33,554,432     |
| 26        | 67,108,864     |
| 27        | 134,217,728    |
| 28        | 268,435,456    |
| 29        | 536,870,912    |
| 30        | 1,073,741,824  |
| 31        | 2,147,483,648  |
| 32        | 4,294,967,296  |



# `Algorithm Efficiency`

<br>

___

<br>

Covered in this file:
1. [`Reasonable Time`](#reasonable-time)
1. [`Big-O Notation`](#big-o-notation)
    1. [`Constant Time`](#constant-time)
    1. [`Logarithmic Time`](#logarithmic)
    1. [`Linearithmic Time`](#linearithmic)
    1. [`Polynomial: Linear Time`](#polynomial-linear-time)
    1. [`Polynomial: Quadratic Time`](#polynomial-quadratic-time)
    1. [`Polynomial: Cubic Time`](#polynomial-cubic-time)
    1. [`Exponential Time`](#exponential-time)
    1. [`Factorial Time`](#factorial-time)




<br>

___

<br>


# `Reasonable Time`
When an algorithm runs in `reasonable time` it means that the algorithm has `constant`, `logarithmic`,`linearithmic` or `polynomial time complexity`. 

<br>

A `polynomial` is a mathematical expression involving a sum of powers of a variable (usually written as n) multiplied by coefficients.

<br>

Generally polynomial time can be represented as n<sup>k</sup>.
Where:
* `n` is the size of the input
* `k` is how the fast the number of steps grows

<br>

`Polynomial Time Equation:`
```
T(n) <= an**k + b
```
Where:
* `n` is the size of the input (ie. number of inputs)
* `T(n)` is the number of steps, operation, or iterations necessary to complete the algorithm
* `a` represents a constant coefficient that scales `n`
* `b` represents the number of steps taken regardless of input size
* `k` represents how fast the the number of steps grows as `n` increases

<br>

`Focusing on the n**k term is important`

<br>

Constant and Polynomial Complexity
| Time Complexity | Name       | Description                                  | Example Use Case                             |
|------------------|------------|----------------------------------------------|----------------------------------------------|
| O(1)             | Constant   | Time stays the same regardless of input size | Accessing an array element                   |
| O(n)             | Linear     | Time grows directly with input size          | Iterating through a list                     |
| O(n²)            | Quadratic  | Time grows with the square of input size     | Comparing all pairs in a list (nested loops) |
| O(n³)            | Cubic      | Time grows with the cube of input size       | Naive matrix multiplication                  |
| O(n^k)           | Polynomial | Time grows with the k-th power of input size | Some dynamic programming algorithms          |


<br>

[Back To Top](#algorithm-efficiency)

___

<br>

# `Big-O Notation`
`Big-O Notation` is a way to describe how the running time or memory requirements of an algorithm grow as the size of the input increases.
* Big-O provides an upper bound on the growth rate of an algorithm
* Think of it as a 'worst case' for how fast time or memory grows
* Focuses on the dominant term, because constant factors don't affect growth rate.

<br>


| Time Complexity | Name | Efficiency | Description  | Example Use Case|
|-|-|-----|--|--|
| O(1) | Constant| 🟢 Best  | Execution time doesn’t depend on input size| Accessing an array element, basic math operation |
| O(log n)| Logarithmic| 🟢 Great | Grows very slowly as input increases | Binary search in a sorted array|
| O(n) | Linear  | 🟢 Good  | Grows proportionally with input size | Looping through an array |
| O(n log n) | Linearithmic  | 🟡 Decent| Efficient, slightly slower than linear  | Merge sort, heapsort  |
| O(n²)| Quadratic  | 🔴 Slower| Time grows with the square of input size| Comparing all pairs in a list (nested loops)  |
| O(n³)| Cubic| 🔴 Worse | Time grows with the cube of input size  | Matrix multiplication (naive approach)  |
| O(n^k)  | Polynomial  | 🔴 Varies| General polynomial time with degree k| Some dynamic programming algorithms  |
| O(2^n)  | Exponential| ❌ Very Bad | Doubles with each additional input| Brute-force solutions, subsets |
| O(n!)| Factorial  | ❌ Worst | Grows faster than exponential  | Brute-force permutations, puzzle solving|


<br>

## `Constant Time`


### `O(1)`
Python Example Accessing a List Element:
```python
def get_elem(lst,i):
    return lst[i]
```
In the snippet above, regardless of the input size (the list size) the number of steps remains unchanged. 

<br>

[Back To Top](#algorithm-efficiency)

___

<br>

## `Logarithmic`

### `O(log n)`
Python Example Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```
Each step halves the number of items to search through.
For an input of size n, the worst case:
* Each step halves the size n of the input
* The base of the log is 2, because we half every time
Thus `log n`
NOTE: The base does not matter in Big-O notation, because the base just adds a constant scalar to the value. 


<br>

NOTE:

Changing the base of a log follows the format:
* Converting from log base b to log base k
$$
\log_b(n) = \frac{\log_k(n)}{\log_k(b)}
$$

Thus 
$$
\log_b(n) = {\log_k(n)}*\frac{1}{\log_k(b)}
$$

<br>

Since the fraction below is just a constant scalar value it is ignored in Big-O notation
$$
\frac{1}{\log_k(b)}
$$


<br>

[Back To Top](#algorithm-efficiency)

___

<br>

## `Linearithmic`

### `O(n log n)`

Python Example: Merge Sort
```python
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] < right[0] else right.pop(0))
    result += left + right
    return result
```
In the worst case, for an input of size n:
* For each step you divide the list in half --> log n
* For each step you merge all n elements --> n
Thus  n * log n --> n log n

<br>

[Back To Top](#algorithm-efficiency)

___

<br>

## `Polynomial: Linear Time`

### `O(n)`
Python Example Iterating Through a List:
```python
def printlist(lst):
    for elem in lst:
        print(elem)
```
In the snippet above the number of steps is equal to the size of the input.
* 1 loop for each element in the list.

In the worst case, for every input of size n
* The loop runs n times


<br>

[Back To Top](#algorithm-efficiency)

___

<br>

## `Polynomial: Quadratic Time`

### `O(n^2)`
Python Example Bubble Sort
```python
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
```
This algorithm uses 2 nested loops
In the worst case, for every input of size n  
* the outer loop loops n times
* the inner loop loops a maximum of n times
Thus n * n --> n<sup>2</sup>

<br>

[Back To Top](#algorithm-efficiency)

___

<br>

## `Polynomial: Cubic Time`

### `O(n^3)`
Python Example Matrix Multiplication
```python
def matrix_multiply(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
```
This algorithm uses 3 nested loops.
In the worst case, for every input of size n
* The outer loop runs a maximum of n times
* The middle loop runs a maximum of n times
* The inner loop runs a maximum of n times
Thus n * n * n --> n<sup>3</sup>

<br>

[Back To Top](#algorithm-efficiency)

___

<br>

## `Exponential Time`

### `O(2^n)`
Python Example Recursive Fibonacci
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
For an input of size n
* Each step calls 2 more steps --> 2<sup>n</sup>

This is exponential growth, and the opposite of logarithmic.<br>

`Exponential growth is considered inefficient.`

<br>

[Back To Top](#algorithm-efficiency)

___

<br>

## `Factorial Time`

### `O(n!)`
Python Example Permutations
```python
def permutations(lst):
    if len(lst) == 0:
        return [[]]  
    result = []
    for i in range(len(lst)):
        current = lst[i]
        remaining = lst[:i] + lst[i+1:]
        for p in permutations(remaining):
            result.append([current] + p)
    return result
```
For an input of size n the number permutations is n!

A `permutation` is an arrangement of all the elements in a set or list in a specific order.

<br>

`Factorial Time is considered very inefficient.`


<br>

[Back To Top](#algorithm-efficiency)

___

<br>

*Created and maintained by Mr. Merritt*
# Attendance Array

## Three patterns
## Where we have to re-iterate the Array again and again we can use this! 
- "Attendce Array with Boolean value" use this method when you want to solve Pangram
- "Attenance Array with Frequencies"
- "Attendace Array with indices"

## Bit Manipulation:

- Decimal -> 0-9 and base is 10
- Binary -> 0 1 and base is 2
- Octal -> 0-7 and base 8
- Hexa decimal - 0-9, A-F - base is 16

## Bitwise operators:

- OR - Ans is 1 if any operand is 1, else 0

- AND - Ans is 0 if any operand is 0, else 1

- NOT - Ans is 1 if any operand is 0, else 0

- XOR - Ans is 1 if both the operands are different, else 0

- set bit - If the bit is 1 

- unset bit - If the bit is 0

- Toggle bit - reverse the bit 

## Properties:

- x & 0 = 0 
- x | 0 = x
- x ^ 0 = x
- x & a1 = x  i.e assume a1 is 1111
- x | a1 = a1
- x ^ a1 = NOT x or toggle of x
- x & x = x
- x | x = x
- x ^ x = 0
1. Commutative = A AND b = B AND A, A | B = B | A, A ^ B = B ^ A
2. Associative = A AND (B AND C) = (A AND B ) AND C
3. left shift = x << k ===> x * 2 ^k
4. Right shift = x / 2 ^k

## Q1. Check if the number is even or ODD using bit manipulation? 

### Explanation: 

- We need to check whether the LSB is 0 or 1. If it is 0, it is even number and if it is 1 number it is 1. 
- In order to get this we need to do bit masking with LSB and do the bitwise AND operation

Why we need to check the LSB is 0 or 1? 

- Because when you convert the decimal to binary LSB bit has the capability to change number to even or odd by adding 1. 
 For an example if it  0 x 2^0 = 0 Even and 1 x 2^0 = 1 which will result the number to be odd. 

***Note*** - Bitwise operator is powerful than the any arithmatic operator


![EvenOrODD](<Screenshot 2025-11-30 at 10.04.09 PM.png>)

## Q2 Check if the kth bit from the end is set or not ? 
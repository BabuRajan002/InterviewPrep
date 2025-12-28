# Bit Manipulation

- ## 11:10 AM Unique path -- > Leetcode

- "Doing nogthing is also one way" - Dynmaic program theory

- Dynamic program is based on recursion

```
#Step1: dp[i][j] - Stores/represenets the number of unique paths to reach (n-1, m-1) from i, j

# Step2: Cells were filled in the reverse manner: Last column got filled firstly.

#Last col:

#Fill the last row

## row - 2

## 
```
Time complexity is O(N2)

## 11:40 AM Unique Paths II with Lions in th random cells.

-  #Step1: dp[i][j] - Stores/represenets the number of unique paths to reach (n-1, m-1) cell from i, j considering there are obstacles in the path.

- Step2: Take number of rows and cols. 

- Step3: Check whether cells [0][0] or at the destination any obstacle is there. if so return 0

- Step4: Initialize the dp matrix

- Step5: Initialize boolean to track lion in row or col 

- Step6: Traverse the last row 
         1 . Is there a lion? - Check it in the current cell in the original matrix grid
         2. Have you seen a lion ahead? - Accordingly toggle the Bool flag

- Step7: Traverse the last col
         1 . Is there a lion? - Check it in the current cell in the original matrix grid
         2. Have you seen a lion ahead? - Accordingly toggle the Bool flag

- Step8: Traverse the row and col
         1. If there is no lion only do something


## 12:25 Bit Manipulation:

- Bit is set - means there is '1' over there.
- ***ODD Number*** - 0th bit is set
- ***Even*** - 0th bit zero

## `AND` Operator `&` is bitwise operator.

```
1 & 1 = 1
0 & 0 = 0 
1 & 0 = 0
0 & 1 = 0
```

## `OR`Operator `|` is bitwise OR operator. If any of the bit is 1 the its 1

```
1 | 1 = 1
0 | 0 = 0 
1 | 0 = 1
0 | 1 = 1

```

## `XOR` operator `^` is bitwise XOR operator. 

```
1 ^ 1 = 0
0 ^ 0 = 0 
1 ^ 0 = 1
0 ^ 1 = 1
```

## `<<` left shift operator
- Every bit will be shifted to left side
- Example: 2 ---> 00000010 << 00000100
- Ex: `1<<2 = 4` --> Left shift 2 by 1 
- Ex: `1<<5 = 10`--> Left shift 5 by 1   

## `>>` right shift operator

- Every bit will be shifted to right side.
- Ex: `1 >> 5 = 2 ` Shift by 1 bit 

## Tricks: 

- How to set a bit at a given position? for example 5th position
  - `1 << 5`

- When the question is to check whether a given bit is set or not, do with bitwise AND. 

# 1:33 PM Solved Single Number problem in Leetcode.

- ***Intuition*** - Do XOR between all the numbers and which cancel the same number and the odd one will be present.

# 1:38 PM Solved Single Number II





     






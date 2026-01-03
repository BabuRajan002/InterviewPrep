# Arrays & Maths II:

## 11:08 AM Missing Number ---> 268.Leetcode Important Problems

- Brute force - - > Sorting and Compare with the index Space O(n log n) and TC: 

- Apply the sum of N natural number logic using this formula n * (n + 1) / 2 

- Calculate the Sum of N Natural numbers and subtract with each element by traversing. 

=============================================================================================================
## 11:21 Majority of elements ----> Very Important Problem

## Problem:

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

### 11:40 AM Brute Force Solution Below:
- Create the Freq array
- Loop through the array and count the freq and update it
- Compare the count with n/2 as mentioned in the question.

***Note: He said we can solve the problem after learning the Hash Map!***

## Why should we use the Brute force method ?
- TRICK: Basically to waste the time during the Interview ***:):)***

## Does every problem has Brute, Better, Best approaches? 

- Not in Graphs, Dynamic Programming etc..! No Brute force! 
- Direct solution! 

## 12:06 PM Optimized Approach for Majority elements:

- Initialize the variable `element = INT_MIN` which are not part of elements! 
- Count 0 Means I dont have any assumed Majority element
- When the count is 1 update the element in element variable 

=============================================================================================================

## 12:13 PM 238. Product of Array Except Self ---> Leetcode

- Find the total multiplication and divide it by traversing - - > Not preferred

- Can be solved using Prefix Array and Suffix array

- left to right --> Prefix [0 to i-1]
- Right to left --> Suffix [n-1 to i + 1]

- Calculate the prefix array and suffix array

- Then calculate the value for the i th index by multuplying pre *suff

***Note: If there is no elements present in left or right initialize it with 1***

- Showed the optimized solution


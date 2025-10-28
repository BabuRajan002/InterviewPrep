# 66. Plus One
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.
from typing import List

class Solution:
    def __init__(self, digits) -> List[int]:
        self.digits = digits
    
    def plusOne(self):
        large_num = "".join([str(num) for num in self.digits])
        number = int(large_num) + 1
        return [int(num) for num in str(number)]

if __name__ == "__main__":
    large_num = Solution([9])
    print(large_num.plusOne())

# #Leetcode version
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         large_num = "".join([str(num) for num in digits])
#         number = int(large_num) + 1
#         return [int(num) for num in str(number)]
        
        

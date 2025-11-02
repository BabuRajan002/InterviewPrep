# 136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def __init__(self, nums):
        self.nums = nums
    
    def singleNumber(self):
        xor = 0
        for num in self.nums:
            xor ^= num
        return xor

            
if __name__ == "__main__":
    single_num = Solution([2,2, 1, 1, 4])
    print(single_num.singleNumber())

# #Leetcode version
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#          xor = 0
#          for num in nums:
#             xor ^= num
#          return xor
        
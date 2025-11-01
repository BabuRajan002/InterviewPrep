# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.
from typing import List

class Solution:
    def __init__(self, nums):
        self.nums = nums
        
    def moveZeroes(self):
        left = 0
        for right in range(len(self.nums)):
            if self.nums[right] != 0:
                self.nums[left], self.nums[right] = self.nums[right], self.nums[left]
                left += 1           
        print(self.nums)

if __name__ == "__main__":
    move_zero = Solution([0,1,0,3,12])
    move_zero.moveZeroes()


         
# 35. Search Insert Position

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.
from typing import List

class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
        
    def searchInsert(self):
        for i in range(len(self.nums)+1):
            if self.nums[i] == self.target:
                return i
            elif self.nums[i] > self.target:
                return i
            else:
                return len(self.nums)
            
if __name__ == "__main__":
    ins_ind = Solution([1,3,5,6], 2)
    print(ins_ind.searchInsert())               

# #Leetcode version
# class Solution:
#     def searchInsert(self, nums, target):
#         left, right = 0, len(nums)  # right is exclusive
#         while left < right:
#             mid = (left + right) // 2
#             if nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid
#         return left

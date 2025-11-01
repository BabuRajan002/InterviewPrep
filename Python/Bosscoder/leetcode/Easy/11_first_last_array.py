# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
        
    def searchRange(self):
        result = []
        nums = self.nums
        target = self.target
        if target in nums:
         for i in range(len(nums)):
            if target == nums[i]:
                result.append(i)
        else:
           return [-1,-1]
        return result
if __name__ == "__main__":
    first_last = Solution([5,7,7,8,8,10],8)
    print(first_last.searchRange())


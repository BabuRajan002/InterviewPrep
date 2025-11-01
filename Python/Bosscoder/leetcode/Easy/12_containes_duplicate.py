# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
class Solution:
    def __init__(self, nums):
        self.nums = nums
        
    def containsDuplicate(self):
        if len(set(self.nums)) < len(self.nums):
            return True
        else:
            return False

if __name__ == "__main__":
    dup = Solution([1,2,3,4,4])
    print(dup.containsDuplicate())


# #Leetcode verison:

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         if len(set(nums)) < len(nums):
#             return True
#         else:
#             return False 
        
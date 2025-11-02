# Q15. Majority Element
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
from collections import Counter

class Solution:
    def __init__(self, nums):
        self.nums = nums
    
    def majorityElement(self):
        count = Counter(self.nums)
        maxvalue = max(count.values())
        for key, val in count.items():
            if val == maxvalue:
                return key          
            

if __name__ == "__main__":
    maj = Solution([2,2,1,1,1,2,2])
    print(maj.majorityElement())

# #Leetcode

# from collections import Counter
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = Counter(nums)
#         maxval = max(count.values())
#         for key, val in count.items():
#             if val == maxval:
#                 return key

        
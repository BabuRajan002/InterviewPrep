# 349. Intersection of Two Arrays
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

from typing import List

class Solution:
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
    
    def intersection(self):
        set1 = set(self.nums1)
        set2 = set(self.nums2)
        interset = set1.intersection(set2)
        return list(interset)

if __name__ == "__main__":
    inter = Solution([1,2,2,1], [2,2])
    print(inter.intersection())

# #Leetcode version

# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         set1 = set(nums1)
#         set2 = set(nums2)
#         interset = set1.intersection(set2)
#         return list(interset)




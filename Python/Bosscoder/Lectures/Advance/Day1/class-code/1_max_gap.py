# class Solution:
#     def maximumGap(self, nums: List[int]) -> int:
#         mx = 0
#         nums.sort()
#         i = 1
#         n = len(nums) 
#         if n < 2:
#             return 0       
#         for i in range(n):
#             diff = nums[i] - nums[i-1]
#             if diff > mx:
#                 mx = diff
#             i += 1
#         return mx 
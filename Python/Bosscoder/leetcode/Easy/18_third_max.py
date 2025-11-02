# Q28. Third Maximum Number
# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

class Solution:
    def __init__(self, nums):
        self.nums = nums
    
    def thirdMax(self):
        nums = list(set(self.nums))
        if len(nums) < 3: 
           return max(self.nums)
        i = 0
        while i < 3:
            number = max(nums)
            nums.remove(number)
            i += 1
        return number        



if __name__ == "__main__":
    max_num = Solution([1,1,2])
    print(max_num.thirdMax())

# #Leetcode version
# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#         nums = set(nums)
#         if len(nums) < 3:
#             return max(nums)
#         else:
#             nums.remove(max(nums))
#             nums.remove(max(nums))
#             return max(nums)


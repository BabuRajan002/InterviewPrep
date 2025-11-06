# Q46. Maximum Product of Three Numbers
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

class Solution:
    def __init__(self, nums):
        self.nums = nums
    
    def maximumProduct(self):
        nums = self.nums
        nums.sort()
        # start_index = max(0, len(nums)-3)
        # result = 1
        # for i in range(start_index, len(nums)):
        #     result = result * nums[i]
        # return result
        return max(nums[-1] * nums[-2] * nums[-3],
                   nums[0] * nums[1] * nums[-1])




if __name__ == "__main__":
    product_res = Solution([-100,-98,-1,2,3,4])
    print(product_res.maximumProduct())


# #Leetcode version:
# class Solution:
#     def maximumProduct(self, nums: List[int]) -> int:
#        nums.sort()
#        return max(nums[-1] * nums[-2] * nums[-3],
#                    nums[0] * nums[1] * nums[-1])
        
# 268. Missing Number

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

class Solution:
    def __init__(self, nums):
        self.nums = nums
        
    def missingNumber(self):
        len_n = len(self.nums)
        for i in range(len_n+1):
            if i not in self.nums:
                return i

if __name__ == "__main__":
    missing = Solution([9,6,4,2,3,5,7,0,1])
    print(missing.missingNumber())


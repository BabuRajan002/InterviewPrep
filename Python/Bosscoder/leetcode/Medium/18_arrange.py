# 2149. Rearrange Array Elements by Sign

# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

# You should return the array of nums such that the array follows the given conditions:

# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

class ReArrangePodNeg:
    def __init__(self, nums):
        self.nums = nums
    
    def solve(self):
        nums = self.nums
        n = len(nums)
        ans = [0] * n
        posIndex = 0
        negIndex = 1

        for i in range(n):
            if nums[i] < 0:
                ans[negIndex] = nums[i]
                negIndex += 2

            else:
                ans[posIndex] = nums[i]
                posIndex += 2
        
        return ans

if __name__ == "__main__":
    arrange = ReArrangePodNeg([3,1,-2,-5,2,-4])
    print(arrange.solve())
# 228. Summary Ranges
# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:
# "a->b" if a != b
# "a" if a == b

class Solution:
    def __init__(self, nums):
        self.nums = nums
    
    def summaryRanges(self):
        i = 0
        sum_range = []

        while i < len(self.nums):
            start = self.nums[i]

            while i < len(self.nums)-1 and self.nums[i] + 1 == self.nums[i+1]:
                i += 1
            if start != self.nums[i]:
                sum_range.append(f"{start} -> {self.nums[i]}")
            else:
                sum_range.append(start)
            i += 1

        return sum_range

if __name__ == "__main__":
    summary = Solution([0,1,2,4,5,7])
    print(summary.summaryRanges())





        

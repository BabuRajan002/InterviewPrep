# 2341. Maximum Number of Pairs in Array
# You are given a 0-indexed integer array nums. In one operation, you may do the following:
# Choose two integers in nums that are equal.
# Remove both integers from nums, forming a pair.
# The operation is done on nums as many times as possible.
# Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs that are formed and answer[1] is the number of leftover integers in nums after doing the operation as many times as possible.

class Solution:
    def __init__(self, nums):
        self.nums = nums
        
    def numberOfPairs(self):
        nums = self.nums
        freq = [0]*101
        p = 0
        lo = 0
        for num in nums:
            freq[num] += 1
        
        for x in freq:
            p += x // 2
            lo += x % 2
        
        return [p, lo]

if __name__ == "__main__":
    nop = Solution([1,3,2,1,3,2,2,2,2])
    print(nop.numberOfPairs())
        


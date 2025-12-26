# 769. Max Chunks To Make Sorted

# You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

# We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

# Return the largest number of chunks we can make to sort the array.

class MaxChunks:
    def __init__(self, nums):
        self.nums = nums
    
    def solve(self):
        nums = self.nums
        max_seen = 0
        count = 0
        n = len(nums)
        for i in range(n):
            max_seen = max(max_seen, nums[i])
            if max_seen == i:
                count += 1
        return count
if __name__ == "__main__":
    mc = MaxChunks([5,4,3,2,1])
    print(mc.solve())
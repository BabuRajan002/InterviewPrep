# 905. Sort Array By Parity

# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

class SortParity:
    def __init__(self, nums):
        self.nums = nums
    
    def solve(self):
        nums = self.nums
        n = len(nums)
        ans = [0] * n
        beg = 0 
        end = n-1

        for i in range(n):
            if nums[i] % 2 == 0:
                ans[beg] = nums[i]
                beg += 1
            else:
                ans[end] = nums[i]
                end -= 1
        return ans

if __name__ == "__main__":
    sortparity = SortParity([0])
    print(sortparity.solve())
                
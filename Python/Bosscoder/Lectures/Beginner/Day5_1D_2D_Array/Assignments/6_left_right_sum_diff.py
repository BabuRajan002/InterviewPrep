# Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

# answer.length == nums.length.
# answer[i] = |leftSum[i] - rightSum[i]|.

# Where:

# leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
# rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.

# Return the array answer.

class LeftRightSumDifferences:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        nums = self.arr
        leftsum = 0
        ans = []
        totalsum = sum(nums)
        for i in range(len(nums)):
            rightsum = totalsum - leftsum - nums[i]
            ans.append(abs(leftsum-rightsum))
            leftsum += nums[i]
        return ans

if __name__ == "__main__":
    lr = LeftRightSumDifferences([10])
    print(lr.solve())

class RunningSum:
    def __init__(self, nums):
        self.nums = nums
    
    def solve(self):
        nums = self.nums

        n = len(nums)
        leftSum = 0
        for i in range(n):
            leftSum += nums[i]
            nums[i] = leftSum
        return nums

if __name__ == "__main__":
    runningsum = RunningSum([1,2,3,4])
    print(runningsum.solve())
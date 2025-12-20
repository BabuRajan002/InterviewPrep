# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.

class RunningSum:
    def __init__(self, arr):
        self.arr = arr
        
    def sum(self):
        sum = 0
        nums = self.arr
        ans = [0]*len(self.arr)
        for i in range(len(self.arr)):
           sum = sum + nums[i]
           ans[i] = sum
        
        

if __name__ == "__main__":
    run = RunningSum([1,1,1,1])
    print(run.sum())
        
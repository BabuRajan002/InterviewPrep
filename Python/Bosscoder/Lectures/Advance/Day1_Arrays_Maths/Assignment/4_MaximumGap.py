class MaximumGap:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        nums = self.arr
        nums.sort()
        n = len(nums)
        mx = 0
        if n < 2:
            return 0
        for i in range(1,n):
           diff = nums[i] - nums[i-1]
           if diff > mx:
               mx = diff
        return mx

if __name__ == "__main__":
    mg = MaximumGap([10])
    print(mg.solve())
    
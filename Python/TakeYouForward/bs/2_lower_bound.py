class LowerBound:
    def __init__(self, nums, x):
        self.nums = nums
        self.x = x 
    
    def solve(self):
        nums = self.nums 
        x = self.x 

        low = 0
        high = len(nums) - 1
        ans = len(nums)

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

if __name__ == "__main__":
    lb = LowerBound([-94183, -91340, -87112, -72026, -65639, -24479, -12167, 29555, 37240, 49615, 67123, 67800], -18095)
    print(lb.solve())




                



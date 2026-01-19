class UpperBound:
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

            if nums[mid] > x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

if __name__ == "__main__":
    ub = UpperBound([3,5,8,15,19], 9)
    print(ub.solve())




                



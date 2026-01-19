class FloorCeil:
    def __init__(self, nums, x):
        self.nums = nums
        self.x = x
    
    def floor(self):
        nums = self.nums 
        x = self.x                 
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= x:
                ans = nums[mid]
                left = mid + 1
            else:
                right = mid - 1
        return ans 
    
    def ceil(self):
        nums = self.nums 
        x = self.x                 
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= x:
                ans = nums[mid]
                right = mid - 1
            else:
                left = mid + 1
        return ans


if __name__ == "__main__":
    fc = FloorCeil([3, 4, 4, 7, 8, 10], 5)
    print(fc.floor(), fc.ceil())


    






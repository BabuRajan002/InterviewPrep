class NumberOfTimes:
    def __init__(self, nums):
        self.nums = nums 
    
    def solve(self):
        nums = self.nums 

        low = 0
        high = len(nums) - 1
        n = len(nums)

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:                
                low = mid + 1
            
            else:
                high = mid 
        return low

if __name__ == "__main__":
    numOfRot = NumberOfTimes([4, 5, 6, 7, 0, 1, 2, 3])
    print(numOfRot.solve())



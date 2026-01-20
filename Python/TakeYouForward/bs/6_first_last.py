class FirstLast:
    def __init__(self, nums, target):
        self.nums = nums 
        self.target = target
    
    def lastOccur(self):
        nums = self.nums
        target = self.target

        low = 0
        high = len(nums) - 1
        lastOccurance = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                lastOccurance = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return lastOccurance
    
    def firstOccur(self):
        nums = self.nums
        target = self.target

        low = 0
        high = len(nums) - 1
        firstOccurance = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                firstOccurance = mid 
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return firstOccurance

if __name__ == "__main__":
    firstlast = FirstLast([5,7,7,8,8,10], 11)
    print(f"[{firstlast.firstOccur()},{firstlast.lastOccur()}]")

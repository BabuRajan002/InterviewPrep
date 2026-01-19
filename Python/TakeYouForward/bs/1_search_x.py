class SearchX:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    
    def solve(self):
        nums = self.nums 
        target = self.target 

        low = 0 
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if target == nums[mid]:
                return mid 
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1
if __name__ == "__main__":
    searchx = SearchX([-1,0,3,5,9,12], 2)
    print(searchx.solve())

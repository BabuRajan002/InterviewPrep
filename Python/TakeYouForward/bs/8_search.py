class Search:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
    
    def solve(self):
        nums = self.nums 
        k = self.k 

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == k:
                return mid
            
            if nums[low] <= nums[mid]:

                if nums[low] <= k < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            
            else:
                if nums[mid] < k <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            
        return -1

if __name__ == "__main__":
    search = Search([4,5,6,7,0,1,2],0)
    print(search.solve())



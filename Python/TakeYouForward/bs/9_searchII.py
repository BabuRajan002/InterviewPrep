class SearchII:
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
                return True
            
            if nums[low] == nums[mid] == nums[high]:
               low += 1
               high -= 1
               continue
            
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
            
        return False

if __name__ == "__main__":
    search = SearchII([4,5,6,7,0,1,2],12)
    print(search.solve())



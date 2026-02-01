# Brute Force

# class AggressiveCows:
#     def __init__(self, nums, k):
#         self.nums = nums 
#         self.k = k
    
#     def canWeplace(self, arr, distance, cows):
#         lastCow = arr[0]
#         countCows = 1

#         for i in range(1, len(arr)):
#             if arr[i] - lastCow >= distance:
#                 countCows += 1
#                 lastCow = arr[i]
            
#         if countCows >= cows:
#             return True
#         else:
#             return False
    

#     def solve(self):
#         nums = self.nums 
#         k = self.k 

#         nums.sort()
#         maxDist = nums[-1] - nums[0]
#         ans = 0

#         for i in range(1, maxDist):
#             if self.canWeplace(nums, i, k) == True:
#                 ans = i
#         return ans
   

# if __name__ == "__main__":
#     aggressiveCows = AggressiveCows([0, 3, 4, 7, 10, 9], 4)
#     print(aggressiveCows.solve())

# BInary Search
class AggressiveCows:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
    
    def canWePlace(self, arr, distance, cows):
        lastCow = arr[0]
        countCoows = 1

        for i in range(1, len(arr)):
            if arr[i] - lastCow >= distance:
                countCoows += 1
                lastCow = arr[i]
        
        if countCoows >= cows:
            return True
        else:
            return False

    
    def solve(self):
        nums = self.nums 
        k = self.k 
        nums.sort()

        low = 0
        high = nums[-1] - nums[0]
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if self.canWePlace(nums, mid, k) == True:
                ans = mid 
                low = mid + 1
            else:
                high = mid - 1
        return ans

if __name__ == "__main__":
    aggressiveCows = AggressiveCows([52,965,113,947,238,619,956,464,185,542,279,998,160,585,431,765,436,986,499,615,477,334,937,740,379,52], 15)
    print(aggressiveCows.solve())


    
    

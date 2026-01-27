# Brute Force

# class KthMissing:
#     def __init__(self, nums, k):
#         self.nums = nums
#         self.k = k
    
#     def solve(self):
#         nums = self.nums 
#         k = self.k 

#         high = max(nums)
#         count = 0
#         for i in range(1,high):
#             if i not in nums:
#                 count += 1
            
#             if count == k:
#                 return i

# if __name__ == "__main__":
#     kthmissing = KthMissing([1, 4, 6, 8, 9],3)
#     print(kthmissing.solve())

class KthMissing:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
    def solve(self):
        nums = self.nums 
        k = self.k

        low = 0
        high = len(nums) - 1

        while low<= high:
            mid = (low +high) // 2
            missing_elements = nums[mid] - (mid + 1)
            if missing_elements < k:
                low = mid + 1
            else:
                high = mid - 1
        return low + k 

if __name__ == "__main__":
    kthmissing = KthMissing([3, 5, 7, 10], 6)
    print(kthmissing.solve())



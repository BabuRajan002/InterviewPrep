# Brute force solution

# class Pivot:
#     def __init__(self, nums):
#         self.nums = nums
    
#     def solve(self):
#         nums = self.nums
#         n = len(nums)
        


#         for i in range(n):
#             rightSum = 0
#             leftSum = 0

#             #Leftsum
#             for l in range(i):
#                 leftSum += nums[l]
            
#             for r in range(i+1, n):
#                 rightSum += nums[r]
#             print(leftSum, rightSum)
#             if leftSum == rightSum:
#                 return i 
#         return -1

# if __name__ == "__main__":
#     pivot = Pivot([1,7,3,6,5,6])
#     print(pivot.solve())

# Optimized Version

class Pivot:
    def __init__(self, nums):
        self.nums = nums
    
    def solve(self):
        nums = self.nums
        n = len(nums)

        leftSum = 0
        totalSum = sum(nums)

        for i in range(n):
            rightSum = totalSum - leftSum - nums[i]

            if leftSum == rightSum:
                return i
            
            leftSum += nums[i]
        return -1

if __name__ == "__main__":
    pivot = Pivot([1,7,3,6,5,6])
    print(pivot.solve())



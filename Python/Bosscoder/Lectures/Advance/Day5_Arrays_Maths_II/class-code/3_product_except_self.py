# class ProductExceptSelf:
#     def __init__(self, nums):
#         self.nums = nums
    
#     def solve(self):
#         nums = self.nums 
#         n = len(nums)
#         ans = []
    
#         prefixArr = [0] * n 
#         suffixArr = [0] * n 

#         prefixArr[0] = 1
#         suffixArr[n-1] = 1

#         #prefixArr
#         prod = 1
#         for i in range(1,n):
#             prod *= nums[i-1]
#             prefixArr[i] = prod
#         print(prefixArr)
#         #SuffixArr
#         suff = 1
#         for i in range(n-2, -1, -1):
#             suff *= nums[i+1]
#             suffixArr[i] = suff
#         for i in range(n):
#             ans.append(prefixArr[i] * suffixArr[i])
        
#         return ans    

# if __name__ == "__main__":
#     product = ProductExceptSelf([1,2,3,4])
#     print(product.solve())

# Optimized version

class ProductExceptSelf:
    def __init__(self, nums):
        self.nums = nums
    
    def solve(self):
        
        nums = self.nums 
        n = len(nums)
        ans = [0] * n
        ans[0] = 1

        for i in range(1,n):
            ans[i] = ans[i-1] * nums[i-1]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            ans[i] = ans[i] * suffix
        
            suffix *= nums[i]
        
        return ans
if __name__ == "__main__":
    product = ProductExceptSelf([1,2,3,4])
    print(product.solve())
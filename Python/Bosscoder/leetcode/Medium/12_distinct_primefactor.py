# 2521. Distinct Prime Factors of Product of Array

# Given an array of positive integers nums, return the number of distinct prime factors in the product of the elements of nums.

# Note that:

# A number greater than 1 is called prime if it is divisible by only 1 and itself.
# An integer val1 is a factor of another integer val2 if val2 / val1 is an integer.

class Solution:
    def __init__(self,nums):
        self.nums = nums
    
    def distinctPrimeFactors(self):
        nums = self.nums
        prod = 1
        for num in nums:
            prod = prod * num        
        ans = set()        
        i = 2
        while i * i <= prod:
            if prod % i == 0:
                ans.add(i)
                prod //= i
            else:
                i += 1
        if prod >= 1:
            ans.add(prod)
        

        return len(ans)
     
if __name__ == "__main__":
    dpf = Solution([2,4,3,7,10,6])
    print(dpf.distinctPrimeFactors())

        
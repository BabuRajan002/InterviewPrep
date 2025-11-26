# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.
class Concatenation:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        n = len(self.arr)
        ans = [0]*2*n        
        nums = self.arr
        for i in range(n):            
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        return ans

if __name__ == "__main__":
    con = Concatenation([1,3,2,1])
    print(con.solve())

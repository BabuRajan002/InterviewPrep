# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

class MaxProduct:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        nums = self.arr
        nums.sort()
        i, j  = nums[-1], nums[-2]
        return (i-1)*(j-1)
    
if __name__ == "__main__":
    maxp = MaxProduct([1,5,4,5])
    print(maxp.solve())
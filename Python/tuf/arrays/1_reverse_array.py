class Reverse:
    def __init__(self, nums):
        self.nums = nums
    
    def solve(self):
        nums = self.nums
        n = len(nums)

        for i in range(n // 2):
            nums[i], nums[n-i-1] = nums[n-i-1], nums[i]

        return nums 

if __name__ == "__main__":
    reverse = Reverse([1,2,3,4,5])
    print(reverse.solve())

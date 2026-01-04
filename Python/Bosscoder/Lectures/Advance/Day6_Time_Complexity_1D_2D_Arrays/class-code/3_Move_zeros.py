class MoveZeros:
    def __init__(self, nums):
        self.nums = nums
    
    def solve(self):
        nums = self.nums 

        n = len(nums)
        left = 0

        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
        return nums

if __name__ == "__main__":
    movezeros = MoveZeros([0,1,0,3,12])
    print(movezeros.solve())
                

class RemoveDup:
    def __init__(self, nums):
        self.nums = nums
    
    def solve(self):
        nums = self.nums 

        n = len(nums)
        i = 0
        for j in range(n):
            if nums[i] != nums[j]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        return i + 1

if __name__ == "__main__":
    removedup = RemoveDup([0,0,1,1,1,2,2,3,3,4])
    print(removedup.solve())
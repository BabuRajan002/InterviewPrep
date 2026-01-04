class SortColors:
    def __init__(self, nums):
        self.nums = nums
    
    def solve(self):
        nums = self.nums
        n = len(nums)

        count0 = 0
        count1 = 0
        count2 = 0

        for i in range(n):
            if nums[i] == 0:
                count0 += 1
            elif nums[i] == 1:
                count1 += 1
            else:
                count2 += 1
        index = 0
        while count0 > 0:
            nums[index] = 0
            count0 -= 1
            index += 1
        
        while count1 > 0:
            nums[index] = 1
            count1 -= 1
            index += 1
        
        while count2 > 0:
            nums[index] = 2
            count2 -= 1
            index += 1
        return nums

if __name__ == "__main__":
    sortcolor = SortColors([2,0,2,1,1,0])
    print(sortcolor.solve())

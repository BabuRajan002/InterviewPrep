class InsertionSort:
    def __init__(self, nums):
        self.nums = nums 
    def solve(self):
        nums = self.nums 
        n = len(nums)
        for i in range(n):
            j = i
            while j > 0 and nums[j-1] > nums[j]:
                temp = nums[j-1]
                nums[j-1] = nums[j]
                nums[j] = temp 
                j -= 1
        return nums

if __name__ == "__main__":
    insert = InsertionSort([7, 4, 1, 5, 3])
    print(insert.solve())
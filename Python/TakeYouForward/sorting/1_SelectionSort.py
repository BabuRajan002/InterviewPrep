class SelectionSort:
    def __init__(self, nums):
        self.nums = nums 
    def solve(self):
        nums = self.nums 
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[j] < nums[i]:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
        return nums 

if __name__ == "__main__":
    selection = SelectionSort([7, 4, 1, 5, 3])
    print(selection.solve())




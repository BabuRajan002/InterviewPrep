class BubbleSortRecursive:
    def __init__(self, nums):
        self.nums = nums
    
    def bubbleSortRecurse(self, n=None):
        nums = self.nums         
        if n is None:
            n = len(nums)

        if n == 1:
            return nums
        
        for i in range(n-1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        
        return self.bubbleSortRecurse(n-1)

if __name__ == "__main__":
    recurseBubbleSort = BubbleSortRecursive([7,4,1,5,3])
    print(recurseBubbleSort.bubbleSortRecurse())
        



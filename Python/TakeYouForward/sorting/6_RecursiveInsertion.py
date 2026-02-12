class RecursiveInsertion:
    def __init__(self, nums):
        self.nums = nums 
    
    def rescursiveInsertionSort(self, i, n=None):
        nums = self.nums
        if n is None:
            n = len(nums)

        if i == n:
            return nums
        
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            temp = nums[j-1]
            nums[j-1] = nums[j]
            nums[j] = temp
            j -= 1
        return self.rescursiveInsertionSort(i+1, n)

if __name__ == "__main__":
    arr = [5,4,6,3,1]
    recursiveinsertion = RecursiveInsertion(arr)
    print(recursiveinsertion.rescursiveInsertionSort(0))
        
        
            

    
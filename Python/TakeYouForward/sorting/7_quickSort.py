class QuickSort:
    def __init__(self, nums):
        self.nums = nums
    
    def recursiveQuick(self, low=None, high=None):
        nums = self.nums

        if low is None:
            low = 0
        if high is None:
            high = len(nums) - 1

        if low < high:
            partitionIndex = self.partition(low, high)
            self.recursiveQuick(low, partitionIndex - 1)
            self.recursiveQuick(partitionIndex + 1, high)
        return nums
    
    def partition(self, low, high):
        nums = self.nums
        i = low 
        j = high 

        pivotNumber = nums[low]
        while i < j:    
            while nums[i] <= pivotNumber and i < high:
                i += 1
            while nums[j] > pivotNumber and j > low:
                j -= 1
            if i < j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
        nums[low], nums[j] = nums[j], nums[low]
        return j 

if __name__ == "__main__":
    recurseQuick = QuickSort([7, 4, 1, 5, 3])
    print(recurseQuick.recursiveQuick())
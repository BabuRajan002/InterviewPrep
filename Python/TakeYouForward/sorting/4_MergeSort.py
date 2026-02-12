class MergeSort:
    def __init__(self, nums, low, high):
        self.nums = nums
        self.low = low 
        self.high = high
    
    def mergeFinal(self, nums, low, mid, high):
        left = low 
        right = mid + 1
        temp = []
        # Changed 'low <= high' to 'right <= high'
        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        
        while left <= mid:
            temp.append(nums[left])
            left += 1
        
        while right <= high:
            temp.append(nums[right])
            right += 1
        
        # Only update the specific range [low : high+1]
        for i in range(len(temp)):
            nums[low + i] = temp[i]
        
        return nums

    def mergeSort(self, nums, low, high):
        # Removed the lines that reset low and high to 0 and n-1
        if low >= high: # Changed from == to >= for safety
            return 
        
        mid = (low + high) // 2
        self.mergeSort(nums, low, mid)
        self.mergeSort(nums, mid + 1, high)
        self.mergeFinal(nums, low, mid, high)
        
        return nums # Added return so print() works

if __name__ == "__main__":
    # Note: For an array of length 5, high should be 4
    arr = [7, 4, 1, 5, 3]
    n = len(arr)
    mergesort = MergeSort(arr, 0, n-1)
    # Passed the required arguments to the method call
    print(mergesort.mergeSort(arr, 0, 4))
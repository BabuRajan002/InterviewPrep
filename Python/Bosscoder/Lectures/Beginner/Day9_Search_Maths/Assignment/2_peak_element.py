# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

class Peak:
    def __init__(self, arr):
        self.arr = arr
        
    def peak(self):
        nums = self.arr
        max_element = 0
        for i in range(len(nums)):
            if nums[i] > max_element:
                max_element = nums[i]
                max_idx = i
        return max_idx

if __name__ == "__main__":
    peak = Peak([1,2,1,3,5,6,4])
    print(peak.peak())
        

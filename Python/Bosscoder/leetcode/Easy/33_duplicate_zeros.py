# 1089. Duplicate Zeros
# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.
from typing import List
class Solution:
    def __init__(self,arr):
        self.arr = arr

    def duplicateZeros(self) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr = self.arr
        l = 0
        r = 1
        n = len(arr)
        while r < n:
            if arr[l] == 0:
                arr.insert(r,0)
                l += 2
                r += 2
                arr.pop(-1)
            else:
                l += 1
                r += 1
        return arr

if __name__ == "__main__":
    dup = Solution([0,2,3,0,5])
    print(dup.duplicateZeros())

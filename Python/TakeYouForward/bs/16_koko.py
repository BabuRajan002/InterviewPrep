import math 

class Koko:
    def __init__(self, nums, h):
        self.nums = nums 
        self.h = h
    
    def solve(self):
        nums = self.nums 
        h = self.h 

        low = 1
        high = max(nums)
        ans = float('inf')

        while low <= high:
            mid = (low + high) // 2
            totalhrs = self.calculateTotal(nums, mid)
            if totalhrs <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def calculateTotal(self, nums, mid):
        summ = 0
        for num in nums:
            summ += math.ceil(num / mid)
        return summ 

if __name__ == "__main__":
    koko = Koko([7, 15, 6, 3], 8)
    print(koko.solve())
    





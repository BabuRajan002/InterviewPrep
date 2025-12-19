class EraseOverlapIntervals:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        nums = self.arr
        n = len(self.arr)
        if n == 0:
            return 0        
        count = 1
        nums.sort(key=lambda x: x[1])
        last_number = nums[0][-1]
        for i in range(1,n):
            if nums[i][0] >= last_number:
                count += 1
                last_number = nums[i][-1]                
        return (n - count)

if __name__ == "__main__":
    noi = EraseOverlapIntervals([[1,2],[1,2],[1,2]])
    print(noi.solve())




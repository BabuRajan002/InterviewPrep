class MaxChunkII:
    def __init__(self, nums):
        self.nums = nums
    
    def solve(self):
        nums = self.nums
        count = 0
        max_left = 0
        min_right = []
        rmin = float('inf')
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < rmin:
                rmin = nums[i]
            min_right.append(rmin)
        min_right.sort()
        print(min_right)
        for i in range(len(nums)-1):
            max_left = max(max_left, nums[i])            
            if max_left <= min_right[i+1]:
                count += 1

        return count+1

if __name__ == "__main__":
    maxchunk = MaxChunkII([2,1,3,4,4])
    print(maxchunk.solve())
class Subarray:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
    
    def solve(self):
        sum = 0
        preSumDict = {}
        count = 0
        k = self.k
        nums = self.nums

        for i in range(len(nums)):
            sum += nums[i]

            if sum == k:
                count += 1
            
            rem = sum - k
            if rem in preSumDict:
                count += 1
            
            if sum not in preSumDict:
                preSumDict[sum] = i
        
        return count

if __name__ == "__main__":
    sa = Subarray([0,0,0,0,0,0,0,0,0,0],0)
    print(sa.solve())




    

    








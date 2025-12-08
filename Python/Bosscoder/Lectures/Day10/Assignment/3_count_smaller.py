class CountSmaller:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        nums = self.arr
        # count = 0
        ans = []
        for i in range(len(nums)):
            count = 0            
            for j in range(i+1,len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            ans.append(count)
        return ans                    
if __name__ == "__main__":
    countsmall = CountSmaller([5,2,6,1])
    print(countsmall.solve())
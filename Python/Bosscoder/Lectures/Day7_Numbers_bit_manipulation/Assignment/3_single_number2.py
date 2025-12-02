class SingleElement:
    def __init__(self, arr):
        self.arr = arr
        
    def find(self):
        nums = self.arr
        n = max(nums)+1
        ans = [0]*n
        for num in nums:
            ans[num] += 1
        
        for idx in nums:
            if ans[idx] == 1:
                return idx


if __name__ == "__main__":
    se = SingleElement([-2,-2,1,1,4,1,4,4,-4,-2])
    print(se.find())    


class Permutation:
    def __init__(self, arr):
        self.arr = arr
        
    def build(self):
        # ans = []
        # arr = self.arr
        # for i in range(len(arr)):
        #     ans.append(arr[arr[i]])
        # return ans
        nums = self.arr
        return [nums[i] for i in nums]

if __name__ == "__main__":
    perm = Permutation([5,0,1,2,3,4])
    print(perm.build())
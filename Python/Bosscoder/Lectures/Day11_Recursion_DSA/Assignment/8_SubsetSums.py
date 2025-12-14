class SubsetsSum:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        n = sum(self.arr)
        ans = []
        for i in range(n):
            ans.append(i)
        return ans

if __name__ == "__main__":
    sss = SubsetsSum([2,3])
    print(sss.solve())
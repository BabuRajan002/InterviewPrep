class SortedSquares:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        nums = self.arr
        n = len(self.arr)
        ans = [0] * n
        for i in range(n):
            ans[i] = nums[i] ** 2
        ans.sort()
        return ans

if __name__ == "__main__":
    ss = SortedSquares([-7,-3,2,3,11])
    print(ss.solve())

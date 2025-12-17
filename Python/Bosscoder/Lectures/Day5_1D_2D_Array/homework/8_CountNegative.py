class CountNegative:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        arr = self.arr
        m = len(arr)
        n = len(arr[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if arr[i][j] < 0:
                    count += 1
        return count

if __name__ == "__main__":
    cn = CountNegative([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
    print(cn.solve())
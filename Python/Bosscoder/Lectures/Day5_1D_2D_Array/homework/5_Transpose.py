class Transpose:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        n = len(self.arr)
        m = len(self.arr[0])

        res = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                res[j][i] = self.arr[i][j]        

        return res
if __name__ == "__main__":
    transpose = Transpose([[1,2,3],[4,5,6]])
    print(transpose.solve())

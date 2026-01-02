class MatrixDiagonalSum:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        sum = 0 
        arr = self.arr
        n = len(arr)
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n-1:
                    sum += arr[i][j] 
        return sum

if __name__ == "__main__":
    mds = MatrixDiagonalSum([[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]])
    print(mds.solve())
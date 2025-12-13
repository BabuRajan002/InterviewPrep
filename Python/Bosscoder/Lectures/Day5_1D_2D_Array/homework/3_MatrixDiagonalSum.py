class MatrixDiagonalSum:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        n = len(self.arr)
        sum = 0
        nums = self.arr
        for i in range(n):
            for j in range(n):
              if i == j or i + j == n - 1:  
                sum += nums[i][j]
        return sum

if __name__ == "__main__":
    mds = MatrixDiagonalSum([[1,2,3], [4,5,6], [7,8,9]])
    print(mds.solve())
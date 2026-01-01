class MatrixReshape:
    def __init__(self, arr, r, c):
        self.arr = arr 
        self.r = r 
        self.c = c
    
    def solve(self):
        arr = self.arr 
        row = len(arr)
        col = len(arr[0])

        r = self.r 
        c = self.c 

        row_num = 0
        col_num = 0

        result = [[0 for _ in range(c)] for _ in range(r)]

        if (row * col) != (r * c):
            return arr

        for i in range(row):
            for j in range(col):
                result[row_num][col_num] = arr[i][j]
                col_num += 1
                if col_num == c:
                    col_num = 0
                    row_num += 1
        return result

if __name__ == "__main__":
    matreshape = MatrixReshape([[1,2],[3,4]], 1, 4)
    print(matreshape.solve())
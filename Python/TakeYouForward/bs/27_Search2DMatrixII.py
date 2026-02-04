class Search2DMatII:
    def __init__(self, mat, target):
        self.mat = mat 
        self.target = target 
    
    def solve(self):
        mat = self.mat 
        target = self.target 

        m = len(mat[0]) #col 
        row = 0
        col = m - 1

        while row < len(mat) and col >= 0:
            if mat[row][col] == target:
                return True
            elif mat[row][col] < target:
                row += 1
            else:
                col -= 1
        return False 

if __name__ == "__main__":
    search2d = Search2DMatII([ [1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30] ], 110)
    print(search2d.solve())
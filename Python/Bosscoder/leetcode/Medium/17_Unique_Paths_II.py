class UniquePathII:
    def __init__(self, grid):
        self.grid = grid
    
    def solve(self):
        grid = self.grid
        row = len(grid)
        col = len(grid[0])

        lionSeenRow = False
        lionSeencol = False

        mat = [[0 for _ in range(col)] for _ in range(row)]
        print(mat)

        if grid[0][0] == 1 and grid[row - 1][col -1] == 1:
            return 0
        
        #last row
        for i in range(col -1, -1, -1):
            if grid[row - 1][i] != 1 and lionSeenRow == False:
                mat[row - 1][i] = 1
            else:
                lionSeenRow = True
                mat[row - 1][i] = 0
        
        #last col
        for i in range(row - 1, -1, -1):
            if grid[i][col - 1] != 1 and lionSeencol == False:
                mat[i][col - 1] = 1                
            else:
                lionSeencol = True
                mat[i][col -1] = 0
        
        for i in range(row - 2, -1, -1):
            for j in range(col - 2, -1, -1):
                if grid[i][j] != 1:
                    waysFromRight = mat[i][j+1]
                    waysFromDown = mat[i+1][j]

                    totalWays = waysFromRight + waysFromDown

                    mat[i][j] = totalWays
        return mat[0][0]

if __name__ == "__main__":
    uniquepath = UniquePathII([[0,0]])
    print(uniquepath.solve())

    
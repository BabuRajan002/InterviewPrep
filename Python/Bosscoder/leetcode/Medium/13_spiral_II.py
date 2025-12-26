class Spiral:
    def __init__(self,n):
        self.n = n
    
    def solve(self):
        n = self.n
        left = 0  #Column
        right = n-1 #Column
        top = 0 #Row
        bottom = n-1 #row
        count = 1

        mat = [[0 for _ in range(n)] for _ in range(n)]

        while (left <= right and top <= bottom):

            #First row
            for i in range(left, right+1):
                mat[top][i] = count
                count += 1            
            top += 1

            #last column
            for i in range(top, bottom+1):
                mat[i][right] = count
                count += 1
            right -= 1

            #Last row
            for i in range(right, left-1, -1):
                mat[bottom][i] = count
                count += 1
            bottom -= 1

            #First column
            for i in range(bottom, top-1, -1):
                mat[i][left] = count
                count += 1
            
            left += 1
        return mat

if __name__ == "__main__":
    spiral = Spiral(5)
    print(spiral.solve())

            


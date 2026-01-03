class SpiralMatrix:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        n = self.n
        left = 0 #col
        right = n-1 #col
        top = 0 #row
        bottom = n-1 #col

        count = 1
        mat = [[0 for _ in range(n)] for _ in range(n)]

        while(left <= right and top <= bottom):
            
            #first row
            for i in range(left, right+1):
                mat[top][i] = count 
                count += 1
            top += 1

            #last col
            for i in range(top, bottom+1):
                mat[i][right] = count
                count += 1
            right -= 1

            #last row
            for i in range(right, left-1, -1):
                mat[bottom][i] = count
                count += 1
            bottom -= 1

            #first col
            for i in range(bottom, top-1, -1):
                mat[i][left] = count
                count += 1
            left += 1
        return mat

if __name__ == "__main__":
    sm = SpiralMatrix(3)
    print(sm.solve())
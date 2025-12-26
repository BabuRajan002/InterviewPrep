class Spiral:
    def __init__(self,matrix):
        self.matrix = matrix
    
    def solve(self):
        matrix = self.matrix

        left = 0 #col
        right = len(matrix[0]) -1 #col

        top = 0 #row
        bottom = len(matrix)-1 #row

        ans = []

        while (left <= right and top <= bottom):
            
            #first row
            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top += 1
            # print(f"Value of top is {top} and ans is {ans}")            

            #last col
            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right -= 1
            # print(f"Value of right is {right} and ans is {ans}")

            #last row
            if top <= bottom:
             for i in range(right, left-1, -1):
                ans.append(matrix[bottom][i])
             bottom -= 1
            #  print(f"Value of bottom is {bottom} and ans is {ans}")

            #first col
            if left <= right:
             for i in range(bottom, top-1, -1):
                ans.append(matrix[i][left])
             left += 1
            # print(f"Value of left is {left} and ans is {ans}")
        return ans

if __name__ == "__main__":
    spiral = Spiral([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    print(spiral.solve())



        
# #Brute Force
# class Search2DMatrix:
#     def __init__(self, mat, target):
#         self.mat = mat 
#         self.target = target 
    
#     def solve(self):
#         mat = self.mat
#         target = self.target 

#         row = len(mat)
#         col = len(mat[0])

#         for i in range(row):
#             for j in range(col):
#                 if mat[i][j] == target:
#                     return True 
#         return False 

# if __name__ == "__main__":
#     search2d = Search2DMatrix([ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ], 0)
#     print(search2d.solve())

# class Search2DMatrix:
#     def __init__(self, mat, target):
#         self.mat = mat 
#         self.target = target
    
    # def performBinary(self, arr, val):
    #     low = 0
    #     high = len(arr) - 1
    #     while low <= high:
    #         mid = (low + high) // 2
    #         if arr[mid] == val:
    #             return arr[mid]
    #         elif arr[mid] > val:
    #             high = mid - 1
    #         else:
    #             low = mid + 1
    #     return -1
    
    # def solve(self):
    #     mat = self.mat 
    #     target = self.target 

    #     row = len(mat)
    #     m = len(mat[0])
    #     result = -1
    #     for i in range(row):
    #         if mat[i][0] <= target <= mat[i][m-1]:
    #             result = self.performBinary(mat[i], target)       
    #     if result > 0:
    #         return True 
    #     else:
    #         return False 


class Search2DMatrix:
    def __init__(self, mat, target):
        self.mat = mat 
        self.target = target
    
    def solve(self):
        mat = self.mat 
        target = self.target
        m = len(mat[0])
        n = len(mat)

        low = 0
        high = (n * m) - 1

        while low <= high:
            mid = (low + high) // 2
            row = mid // m 
            col = mid % m 

            if mat[row][col] == target:
                return True
            elif mat[row][col] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False 
    
if __name__ == "__main__":
    search2dmat = Search2DMatrix([ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ], 2)
    print(search2dmat.solve())

    

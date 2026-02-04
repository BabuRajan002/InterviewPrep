# #Brute Force
# class RowWithMaxOnes:
#     def __init__(self, mat):
#         self.mat = mat 
    
#     def solve(self):
#         mat = self.mat 

#         row = len(mat)
#         col = len(mat[0])

#         maxOnes = float('-inf')
#         index = 0
#         for i in range(row):
#             countOnes = 0
#             for j in range(col):
#                 if mat[i][j] == 1:
#                     countOnes += 1
#             if countOnes > maxOnes:
#                 maxOnes = countOnes 
#                 index = i
#         if countOnes == 0:
#             return -1
#         return index
    
# if __name__ == "__main__":
#     rowwithmaxones = RowWithMaxOnes([[0, 0], [0, 0]])
#     print(rowwithmaxones.solve())

class RowWithMaxOnes:
    def __init__(self, mat):
        self.mat = mat

    def lowerBount(self, arr, x):
        low = 0
        high = len(arr) - 1
        ans = len(arr)

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                ans = mid 
                high = mid - 1
            else:
                low = mid + 1
        return ans
    
    def solve(self):
        mat = self.mat 
        m = len(mat)
        countMax = -1
        
        index = -1
        

        for i in range(len(mat)):            
            countOnes = m - self.lowerBount(mat[i], 1)
        
            if countOnes > countMax:
                countMax = countOnes
                index = i 
        return index

if __name__ == "__main__":
    rowwithmaxones = RowWithMaxOnes( [ [1, 1, 1], [0, 0, 1], [0, 0, 0] ])
    print(rowwithmaxones.solve())





                 

        
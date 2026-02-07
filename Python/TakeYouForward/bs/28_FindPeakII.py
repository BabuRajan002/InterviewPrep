class FindPeakII:
    def __init__(self, mat):
        self.mat = mat 
    
    def findMaxRow(self, mat, mid):
        index = -1
        maxValue = float('-inf')
        for i in range(len(mat)):
            if mat[i][mid] > maxValue:
                maxValue = mat[i][mid]
                index = i
        return index
    
    def solve(self):
        mat = self.mat
        low = 0
        high = len(mat[0]) - 1
        m = len(mat[0])

        while low <= high:
            mid = (low + high) // 2

            rowIndex = self.findMaxRow(mat, mid)
            left = mat[rowIndex][mid-1] if mid - 1 >= 0 else float('-inf')
            right = mat[rowIndex][mid+1] if mid + 1 < m else float('-inf')

            if mat[rowIndex][mid] > left and mat[rowIndex][mid] > right:
                return [rowIndex, mid]
            elif mat[rowIndex][mid] < left:
                high = mid - 1
            else:
                low = mid + 1
        return [-1, -1]

if __name__ == "__main__":
    findpeak = FindPeakII([[10, 20, 15], [21, 30, 14], [7, 16, 32]])
    print(findpeak.solve())




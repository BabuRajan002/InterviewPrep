class Median:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def upperBound(self, mat, val):
        lower = 0
        higher = len(mat) - 1
        # Default to len(mat) because if no element is > val, 
        # then all elements are <= val.
        ans = len(mat) 

        while lower <= higher:
            mid = (lower + higher) // 2
            # We look for the first element strictly greater than val
            if mat[mid] > val:
                ans = mid 
                higher = mid - 1
            else:
                lower = mid + 1
        return ans # This index represents the count of elements <= val
    
    def countSmall(self, arr, row, col, val):
        count = 0
        for i in range(row):
            # val is the number we are testing as a potential median
            count += self.upperBound(arr[i], val)
        return count
    
    def solve(self):
        matrix = self.matrix
        n = len(matrix)
        m = len(matrix[0])
        
        low = float('inf')
        high = float('-inf')
        for i in range(n):
            low = min(low, matrix[i][0])
            high = max(high, matrix[i][m-1])

        # For median, we want the first value that has more than 
        # half the total elements behind/equal to it.
        req = (m * n) // 2

        while (low <= high):
            mid = (low + high) // 2
            smallEqual = self.countSmall(matrix, n, m, mid)
            
            if smallEqual <= req:
                low = mid + 1
            else:
                high = mid - 1 # Fixed to avoid infinite loop
        return low 

if __name__ == "__main__":
    # With this logic, the result for this matrix is 5
    median = Median([ [1, 4, 9], [2, 5, 6], [3, 7, 8] ] )
    print(median.solve())
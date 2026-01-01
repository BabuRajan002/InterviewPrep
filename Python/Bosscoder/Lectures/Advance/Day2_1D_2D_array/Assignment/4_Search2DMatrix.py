class SearchMatrix:
    def __init__(self, arr, target):
        self.arr = arr 
        self.target = target
    
    def solve(self):
        arr = self.arr 
        target = self.target 
        n = len(arr)
        m = len(arr[0])
        lo = 0 
        hi = (n * m) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            row = mid // m # Find the row index 
            col = mid % m #Find col index 

            if arr[row][col] == target:
                return True
            
            elif target < arr[row][col]:
                hi = mid - 1
            
            else:
                lo = mid + 1
        return False

if __name__ == "__main__":
    searchmat = SearchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
    print(searchmat.solve())

#Notes: 

# Method: Apply the binary search index in 2D matrix.

# This is a bit tricky to achieve the given TC : `O(log(m * n))`. we have to hypothetically convert this into 1D co-ordinates which is indices. 
# Then we have to apply the binary seach algorithm. 
# Steps: 
# 1. Convert into 1D co-ordinates. Here 3*4 matrix is given! 
# 2. So that total indices are 12 which 0 -> 11. 
# 3. Now you can find the middle index easily by (lo + hi) // 2 = mid. 
# 4. Now the tricky part is convert the mid into 2D co-ordinates. 
# 5. In order to do that we have to find the row index and col index. by the above coded way







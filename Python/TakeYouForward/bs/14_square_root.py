class SqaureRoot:
    def __init__(self, n):
        self.n = n 
    
    def solve(self):
        n = self.n 

        low = 1
        high = n 
        ans = 0 
        while low <= high:
            mid = (low + high) // 2

            if mid * mid == n:
                return mid 
            
            elif mid * mid <= n:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans 

if __name__ == "__main__":
    squareroot = SqaureRoot(28)
    print(squareroot.solve())

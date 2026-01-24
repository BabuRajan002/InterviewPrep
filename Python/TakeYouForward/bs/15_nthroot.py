class NthRoot:
    def __init__(self, n, m):
        self.n = n
        self.m = m
    
    def solve(self):
        n = self.n 
        m = self.m 

        low = 1
        high = m 

        while low <= high:
            mid = (low + high) // 2

            if mid ** n == m:
                return mid 
            
            elif mid ** n < m:
                low = mid + 1
            else:
                high = mid - 1 
        return -1

if __name__ == "__main__":
    nthroot = NthRoot(4, 69)
    print(nthroot.solve())
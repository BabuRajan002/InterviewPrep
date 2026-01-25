class SumOfN:
    def __init__(self, n):
        self.n = n
    
    def solve(self):        
        n = self.n

        def add(n):
            if n <= 1:
                return n
            return n + add(n - 1)          
            
        return add(n)

if __name__ == "__main__":
    sumofn = SumOfN(5)
    print(sumofn.solve())


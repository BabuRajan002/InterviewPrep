class Maximum:
    def __init__(self, n, m):
        self.n = n
        self.m = m
    
    def solve(self):
        if self.n > self.m:
            return self.n
        else:
            return self.m
    
if __name__ == "__main__":
    max_num = Maximum(7,6)
    print(max_num.solve())
        
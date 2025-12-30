class CountOfMatches:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        return self.n-1

if __name__ == "__main__":
    com = CountOfMatches(7)
    print(com.solve())
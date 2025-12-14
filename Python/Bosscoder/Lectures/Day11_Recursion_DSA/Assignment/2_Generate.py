class Generate:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        ans = []
        while self.n >= 1:
            ans.append(self.n)
            self.n -= 1
        
        return ans

if __name__ == "__main__":
    generate = Generate(5)
    print(generate.solve())
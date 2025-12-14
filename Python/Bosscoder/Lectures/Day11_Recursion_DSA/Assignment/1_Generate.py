class Generate:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        ans = []
        for i in range(1, self.n+1):
            ans.append(i)
        return ans

if __name__ == "__main__":
    generate = Generate(5)
    print(generate.solve())
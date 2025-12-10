class CountBits:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        n = self.n
        ans = [0] * (n + 1)
        for i in range(n+1):
          x = i
          count = 0
          while x > 0: 
            if x & 1 == 1:
               count += 1               
            x >>= 1
          ans[i] = count
        return ans

if __name__ == "__main__":
   cb = CountBits(5)
   print(cb.solve())


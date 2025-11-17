class Reverse:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        rev = 0
        while self.n:
         rev = (rev*10) + (self.n % 10)
         self.n = self.n // 10
        return rev

if __name__ == "__main__":
   rev = Reverse(123)
   print(rev.solve())
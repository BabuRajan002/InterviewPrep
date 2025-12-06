class EvenOddBit:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        num = self.n
        even = 0
        odd = 0
        idx = 0
        while num != 0:
          if num & 1 and idx % 2 == 0:
              even += 1
          elif num & 1 and idx % 2 != 0: 
              odd += 1
          num >>= 1
          idx += 1
        return [even, odd]
if __name__ == "__main__":
    eo = EvenOddBit(50)
    print(eo.solve())


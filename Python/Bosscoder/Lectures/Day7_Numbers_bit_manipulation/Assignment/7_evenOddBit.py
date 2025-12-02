class EvenOddBit:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        num = self.n
        even = 0
        odd = 0
        cnt = 0
        while num != 0:
            val = num & 1
            
            if val == 1 and cnt % 2 == 0:
                even += 1
                cnt += 1                              
            elif val == 1:
                odd += 1
                cnt += 1
            cnt += 1
            num >>= 1
        return [even, odd]

if __name__ == "__main__":
    eo = EvenOddBit(17)
    print(eo.solve())


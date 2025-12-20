class TrailingZero:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        num = abs(self.n)        

        if num == 0:
            return 0
        
        count = 0
        while num != 0:
           val = num & 1
           
           if val == 0:
               count += 1
           else:               
               break               
           num >>= 1            
        return count

if __name__ == "__main__":
    tz = TrailingZero(0)
    print(tz.solve())


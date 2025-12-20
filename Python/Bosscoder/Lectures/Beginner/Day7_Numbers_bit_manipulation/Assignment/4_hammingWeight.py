class HammingWeight:
    def __init__(self, s):
        self.s = s
        
    def solve(self):
        decimal_number = int(self.s,2)
        count = 0
        while decimal_number != 0:
            count += decimal_number & 1
            decimal_number >>= 1
        return count    

if __name__ == "__main__":
    hw = HammingWeight('00000000000000000000000010000000')
    print(hw.solve())
class Gcd:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def solve(self):
        a = self.a
        b = self.b
        while (a > 0 and b > 0):
            if a > b:
                a = a % b 
            else:
                b = b % a
        if a == 0:
            return b
        else:
            return a

if __name__ == "__main__":
    gcd = Gcd(9,12)
    print(gcd.solve())
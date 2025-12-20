class PowerofThree:
    def __init__(self, n):
        self.n = n
        
    def check(self):
        n = self.n
        if n <= 0:
            return False
        while n % 3 == 0:
            n = n // 3
        return n == 1



if __name__ == "__main__":
    powofthree = PowerofThree(28)
    print(powofthree.check())
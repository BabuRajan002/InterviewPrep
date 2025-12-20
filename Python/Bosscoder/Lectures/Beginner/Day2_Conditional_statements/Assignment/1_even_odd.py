class EvenOdd:
    def __init__(self, n):
        self.n = n
    
    def check(self):
        if self.n % 2 == 0:
            return True
        return False

if __name__ == "__main__":
    result = EvenOdd(3)
    print(result.check())
        
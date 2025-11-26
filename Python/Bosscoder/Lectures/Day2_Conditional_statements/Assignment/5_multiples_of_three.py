class MultipleOfThree:
    def __init__(self,n):
        self.n = n
    
    def check(self):
        if self.n % 3 == 0:
            return True
        return False

if __name__ == "__main__":
    three = MultipleOfThree(10)
    print(three.check())
        
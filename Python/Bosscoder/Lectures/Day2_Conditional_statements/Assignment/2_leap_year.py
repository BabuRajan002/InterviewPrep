class LeapYear:
    def __init__(self, n):
        self.n = n
    
    def check(self):
        if self.n % 4 == 0:
            if self.n % 100 == 0:
                return self.n % 400 == 0
            return True
        return False

if __name__ == "__main__":
    leapyear = LeapYear(-400)
    print(leapyear.check())
            
class Positive:
    def __init__(self,n):
        self.n = n
    
    def check(self):
        if self.n > 0:
            return True
        else:
            return False

if __name__ == "__main__":
    pos = Positive(-3)
    print(pos.check())


        
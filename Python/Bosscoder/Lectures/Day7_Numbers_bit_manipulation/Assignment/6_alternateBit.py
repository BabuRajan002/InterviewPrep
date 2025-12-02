class Alternate:
    def __init__(self, n):
        self.n = n
        
    def check(self):
        num = self.n
        if num == 0:
            return False
        prev = num & 1
        num >>= 1
        while num != 0:
            curr = num & 1
            if curr == prev:
                return False
            prev = curr
            num >>= 1
        return True    


if __name__ == "__main__":
    alter = Alternate(0)
    print(alter.check())

            


# Take 2 numbers from the user, x & n. Find xn (Calculate this without using the inbuilt function).

class Pow:
    def __init__(self, x, n):
        self.x = x
        self.n = n
        
    def pow(self):
        return self.x ** self.n

if __name__ == "__main__":
    sq = Pow(3,3)
    print(sq.pow())
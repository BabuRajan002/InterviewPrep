class Reverse:
    def __init__(self, s):
        self.s = s
        
    def solve(self):
       s = self.s
       return s[::-1]

if __name__ == "__main__":
    reverse = Reverse("abc")
    print(reverse.solve())
    
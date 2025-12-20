class Reverse:
    def __init__(self, s):
        self.s = s
        
    def solve(self):
        s = self.s.split()
        reverse_s = s[::-1]
        return " ".join(reverse_s)

if __name__ == "__main__":
    reverse = Reverse("i love programming very much")
    print(reverse.solve())
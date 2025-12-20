class LowerCase:
    def __init__(self, s):
        self.s = s
        
    def solve(self):
        return self.s.lower()

if __name__ == "__main__":
    lowercase = LowerCase("Hello")
    print(lowercase.solve())
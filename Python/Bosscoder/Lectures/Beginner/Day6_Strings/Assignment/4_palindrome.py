class Palindrome:
    def __init__(self, s):
        self.s = s
        
    def check(self):
        s = self.s
        rev = s[::-1]
        return s == rev

if __name__ == "__main__":
    pal = Palindrome("malayalam")
    print(pal.check)
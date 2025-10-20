# Implement a function that checks if a string is a palindrome (reads the same forward and backward), but ignores spaces, punctuation, and is case-insensitive.
import re

class PalindromeChecker:
    def __init__(self, s):
        self.s = re.sub(r'[^A-Za-z0-9]', '', s)
        
    def check(self):
        reversed_string = []
        for i in range(len(self.s)-1, -1, -1):
            reversed_string.append(self.s[i])
        reversed = "".join(reversed_string)
        if self.s.lower() == reversed.lower():
            return True
        else:
            return False

if __name__ == "__main__":
    out_s = PalindromeChecker("race a car")
    print(out_s.check())
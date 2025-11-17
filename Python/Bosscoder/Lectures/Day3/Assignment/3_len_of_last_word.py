# Given a string s consisting of words and spaces, return the length of the last word in the string. A word is a maximal substring consisting of non-space characters only.

class LastWord:
    def __init__(self, s):
        self.s = s
        
    def solve(self):
        words = self.s.strip().split()
        return len(words[-1])

if __name__ == "__main__":
    lastword = LastWord("Hello World")
    print(lastword.solve())


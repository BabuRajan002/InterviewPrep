# Check whether two Strings are anagram of each other.
# Note : An anagram of a string is another string that contains the same characters, only the order of characters can be different.

class Anagram:
    def __init__(self, s, t):
        self.s = s
        self.t = t
        
    def check(self):
        s1 = sorted(self.s.lower())
        s2 = sorted(self.t.lower())

        return s1 == s2

if __name__ == "__main__":
    anagram = Anagram("gram", "aram")
    print(anagram.check())
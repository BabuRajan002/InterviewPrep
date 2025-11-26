import string
class Pangram:
    def __init__(self, s):
        self.s = s
        
    def check(self):
        alphabet_set = set(string.ascii_lowercase)
        sentence_set = set(self.s)

        return alphabet_set.issubset(sentence_set)


    
if __name__ == "__main__":
    pangram = Pangram("The quick brown fox jumps over the lazy dog")
    print(pangram.check())
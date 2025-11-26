class SortSentence:
    def __init__(self, s):
        self.s = s
        
    def solve(self):
        s = self.s[::-1].split()
        s.sort()
        for i in range(len(s)):            
            s[i] = s[i][1:][::-1]
        return " ".join(s)
            
        

if __name__ == "__main__":
    sortsentence = SortSentence("Myself2 Me1 I4 and3")
    print(sortsentence.solve())

 
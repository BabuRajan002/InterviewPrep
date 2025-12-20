class CircularSentence:
    def __init__(self, s):
        self.s = s
        
    def check(self):
        words = self.s.strip().split()
        if len(words) == 1:
            if words[0][0] == words[0][-1]:
                return True
        else:
            fl = words[0][0]
            ll = words[0][-1]
            for i in range(1,len(words)):
                if ll == words[i][0]:
                    ll = words[i][-1]                    
                if ll == fl:
                    return True        
        return False

if __name__ == "__main__":
    cs = CircularSentence("leetcode exercises sound delightful")
    print(cs.check())
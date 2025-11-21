class Solution:
    def __init__(self, s, t):
         self.s = s
         self.t = t
         
    def isSubsequence(self):
        i = 0
        j = 0
        s = self.s
        t = self.t       
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)


if __name__ == "__main__":
   subseq = Solution("b", "abc")
   print(subseq.isSubsequence())
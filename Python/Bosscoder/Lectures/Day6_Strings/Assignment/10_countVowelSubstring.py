class CountVowelSubstrings:
    def __init__(self, s):
        self.s = s
        
    def solve(self):
        ans = 0 
        n = len(self.s)
        
        for i in range(n):
            vow = set()
            for j in range(i, n):
               if self.s[j] in ['a', 'e', 'i', 'o', 'u']:
                   vow.add(self.s[j])
                   if len(vow) == 5:
                       ans += 1          
               else:
                   break
        return ans

if __name__ == "__main__":
    countvow = CountVowelSubstrings('unicornarihan')
    print(countvow.solve())
            

               
                   
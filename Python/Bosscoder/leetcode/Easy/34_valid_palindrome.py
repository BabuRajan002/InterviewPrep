import re
class Solution:
    def __init__(self,s):
        self.s = s
    
    def isPalindrome(self):
        s = self.s
        word = re.sub(r'[^A-Za-z0-9]','',s).lower()
        rev_word = word[::-1]
        if word == rev_word:
            return True
        else:
            return False

if __name__ == "__main__":
    pal = Solution("A man, a plan, a canal: Panama")
    print(pal.isPalindrome())
# 387. First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

from collections import Counter
class Solution:
    def __init__(self,s):
        self.s = s
    
    def firstUniqChar(self):
        
        # for i, ch in enumerate(self.s):
        #     if self.s.count(ch) == 1:
        #         return i
        freq = Counter(self.s)
        for i, ch in enumerate(self.s):
            if freq[ch] == 1:
                return i
        return -1

if __name__ == "__main__":
    non_repeat = Solution("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print(non_repeat.firstUniqChar())

#Leetcode version:

# from collections import Counter
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         freq = Counter(s)
#         for i, ch in enumerate(s):
#             if freq[ch] == 1:
#                 return i
#         return -1
    # Find the Index of the First Occurrence in a String

    # Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def __init__(self,haystack, needle):
        self.haystack = haystack
        self.needle = needle
        
    def strStr(self):
          h, n = self.haystack, self.needle
          len_h, len_n = len(h), len(n)

          for i in range(len_h - len_n + 1):
               if h[i:i+len_n] == n:
                    return i
          return -1
                

if __name__ == "__main__":
    str_index = Solution("mississippi", "issip")
    print(str_index.strStr())

# Leetcode version

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         len_h, len_n = len(haystack), len(needle)            
#         for i in range(len_h - len_n + 1):
#             if haystack[i:i+len_n] == needle:
#                 return i
#         return -1


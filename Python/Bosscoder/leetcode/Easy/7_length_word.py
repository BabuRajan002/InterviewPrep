# 58. Length of Last Word

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.
class Solution:
    def __init__(self, s):
        self.s = s
        
    def lengthOfLastWord(self):
        words = self.s.strip(" ").split()
        return len(words[-1])


if __name__ == "__main__":
    len_word = Solution("luffy is still joyboy")
    print(len_word.lengthOfLastWord())

# #Leetcode version
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         words = s.strip(" ").split()
#         return len(words[-1])
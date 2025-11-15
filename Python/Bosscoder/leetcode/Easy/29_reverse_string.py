# 344. Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

from typing import List
class Solution:
    def __init__(self, s):
        self.s = s
        
    def reverseString(self):
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(self.s)-1
        while left < right:
            self.s[left], self.s[right] = self.s[right], self.s[left]
            left += 1
            right -= 1
        return self.s

if __name__ == "__main__":
    rev = Solution(["h","e","l","l","o"])
    print(rev.reverseString())

        
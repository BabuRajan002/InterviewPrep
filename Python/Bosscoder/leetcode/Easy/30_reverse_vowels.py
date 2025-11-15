class Solution:
    def __init__(self, s):
        self.s = s
    def reverseVowels(self):
        s = self.s
        left, right = 0, len(s)-1
        sa = list(s)
        print(sa)
        while left < right:
            if sa[right] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                sa[left], sa[right] = sa[right], sa[left]
                left += 1
                right -= 1
            left += 1
            right -= 1
        return sa

if __name__ == "__main__":
    vowrev = Solution("leetcode")
    print(vowrev.reverseVowels())
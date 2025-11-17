class Solution:
    def __init__(self, s):
        self.s = s
    def reverseVowels(self):
        s = list(self.s)
        vowels = set('aeiouAEIOU')
        index_arr = []
        for i in range(0, len(s)):
            if s[i] in vowels:
                index_arr.append(i)
               
        l ,r = 0, len(index_arr)-1
        while l < r:
            i , j = index_arr[l], index_arr[r]
            s[i], s[j] = s[j], s[i]
            l += 1
            r -= 1
        return "".join(s)    

if __name__ == "__main__":
    vowrev = Solution("leetcode")
    print(vowrev.reverseVowels())
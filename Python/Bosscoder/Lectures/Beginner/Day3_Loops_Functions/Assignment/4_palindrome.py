# Given an integer x, return true if x is a palindrome , and false otherwise.

# A palindrome number is a number that remains the same when its digits are reversed. For example, 121 and 12321 are palindrome numbers.

class Palindrome:
    def __init__(self, n):
        self.n = n
        
    def check(self):
        num = str(self.n)
        return num == num[::-1]


if __name__ == "__main__":
    pal = Palindrome('1771')
    print(pal.check())

# #Another Solution:
# def isPalindrome(x: int):
#         rev = 0
#         xcopy = x

#         while(x>0):
#             rev = (rev * 10) + (x % 10)
#             x = x // 10
#         return xcopy == rev

# print(isPalindrome(121))
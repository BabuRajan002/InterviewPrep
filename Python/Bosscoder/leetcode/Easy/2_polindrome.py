# Given an integer x, return true if x is a palindrome, and false otherwise.

# class Solution:
def isPalindrome(x: int):

        # num = str(x)
        # reversed_num = []
        # for i in range(len(num)-1, -1, -1):
        #     reversed_num.append(num[i])
        # reversed = "".join(reversed_num)
        # if num == reversed:
        #     return f"true"
        # else:
        #     return f"false"  
        rev = 0
        xcopy = x

        while(x>0):
            rev = (rev * 10) + (x % 10)
            x = x // 10
        return xcopy == rev

print(isPalindrome(121))


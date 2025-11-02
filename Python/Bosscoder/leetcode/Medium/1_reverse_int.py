# 7. Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def __init__(self, x):
        self.x = x
        
    def reverse(self):
        if self.x < 0:            
            sign = -1
        else:
            sign = 1
        number = abs(self.x)
        # nums = [num for num in str(number)]
        # nums.reverse()
        # rev_num = "".join([str(i) for i in nums])
        rev = 0
        while number != 0:
            digit = number % 10
            rev = rev * 10 + digit
            number //= 10

        result = sign * rev
        if result < -2**31 or result > 2**31 -1:
            return 0
        else:
            return result


if __name__ == "__main__":
    numrev = Solution(-432)
    print(numrev.reverse())

# #Leetcode
# class Solution:
#     def reverse(self, x: int) -> int:
#         if x < 0:
#             sign = -1
#         else:
#             sign = 1

#         number = abs(x)
#         rev = 0
#         while number != 0:
#             digit = number % 10
#             rev = rev * 10 + digit
#             number //= 10

#         result = sign * rev 
#         if result < -2**31 or result > 2**31 -1:
#             return 0 
#         else:
#             return result 

# Rule:

# Divisibility Rule Implementation
# The rule states:
# Take the last digit of the number and double it.
# Subtract this result from the remaining part of the number.
# Repeat this process until you get a small number (e.g., one or two digits).
# If the final number is 0 or a multiple of 7 (like 7, 14, 21, -7, -14, etc.), the original number is divisible by 7. 

class DivisibleBySeven:
    def __init__(self, n):
        self.n = n
        
    def check(self):
        n = self.n
        if n < 0:
            return False
        
        if n == 0 or n == 7:
            return True
        if n < 10:
            return False
        
        while n >= 10:
            s = str(n)
            last_digit = int(s[-1])
            remaining_part = int(s[:-1])
            n = remaining_part - 2 * last_digit
        return n == 0 or abs(n) == 7 or abs(n) == 14

if __name__ == "__main__":
    d7 = DivisibleBySeven(23)
    print(d7.check())
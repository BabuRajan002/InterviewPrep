# Write a program to check Armstrong’s number. The Armstrong number can be defined as n-digit numbers equal to the sum of the nth powers of their digits are called Armstrong numbers. Print whether the given number is an Armstrong number or not.

class Armstrong:
    def __init__(self, n):
        self.n = n
        
    def check(self):
        orginal_number = self.n
        length = len(str(self.n))
        sum = 0
        while self.n != 0:
            sum += (self.n % 10) ** length
            self.n = self.n // 10
        return sum == orginal_number

if __name__ == "__main__":
    arm = Armstrong(371)
    print(arm.check())


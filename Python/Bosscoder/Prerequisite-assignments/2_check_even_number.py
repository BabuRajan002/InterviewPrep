# Write a program to check if a given number is even or odd.

class EvenOddPrint:
    def __init__(self, n):
        self.n = n
        
    def check(self):
        if self.n % 2 == 0:
            return f"Even"
        else:
            return f"Odd"

if __name__ == "__main__":
    even_number = EvenOddPrint(8)
    print(even_number.check())
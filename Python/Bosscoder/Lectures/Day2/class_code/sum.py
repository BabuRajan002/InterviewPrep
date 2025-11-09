class Sum:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add_numbers(self):
        return int(self.num1) + int(self.num2)

if __name__ == "__main__":
    number1 = input("Please enter the first number: ")
    number2 = input("Please enter the second number: ")
    sumofnumbers = Sum(number1, number2)
    print(f"Sum of these numbers is : {sumofnumbers.add_numbers()}")
        
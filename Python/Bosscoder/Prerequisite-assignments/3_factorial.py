# Write a program to calculate the factorial of a given number using loops.

class FactorialLoop:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        factorial = 1
        for i in range(1, self.n+1):
            factorial = factorial * i
        return factorial

# if __name__ == "__main__":
factorial_res = FactorialLoop(3)
print(factorial_res.solve())
print(type(factorial_res))

class Factorial:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        number = self.n
        fact = 1
        for i in range(1, number+1):
            fact = fact * i
        return fact


if __name__ == "__main__":
    fact = Factorial(6)
    print(fact.solve())
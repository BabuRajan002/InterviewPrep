import random

class Rand7:
    def __init__(self, n):
        self.n = n
    
    def rand7(self):
        return random.randint(1,7)
    
    def solve(self):
        n = self.n 

        while True:
            a = self.rand7()
            b = self.rand7()

            idx = (a - 1) * 7 + b

            if idx <= 40:
                return (idx - 1) % 10 + 1

if __name__ == "__main__":
    rand = Rand7(3)
    print(rand.solve())

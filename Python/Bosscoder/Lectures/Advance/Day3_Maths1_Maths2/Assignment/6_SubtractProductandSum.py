class SubtractProductandSum:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        original = self.n

        product = 1
        sum = 0

        while original > 0:
            sum += original % 10
            product *= original % 10
            original //= 10
        return product - sum

if __name__ == "__main__":
    prodsum = SubtractProductandSum(4421)
    print(prodsum.solve())

        
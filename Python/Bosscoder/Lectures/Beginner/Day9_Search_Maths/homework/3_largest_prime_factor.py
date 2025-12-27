class LargestPrime:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        n = self.n
        max_prime = 0
        i = 2
        while i * i <= n:
            while n % i == 0:
                max_prime = i
                n = n // i                               
            i += 1
        if n > 1:
            max_prime = n
        return max_prime

if __name__ == "__main__":
    largestPrime = LargestPrime(12)
    print(largestPrime.solve())


# Number,Factors,Type
# 2,"1, 2",Prime
# 3,"1, 3",Prime
# 4,"1, 2, 4",Composite (2 × 2)
# 5,"1, 5",Prime
# 6,"1, 2, 3, 6",Composite (2 × 3)
# 7,"1, 7",Prime

class LargestPrime:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        n = self.n
        max_prime = 0
        i = 2
        while i * i <= n:
            if n % i == 0:
                max_prime = max(max_prime, i)
            i += 1
        return max_prime

if __name__ == "__main__":
    largestPrime = LargestPrime(6)
    print(largestPrime.solve())


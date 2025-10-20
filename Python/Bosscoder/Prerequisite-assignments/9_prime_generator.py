# Write a program that takes an integer n and returns an array of all prime numbers less than or equal to n.
# You should use proper optimization techniques, such as checking up to the square root of a number or using the Sieve of Eratosthenes for efficiency.
import math

class PrimeGenerator:
    def __init__(self, n):
        self.n = n
    
    def solve(self):
        prime_lst = []
        for num in range(self.n + 1):
            if num <= 1:
                continue
            is_prime = True
            for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_lst.append(str(num))      
        return prime_lst

if __name__ == "__main__":
    prime_list = PrimeGenerator(2)
    print(prime_list.solve())




import math

class PrimeRange:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def contains_digits_three(self, num):
        while num > 0:
            if num % 10 == 3:
                return True
            num //= 10
        return False
        
    def check(self):
        prime_lst = []
        for num in range(self.n, self.m + 1):
            if num <= 1:
                continue
            is_prime = True
            for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime and not self.contains_digits_three(num):
                prime_lst.append(str(num))
        if not prime_lst:
            prime_lst.append("No valid primes found.")        
        return prime_lst


if __name__ == "__main__":
    prime_num = PrimeRange(10, 20)
    print(prime_num.check())
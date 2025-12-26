class Even:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        sum = 0
        n = self.n
        i = 1

        while i * i <= n:
            if n % i == 0:
                  a = i
                  b = n // i

                  if a % 2 == 0:
                        sum += a
                  if b % 2 == 0 and b != a:
                        sum += b
            i += 1
        return sum

if __name__ == "__main__":
     even = Even(30)
     print(even.solve())

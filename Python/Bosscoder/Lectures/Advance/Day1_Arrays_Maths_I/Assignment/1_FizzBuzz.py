class FizzBuzz:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        n = self.n
        ans = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
               ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(i)
        return ans

if __name__ == "__main__":
    fb = FizzBuzz(15)
    print(fb.solve())
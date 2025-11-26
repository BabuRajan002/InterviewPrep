# Write a function to find sum of all even numbers from 1 to N.

class Sum:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        sum = 0
        for num in range(1,self.n+1):
            if num % 2 == 0:
                sum += num
        return sum

if __name__ == "__main__":
    eve = Sum(6)
    print(eve.solve())
# Write a function to print the average of 3 numbers. Return result in integer form only.


class Average:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def solve(self):
        return int((self.a + self.b + self.c) / 3)

if __name__ == "__main__":
    avg = Average(1,2,3)
    print(avg.solve())
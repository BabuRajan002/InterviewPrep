# Write a program that prints a conditional multiplication table for a given number.
# You are given two integers:
# n — the base number for the multiplication table
# m — the range limit (inclusive) up to which the table should be printed
# Your task is to print only those results from the multiplication table of n (from 1 to m) that satisfy both of the following conditions:
# The product n * i is an even number
# The product n * i is divisible by 4
# Each qualifying line should be printed in the following format: n x i = result
# If no such result exists within the range, print: No qualifying multiples found.

class MultiplicationTableConditional:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        
    def solve(self):
        multi_table = []
        for i in range(1, self.m+1):
            result = self.n * i 
            if result % 2 == 0 and result % 4 == 0:
                    multi_table.append(f"{self.n} x {i} = {result}")
        if not multi_table:
             multi_table.append("No qualifying multiples found.")
        return multi_table

if __name__ == "__main__":
    table = MultiplicationTableConditional(3,10)
    for item in table.solve():
         print(item)




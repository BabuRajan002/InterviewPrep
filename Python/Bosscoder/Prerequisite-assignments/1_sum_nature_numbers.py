# Write a program to calculate the sum of the first N natural numbers.
# Input 1: N = 5
# Output 1: 15
# Explanation 1: (1 + 2 + 3 + 4 + 5).

# Input 2: N = 13
# Output 2: 91
# Constraints:
# 1 <= N <= 109

class SumofFirstNNaturalNumbers:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        sum = 0
        for i in range(1,self.n+1):
            sum += i
        return sum

if __name__ == "__main__":
    sum_result = SumofFirstNNaturalNumbers(13)
    print(sum_result.solve())


class SumZero:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        ans = []
        k = self.n // 2

        for i in range(1, k+1):
            ans.append(i)
            ans.append(-i)
        
        if self.n % 2 != 0:
            ans.append(0)
        
        return ans

if __name__ == "__main__":
    sumzero = SumZero(5)
    print(sumzero.solve())    
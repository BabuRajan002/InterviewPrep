class DifferenceofSum:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        arr = self.arr
        total = sum(arr)
        summ = 0
        for num in arr:
            while num > 0:
                summ = summ + (num % 10)
                num //= 10
        return total - summ

if __name__ == "__main__":
    diffsum = DifferenceofSum([1,2,3,4])
    print(diffsum.solve())
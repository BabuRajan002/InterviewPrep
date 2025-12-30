class PairDivisibleByK:
    def __init__(self, arr, k):
        self.arr = arr 
        self.k = k 

    def solve(self):
        arr = self.arr 
        k = self.k 

        left = 0 
        right = len(arr) - 1

        n = len(arr) // 2
        while left <= n and right >= n:
            print(arr[left], arr[right], arr[left] + arr[right])
            if (arr[left] + arr[right]) % k != 0:
                return False
            left += 1
            right -= 1

        return True

if __name__ == "__main__":
    pairdiv = PairDivisibleByK([-1,1,-2,2,-3,3,-4,4], 3)
    print(pairdiv.solve())
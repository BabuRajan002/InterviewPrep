class PairDivisibleByK:
    def __init__(self, arr, k):
        self.arr = arr 
        self.k = k 

    def solve(self):
        arr = self.arr 
        k = self.k 
        
        remCount = {}
        for num in arr:
            remCount[(num % k + k) % k] = remCount.get((num % k + k) % k, 0) + 1
        
        for i in arr:
            rem = (i % k + k) % k

            if rem == 0:
                if remCount[rem] % 2 == 1:
                    return False
            
            elif remCount[rem] != remCount.get(k - rem, 0):
                return False
        return True


if __name__ == "__main__":
    pairdiv = PairDivisibleByK([1,2,3,4,5,6], 10)
    print(pairdiv.solve())
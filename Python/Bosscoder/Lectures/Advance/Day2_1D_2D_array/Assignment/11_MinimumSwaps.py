class MinimumSwaps:
    def __init__(self, arr, k):
        self.arr = arr 
        self.k = k
    
    def solve(self):
        arr = self.arr 
        k = self.k

        remMap = {}

        for num in arr:
            rem = num % k
            if rem < 0:
                rem += k
            remMap[rem] = remMap.get(rem, 0) + 1
        
        for key, value in remMap.items():
            print(key, value)

        # return remMap
    

if __name__ == "__main__":
    minswaps = MinimumSwaps([1,10,2,3,20,4,5], 5)
    print(minswaps.solve())



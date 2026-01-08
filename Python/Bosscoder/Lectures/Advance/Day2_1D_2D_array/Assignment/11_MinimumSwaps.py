class MinimumSwaps:
    def __init__(self, arr, k):
        self.arr = arr 
        self.k = k
    
    def solve(self):
        arr = self.arr 
        k = self.k
        n = len(arr)

        favCount = 0
        for num in arr:
            if num <= k:
                favCount += 1
        
        badElements = 0
        for i in range(favCount):
            if arr[i] > k:
                badElements += 1
        minSwaps = badElements

        i = 0 
        j = favCount
        while j < n:
            if arr[i] > k:
                badElements -= 1
            
            if arr[j] > k:
                badElements += 1
            
            minSwaps = min(minSwaps, badElements)

            j += 1
            i += 1
        return minSwaps

if __name__ == "__main__":
    minswap = MinimumSwaps([2, 7, 9, 5, 8, 7, 4], 5)
    print(minswap.solve())



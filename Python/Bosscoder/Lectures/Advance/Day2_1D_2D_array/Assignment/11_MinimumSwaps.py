class MinimumSwaps:
    def __init__(self, arr, k):
        self.arr = arr 
        self.k = k
    
    def solve(self):
        arr = self.arr
        k = self.k
        n = len(arr)
        favCount = 0
        badElements = 0
        
        #Total number of elements lesser than k. This is the sliding window size
        for i in range(n):
            if arr[i] <= k:
                favCount += 1
                 
        for i in range(favCount):
            if arr[i] > k:
                badElements += 1
                
        minSwaps = badElements
        i = 0
        j = favCount

        while j < n:
            if arr[i] >k:
                badElements -= 1
            
            if arr[j] > k:
                badElements += 1
            minSwaps = min(minSwaps, badElements)
            i += 1
            j += 1        
        return minSwaps
if __name__ == "__main__":
    minswap = MinimumSwaps([2,1,5,6,3], 3)
    print(minswap.solve())



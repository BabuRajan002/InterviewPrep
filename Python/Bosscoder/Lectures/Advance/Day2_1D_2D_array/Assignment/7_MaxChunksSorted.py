class MaxChunksSorted:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        arr = self.arr
        n = len(arr)
        max_left = 0
        min = float('inf')
        min_right = []
        count = 0

        for i in range(n-1, -1, -1):
            if arr[i] < min:
                min = arr[i]
            min_right.append(min)
        
        min_right.sort()

        for i in range(n-1):
            max_left = max(max_left,arr[i])
            if max_left <= min_right[i+1]:
                count += 1
        return count +1

if __name__ == "__main__":
    machunk = MaxChunksSorted([2,1,3,4,4])
    print(machunk.solve())
            
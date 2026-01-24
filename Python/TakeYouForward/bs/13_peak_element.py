class Peak:
    def __init__(self, arr):
        self.arr = arr 
    
    def solve(self):
        arr = self.arr 

        low = 0
        high = len(arr) - 1

        while low < high:
            mid = (low + high) // 2

            if arr[mid] > arr[mid+1]:
                high = mid
            else:
                low = mid + 1
        return low 

if __name__ == "__main__":
    peak = Peak([1,2,3,4,5,6,7,8,5,1])
    print(peak.solve())

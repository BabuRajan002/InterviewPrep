class Sort:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        n = len(self.arr)
        for round in range(1,n):
            i = round
            while i > 0 and self.arr[i] < self.arr[i-1]:
                temp = self.arr[i-1]
                self.arr[i-1] = self.arr[i]
                self.arr[i] = temp
                i -= 1
        return self.arr

if __name__ == "__main__":
    ins = Sort([5, 1, 4, 2, 8])
    print(ins.solve())


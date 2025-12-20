class Sort:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        for round in range(len(self.arr)):
            i = round
            flag = 'False'
            for i in range(len(self.arr)-round-1):
                if self.arr[i] > self.arr[i+1]:
                    temp = self.arr[i]
                    self.arr[i] = self.arr[i+1]
                    self.arr[i+1] = temp
                    flag = 'True'
            if flag == "False":
                break
        return self.arr     

if __name__ == "__main__":
    bs = Sort([5, 1, 4, 2, 8])
    print(bs.solve())


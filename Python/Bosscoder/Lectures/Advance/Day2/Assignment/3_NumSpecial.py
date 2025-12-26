class NumSpecial:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        arr = self.arr
        r = len(arr)
        c = len(arr[0])
        row = [0] * r
        col = [0] * c
        count = 0
        for i in range(r):
            for j in range(c):
                if arr[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        
        for i in range(r):
            for j in range(c):
                if arr[i][j] == 1 and row[i] == 1 and col[j] == 1:
                    count += 1

        return count
    

if __name__ == "__main__":
    numspecial = NumSpecial([[1,0,0],[0,0,1],[1,0,0]])
    print(numspecial.solve())

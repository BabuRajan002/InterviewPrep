class OddCells:
    def __init__(self,n,m, arr):
        self.n = n #row 
        self.m = m #Col
        self.arr = arr
        
    def solve(self):
        rows, columns = [0] * self.n, [0] * self.m
        sum = 0
        for r ,c in self.arr:
            rows[r] += 1
            columns[c] += 1
        
        for i in range(self.n):
            for j in range(self.m):
                if rows[i] + columns[j] % 2 == 1:
                    sum += 1
        
        return sum

           
            


if __name__ == "__main__":
    oc = OddCells(2,3,[[0,1],[1,1]])
    print(oc.solve())
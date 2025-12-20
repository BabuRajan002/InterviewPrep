class OddCells:
    def __init__(self,n,m, arr):
        self.n = n #row 
        self.m = m #Col
        self.arr = arr
        
    def solve(self):
        defaul_val = 0
        n = self.n
        m = self.m
        indices = self.arr
        mat = [[defaul_val for _ in range(m)] for _ in range(n)]
        for ri, ci in indices:
            for j in range(m):
                mat[ri][j] += 1
            
            for i in range(n):
                mat[i][ci] += 1
        odd_count = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] % 2 == 1:
                    odd_count += 1
        return odd_count          


if __name__ == "__main__":
    oc = OddCells(2,3,[[0,1],[1,1]])
    print(oc.solve())
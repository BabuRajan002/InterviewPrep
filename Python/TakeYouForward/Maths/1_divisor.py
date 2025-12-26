class Divisor:
    def __init__(self,n):
        self.n = n
    
    def solve(self):
        number = int(self.n ** 0.5)
        n = self.n
        ans = []
        for i in range(1,number+1):
            if n % i == 0:
                ans.append(i)               
                if n // i != i:
                    ans.append(int(n//i))
        ans.sort()
        return ans

if __name__ == "__main__":
    div = Divisor(36)
    print(div.solve())


         

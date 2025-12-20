class Prime:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        n = self.n
        number = int(self.n ** 0.5)
        ans = []
        for i in range(2,number):
                print(i)
                while (n%i == 0):
                    ans.append(int(i))                    
                    n = n / i                
        if n != 1:
            ans.append(int(n))
        return ans

if __name__ == "__main__":
    prime = Prime(320)
    print(prime.solve())

# class Prime:
#     def __init__(self, n):
#         self.n = n
        
#     def solve(self):
#         n = self.n
#         ans = []
#         i = 2
        
#         # The limit updates automatically as n decreases
#         while i * i <= n:
#             if n % i == 0:
#                 ans.append(i)
#                 n //= i
#                 # Note: we don't increment i here because 
#                 # we want to check the same factor again (like 3, 3)
#             else:
#                 i += 1
        
#         # If there's anything left, it's the final prime factor
#         if n > 1:
#             ans.append(n)
            
#         return ans

# if __name__ == "__main__":
#     prime = Prime(315)
#     print(prime.solve()) # Output: [3, 3, 5, 7]
# Notes:

# Why we stop at the Square RootMathematically, a number $n$ cannot have more than one prime factor larger than $\sqrt{n}$. In your case, $\sqrt{315} \approx 17.7$. Once your loop finishes checking small numbers, if any $n$ is left over, that remainder must be prime.
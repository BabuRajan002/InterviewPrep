class Solution:
    def __init__(self,n):
        self.n = n
        
    def reverseBits(self):
        n = self.n[::-1]
        return int(n,2)

if __name__ == "__main__":
    reversebits = Solution('11111111111111111111111111111101')
    print(reversebits.reverseBits())

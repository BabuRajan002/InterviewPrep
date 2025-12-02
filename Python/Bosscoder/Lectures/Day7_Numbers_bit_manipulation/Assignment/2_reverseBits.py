class Solution:
    def __init__(self,n):
        self.n = n
        
    def reverseBits(self):
        n = self.n
        deci_number = str(int(n,2))
        return deci_number[::-1]

if __name__ == "__main__":
    reversebits = Solution('00000010100101000001111010011100')
    print(reversebits.reverseBits())

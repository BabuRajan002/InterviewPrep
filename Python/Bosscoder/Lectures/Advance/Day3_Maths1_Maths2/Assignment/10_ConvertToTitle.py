class ConvertToTitle:
    def __init__(self, n):
        self.n = n
    
    def solve(self):
        res = ""

        n = self.n

        while n > 0:
            n -= 1
            res = chr((n % 26) + ord("A")) + res
            n //= 26
        return res

if __name__ == "__main__":
    convert = ConvertToTitle(1)
    print(convert.solve())

#Notes:

# “Excel columns use a 1-indexed base-26 system where A=1 and Z=26, unlike normal base-26 which is 0-indexed.
# To handle this, I subtract 1 from the number before applying modulo.
# Each modulo gives me a letter, and integer division reduces the number for the next iteration.
# I prepend characters because we extract from least significant to most significant position.”
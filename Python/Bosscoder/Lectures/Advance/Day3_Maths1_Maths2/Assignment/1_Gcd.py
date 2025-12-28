class Gcd:
    def __init__(self, arr):
        self.arr = arr
        
    def gcd(self):
        nums = self.arr
        a = max(nums)
        b = min(nums)

        while (a > 0 and b > 0):
            if a > b:
                a = a % b
            else:
                b = b % a
        if a == 0:
            return b
        if b == 0:
            return a

if __name__ == "__main__":
    gcdarr = Gcd([7,5,6,8,3])
    print(gcdarr.gcd())

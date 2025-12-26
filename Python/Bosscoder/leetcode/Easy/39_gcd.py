class Gcd:
    def __init__(self,nums):
        self.nums = nums
    
    def solution(self):
        nums = self.nums
        a = max(nums)
        b = min(nums)

        while (a > 0 and b > 0):
            if a > b:
                a = a % b
            else:
                b = b % a
        
        if a == 0:
            return b
        else:
            return a

if __name__ == "__main__":
    gcd = Gcd([3,3])
    print(gcd.solution())
       
class MissingNumber:
    def __init__(self, nums):
        self.nums = nums
    
    def solve(self):
        nums = self.nums
        n = len(nums)
        sumOfNumbers = sum(nums)

        sumOfNatural = n * (n + 1) // 2

        return sumOfNatural - sumOfNumbers

if __name__ == "__main__":
    missing = MissingNumber([9,6,4,2,3,5,7,0,1])
    print(missing.solve())
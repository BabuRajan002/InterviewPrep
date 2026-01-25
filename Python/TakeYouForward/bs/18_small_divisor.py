import math

class SmallDivisor:
    def __init__(self, nums, limit):
        self.nums = nums 
        self.limit = limit 
    
    def solve(self):
        nums = self.nums 
        limit = self.limit

        low = 1 
        high = max(nums)
        # ans = high

        while low <= high:
            mid = (low + high) // 2           
            div_sum = 0
            for num in nums:
                div_sum += math.ceil (num / mid )
            if div_sum > limit:
                low = mid + 1
            else:
                # ans = mid
                high = mid - 1
        return low

if __name__ == "__main__":
    smalldiv = SmallDivisor([1,2,5,9], 6)
    print(smalldiv.solve())

                



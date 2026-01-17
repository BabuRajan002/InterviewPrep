class HighestOccur:
    def __init__(self, nums):
        self.nums = nums
    
    def solve(self):
        nums = self.nums 

        freq = {}
        for num in nums:
                freq[num] = freq.get(num, 0) + 1

        mx_freq = 0
        for num, count in freq.items():
             if count > mx_freq:
                  mx_freq = count
        return count
                  

if __name__ == "__main__":
    high = HighestOccur([3, 3, 3, 2, 1])
    print(high.solve())
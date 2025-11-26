# You are given a 0-indexed integer array nums and an integer k. Your task is to perform the following operation exactly k times in order to maximize your score:

# Select an element m from nums.

# Remove the selected element m from the array.

# Add a new element with a value of m + 1 to the array.

# Increase your score by m.

# Return the maximum score you can achieve after performing the operation exactly k times.

class MaximizeSum:
    def __init__(self, arr,k):
        self.arr = arr
        self.k = k
        
    def solve(self):
        nums = self.arr
        nums.sort()
        i = 1
        sum = 0
        m = nums[-1]
        while i <= self.k:
            sum = sum + m
            m += 1
            i += 1          
        return sum
    
if __name__ == "__main__":
    maxsum = MaximizeSum([5,5,5],2)
    print(maxsum.solve())


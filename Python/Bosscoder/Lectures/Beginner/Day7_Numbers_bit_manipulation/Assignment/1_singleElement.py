# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

class SingleElement:
    def __init__(self, arr):
        self.arr = arr
        
    def find(self):
        xor = 0
        for num in self.arr:
            xor ^= num
        return xor

if __name__ == "__main__":
    se = SingleElement([4,1,2,1,2])
    print(se.find())

        

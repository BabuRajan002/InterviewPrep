## My Brute force Solution

class Inversion:
    def __init__(self, arr):
        self.arr = arr
        
    def count(self):
        nums = self.arr
        count = 0
        for i in range(len(nums)):            
          for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                count += 1
        return count

if __name__ == "__main__":
    inv = Inversion([1,20,6,4,5])
    print(inv.count())

# Optimized Solution with Merge Sort:


               
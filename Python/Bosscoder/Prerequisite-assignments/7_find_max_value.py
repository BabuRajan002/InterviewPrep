# Write a program to find and return the largest number in an array.
# You must not use any built-in max() functions or library methods that directly give the maximum value.

class LargestElement:
    def __init__(self, arr):
        self.arr = arr
    
    def solve(self):
        temp = self.arr[0]
        for num in self.arr:
            if num > temp:
                temp = num
        return temp
    

if __name__ == "__main__":
  max_val = LargestElement([10, 4, 2, 99, 23])
  print(max_val.solve())
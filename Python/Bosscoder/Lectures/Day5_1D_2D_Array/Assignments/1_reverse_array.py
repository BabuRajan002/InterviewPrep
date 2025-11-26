class ReverseArray:
    def __init__(self, arr):
        self.arr = arr
        
    def reverse(self):
        return self.arr[::-1]

if __name__ == "__main__":
    rev = ReverseArray([1,2,3,4,5])
    print(rev.reverse())
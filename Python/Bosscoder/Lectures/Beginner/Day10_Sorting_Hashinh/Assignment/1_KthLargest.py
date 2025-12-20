class KthLargest:
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k
        
    def solve(self):
        nums = self.arr
        k = self.k
        nums.sort()

        return nums[-k]

if __name__ == "__main__":
    kth = KthLargest([3,2,3,1,2,4,5,5,6], 4)
    print(kth.solve())

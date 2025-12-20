class RichestCustomerWealth:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        arr = self.arr
        max = 0
        for nums in arr:
            total = sum(nums)
            if total > max:
                max = total
        return max

if __name__ == "__main__":
    rcw = RichestCustomerWealth([[1,5],[7,3],[3,5]])
    print(rcw.solve())

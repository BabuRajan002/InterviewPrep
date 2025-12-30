class MaxConsecutiveOnes:
    def __init__(self, arr):
        self.arr = arr
        
    def count(self):
        arr = self.arr
        mx = 0
        sum = 0
        for num in arr:
            if num == 1:
                sum += 1
                mx = max(mx, sum)
            else:
                sum = 0
        return mx

if __name__ == "__main__":
    maxconsectiveones = MaxConsecutiveOnes([1,0,1,1,0,1])
    print(maxconsectiveones.count())

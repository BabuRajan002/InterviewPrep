class sortColors:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        # n = max(self.arr)+1
        # nums = self.arr

        # ans = [0]*n
        # for num in nums:
        #     ans[num] += 1
        
        # for i in range(len(ans)):
        #     temp = ans[i]
        #     while temp > 0:
        #         print(i, end=",")
        #         temp -= 1
        count = [0,0,0]
        nums = self.arr
        for num in nums:
            count[num] += 1
        
        result = []
        for value in range(3):
            result.extend([value] * count[value])
        
        return result


if __name__ == "__main__":
    sc = sortColors([0,2,2,1,1,1,1,1,1,1,0,0,0,0])
    print(sc.solve())
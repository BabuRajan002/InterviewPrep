class CountGoodRectangles:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        arr = self.arr
        ans = []
        m = len(arr)
        n = len(arr[0])
        count = 0
        for rect in arr:
            i = 0
            if rect[i] < rect[i+1]:
                ans.append(rect[i])
            else:
                ans.append(rect[i+1])
        max_len = max(ans)
        print(max_len)

        for rect in arr:
            if min(rect) == max_len:
                count += 1
        return count


if __name__ == "__main__":
    cgr = CountGoodRectangles([[2,3],[3,7],[4,3],[3,7]])
    print(cgr.solve())



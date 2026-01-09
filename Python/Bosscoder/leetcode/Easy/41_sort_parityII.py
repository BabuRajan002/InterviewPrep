class SortByParity:
    def __init__(self, arr):
        self.arr = arr
    
    def solve(self):
        # arr = self.arr 
        # evenArr = []
        # oddArr = []
        # n = len(arr)
        # ans = [0] * n

        # for i in range(n):
        #     if arr[i] % 2 == 0:
        #         evenArr.append(arr[i])
        #     else:
        #         oddArr.append(arr[i])
 
        # for i in range(n//2):
        #     ans[2 * i] = evenArr[i]
        #     ans[2 * i + 1] = oddArr[i]
        # return ans
        nums = self.arr
        n = len(nums)
        ans = [0] * n
        evenIndex = 0
        oddIndex = 1

        for i in range(n):
            if nums[i] %2 == 0:
                ans[evenIndex] = nums[i]
                evenIndex += 2

            else:
                ans[oddIndex] = nums[i]
                oddIndex += 2
        
        return ans



if __name__ == "__main__":
    sortbypair = SortByParity([4,2,5,7])
    print(sortbypair.solve())
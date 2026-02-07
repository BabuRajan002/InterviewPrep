class BubbleSort:
    def __init__(self, nums):
        self.nums = nums
    def solve(self):
        nums = self.nums 
        n = len(nums)
        for round in range(n):
            i = round
            flag = 'False'
            for i in range(n-round-1):
                if nums[i] > nums[i+1]:
                    temp = nums[i]
                    nums[i] = nums[i+1] 
                    nums[i+1] = temp 
                    flag = 'True'
            if flag == 'False':
                break
        return nums

if __name__ == "__main__":
    bubble = BubbleSort([7, 4, 1, 5, 3])
    print(bubble.solve())
                

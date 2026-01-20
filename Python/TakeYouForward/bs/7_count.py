class CountOccur:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target 
    
    def countLeft(self):
        arr = self.arr 
        target = self.target

        left = 0
        right = len(arr) - 1
        leftCount = -1
        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                leftCount = mid
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return leftCount
    
    def countRight(self):
        arr = self.arr 
        target = self.target

        left = 0
        right = len(arr) - 1
        rightCount = -1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                rightCount = mid
                left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return rightCount 
    
if __name__ == "__main__":
    countoccur = CountOccur([5,5,5,5,5,5], 5)
    total = countoccur.countRight() - countoccur.countLeft() + 1
    print(total)





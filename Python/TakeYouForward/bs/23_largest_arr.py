class Books:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
    
    def booksAllocation(self, nums, pages):
        countStudent = 1
        pagesCount = 0
        for i in range(len(nums)):
            if pagesCount + nums[i] <= pages:
                pagesCount += nums[i]
            else:
                countStudent += 1
                pagesCount = nums[i]
        return countStudent

    
    def solve(self):
        nums = self.nums 
        k = self.k 

        low = max(nums)
        high = sum(nums)
        if k > len(nums):
            return -1

        while low <= high:
            mid = (low + high) // 2
            studentCount = self.booksAllocation(nums, mid)
            if studentCount <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low 
if __name__ == "__main__":
    books = Books( [1, 2, 3, 4, 5], 3)
    print(books.solve())

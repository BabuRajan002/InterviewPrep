class GoodPairs:
    def __init__(self, arr):
        self.arr = arr
        
    def count(self):
        count = 0
        pairs = {}
        nums = self.arr
        for i in range(len(nums)):
            if nums[i] in pairs:
                count += pairs[nums[i]]            
            pairs[nums[i]] = pairs.get(nums[i], 0) + 1
        return count

if __name__ == "__main__":
    gp = GoodPairs([1,2,3,1,1,3])
    print(gp.count())
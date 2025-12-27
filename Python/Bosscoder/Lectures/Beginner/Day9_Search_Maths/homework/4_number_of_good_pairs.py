class GoodPair:
    def __init__(self, nums):
        self.nums = nums
    
    def solve(self):
        count = 0
        pairs = {}
        nums = self.nums
        for i in range(len(nums)):
            if nums[i] in pairs:
                print(count)
                count += pairs[nums[i]]
            
            pairs[nums[i]] = pairs.get(nums[i], 0) + 1
        return count

        # nums = self.nums
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i < j and nums[i] == nums[j]:
        #             count += 1
        # return count

if __name__ == "__main__":
    goodpair = GoodPair([1,2,3,1,1,3])
    print(goodpair.solve())
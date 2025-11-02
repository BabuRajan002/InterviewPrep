# Q48. Set Mismatch
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

class Solution:
    def __init__(self, nums):
        self.nums = nums
    
    def findErrorNums(self):
        nums = self.nums 
        repeated_list = []
        # repeat_num = [i for i in set(nums) if nums.count(i) > 1]
        for i in set(nums):
            if nums.count(i) > 1:
                repeated_list.append(i)
                repeated_list.append(i+1)
        return repeated_list
        

if __name__ == "__main__":
    repeat = Solution([1,1])
    print(repeat.findErrorNums())

# #Leetcode version
# class Solution:
#     def findErrorNums(self, nums: List[int]) -> List[int]:
#         actual_sum = sum(nums)
#         duplicate = actual_sum - sum(set(nums))

#         n = len(nums)
#         expected_sum = n * (1 + n) // 2

#         missing = expected_sum + duplicate - actual_sum

#         return [duplicate, missing]
 



        

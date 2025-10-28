class Solution:
    def __init__(self, nums):
        self.nums = nums
    
    def removeDuplicates(self):
        length = len(self.nums)
        unique_lst = sorted(list(set(self.nums)))
        k = len(unique_lst)
        diff_len = length - len(unique_lst)
        # for i in range(diff_len):
        #     unique_lst.append('_')
        return f"{k}, nums = {unique_lst}"       

if __name__ == "__main__":
    elements = Solution([0,0,1,1,1,2,2,3,3,4])
    print(elements.removeDuplicates())

# #Leetcode version
# from typing import List
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         unique_lst = sorted(list(set(nums)))
#         k = len(unique_lst)
#         nums[:k] = unique_lst
#         return k
        
    
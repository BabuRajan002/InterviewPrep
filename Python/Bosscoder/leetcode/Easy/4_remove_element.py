class Solution:         
     def __init__(self, nums, val):
         self.nums = nums
         self.val = val
     
     def removeElement(self):
          for i in range(len(self.nums)-1, -1, -1):
               if self.nums[i] == self.val:
                    self.nums.remove(self.nums[i])
          
          return len(self.nums), self.nums

if __name__ == "__main__":
     remove_num = Solution([0,1,2,2,3,0,4,2], 2)
     print(remove_num.removeElement())
          
        

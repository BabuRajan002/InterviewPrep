# Given the array nums consisting of n(n will be even) elements in the form [x1,x2,...,xn,y1,y2,...,yn]. Return the array in the form [x1,y1,x2,y2,...,xn,yn].
class Shuffle:
    def __init__(self, arr):
        self.arr = arr
        
    def shuffle(self):
        nums = self.arr
        ans = []
        n = len(nums) // 2        
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans

if __name__ == "__main__":
    shuff = Shuffle([2,5,1,3,4,7])
    print(shuff.shuffle())
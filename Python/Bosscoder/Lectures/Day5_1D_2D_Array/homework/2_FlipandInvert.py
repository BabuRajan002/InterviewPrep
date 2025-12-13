# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1,1,0] horizontally results in [0,1,1]. To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

class FlipandInvert:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        nums = self.arr
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i][j] == 0:
                    nums[i][j] = 1
                else:
                    nums[i][j] = 0
        
        for num in nums:
            ans.append(num[::-1])
        
        return ans          
         

if __name__ == "__main__":
    fi = FlipandInvert([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])
    print(fi.solve())
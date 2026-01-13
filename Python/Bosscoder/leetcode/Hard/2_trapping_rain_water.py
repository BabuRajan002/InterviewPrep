class Trapping:
   def __init__(self, height):
      self.height = height 
   
   def solve(self):
      height = self.height 
      l ,r = 0, len(height) - 1
      leftMax = height[l]
      rightMax = height[r]

      totalWater = 0

      while l < r:

        if leftMax < rightMax:
            l += 1 
            leftMax = max(leftMax, height[l]) 
            totalWater += leftMax - height[l]
            print(totalWater)
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            totalWater += rightMax - height[r]
            print(totalWater)
      return totalWater

if __name__ == "__main__":

  trap = Trapping([0,1,0,2,1,0,1,3,2,1,2,1])  
  print(trap.solve())
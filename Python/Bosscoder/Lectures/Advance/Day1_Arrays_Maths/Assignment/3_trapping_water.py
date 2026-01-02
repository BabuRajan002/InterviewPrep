# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class TrappingRainwater:
    def __init__(self, arr):
        self.arr = arr
    
    def trap(self):
        arr = self.arr 
        n = len(arr)

        water = 0
        for i in range(n):
            leftMaxBuildingHeight = 0
            rightMaxBuildingHeight = 0

            for l in range(i):
                leftMaxBuildingHeight = max(leftMaxBuildingHeight, arr[l])

            
            for r in range(i+1, n):
                rightMaxBuildingHeight = max(rightMaxBuildingHeight, arr[r])

            
            trapped = min(leftMaxBuildingHeight, rightMaxBuildingHeight) - arr[i]

            if trapped > 0:
                water += trapped
        return water

if __name__ == "__main__":
    trapping = TrappingRainwater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(trapping.trap())
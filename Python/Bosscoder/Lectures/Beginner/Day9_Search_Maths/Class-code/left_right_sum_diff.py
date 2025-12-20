def leftRightSumDiff(nums):
    leftsum = 0
    totalsum = sum(nums)
    ans = []
    for i in range(len(nums)):
        rightsum = totalsum - leftsum - nums[i]
        ans.append(abs(leftsum-rightsum))
        leftsum += nums[i]
    return ans

print(leftRightSumDiff([10,4,8,3]))

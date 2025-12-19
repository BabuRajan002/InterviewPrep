def addElements(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        nums[i] = sum
    return nums

print(addElements([5,2,7,9,1]))

def maxProduct(nums):
    ln = 0
    sl = 0
    for i in range(len(nums)):
       if nums[i] > ln:
           sl = ln
           ln = nums[i]
       elif nums[i] > sl:
           sl = nums[i]
           
    return (ln-1)*(sl-1)
print(maxProduct([3,4,5,2]))
# Find the Longest   subarray with the sum k=3. Where the arr = [1,2,3,1,1,1,1,4,2,3] k=3 [Positivies]

# Brute - Force! 
# Step1 - Generate all the subarrays. 

# def subArray(nums, k):
#     n = len(nums)
#     sum = 0
#     mx = 0
#     lengthSubarray = 0
#     for i in range(n):        
#         for j in range(i,n):
#             sum = 0
#             for l in range(i,j+1):
#                 sum += nums[l]
#             if sum == k:
#                 lengthSubarray = max(lengthSubarray, j - i +1)
#     return lengthSubarray

# print(subArray([1,2,3,1,1,1,1,4,2,3],3))

#Time Complexity for the method is Some where around O(n^3) but not exactly.
# No space complexity.

###########################################################################################################################################

# 2. Improved than the above method:

# def subArray(nums, k):
#     n = len(nums)
#     sum = 0
#     lengthSubarray = 0
#     for i in range(n):
#         sum = 0     
#         for j in range(i,n):           
#             sum += nums[j]
#             if sum == k:
#                 lengthSubarray = max(lengthSubarray, j - i +1)
#     return lengthSubarray

# print(subArray([1,2,3,1,1,1,1,4,2,3],3))

# TC Is bit reduced here which is somewhere around O(N^2).

###########################################################################################################################################

# 3. Better Solution with Hashing (Directory) and prefix Sum

def subArray(nums, k):
    preSumdict = {}
    sum = 0
    maxLen = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum == k:
            maxLen = max(maxLen,i+1)
        rem = sum - k
        if rem in preSumdict:
            length = i - preSumdict[rem]
            maxLen = max(maxLen, length)
        
        if sum not in preSumdict:
            preSumdict[sum] = i   

    return maxLen



print(subArray([1,2,3,1,1,1,1,1,4,2,3],4))

# Key takeaway (interview gold line)

# For “count of subarrays”, the prefix-sum map must store frequencies,
# whereas for “longest subarray”, it stores earliest indices.









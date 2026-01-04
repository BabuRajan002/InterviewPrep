# Time Complexity and 1D and 2D arrays:


# 11:07 AM 724. Find the Pivot index --> Leetcode

## Brute Force
- Calculate the Prefix and Suffix sum for a particular 'i' index.
- If both are equal at any point of time then return the index0
- left sum [0 to i-1] #Run a loop
- right sum [i+1 to n-1] #Run a loop
- TC: O(N^2) 

## Optimized version:

- rightSum = total - leftSum - nums[i] ---> To calculate the rightSum
- Keeping adding the leftSum for each Iteration.


```
totalSum = 0
n = len(nums)

for i in range(n):
  totalSum += nums[i]

leftSum = 0
for i in range(n):
  
  rightSum = totalSum - leftSum - nums[i]
  
  if leftSum == rightSum:
     return i
  
  leftSum += nums[i]

return -1

```

# 11:42 AM 121. Best Time to Buy and Sell Stock ---> Leetcode

```
n = len(prices)
cheapStock = prices[0]
ans = 0

for i in range(1,n):
   if cheapStock < prices[i]:
      ans = max(ans, prices[i] - cheapStock)
   
   cheapStock = min(cheapStock, prices[i])

return ans

```

# 283. Move Zeros ---> Leetcode

- Solved using the pointers
- K should always sitting in one of the zeros (That is the alogirthm)
- i is traversing if its found any non-zero value just swap with k and increase the K

```
n = len(nums)

k = 0

for i in range(n):
  if nums[i] != 0:
     swap(nums[i], nums[k]) # Find the relevant syntax in Python
     k += 1
return nums
```

# 12:28 PM 75. Sort Colors --> Leetcode

- Calculate the frequency of each numbers

```
n = len(nums)
count0 = 0
count1 = 0 
count2 = 0

for i in range(n):
  if nums[i] == 0:
    count0 += 1
  elif nums[i] == 1:
    count1 += 1
  else:
    count2 += 1

index = 0

while count0 > 0:
  nums[index] = 0
  count0 -= 1
  index += 1

while count1 > 0:
  nums[index] = 1
  count1 -= 1
  index += 1

while count2 > 0:
  nums[index] = 2
  count2 -= 1
  index += 1

return nums
```

# 1:15 1572.Matrix Diagonal Sum --- leetcode

- o(N) solution

- formula is `if i == j or i + j == n -1`

# 1:37  PM Remove duplicates ---> leetcode

```
n = len(nums)

i = 0
for j in range(n):
  if nums[i] != nums[j]:
    i += 1
    swap(nums[i], nums[j])

return i+1
```

# 1:57 PM 1480. Running sum of 1D array

- Homework




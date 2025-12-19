def maxPair(nums):
    freq = [0] * 101 # 101 got it feom the question constraints
    for num in nums:
        freq[num] += 1
    p = 0
    lo = 0
    for f in freq:
        p += f // 2
        lo = f % 2
    return [p, lo]

print(maxPair([1,3,2,1,3,2,2]))


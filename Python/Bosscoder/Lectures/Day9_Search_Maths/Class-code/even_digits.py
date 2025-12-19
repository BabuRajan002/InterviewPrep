def solve(nums):
    count = 0
    for x in nums:
        count += 1-countDigits(x) % 2
    return count

def countDigits(n):
    count = 0
    while(n):
        n //= 10
        count += 1
    return count 

print(solve([12,345,2,6,2345]))
def mulOfFive(n):
    times = n // 5
    ans = []
    for i in range(1, times+1):
        ans.append(i*5)
    return ans

print(mulOfFive(7))

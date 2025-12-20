# given an integer N, create an array with N distinct elements having sum zero
def sum_zero(n):
    ans = []
    k = n // 2
    for i in range(1,k+1):
        ans.append(i)
        ans.append(-i)
    
    if n%2 != 0:
        ans.append(0)
    return ans

print(sum_zero(5))

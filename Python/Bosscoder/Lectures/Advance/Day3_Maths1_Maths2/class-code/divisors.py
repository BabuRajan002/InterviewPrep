def divisors(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            print(i, end=" ")
            count += 1
    return count

print(divisors(1000))


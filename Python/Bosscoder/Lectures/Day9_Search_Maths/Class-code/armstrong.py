def armstrong(n):
    temp = n
    sum = 0
    while(n):
        r = n % 10
        n //= 10
        sum += r ** 3
    if temp == sum:
        return True
    return False



    

print(armstrong(371))
  
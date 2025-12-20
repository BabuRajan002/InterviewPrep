# Given N add the n odd numbers

def oddAdd(num):
    n = (2 * num) - 1
    sum = 0
    for i in range(1,n+1):
        if i % 2 != 0:
            sum += i
    return sum

print(oddAdd(3)) 


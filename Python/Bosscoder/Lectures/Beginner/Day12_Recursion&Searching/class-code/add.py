# Parameterized Recursion
def add(i, sum):
    if i == 0:
        return sum
    return add(i-1, sum+i)

print(add(5, 0))


#n + fn(n-1) -> Fucntional reverse

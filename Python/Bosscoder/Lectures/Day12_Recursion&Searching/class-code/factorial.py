# Parameterized
# def fact(i, f):
#     if i == 0:
#         return f
#     return fact(i-1, f*i)

# print(fact(5, 1))

# Functional
def fact(i):
    if i == 0:
        return 1
    return i*fact(i-1)

print(fact(5))


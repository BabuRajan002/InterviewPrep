# Recursive stack Example
def print_number(n): 
    if n == 6:
        return
    print_number(n+1)
    print(n)

print_number(1)
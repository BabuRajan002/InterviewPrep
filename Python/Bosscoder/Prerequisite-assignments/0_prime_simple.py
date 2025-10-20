n = int(input("Enter a number: "))
def isPrime(n):
    for i in range(2, n):
        if n % 2 == 0:
            return False
    return True

if isPrime(n):
    print("Number is a Prime number")
else:
    print("Number is not a prime number")
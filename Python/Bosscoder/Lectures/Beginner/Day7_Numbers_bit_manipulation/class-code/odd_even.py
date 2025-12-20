## Q1. Check if the number is even or ODD using bit manipulation? 
def oddEven(n):
    if n&1 == 0:
        print("even")
    else:
        print("odd")

oddEven(8)


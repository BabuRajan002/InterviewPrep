#Q1 Find the GCD of 'a' and 'b' when the valid numbers provided? Return the maximum possible GCD Lets say if the divisible is 1,2,3,4,5 you have 
# to return the maximum value
 
def gcd(a,b):
    while(b):
        temp = a
        a = b
        b = temp % b
    return a

print(gcd(25,30))

# TC: O(logarithmic)
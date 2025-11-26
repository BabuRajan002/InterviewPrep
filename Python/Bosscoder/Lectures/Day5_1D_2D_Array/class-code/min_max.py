n = int(input("Enter the number of subjects: "))

scores = [0]*n

for i in range(0,n):
    scores[i] = int(input())

mn = scores[0]
mx = scores[0]

for i in range(1, n):
    if scores[i] > mx:
        mx = scores[i]
    if scores[i] < mn:
        mn = scores[i]

print(f"Max= {mx}")
print(f"Minimum = {mn}")

## Comparison based Algorithm

def insertionSort(arr):
    n = len(arr)
    for round in range(1,n):
        i = round
        while i > 0 and arr[i] < arr[i-1]:
            temp = arr[i-1]
            arr[i-1] = arr[i]
            arr[i] = temp
            i -= 1
        
    return arr

print(insertionSort([9,1,2,5,7,-1]))

# Time complexity will O(N^2)

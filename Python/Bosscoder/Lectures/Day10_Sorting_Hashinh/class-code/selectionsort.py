def selectionSort(arr):
    for round in range(1,len(arr)):
        start = round - 1
        minIdx = start
        mn = arr[start]
        for i in range(1,len(arr)):
            if arr[i] < mn:
                mn = arr[i]
                minIdx = i
        temp = arr[i]               

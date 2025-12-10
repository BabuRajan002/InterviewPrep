# Time complexity of this algorthm is O(N^2)
# def bubbleSort(arr):
#     for round in range(len(arr)):
#         i = round
#         for i in range(len(arr)-round-1):
#             if arr[i] > arr[i+1]:
#                 temp = arr[i]
#                 arr[i] = arr[i+1]
#                 arr[i+1] = temp
#     return arr

# print(bubbleSort([9,1,2,5,4,7,-1]))

#Optimized version of Bubble Sort 

def bubbleSort(arr):
    for round in range(len(arr)):
        i = round
        flag = 'False'
        for i in range(len(arr)-round-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                flag = 'True'
        if flag == 'False':
            break
    return arr

print(bubbleSort([7,3,1,8,1,4,9000,4,2,4,1,5,6,1000]))

# Time Complexity of optimized bubble sort is still O(N^2):


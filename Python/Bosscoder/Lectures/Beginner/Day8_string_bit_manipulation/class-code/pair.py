# Given an array of intergers and an interger K, check if there exists any pair (i,j) set to a[i] + a[j] = k

# arr = [5,7,2,1,6] k = 11
def solve(arr,k):
   n = max(arr)+1
   res = ['False']*n
   for num in arr:
      res[num] = 'True'
   for num in arr:
      if (k-num > n) or (k < num):
         continue
      if res[k-num] == 'True':
         return num, k-num

print(solve([5,7,2,1,6],30))
         

      

   
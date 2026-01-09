class Alternate:
     def __init__(self, arr):
         self.arr = arr
     
     def solve(self):
          arr = self.arr 
          n = len(arr)

          pos = []
          neg = []
          for i in range(n):
               if arr[i] < 0:
                    neg.append(arr[i])
               else:
                    pos.append(arr[i])

          if len(pos) > len(neg):
               for i in range(len(neg)):
                    arr[2 * i] = pos[i]
                    arr[2 * i + 1] = neg[i]
               
               index = 2 * len(neg)
               for i in range(len(neg), len(pos)):
                    arr[index] = pos[i]
                    index += 1
        
          else:
               for i in range(len(pos)):
                    arr[2 * i] = pos[i]
                    arr[2 * i + 1] = neg[i]
               
               index = 2 * len(pos)
               for i in range(len(pos), len(neg)):
                    arr[index] = neg[i]
                    index += 1
          return arr        
               

if __name__ == "__main__":
     alter = Alternate([6, 1, 2, 3, -4, -1, 4])
     print(alter.solve())



		
    
		   
		  
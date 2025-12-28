class FourDivisors:
    def __init__(self, numbers):
        self.numbers = numbers
        
    def solve(self):
        numbers = self.numbers        
        total = 0
        for n in numbers:
          i = 1
          original = n

          count = 0
          sum_div = 0
          while i * i <= original:
              if original % i == 0:
                  pair = original // i
              
                  if pair == i:
                     count += 1
                     sum_div += i

                  else:
                     count += 2
                     sum_div += pair + i
                    
                  if count > 4:
                      break
              i += 1

          if count == 4:
              total += sum_div    
              

        return total           
     

if __name__ == "__main__":
    fourdiv = FourDivisors([90779,36358,90351,75474,32986])
    print(fourdiv.solve())






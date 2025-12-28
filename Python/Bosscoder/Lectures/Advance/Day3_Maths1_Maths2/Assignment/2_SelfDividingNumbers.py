class SelfDividingNumbers:
    def __init__(self, left, right):
        self.left = left
        self.right = right

        
    def solve(self):
        left = self.left 
        right = self.right
        ans = []
        for left in range(left, right + 1):
            number = left
            flag = "True"   
            while number > 0:
                digit = number % 10
                if digit != 0 and left % digit == 0:
                    number  //= 10
                else:
                    flag = "False"
                    break                 
            if flag == "True":
                ans.append(left)         
  
        return ans      


if __name__ == "__main__":
    selfdiv = SelfDividingNumbers(47,85)
    print(selfdiv.solve())


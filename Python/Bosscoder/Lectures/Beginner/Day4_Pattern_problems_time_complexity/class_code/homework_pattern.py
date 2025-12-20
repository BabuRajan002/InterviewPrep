# Pattern1: 

# * * * * *  
# * * * * *  
# * * * * *  
# * * * * *  
# * * * * *

# class Patttern1:
#     def __init__(self,n):
#         self.n = n
    
#     def pattern1(self):
#         for i in range(self.n):
#             for j in range(self.n):
#                 print(f"*", end=" ")
#             print(" ")

# if __name__ == "__main__":
#     pat1 = Patttern1(5)
#     pat1.pattern1()

# Pattern2:
# *  
# * *  
# * * *  
# * * * *  
# * * * * *  
# class Patttern1:
#     def __init__(self,n):
#         self.n = n
    
#     def pattern1(self):
#         for i in range(1,self.n+1):
#             for j in range(i):
#                 print(f"*", end=" ")
#             print(" ")

# if __name__ == "__main__":
#     pat1 = Patttern1(5)
#     pat1.pattern1()

# #Pattern 3:
# 1  
# 1 2  
# 1 2 3  
# 1 2 3 4  
# 1 2 3 4 5

# class Patttern1:
#     def __init__(self,n):
#         self.n = n
    
#     def pattern1(self):
#         for i in range(self.n):
#             for j in range(i+1):
#                 print(f"{j+1}", end=" ")
#             print(" ")

# if __name__ == "__main__":
#     pat1 = Patttern1(5)
#     pat1.pattern1()

# Pattern 4:
# 1  
# 2 2  
# 3 3 3  
# 4 4 4 4  
# 5 5 5 5 5 
# class Patttern5:
#     def __init__(self,n):
#         self.n = n
    
#     def pattern1(self):
#         for i in range(self.n):
#             for j in range(i+1):
#                 print(f"{i+1}", end=" ")
#             print(" ")

# if __name__ == "__main__":
#     pat5 = Patttern5(5)
#     pat5.pattern1()

#Pattern 5:
# * * * * *  
# * * * *  
# * * *  
# * *  
# *  
# class Patttern5:
#     def __init__(self,n):
#         self.n = n
    
#     def pattern1(self):
#         for i in range(self.n):
#             for j in range(self.n-i):
#                 print(f"*", end=" ")
#             print(" ")

# if __name__ == "__main__":
#     pat5 = Patttern5(5)
#     pat5.pattern1()

#Patter6:
# 1 2 3 4 5  
# 1 2 3 4  
# 1 2 3  
# 1 2  
# 1 

# class Patttern5:
#     def __init__(self,n):
#         self.n = n
    
#     def pattern1(self):
#         for i in range(self.n):
#             for j in range(self.n-i):
#                 print(f"{j+1}", end=" ")
#             print(" ")

# if __name__ == "__main__":
#     pat5 = Patttern5(5)
#     pat5.pattern1()

#Pattern 7:
# 1 1 1 1 1  
# 1 1 1 1  
# 1 1 1  
# 1 1  
# 1  
# class Patttern7:
#     def __init__(self,n):
#         self.n = n
    
#     def pattern7(self):
#         for i in range(self.n):
#             for j in range(self.n-i):
#                 print(f"{1}", end=" ")
#             print(" ")

# if __name__ == "__main__":
#     pat7 = Patttern7(5)
#     pat7.pattern7()

#Pattern8:
# 1 1 1 1 1  
# 2 2 2 2  
# 3 3 3  
# 4 4  
# 5  

# class Patttern8:
#     def __init__(self,n):
#         self.n = n
    
#     def pattern8(self):
#         for i in range(self.n):
#             for j in range(self.n-i):
#                 print(f"{i+1}", end=" ")
#             print(" ")

# if __name__ == "__main__":
#     pat8 = Patttern8(5)
#     pat8.pattern8()

#Pattern 9
#         *  
#       * * *  
#     * * * * *  
#   * * * * * * *  
# * * * * * * * * *  
# class Patttern9:
#     def __init__(self,n):
#         self.n = n
    
#     # def pattern9(self):
#     #     for i in range(self.n):
#     #         for j in range(self.n+i):
#     #             if j < self.n-i-1:
#     #                 print(" ", end=" ")
#     #             else:                
#     #                 print(f"*", end=" ")
#     #         print(" ")
#     def pattern9(self):
#         for i in range(self.n):
#             for j in range(self.n-i-1):
#                 print(" ", end=" ")
#             for k in range(2*i+1):
#                 print("*", end=" ")
#             print(" ")

# if __name__ == "__main__":
#     pat9 = Patttern9(5)
#     pat9.pattern9()

#Pattern 10:
class Patttern10:
    def __init__(self,n):
        self.n = n    

    def pattern10(self):
        for i in range(self.n*2-1):
            # if i <= self.n-1:
            #     for j in range(i+1):
            #         print("*", end=" ")
            # else:
            #     for k in range(2*self.n-i-1):
            #         print("*", end=" ")
            # print(" ")
            stars = i + 1
            if i >= self.n:
                stars = 2*self.n - i - 1
            for j in range(stars):
                print("*", end=" ")
            print(" ") 



if __name__ == "__main__":
    pat10 = Patttern10(5)
    pat10.pattern10()






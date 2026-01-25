# #Brute Force
# class Bouquet:
#     def __init__(self, n, nums, k, m):
#         self.n = n
#         self.nums = nums 
#         self.k = k
#         self.m = m
    
#     def possible(self):
#         low = min(self.nums)
#         high = max(self.nums)
#         n = self.n 
#         nums = self.nums
#         k = self.k #Number of flowers in the each bouquet
#         m = self.m #Numver of bouquets

#         if n < m * k:
#             return -1
        
#         for low in range(high+1):
#             count = 0
#             numberOfBouquests = 0

#             for i in range(n):
#                 if low >= nums[i]:
#                     count += 1
#                     if count == k:
#                         numberOfBouquests += 1
#                         count = 0
#                 else:                    
#                     count = 0
               
#             if numberOfBouquests >= m:
#                 return low 
#         return -1

# if __name__ == "__main__":
#     bouquet = Bouquet(8,[7, 7, 7, 7, 13, 11, 12, 7], 2, 3)
#     print(bouquet.possible())

# Optimzation

class Bouquest:
    def __init__(self, n, nums, k, m):
        self.n = n
        self.nums = nums 
        self.k = k
        self.m = m
    
    def solve(self):
        n = self.n 
        nums = self.nums 
        k = self.k 
        m = self.m 

        low = min(nums)
        high = max(nums)
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            adjacent_count = 0
            bouquest_formed = 0

            for i in range(n):
                if mid >= nums[i]:
                    adjacent_count += 1
                    if adjacent_count == k:
                        bouquest_formed += 1
                        adjacent_count = 0
                else:
                    adjacent_count = 0
            if bouquest_formed >= m:
                ans = mid
                high = mid - 1                
            else:
                low = mid + 1

        return ans

if __name__ == "__main__":
    bouquest = Bouquest(2,[642822109,590192314], 1, 1)  
    print(bouquest.solve())                  



    
        
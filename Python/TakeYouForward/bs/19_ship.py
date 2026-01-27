# Brute Force

# class ShipCapacity:
#     def __init__(self, weights, days):
#         self.weights = weights 
#         self.days = days 
    
#     def capacity(self):
#         weights = self.weights
#         days = self.days

#         minCapacity = max(weights)
#         maxCapacity = sum(weights)

#         for i in range(minCapacity, maxCapacity + 1):
#             currentLoad = 0
#             daysToShip = 1
#             for weight in weights:
#                 if currentLoad + weight > i:
#                     daysToShip += 1
#                     currentLoad = weight
#                 else:
#                     currentLoad += weight        
#             if daysToShip <= days:
#                 return i 

# if __name__ == "__main__":
#     shipcapacity = ShipCapacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
#     print(shipcapacity.capacity())

class ShipCapacity:
    def __init__(self, weights, days):
        self.weights = weights
        self.days = days 
    
    def solve(self):
        weights = self.weights
        days = self.days 

        low = max(weights)
        high = sum(weights)
        result = high

        while low <= high:
            mid = (low + high) // 2

            currentLoad = 0
            daysToShip = 1

            for weight in weights:
                if currentLoad + weight > mid:
                    daysToShip += 1
                    currentLoad = weight
                else:
                    currentLoad += weight
            
            if daysToShip <= days:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result 

if __name__ == "__main__":
    shipcap = ShipCapacity([3, 2, 2, 4, 1, 4], 3)
    print(shipcap.solve())




                

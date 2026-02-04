class Kthelement:
    def __init__(self, a, b, k):
        self.a = a
        self.b = b 
        self.k = k 
    
    def solve(self):
        a = self.a 
        b = self.b 
        k = self.k 

        if len(a) > len(b):
            return self.solve(b, a, k)
        
        n1, n2 = len(a), len(b)
        low, high = max(k - n2, 0), min(k, n1)
        left = k
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1

            l1 = float('-inf') if mid1 == 0 else a[mid1 - 1]
            l2 = float('-inf') if mid2 == 0 else b[mid2 - 1]
            r1 = float('inf') if mid1 == n1 else a[mid1]
            r2 = float('inf') if mid2 == n2 else b[mid2]

            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            
            elif l1 > l2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0
    
if __name__ == "__main__":
    kthelement = Kthelement([100, 112, 256, 349, 770],  [72, 86, 113, 119, 265, 445, 892], 7)
    print(kthelement.solve())






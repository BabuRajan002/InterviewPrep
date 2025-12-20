class SearchMatrix:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target
        
    def solve(self):
        arr = self.arr
        target = self.target

        for element in arr:
            n = len(element)
            if target >= element[0] and target <= element[n-1]:
                for num in element:
                    if num == target:
                        return True
        return False

if __name__ == "__main__":
    sm = SearchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 20)
    print(sm.solve())
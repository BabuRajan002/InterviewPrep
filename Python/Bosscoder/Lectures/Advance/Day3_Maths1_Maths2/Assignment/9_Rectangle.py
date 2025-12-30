class Rectangle:
    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2
        
    def check(self):
        rec1 = self.arr1
        rec2 = self.arr2
        return rec1[0] < rec2[2] and rec1[1] < rec2[3] and rec1[2] > rec2[0] and rec1[3] > rec2[1]

if __name__ == "__main__":
    rect = Rectangle([0,0,2,2], [1,1,3,3])
    print(rect.check())
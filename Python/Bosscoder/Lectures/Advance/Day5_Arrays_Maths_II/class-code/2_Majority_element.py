class Majority:
    def __init__(self, arr):
        self.arr = arr 
    
    def solution(self):
        arr = self.arr 
        element = float('inf')
        count = 0
        n = len(arr)

        for i in range(n):
            if count == 0:
                element = arr[i]
                count += 1
            elif element == arr[i]:
                count += 1
            else:
                count -= 1
        return element

if __name__ == "__main__":
    major = Majority([6,6,6,7,7])
    print(major.solution())

# Logic Behind this 

# count tracks the balance between the current candidate and other elements

# When count == 0, we pick a new candidate

# When we see the same element, we increase the count

# When we see a different element, we decrease the count
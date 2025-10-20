# Create a program that filters an array to return only the even numbers.
# If the array is empty or contains no even numbers, return an empty array.
class ArrayFilter:
    def __init__(self, arr):
        self.arr = arr
        
    def sort(self):
        res = []
        for num in self.arr:
            if num % 2 == 0:
                res.append(num)
        return res

if __name__ == "__main__":
    result_array = ArrayFilter([1,3,5,7])
    print(result_array.sort())       

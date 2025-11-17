class Positive:
    def __init__(self, arr):
        self.arr = arr
        
    def count(self):
        count = 0
        for num in self.arr:
            if num >= 0:
                count += 1
        return count

if __name__ == "__main__":
    post_count = Positive([-2, -1])
    print(post_count.count())

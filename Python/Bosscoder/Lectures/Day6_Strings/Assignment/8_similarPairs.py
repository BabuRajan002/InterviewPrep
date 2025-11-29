class SimilarPairs:
    def __init__(self, arr):
        self.arr = arr
        
    def find(self):
        arr = self.arr
        freq = {}
        for word in arr:
            key = "".join(sorted(set(word)))

            if key in freq:
                freq[key] += 1
            else:
                freq[key] = 1
        # return freq
        print(freq)
        count = 0
        for k in freq.values():
            if k > 1:
                count += (k * (k - 1)) // 2
        return count            
    
if __name__ == "__main__":
    sp = SimilarPairs(["aabb","ab","ba"])
    print(sp.find())
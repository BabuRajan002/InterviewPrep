class SimilarPairs:
    def __init__(self, arr):
        self.arr = arr
        
    def find(self):
        arr = self.arr
        original_lst = set()
        for words in arr:
            word = set(words)
            print(word)
        #     original_lst.add(word)
        # return len(list(original_lst))

if __name__ == "__main__":
    sp = SimilarPairs(["aba","aabb","abcd","bac","aabc"])
    sp.find()
class SimilarPairs:
    def __init__(self, arr):
        self.arr = arr
    
    def find(self):
        count = 0
        n = len(self.arr)
        words = self.arr

        for i in range(n):
            s = words[i]
            st = set(s)
            print(st)

            for j in range(i+1, n):
                t = words[j]
                temp = set(t)
                print(temp)

                if st == temp:
                    count += 1
        return count       
         
    
if __name__ == "__main__":
    sp = SimilarPairs(["aba","aabb","abcd","bac","aabc"])
    print(sp.find())
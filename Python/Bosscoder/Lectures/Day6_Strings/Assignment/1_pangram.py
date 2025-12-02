class Pangram:
    def __init__(self, s):
        self.s = s
        
    def check(self):
       sentence = self.s.strip().lower().replace(" ","")
       attend = ['False']*26
       counter = 0
       for ch in sentence:
            if attend[(ord(ch)-ord('a'))] == 'False':
                  attend[(ord(ch)-ord('a'))] = 'True'
                  counter += 1
       return counter==26
    
if __name__ == "__main__":
    pan = Pangram('The quick brown fox jumps over the dog')
    print(pan.check())



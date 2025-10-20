# Implement a program that counts how many times a specific character appears in a given string.
# The function should be case-insensitive.

class Count:
    def __init__(self, word, chr):
        self.word = word
        self.chr = chr
        
    def solve(self):
        count = 0
        word_recv = self.word.strip(" ").replace(" ", "").lower()
        for letter in word_recv:
            if letter == self.chr:
                count += 1
        return count



if __name__ == "__main__":
    count_char = Count("Bosscoder Academy","a")
    print(count_char.solve())
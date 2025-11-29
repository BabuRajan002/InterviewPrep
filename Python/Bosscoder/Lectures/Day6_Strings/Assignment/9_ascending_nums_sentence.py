# A sentence is a list of tokens separated by a single space with no leading or trailing spaces. Every token is either a positive number consisting of digits 0-9 with no leading zeros, or a word consisting of lowercase English letters.

# For example, "a puppy has 2 eyes 4 legs" is a sentence with seven tokens: "2" and "4" are numbers and the other tokens such as "puppy" are words.

# Given a string s representing a sentence, you need to check if all the numbers in s are strictly increasing from left to right (i.e., other than the last number, each number is strictly smaller than the number on its right in s).

# Return true if so, or false otherwise.

class AreNumbersAscending:
    def __init__(self, s):
        self.s = s
        
    def check(self):
        s = self.s.split()
        nums = []
        for num in s:
           if num.isdigit():               
               nums.append(int(num))
        print(nums)
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                return False
        return True


if __name__ == "__main__":
    ascend = AreNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles")
    print(ascend.check())
        
# Q43. Minimum Index Sum of Two Lists
# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
# A common string is a string that appeared in both list1 and list2.
# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
# Return all the common strings with the least index sum. Return the answer in any order.

class Solution:
    def __init__(self, list1, list2):
        self.list1 = list1 
        self.list2 = list2
    
    def findRestaurant(self):
        list1 = self.list1
        list2 = self.list2
        final = []
        least = float('inf')
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    index_sum = i + j
                    if index_sum < least:
                      least = index_sum
                      final = [list1[i]]
                    elif index_sum == least:
                      final.append(list1[i])
        return final

if __name__ == "__main__":
    index_summation = Solution(["happy", "sad", "good"], ["sad", "happy", "good"])
    print(index_summation.findRestaurant())



                    


        
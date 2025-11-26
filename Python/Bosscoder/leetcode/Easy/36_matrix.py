# 1572. Matrix Diagonal Sum

# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

# class Solution:
#     def diagonalSum(self, mat: List[List[int]]) -> int:
#         n = len(mat)
#         sum = 0
#         for i in range(n):
#             for j in range(n):
#               if i == j or i + j == n-1:
#                   sum += mat[i][j]
#         return sum
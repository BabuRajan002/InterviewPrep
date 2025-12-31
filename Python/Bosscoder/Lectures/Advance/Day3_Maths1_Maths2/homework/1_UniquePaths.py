class UniquePaths:
	def __init__(self, m, n):
		self.m = m
		self.n = n

	def sum(self):
		row = self.m
		col = self.n 
		mat = [[0 for _ in range(col)] for _ in range(row)]

		# Last col
		for i in range(row):
			mat[i][col-1] = 1
		
		#Last row
		for i in range(col):
			mat[row-1][i] = 1
		
		for i in range(row-2, -1, -1):
			for j in range(col-2,-1,-1):
				waysFromRightSteps = mat[i][j+1]
				waysFromLeftSteps = mat[i+1][j]

				totalWays = waysFromRightSteps + waysFromLeftSteps

				mat[i][j] = totalWays
		return mat[0][0]

if __name__ == "__main__":
	up = UniquePaths(3,7)
	print(up.sum())

# Rotate a matrix
def rotate(matrix) :
    res = [[0 for i in range(len(matrix))] for i in range(len(matrix))]
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            res[c][-1 - r] = matrix[r][c]
    return res

# Largest sum submatrix
def kadane(arr, start, finish, n):
	Sum = 0
	maxSum = -999999999999
	i = None
	finish[0] = -1
	local_start = 0
	for i in range(n):
		Sum += arr[i]
		if Sum < 0:
			Sum = 0
			local_start = i + 1
		elif Sum > maxSum:
			maxSum = Sum
			start[0] = local_start
			finish[0] = i
	if finish[0] != -1:
		return maxSum
	maxSum = arr[0]
	start[0] = finish[0] = 0
	for i in range(1, n):
		if arr[i] > maxSum:
			maxSum = arr[i]
			start[0] = finish[0] = i
	return maxSum

def findMaxSum(M):
	global ROW, COL
	maxSum, finalLeft = -999999999999, None
	finalRight, finalTop, finalBottom = None, None, None
	left, right, i = None, None, None

	temp = [None] * ROW
	Sum = 0
	start = [0]
	finish = [0]
	for left in range(COL):
		temp = [0] * ROW
		for right in range(left, COL):
			for i in range(ROW):
				temp[i] += M[i][right]
			Sum = kadane(temp, start, finish, ROW)
			if Sum > maxSum:
				maxSum = Sum
				finalLeft = left
				finalRight = right
				finalTop = start[0]
				finalBottom = finish[0]
	print("(Top, Left)", "(", finalTop,
		finalLeft, ")")
	print("(Bottom, Right)", "(", finalBottom,
		finalRight, ")")
	print("Max sum is:", maxSum)

ROW = 4
COL = 5
M = [[1, 2, -1, -4, -20],
	[-8, -3, 4, 2, 1],
	[3, 8, 10, 1, 3],
	[-4, -1, 1, 7, -6]]

# Flood Fill
n = rows = 10
m = columns = 10
a = [] # input array
q = []
four = [(1, 0), (-1, 0), (0, 1), (0, -1)]
eight = [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for i in range(1, n):
    for j in range(1, m):
        if a[i][j] == '.':
            q.append((i, j))
            while q:
                x, y = q.pop()           
                a[x][y] = '#'                
                for dx, dy in four:
                    if a[x + dx][y + dy] == '.':
                        q.append((x + dx, y + dy))

			


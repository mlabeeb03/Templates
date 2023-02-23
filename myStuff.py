def isBipartite(g):
	col = [-1]*(len(g))
	q = []
	for i in range(len(g)):
		if (col[i] == -1):
			q.append([i, 0])
			col[i] = 0		
			while len(q) != 0:
				p = q[0]
				q.pop(0)
				v = p[0]
				c = p[1]
				for j in g[v]:
					if (col[j] == c):
						return False
					if (col[j] == -1):
						if c == 1:
							col[j] = 0
						else:
							col[j] = 1
						q.append([j, col[j]])
	return True

g = [[1, 2], [0], [0, 3], [2]]
print(isBipartite(g))





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

			



def fastSieve(n):
    r = [False, True] * (n//2) + [True]
    r[1], r[2] = False, True
    for i in range(3, int(1 + n**0.5), 2):
        if r[i]:
            r[i*i::2*i] = [False] * ((n+2*i-1-i*i)//(2*i))
    return r

def factors(n):    
    return list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))








# segment tree

N = 100000
tree = [0] * (4 * N + 10)
def build(arr):
    for i in range(n):
        tree[n + i] = arr[i]
    for i in range(n - 1, 0, -1):
        tree[i] = tree[i << 1] + tree[i << 1 | 1]

def updateTreeNode(p, value):
    tree[p + n] = value
    p = p + n
    i = p  
    while i > 1:       
        tree[i >> 1] = tree[i] + tree[i ^ 1]
        i >>= 1
def query(l, r):
    res = 0
    l += n
    r += n   
    while l < r:    
        if (l & 1):
            res += tree[l]
            l += 1    
        if (r & 1):
            r -= 1
            res += tree[r];          
        l >>= 1
        r >>= 1   
    return res

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(a)
build(a)
print(query(1, 3)) # print the sum in range(1,2) index-based
updateTreeNode(2, 1) # modify element at 2nd index
print(query(1, 3)) # print the sum in range(1,2) index-based






# count subarrays with xor
n = int(input())
a = list(map(int, input().split()))

sq=[]
p=0
while p*p<=4*10**5:
    sq.append(p*p)
    p+=1
 
occ = [0] * (2 * n)     # number of times each element occured in the xor prefix array
occ[0] = 1      # 0 obviously occured 1 times already if we take empty subarray

c = 0 # count for subarrays with xor equal to any value is sq
x = 0 # prefix xor uptill i

for i in range(n):
    x ^= a[i]
    for j in sq:
        if j ^ x < 2 * n:
            c += (occ[j ^ x])
    occ[x] += 1
print(c)





# Longest increasing subsequence in nlgn
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            else:
                ind = bisect_left(ans, nums[i])
                ans[ind] = nums[i]
        return len(ans)
    







# find number of bits required to store an integer
print((999999).bit_length())

# convert decimal to binary
#018 formats the number to eighteen digits zero-padded on the left
#b converts the number to its binary representation
print(format(8, '018b'))
#'00000110'

def ConvertDecimalToBaseX(num, x):
    if num == 0:
        return [0]
    digits = []
    while num:
        digits.append(int(num % x))
        num //= x
    return digits[::-1]
        
def ConvertBaseXToDecimal(num, CurrBase):
    ans = 0
    for i in map(int, num):
        ans = CurrBase * ans + i
    return ans






def is_square(apositiveint):
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True
# arr(original array), xorArr(prefix xor arrays), n(length), m(target number)
def CountSubarraysWithXor(arr, xorArr, n, m):
    ans = 0  
    mp = {}
    for i in range(n):
        tmp = m ^ xorArr[i]
        if tmp in mp:
            ans = ans + (mp[tmp])
        if (xorArr[i] == m):
            ans += 1
        if xorArr[i] in mp:
            mp[xorArr[i]] += 1
        else:
            mp[xorArr[i]] = 1
    return ans

# better approach
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






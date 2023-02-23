def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x * y) // gcd(x, y)
    

def sieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    for p in range(2, num+1):
        if prime[p]:
            PRIMES.append(p)
PRIMES = []

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



# c will contains the number of pairs x, y such that gcd(x, y) = i for all i in[1, n + 1]
c = [0] * (n + 1)		
for i in range(n, 0, -1):
    cnt = n // i 		# count of numbers divisible by i
    c[i] = (cnt * (cnt - 1)) // 2		# c[i] now contains the number of "pairs" such that their gcd is i or a multiple of i
    j = 2 * i
    while j <= n:		# if the gcd of above mentioned pairs is a multiple of i and not i then we must remove it from answer, here j will be all the multiples of i and their already calculated answer is subtracted
        c[i] -= c[j]
        j += i

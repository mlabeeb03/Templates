class DisjointSet:
    def __init__(self, n):
        self.rank, self.parent, self.n = [0] * (n + 1), [i for i in range(n + 1)], n

    def find(self, x):
        xcopy = x
        while x != self.parent[x]:
            x = self.parent[x]

        while xcopy != x:
            self.parent[xcopy], xcopy = x, self.parent[xcopy]
        return x

    def union(self, x, y):
        xpar, ypar = self.find(x), self.find(y)
        if xpar == ypar:
            return

        par, child = xpar, ypar
        if self.rank[xpar] < self.rank[ypar]:
            par, child = ypar, xpar

        elif self.rank[xpar] == self.rank[ypar]:
            self.rank[xpar] += 1

        self.parent[child] = par
        self.n -= 1

 # ANOTHER APPROACH

def make_set(n):
    for v in range(n + 1): 
        parent[v] = v 
        size[v] = 1
def find_set(v):
    if (v == parent[v]): return v
    parent[v] = find_set(parent[v])
    return parent[v]
def union_sets(a, b):
    a = find_set(a)
    b = find_set(b)
    if (a != b):
        if (size[a] < size[b]):
            a, b = b, a
        parent[b] = a
        size[a] += size[b]

n, parent, size = 5, [None] * (n + 1), [None] * (n + 1)
make_set(n)
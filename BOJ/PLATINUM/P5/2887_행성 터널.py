import sys
input = sys.stdin.readline

def FindParent(x):
    if parent[x] != x:
        parent[x] = FindParent(parent[x])
    return parent[x]

def UnionParent(x, y):
    x = FindParent(x)
    y = FindParent(y)
    if x < y: parent[y] = x
    else: parent[x] = y


x = []
y = []
z = []
N = int(input())
for i in range(N):
    X, Y, Z = map(int, input().split())
    x.append((i, X))
    y.append((i, Y))
    z.append((i, Z))

x.sort(key = lambda x : x[1])
y.sort(key = lambda x : x[1])
z.sort(key = lambda x : x[1])

edges = []
for i in range(1, N):
    edges.append((x[i-1][0], x[i][0], abs(x[i][1] - x[i-1][1])))
    edges.append((y[i-1][0], y[i][0], abs(y[i][1] - y[i-1][1])))
    edges.append((z[i-1][0], z[i][0], abs(z[i][1] - z[i-1][1])))

parent = list(i for i in range(N+1))

edges.sort(key = lambda x : x[2])
ans = 0
for f, t, c in edges:
    if FindParent(f) != FindParent(t):
        UnionParent(f, t)
        ans += c

print(ans)

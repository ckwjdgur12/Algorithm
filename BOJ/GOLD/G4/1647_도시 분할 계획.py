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



N, M = map(int, input().split())
graph = []

for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((A, B, C))

graph.sort(key = lambda x : x[2])
parent = list(i for i in range(N+1))

ans = []
for f, t, c in graph:
    if FindParent(f) != FindParent(t):
        UnionParent(f, t)
        ans.append(c)

print(sum(ans) - ans[-1])


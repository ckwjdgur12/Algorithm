import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")
sys.setrecursionlimit(10**6)

id = 0

def dfs(v):
    global id
    id += 1
    d[v] = id

    s.append(v)

    parent = d[v]
    for next_v in graph[v]:
        if not d[next_v]: parent = min(parent, dfs(next_v))
        elif not finished[next_v]: parent = min(parent, d[next_v])

    scc = []
    if parent == d[v]:
        while True:
            elem = s.pop()
            scc.append(elem)
            finished[elem] = True
            if elem == v:
                break
        SCC.append(sorted(scc))

    return parent


V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    f, t = map(int, input().split())
    graph[f].append(t)

d = [0] * (V+1)
finished = [False] * (V+1)
s = []

SCC = []
for i in range(1, V+1):
    if not d[i]:
        dfs(i)

SCC.sort()
print(len(SCC))
for scc in SCC:
    scc.append(-1)
    print(*scc)

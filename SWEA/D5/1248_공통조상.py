import sys

sys.stdin = open("BOJ/input.txt", "r")


LOG = 14


def dfs(v, depth):
    d[v] = depth

    for next in tree[v]:
        parent[next][0] = v
        size[v] += dfs(next, depth+1) 

    return size[v]


def set_parent():
    dfs(1, 0)

    for i in range(1, LOG):
        for j in range(1, V+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]


def LCA(a, b):
    if d[a] < d[b]: a, b = b, a

    for i in range(LOG-1, -1, -1):
        if d[a] - d[b] >= (1<<i): 
            a = parent[a][i]

    if a == b: return a
    
    for i in range(LOG-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]


T = int(input())
for test_case in range(1, T+1):
    
    V, E, v1, v2 = map(int, input().split())

    input_data = list(map(int, input().split()))
    tree = [[] for _ in range(V+1)]

    for i in range(0, E*2, 2):
        f, t = input_data[i], input_data[i+1]
        tree[f].append(t)

    parent = [[0] * LOG for _ in range(V+1)]
    d = [0] * (V+1)
    size = [1] * (V+1)

    set_parent()

    lca = LCA(v1, v2)

    print(f'#{test_case} {lca} {size[lca]}')

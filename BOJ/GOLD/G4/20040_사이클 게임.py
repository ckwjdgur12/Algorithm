import sys
input = sys.stdin.readline

def FindParent(x):
    if parent[x] != x: parent[x] = FindParent(parent[x])
    return parent[x]

def UnionParent(x, y):
    x = FindParent(x)
    y = FindParent(y)
    if x < y: parent[y] = x
    else: parent[x] = y


n, m = map(int, input().split())
parent = list(i for i in range(n+1))

for i in range(1, m+1):
    pos1, pos2 = map(int, input().split())
    if FindParent(pos1) != FindParent(pos2): UnionParent(pos1, pos2)
    else:
        print(i)
        exit(0)
        
print(0)

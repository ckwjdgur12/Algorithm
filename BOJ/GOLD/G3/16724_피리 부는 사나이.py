import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def findParent(x):
    if parent[x] != x:
        parent[x] = findParent(parent[x])
    return parent[x]

def unionParent(x, y):
    x = findParent(x)
    y = findParent(y)
    if x < y: parent[y] = x
    else: parent[x] = y

def makeSafeZone(x, y, num):
    while visited[x][y] == 0:
        visited[x][y] = num
        if MAP[x][y] == 'D':
            if not 0 <= x+1 < N: break
            x += 1
            continue
        if MAP[x][y] == 'U':
            if not 0 <= x-1 < N: break
            x -= 1
            continue
        if MAP[x][y] == 'R':
            if not 0 <= y+1 < M: break
            y += 1
            continue
        if MAP[x][y] == 'L':
            if not 0 <= y-1 < M: break
            y -= 1
            continue
    
    if visited[x][y] == num: return
    else:
        unionParent(visited[x][y], num)
        return


N, M = map(int, input().split())
MAP = list(input().strip() for _ in range(N))
visited = list([0] * M for _ in range(N))
parent = list(i for i in range(N*M+1))

num = 1
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            makeSafeZone(i, j, num)
            num += 1

ans = set()
for i in range(1, num):
    ans.add(findParent(i))

print(len(ans))

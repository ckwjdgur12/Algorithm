import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(x, y, gNum):
    dq = deque()
    dq.append((x, y))
    visited[x][y] = True
    cnt = 1

    while dq:
        x, y = dq.popleft()
        savedGroupNum[x][y] = gNum

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N and 0 <= ny < M): continue
            if lst[nx][ny] != 0: continue
            if visited[nx][ny]: continue

            visited[nx][ny] = True
            cnt += 1
            dq.append((nx, ny))

    return cnt


def GetValue(x, y):

    value = 1
    groups = set()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < N and 0 <= ny < M): continue
        groups.add(savedGroupNum[nx][ny])

    for group in groups:
        value += grouping[group]
        value %= 10
    
    return value



N, M = map(int, input().split())
lst = [list(map(int, input().strip())) for _ in range(N)]
savedGroupNum = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
grouping = {}
grouping[0] = 0

pos = []
gNum = 1
for i in range(N):
    for j in range(M):
        if lst[i][j] == 0 and not visited[i][j]:
            value = BFS(i, j, gNum)
            grouping[gNum] = value
            gNum += 1
        elif lst[i][j] == 1:
            pos.append((i, j))

for x, y, in pos:
    lst[x][y] = GetValue(x, y)

for i in range(N):
    print("".join(map(str, lst[i])))


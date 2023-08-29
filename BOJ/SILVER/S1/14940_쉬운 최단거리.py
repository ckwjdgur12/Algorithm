import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def get_first_pos():
    for i in range(n):
        for j in range(m):
            if land[i][j] == 2:
                return i, j


def bfs(x, y):

    dq = deque([(x, y)])

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m): continue
            if not land[nx][ny]: continue
            if ans[nx][ny]: continue

            ans[nx][ny] = ans[x][y] + 1
            dq.append((nx, ny))

    return


n, m = map(int, input().split())

land = list(list(map(int, input().split())) for _ in range(n))
ans = list([0] * m for _ in range(n))

x, y = get_first_pos()
bfs(x, y)

for i in range(n):
    for j in range(m):
        if ans[i][j] == 0 and land[i][j] != 0:
            ans[i][j] = -1

ans[x][y] = 0

for a in ans:
    print(*a)

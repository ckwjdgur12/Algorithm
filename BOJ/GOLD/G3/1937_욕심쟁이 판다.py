import sys

input = sys.stdin.readline
# sys.stdin = open("BOJ/input.txt", "r")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def check(x, y):
    if dist[x][y] != 0:
        return dist[x][y]

    dist[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < n and 0 <= ny < n): continue
        if forest[nx][ny] <= forest[x][y]: continue

        dist[x][y] = max(dist[x][y], check(nx, ny) + 1)

    return dist[x][y]


n = int(input())
forest = list(list(map(int, input().split())) for _ in range(n))
dist = list([0] * n for _ in range(n))

for i in range(n):
    for j in range(n):
        check(i, j)

ans = 1
for d in dist:
    ans = max(ans, max(d))

print(ans)

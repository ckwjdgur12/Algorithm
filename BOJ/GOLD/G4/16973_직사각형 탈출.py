import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def down_nx_valid(x, y):
    for i in range(y, y+W):
        if grid[x+H-1][i] == 1: return False
    return True


def right_ny_valid(x, y):
    for i in range(x, x+H):
        if grid[i][y+W-1] == 1: return False
    return True


def up_nx_valid(x, y):
    for i in range(y, y+W):
        if grid[x][i] == 1: return False
    return True


def left_ny_valid(x, y):
    for i in range(x, x+H):
        if grid[i][y] == 1: return False
    return True


def in_range(x, y):
    if 0 <= x < N and 0 <= y < M: return True
    else: return False


def bfs():

    dq = deque([(sx, sy)])

    while dq:
        x, y = dq.popleft()

        for (nx, ny), valid in zip([(x - 1, y), (x, y - 1)], [up_nx_valid, left_ny_valid]):
            if not in_range(nx, ny): continue
            if visited[nx][ny]: continue
            if not valid(nx, ny): continue

            visited[nx][ny] = visited[x][y] + 1
            dq.append((nx, ny))

        for (nx, ny), valid in zip([(x + 1, y), (x, y + 1)], [down_nx_valid, right_ny_valid]):
            if not in_range(nx+H-1, ny+W-1): continue
            if visited[nx][ny]: continue
            if not valid(nx, ny): continue

            visited[nx][ny] = visited[x][y] + 1
            dq.append((nx, ny))

    return


N, M = map(int, input().split())

grid = list(list(map(int, input().split())) for _ in range(N))
H, W, sx, sy, fx, fy = map(int, input().split())
visited = list([0] * M for _ in range(N))
sx -= 1
sy -= 1
fx -= 1
fy -= 1

bfs()

if not visited[fx][fy]: print(-1)
else: print(visited[fx][fy])

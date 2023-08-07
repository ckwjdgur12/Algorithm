import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M, R = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(N))
ans = list([None] * M for _ in range(N))

dq = deque()
cycle = min(N, M) // 2

for i in range(cycle):
    dq.append((i, i))

poses = []
while dq:
    x, y = dq.popleft()
    
    elems = []
    for i in range(4):
        if i%2 == 0:
            for j in range(N-1):
                elems.append((x, y))
                x += dx[i]
                y += dy[i]
        else:
            for j in range(M-1):
                elems.append((x, y))
                x += dx[i]
                y += dy[i]

    poses.append(elems)
    N -= 2
    M -= 2

for i in range(cycle):
    length = len(poses[i])
    for j in range(length):
        x, y = poses[i][j]
        nx, ny = poses[i][(j+R) % length]
        ans[nx][ny] = arr[x][y]

for a in ans:
    print(*a)

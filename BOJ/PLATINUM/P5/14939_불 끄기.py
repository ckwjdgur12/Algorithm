import sys
from copy import deepcopy
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")
INF = 987654321

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]

def press(board, x, y):

    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < 10 and 0 <= ny < 10): continue

        if board[nx][ny] == 1: board[nx][ny] = 0
        else: board[nx][ny] = 1



bulbs = [[] for _ in range(10)]
for i in range(10):
    line = input().strip()
    for sign in line:
        if sign == '#': bulbs[i].append(1)
        else: bulbs[i].append(0)

ans = INF
for case in range(1 << 10):
    tmp_bulbs = deepcopy(bulbs)

    cnt = 0
    for i in range(10):
        if case & (1 << i):
            press(tmp_bulbs, 0, i)
            cnt += 1

    for i in range(1, 10):
        for j in range(10):
            if tmp_bulbs[i-1][j] == 0:
                press(tmp_bulbs, i, j)
                cnt += 1

    if 0 in tmp_bulbs[9]: continue
    else: ans = min(ans, cnt)

if ans == INF: print(-1)
else: print(ans)


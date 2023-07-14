import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    visited = [[False] * M for _ in range(N)]
    dq = deque()

    for i in range(N):
        if board[i][0] == 0:
            dq.append((i, 0))
            safe_zone[i][0] = False
            visited[i][0] = True
        if board[i][M-1] == 0: 
            dq.append((i, M-1))
            safe_zone[i][M-1] = False
            visited[i][M-1] = True
    for i in range(1, M-1):
        if board[0][i] == 0: 
            dq.append((0, i))
            safe_zone[0][i] = False
            visited[0][i] = True
        if board[N-1][i] == 0:
            dq.append((N-1, i))
            safe_zone[N-1][i] = False
            visited[N-1][i] = True
    
    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not(0 <= nx < N and 0 <= ny < M): continue
            if visited[nx][ny]: continue
            if board[nx][ny]: continue
            safe_zone[nx][ny] = False
            visited[nx][ny] = True
            dq.append((nx, ny))


def melt():

    for x, y in cheeses:
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not(0 <= nx < N and 0 <= ny < M): continue
            if safe_zone[nx][ny]: continue
            cnt += 1
        if cnt >= 2: board[x][y] = 0
    
    return board


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while True:
    cheeses = []
    safe_zone = [[True] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                cheeses.append((i, j))
    if not cheeses: break
    bfs()
    melt()
    ans += 1

print(ans)

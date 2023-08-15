import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")
INF = 100001

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    dq = deque()
    dq.append((0, 0, 0))
    dist[0][0][0] = 1

    while dq:
        x, y, cnt = dq.popleft()

        if x == N-1 and y == M-1: return dist[N-1][M-1][cnt]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N and 0 <= ny < M): continue
            
            if board[nx][ny] == 0 and dist[nx][ny][cnt] == INF:
                dist[nx][ny][cnt] = dist[x][y][cnt] + 1
                dq.append((nx, ny, cnt))
            elif cnt < K and dist[nx][ny][cnt+1] == INF:
                dist[nx][ny][cnt+1] = dist[x][y][cnt] + 1
                dq.append((nx, ny, cnt+1))
                
    return -1


N, M, K = map(int, input().split())
board = list(list(map(int, input().strip())) for _ in range(N))
dist = list(list([INF] * (K+1) for _ in range(M)) for _ in range(N))

print(bfs())

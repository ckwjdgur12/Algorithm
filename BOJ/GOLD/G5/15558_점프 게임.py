import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def bfs():

    dq = deque([(0, 0, 0)])
    visited = list([False] * N for _ in range(2))
    visited[0][0] = True

    while dq:

        nx, y, limit = dq.popleft()

        for i in range(3):
            if i == 2: nx ^= 1
            ny = y + dy[i]

            if ny <= limit: continue

            if ny >= N: return 1

            if board[nx][ny] == '0': continue
            if visited[nx][ny]: continue

            visited[nx][ny] = True
            dq.append((nx, ny, limit + 1))

    return 0


N, K = map(int, input().split())

dy = [1, -1, K]

board = list(input().strip() for _ in range(2))

print(bfs())

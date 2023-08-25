import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def in_range(x, y):
    if not (0 <= x < N and 0 <= y < M): return False
    return True


def find_start_pos():
    for i in range(N):
        for j in range(M):
            if campus[i][j] == 'I': 
                campus[i][j] = 'X'
                return (i, j)
                

def bfs():
    cnt = 0

    dq = deque([find_start_pos()])

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            if not in_range(nx := x + dx[i], ny := y + dy[i]): continue
            if campus[nx][ny] == 'X': continue
            
            if campus[nx][ny] == 'P': cnt += 1

            campus[nx][ny] = 'X'
            dq.append((nx, ny))

    return cnt


N, M = list(map(int, input().split()))
campus = list(list(input().strip()) for _ in range(N))

print(bfs() or "TT")

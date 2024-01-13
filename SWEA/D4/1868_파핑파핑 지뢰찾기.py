import sys
from collections import deque


sys.stdin = open("BOJ/input.txt", "r")


dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]


def bfs(x, y):
    dq = deque([(x, y)])
    
    while dq:
        x, y = dq.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < N and 0 <= ny < N): continue
            if visited[nx][ny]: continue
            if mine[nx][ny] == '*': continue

            visited[nx][ny] = True

            if mine_cnt[nx][ny]: continue

            dq.append((nx, ny))
    return


T = int(input())
for test_case in range(1, T+1):

    N = int(input())
    mine = list(list(input().strip()) for _ in range(N))
    mine_cnt = list([0] * N for _ in range(N))
    visited = list([False] * N for _ in range(N))

    for x in range(N):
        for y in range(N):
            if mine[x][y] == '*':
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if not (0 <= nx < N and 0 <= ny < N): continue
                    if mine[nx][ny] == '*': continue
                    mine_cnt[nx][ny] += 1

    ans = 0
    for x in range(N):
        for y in range(N):
            if mine_cnt[x][y]: continue
            if visited[x][y]: continue
            if mine[x][y] == '*': continue
            ans += 1
            visited[x][y] = True
            bfs(x, y)

    for x in range(N):
        for y in range(N):
            if mine[x][y] == '*': continue
            if visited[x][y]: continue
            ans += 1

    print(f'#{test_case} {ans}')
    
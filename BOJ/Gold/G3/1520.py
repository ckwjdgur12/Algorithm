import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

M, N = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):

    if (x == M-1 and y == N-1): return 1
    if dp[x][y] != -1: return dp[x][y]

    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < M and 0 <= ny < N): continue
        if MAP[nx][ny] >= MAP[x][y]: continue
        if MAP[nx][ny] < MAP[M-1][N-1]: continue

        dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print((dfs(0, 0)))





# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# M, N = map(int, input().split())
# MAP = [list(map(int, input().split())) for _ in range(M)]

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1] 

# cnt = 0

# def dfs(x, y):
#     global cnt

#     if (x == M-1 and y == N-1):
#         cnt += 1
#         return
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if not (0 <= nx < M and 0 <= ny < N): continue
#         if MAP[nx][ny] >= MAP[x][y]: continue
#         if MAP[nx][ny] < MAP[M-1][N-1]: continue

#         dfs(nx, ny)


# dfs(0, 0)

# print(cnt)

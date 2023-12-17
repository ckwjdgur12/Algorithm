import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")
sys.setrecursionlimit(10**6)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

H = 'H'


def dfs(x, y):
    
    if visited[x][y]:
        print(-1)
        exit(0)

    if dp[x][y]: return dp[x][y]

    for i in range(4):
        dist = int(board[x][y])
        nx = x + dx[i]*dist
        ny = y + dy[i]*dist

        if not (0 <= nx < N and 0 <= ny < M): continue
        if board[nx][ny] == H: continue

        visited[x][y] = True
        dp[x][y] = max(dp[x][y], dfs(nx, ny)+1)
        visited[x][y] = False

    return dp[x][y]


N, M = map(int, input().split())
board = list(list(input().strip()) for _ in range(N))

dp = list([0] * M for _ in range(N))
visited = list([False] * M for _ in range(N))

print(dfs(0, 0)+1)

import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")
sys.setrecursionlimit(100000)


INF = -987654321
DOWN = 0
LEFT = 1
RIGHT = 2

dx = [1, 0, 0]
dy = [0, 1, -1]


def dfs(x, y, pre):

    if x == N-1 and y == M-1: return Mars[x][y]
    if dp[x][y][pre] != -1: return dp[x][y][pre]

    dp[x][y][pre] = INF

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < N and 0 <= ny < M): continue
        if pre == LEFT and i == RIGHT: continue
        if pre == RIGHT and i == LEFT: continue

        dp[x][y][pre] = max(dp[x][y][pre], dfs(nx, ny, i) + Mars[x][y])

    return dp[x][y][pre]


N, M = map(int, input().split())
Mars = list(list(map(int, input().split())) for _ in range(N))

dp = list(list([-1] * 3 for _ in range(M)) for _ in range(N))

print(dfs(0, 0, LEFT))

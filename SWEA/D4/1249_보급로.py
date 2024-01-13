import sys

sys.stdin = open("BOJ/input.txt", "r")


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

INF = 987654321


def dfs(x, y):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < N and 0 <= ny < N): continue
        if cost[nx][ny] <= cost[x][y] + road[nx][ny]: continue

        cost[nx][ny] = cost[x][y] + road[nx][ny]
        dfs(nx, ny)


T = int(input())
for test_case in range(1, T+1):
    
    N = int(input())
    road = list(list(map(int, input().strip())) for _ in range(N))
    cost = list([INF] * N for _ in range(N))

    cost[0][0] = road[0][0]
    dfs(0, 0)

    print(f'#{test_case} {cost[N-1][N-1]}')
    
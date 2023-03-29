import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

M, N = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):

    if (x == M-1 and y == N-1): return 1    # 도착지에 도착하면 1 return
    if dp[x][y] != -1: return dp[x][y]      # 방문 했던 지점이면 그 지점 값 리턴

    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < M and 0 <= ny < N): continue  # 범위를 벗어나면 continue
        if MAP[nx][ny] >= MAP[x][y]: continue           # 현재 높이보다 같거나 높으면 continue
        if MAP[nx][ny] < MAP[M-1][N-1]: continue        # 도착 지점보다 낮으면 continue

        dp[x][y] += dfs(nx, ny) # 현재 지점까지의 branch 개수 모으기

    return dp[x][y] # 더이상 탐색할 수 있는 곳이 없다면 자기자신 리턴


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

import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")
sys.setrecursionlimit(10**6)


def get_dist(f, t):
    return abs(f[0] - t[0]) + abs(f[1] - t[1])


def dfs(x, y):
    if x == W or y == W: return 0
    if dp[x][y] != -1: return dp[x][y]

    n_e = max(x, y) + 1

    if x == 0: d_1 = get_dist([1, 1], event[n_e])
    else: d_1 = get_dist(event[x], event[n_e])
    
    if y == 0: d_2 = get_dist([N, N], event[n_e])
    else: d_2 = get_dist(event[y], event[n_e])

    dp[x][y] = min(dfs(n_e, y) + d_1, dfs(x, n_e) + d_2)
    return dp[x][y]


def print_result(x, y):
    if x == W or y == W: return

    n_e = max(x, y) + 1

    if x == 0: d_1 = get_dist([1, 1], event[n_e])
    else: d_1 = get_dist(event[x], event[n_e])
    
    if y == 0: d_2 = get_dist([N, N], event[n_e])
    else: d_2 = get_dist(event[y], event[n_e])

    if dp[n_e][y] + d_1 < dp[x][n_e] + d_2:
        print(1)
        print_result(n_e, y)
    else:
        print(2)
        print_result(x, n_e)

    return


N = int(input())
W = int(input())

event = [(0, 0)]
for _ in range(W):
    x, y = map(int, input().split())
    event.append((x, y))

dp = list([-1] * (W+1) for _ in range(W+1))

print(dfs(0, 0))
print_result(0, 0)

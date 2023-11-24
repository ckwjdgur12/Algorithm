import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")
sys.setrecursionlimit(10**6)


EARLY_ADOPTER = 0
ROOT = 1


def dfs(v):
    visited[v] = True

    for n_v in graph[v]:
        if visited[n_v]: continue
        dfs(n_v)
        dp[v][EARLY_ADOPTER] += min(dp[n_v][EARLY_ADOPTER], dp[n_v][not EARLY_ADOPTER])
        dp[v][not EARLY_ADOPTER] += dp[n_v][EARLY_ADOPTER]
    
    return


N = int(input())
graph = list([] for _ in range(N+1))
visited = [False] * (N+1)

for _ in range(N-1):
    f, t = map(int, input().split())
    graph[f].append(t)
    graph[t].append(f)

dp = list([1, 0] for _ in range(N+1))

dfs(ROOT)

print(min(dp[ROOT][EARLY_ADOPTER], dp[ROOT][not EARLY_ADOPTER]))

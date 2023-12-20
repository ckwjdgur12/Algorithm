import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")
sys.setrecursionlimit(10**6)


G = 0
NG = 1


def dfs(v):

    dp[G][v] += population[v]

    for n_v in graph[v]:
        if dp[G][n_v] != 0: continue

        n_p = dfs(n_v)
        dp[G][v] += n_p[NG]
        dp[NG][v] += max(n_p)

    return dp[G][v], dp[NG][v]


N = int(input())
population = list(map(int, input().split()))
population.insert(0, 0)
graph = list([] for _ in range(N+1))

for _ in range(N-1):
    fr, to = map(int, input().split())
    graph[fr].append(to)
    graph[to].append(fr)

dp = list([0] * (N+1) for _ in range(2))

print(max(dfs(1)))
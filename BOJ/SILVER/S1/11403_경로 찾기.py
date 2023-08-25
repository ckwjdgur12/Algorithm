import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def find_path(v):

    dq = deque([v])
    visited = [False] * N

    while dq:
        cur = dq.popleft()

        for next in graph[cur]:
            if visited[next]: continue

            visited[next] = True
            dq.append(next)
            ans[v][next] = 1

    return


N = int(input())
adj_matrix = list(list(map(int, input().split())) for _ in range(N))
graph = list([] for _ in range(N))

for i in range(N):
    for j in range(N):
        if adj_matrix[i][j]:
            graph[i].append(j)

ans = list([0] * N for _ in range(N))

for i in range(N):
    find_path(i)

for a in ans:
    print(*a)

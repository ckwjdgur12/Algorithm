import sys
from collections import defaultdict
from heapq import heappush, heappop
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

INF = 987654321
MOD = 1000000007

def dijkstra(start):

    hq = []
    heappush(hq, (0, start))
    dist[start] = 0

    while hq:
        c_t, c_v = heappop(hq)

        if dist[c_v] < c_t: continue

        for n_v in graph[c_v]:
            n_t = c_t + 1
            if n_t < dist[n_v]:
                dist[n_v] = n_t
                heappush(hq, (n_t, n_v))

    return


N, M = map(int, input().split())

graph = defaultdict(list)
dist = [INF] * (N+1)

for _ in range(M):
    f, t = map(int, input().split())
    graph[f].append(t)
    graph[t].append(f)

dijkstra(1)

dist_cnt = defaultdict(int)
for d in dist:
    if d == INF: continue
    dist_cnt[d] += 1

dist_info = list(dist_cnt.keys())

ans = 1
for d in dist_info:
    ans *= (dist_cnt[d] + 1)

ans -= 1
print(ans%MOD)

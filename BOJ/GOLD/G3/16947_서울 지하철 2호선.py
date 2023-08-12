import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")
sys.setrecursionlimit(10**6)

def dfs(cur_station, cnt):
    
    if visited[cur_station]:
        if cnt - dist[cur_station] > 2: return cur_station
        else: return -1
    
    visited[cur_station] = True
    dist[cur_station] = cnt
    for next_station in subway[cur_station]:
        first_station = dfs(next_station, cnt + 1)

        if first_station == -1: continue

        is_cycle[cur_station] = True

        if first_station == cur_station: return -1
        else: return first_station

    return -1


def bfs():

    while dq:
        cur_station = dq.popleft()

        for next_station in subway[cur_station]:
            if dist[next_station] != -1: continue

            dist[next_station] = dist[cur_station] + 1
            dq.append(next_station)

    return


N = int(input())
subway = list([] for _ in range(N+1))
for _ in range(N):
    f, t = map(int, input().split())
    subway[f].append(t)
    subway[t].append(f)

visited = [False] * (N+1)
is_cycle = [False] * (N+1)
dist = [-1] * (N+1)

dfs(1, 0)

dq = deque()
for i in range(1, N+1):
    if is_cycle[i]:
        dq.append(i)
        dist[i] = 0
    else:
        dist[i] = -1

bfs()

ans = []
for i in range(1, N+1):
    if is_cycle[i]: ans.append(0)
    else: ans.append(dist[i])

print(*ans)

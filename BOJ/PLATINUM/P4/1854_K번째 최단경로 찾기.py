import sys
import heapq
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")
INF = 987654321

def dijkstra():

    hq = []
    heapq.heappush(hq, (0, 1))

    while hq:
        cur_cost, cur_city = heapq.heappop(hq)

        if -distance[cur_city][0] < cur_cost:
            continue

        for new_city, new_cost in city[cur_city]:
            next_cost = cur_cost + new_cost
            if -distance[new_city][0] > next_cost:
                # heapq.heappop(distance[new_city])
                # heapq.heappush(distance[new_city], -next_cost)
                heapq.heappushpop(distance[new_city], -next_cost)
                heapq.heappush(hq, (next_cost, new_city))
                
    return


n, m, k = map(int, input().split())

city = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    city[a].append((b, c))

distance = [[-INF] * (k) for _ in range(n+1)]
distance[1][k-1] = 0

dijkstra()

for i in range(1, n+1):
    if distance[i][0] == -INF:
        print(-1)
    else:
        print(-distance[i][0])


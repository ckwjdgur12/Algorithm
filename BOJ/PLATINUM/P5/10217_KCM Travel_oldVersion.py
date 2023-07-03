import sys
from collections import deque
import heapq
input = sys.stdin.readline
INF = 9876543210

T = int(input())

for _ in range(T):

    N, M, K = map(int, input().split())

    if M == 0:
        print("Poor KCM")
        exit(0)

    airport = [[] for _ in range(N+1)]
    time_arr = [[INF] * (M+1) for _ in range(N+1)]
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        airport[u].append((v, c, d))

    time_arr[1][0] = 0

    hq = []
    heapq.heappush(hq, (0, 0, 1))

    limit = M
    while hq:
        updated = False
        time, cost, now = heapq.heappop(hq)

        if time_arr[now][cost] < time: continue

        for nextAirport, nextCost, nextTime in airport[now]:
            total_cost = cost + nextCost
            total_time = time + nextTime

            if total_cost > limit: continue
            if total_time > time_arr[nextAirport][total_cost]: continue

            for i in range(total_cost, limit+1):
                if total_time < time_arr[nextAirport][i]:
                    time_arr[nextAirport][i] = total_time
                    updated = True
                else:
                    break

            if updated: heapq.heappush(hq, (total_time, total_cost, nextAirport))


    if time_arr[N][M] == INF:
        print("Poor KCM")
    else:
        print(time_arr[N][M])

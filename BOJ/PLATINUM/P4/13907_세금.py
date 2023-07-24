import sys
import heapq
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")
INF = 987654321

def dijkstra():

    distance = [[INF] * N for _ in range(N+1)]
    distance[S][0] = 0
    hq = []
    heapq.heappush(hq, (0, S, 0))

    while hq:
        flag = False
        cur_c, cur_v, passed_cnt = heapq.heappop(hq)

        if passed_cnt == N-1: continue
        
        for i in range(passed_cnt + 1):
            if distance[cur_v][i] < cur_c:
                flag = True
                break
        if flag: continue

        for new_v, new_c in road[cur_v]:
            next_c = cur_c + new_c
            if distance[new_v][passed_cnt + 1] > next_c:
                distance[new_v][passed_cnt + 1] = next_c
                heapq.heappush(hq, (next_c, new_v, passed_cnt + 1))

    return distance[D]


N, M, K = map(int, input().split())
S, D = map(int, input().split())

road = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    road[a].append((b, w))
    road[b].append((a, w))

tax_lst = [0]
next_tax = 0
for _ in range(K):
    next_tax += int(input())
    tax_lst.append(next_tax)

distance_D = dijkstra()

answers = []
max_cnt = N-1
for tax in tax_lst:
    min_v = INF
    for passed_cnt in range(1, max_cnt+1):
        cost = distance_D[passed_cnt] + (passed_cnt*tax)
        if min_v > cost:
            min_v = cost
            max_cnt = passed_cnt
    answers.append(min_v)

for ans in answers:
    print(ans)
        
import sys
from heapq import heappush, heappop
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")
INF = 2100000000

def dijkstra():
    hq = []
    heappush(hq, (0, 0))

    while hq:
        c_c, c_v = heappop(hq)

        if c_c > dist[c_v]: continue

        for n_v in range(8):
            if c_v == n_v: continue
            n_c = c_c + graph[c_v][n_v]
            if dist[n_v] > n_c:
                dist[n_v] = n_c
                heappush(hq, (n_c, n_v))

    return


infos = {}
infos[0] = tuple(map(int, input().split()))
infos[7] = tuple(map(int, input().split()))

for i in range(1, 6, 2):
    poses = list(map(int, input().split()))
    infos[i] = (poses[0], poses[1])
    infos[i+1] = (poses[2], poses[3])

graph = list([INF] * 8 for _ in range(8))
for i in range(1, 6, 2):
    graph[i][i+1] = 10
    graph[i+1][i] = 10
    
for i in range(8):
    graph[i][i] = 0
        
for i in range(7):
    for j in range(i+1, 8):
        if graph[i][j] == 10: continue
        graph[i][j] = graph[j][i] = (abs(infos[i][0] - infos[j][0]) + abs(infos[i][1] - infos[j][1]))

dist = [INF] * 8
dijkstra()
print(dist[7])

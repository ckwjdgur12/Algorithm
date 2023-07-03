import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
inDegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    inDegree[B] += 1

def topologicalSort():

    pq = []

    for i in range(1, N+1):
        if inDegree[i] == 0: heapq.heappush(pq, i)

    while pq:
        v = heapq.heappop(pq)
        seq.append(v)
        for nextV in graph[v]:
            inDegree[nextV] -= 1
            if inDegree[nextV] == 0: heapq.heappush(pq, nextV)

    return


seq = []
topologicalSort()
print(*seq)

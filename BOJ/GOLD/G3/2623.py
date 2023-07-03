import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
inDegree = [0] * (N+1)

for _ in range(M):
    li = list(map(int, input().split()))[1:]
    
    for i in range(1, len(li)):
        graph[li[i-1]].append(li[i])
        inDegree[li[i]] += 1    # 진입차수 저장


def topologicalSort():
    dq = deque()
    result = []

    for i in range(1, N+1):
        if inDegree[i] == 0: dq.append(i)       # 진입 차수가 0인 정점 q에 넣기

    while dq:
        now = dq.popleft()                      # 진입차수가 0인 정점을 빼서
        result.append(now)                      # 결과 배열에 넣기

        for v in graph[now]:                    # 연결된 정점들 확인하면서
            inDegree[v] -= 1                    # 진입차수 1씩 줄이기
            if inDegree[v] == 0: dq.append(v)   # 진입차수가 0이 된 정점 q에 넣기

    for i in range(len(inDegree)):
        if inDegree[i] != 0: return []          # 위상정렬이 불가능한 경우

    return result


result = topologicalSort()

if not result: print(0)
else:
    for value in result:
        print(value)

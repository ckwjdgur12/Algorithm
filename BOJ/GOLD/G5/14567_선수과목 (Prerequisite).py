import sys
# from collections import deque

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")


N, M = map(int, input().split())
indegree = [0] * (N+1)
semester = [0] * (N+1)
graph = list([] for _ in range(N+1))

for _ in range(M):
    pre, pos = map(int, input().split())
    graph[pre].append(pos)
    indegree[pos] += 1

cur_semester = 1
indegree[0] = -1
cnt = 0
while True:
    n_indegree = indegree[:]

    for i in range(1, N+1):
        if not indegree[i]: 
            n_indegree[i] = -1
            semester[i] = cur_semester
            cnt += 1
            for next_i in graph[i]:
                n_indegree[next_i] -= 1

    if cnt == N: break

    indegree = n_indegree[:]
    cur_semester += 1

print(*semester[1:])


# deque를 이용한 풀이. 더 느림.
#
# N, M = map(int, input().split())
# indegree = [0] * (N+1)
# semester = [0] * (N+1)
# graph = list([] for _ in range(N+1))

# for _ in range(M):
#     pre, pos = map(int, input().split())
#     graph[pre].append(pos)
#     indegree[pos] += 1

# indegree[0] = -1
# dq = deque()
# for i in range(1, N+1):
#     if indegree[i] == 0: 
#         dq.append(i)
#         semester[i] = 1

# while dq:
#     c_c = dq.popleft()

#     for n_c in graph[c_c]:
#         semester[n_c] = semester[c_c]+1
#         indegree[n_c] -= 1

#         if not indegree[n_c]: dq.append(n_c)

# print(*semester[1:])

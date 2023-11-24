import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")


N = int(input())

build_time = [0] * (N+1)
pre_build_time = [0] * (N+1)
indegree = [0] * (N+1)
graph = list([] for _ in range(N+1))

for i in range(1, N+1):
    t, _, *pre = map(int, input().split())
    build_time[i] = t
    for p in pre:
        indegree[i] += 1
        graph[p].append(i)

next_build = []
for i in range(1, N+1):
    if not indegree[i]:
        next_build.append(i)

while next_build:
    cur_build = next_build.pop()

    for cur in graph[cur_build]:
        indegree[cur] -= 1
        pre_build_time[cur] = max(pre_build_time[cur], pre_build_time[cur_build] + build_time[cur_build])
        
        if not indegree[cur]: 
            next_build.append(cur)

ans = 0
for b_t, pb_t in zip(build_time[1:], pre_build_time[1:]):
    time = b_t + pb_t
    ans = max(ans, time)

print(ans)
    
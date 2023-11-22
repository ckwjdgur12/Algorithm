import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")


def find_b():
    next_b = []
    for i in range(1, N+1):
        if indegree[i] == 0: next_b.append(i)
    return next_b


N = int(input())

graph = list([] for _ in range(N+1))
indegree = [0] * (N+1)
build_time = [0]
before_build_time = [0] * (N+1)

for i in range(1, N+1):
    t, *pre, _ = map(int, input().split())
    build_time.append(t)
    for p in pre:
        graph[p].append(i)
        indegree[i] += 1

ans = 0
can_build_now = find_b()
while can_build_now:
    cur_b = can_build_now.pop()

    for next_b in graph[cur_b]:
        indegree[next_b] -= 1
        if indegree[next_b] == 0: can_build_now.append(next_b)
        before_build_time[next_b] = max(before_build_time[next_b], before_build_time[cur_b] + build_time[cur_b]) 
    
ans = []
for i in range(1, N+1):
    ans.append(before_build_time[i] + build_time[i])
print("\n".join(map(str, ans)))


'''

음...
미리 끝내야 하는 건물들 중 가장 느린거 기준으로 잡아야함.

5 4 3
4 2
3 1

11
12
13
14
15

1 끝내는데 11
2 끝내는데 12
3 끝내는데 가장 느리게 끝난 필요건물 + 3에 필요한 시간 = 24
4 끝내는데 가장 느리게 끝난 필요건물 + 4에 필요한 시간 = 26
5 끝내는데 가장 느리게 끝난 필요건물 + 5에 필요한 시간 = 41

가장 느리게 끝나는 건물 기준으로 끝날 시간 저장해야함.
그 끝날 시간에 필요 시간 더해줌

각 건물마다 이전에 필요한 시간을 저장해두자!
그럼 다시 계산 안해도 됨!

'''
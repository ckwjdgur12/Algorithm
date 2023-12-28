import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")


def dfs(lec):

    if semester[lec]: return semester[lec]+1

    cur_semester = 1
    for pre_lec in graph[lec]:
        cur_semester = max(dfs(pre_lec), cur_semester)
        
    semester[lec] = cur_semester
    return semester[lec]


N, M = map(int, input().split())
semester = [0] * (N+1)
graph = list([] for _ in range(N+1))

for _ in range(M):
    pre, pos = map(int, input().split())
    graph[pos].append(pre)

for i in range(1, N+1):
    if not semester[i]: dfs(i)

print(*semester[1:])

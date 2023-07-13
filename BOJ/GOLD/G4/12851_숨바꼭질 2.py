import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")
TIME = 0
WAY = 1

def BFS():

    dq = deque()
    dq.append(N)

    while dq:
        now = dq.popleft()
        for next in [now + 1, now - 1, now * 2]:
            if not (0 <= next <= 100000): continue
            if visited[next][TIME] == -1:
                visited[next][TIME] = visited[now][TIME] + 1
                visited[next][WAY] = visited[now][WAY]
                dq.append(next)
            elif visited[next][TIME] == visited[now][TIME] + 1:
                visited[next][WAY] += visited[now][WAY]
        

N, K = map(int, input().split())
visited = [[-1, 0] for _ in range(100001)]
visited[N][TIME], visited[N][WAY] = 0, 1
BFS()
print(visited[K][TIME])
print(visited[K][WAY])

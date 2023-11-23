import sys
from collections import deque

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")


def bfs():

    dq = deque()
    dq.append((1, 1, 1))

    while dq:
        l, c, cnt = dq.popleft()
        
        if l == S:
            print(cnt)
            exit()

        if l+c <= S and not visited[l+c][c]:
            visited[l+c][c] = True
            dq.append((l+c, c, cnt+1))
        if l > 0 and not visited[l-1][c]:
            visited[l-1][c] = True
            dq.append((l-1, c, cnt+1))
        if l != c and not visited[l][l]:
            visited[l][l] = True
            dq.append((l, l, cnt+1))

    return


S = int(input())

visited = list([False] * (S+1) for _ in range(S+1))
visited[1][1] = True

bfs()

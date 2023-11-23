import sys
from collections import deque

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")


INF = 987654321


def bfs():

    dq = deque()
    dq.append((1, 1))

    while dq:
        l, c = dq.popleft()

        if l+c <= S and emtc[l+c][c] == INF:
            emtc[l+c][c] = emtc[l][c] + 1
            dq.append((l+c, c))
        if l > 0 and emtc[l-1][c] == INF:
            emtc[l-1][c] = emtc[l][c] + 1
            dq.append((l-1, c))
        if l != c and emtc[l][l] == INF:
            emtc[l][l] = emtc[l][c] + 1
            dq.append((l, l))

    return


S = int(input())

emtc = list([INF] * (S+1) for _ in range(S+1))
emtc[1][1] = 1

bfs()

print(min(emtc[S]))

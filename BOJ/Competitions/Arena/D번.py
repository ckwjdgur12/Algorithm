import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    dq = deque()
    for r, c, in s_p:
        dq.append((r, c))
        water[r][c] = False

    while dq:
        x, y = dq.popleft() 

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < N and 0 <= ny < M): continue
            if cross[nx][ny] < cross[x][y]: continue
            if not water[nx][ny]: continue

            water[nx][ny] = False
            dq.append((nx, ny))

    return


def check(i, j):
    for idx in range(i, i+h):
        for wx, wy in water_pos[idx]:
            if wy > j+w: break
            if i <= wx < i+h and j <= wy < j+w:
                return False
    return True


N, M = map(int, input().split())
h, w = map(int, input().split())

cross = list(list(map(int, input().split())) for _ in range(N))
water = list([True] * M for _ in range(N))
place = list([True] * M for _ in range(N))

s_p = []

K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    s_p.append((r-1, c-1))
    
bfs()

water_pos = list([] for _ in range(N))

for i in range(N):
    for j in range(M):
        if water[i][j]: water_pos[i].append((i, j))

ans = 0
for i in range(N-h+1):
    for j in range(M-w+1):
        if water[i][j]: continue
        if check(i, j): ans += 1
            
print(ans)


# print("w")
# for w in water:
#     print(w)

# print("p")
# for p in place:
#     print(p)

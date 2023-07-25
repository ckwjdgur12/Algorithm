import sys
from heapq import heappop, heappush
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def push_item(x, y, height):
    if water_height[x][y] <= height: 
        return

    water_height[x][y] = height
    heappush(pq, (water_height[x][y], x, y))
   

def BFS():

    while pq:
        height, x, y = heappop(pq)

        if height != water_height[x][y]: continue

        for i in range(4):
            if water_tank[i][x][y] == -1: continue

            nx = x + dx[i]
            ny = y + dy[i]
            if not (1 <= nx <= N and 1 <= ny <= M): continue
            
            next_height = max(water_height[x][y], min(water_tank[i][x][y], water_height[nx][ny]))
            
            push_item(nx, ny, next_height)

    return


N, M, H = map(int, input().split()) # 세로, 가로, 높이

water_height = [[H] * (1004) for _ in range(1004)]
water_tank = [[[-2] * 1004 for _ in range(1004)] for _ in range(4)]

for i in range(1, N+2):
    row_holes = list(map(int, input().split()))
    for j in range(1, M+1):
        water_tank[DOWN][i-1][j] = row_holes[j-1]
        water_tank[UP][i][j] = row_holes[j-1]

for i in range(1, N+1):
    col_holes = list(map(int, input().split()))
    for j in range(1, M+2):
        water_tank[RIGHT][i][j-1] = col_holes[j-1]
        water_tank[LEFT][i][j] = col_holes[j-1]

pq = []
for i in range(1, M+1):
    if water_tank[UP][1][i] != -1: push_item(1, i, water_tank[UP][1][i])
    if water_tank[DOWN][N][i] != -1: push_item(N, i, water_tank[DOWN][N][i])
        
for i in range(1, N+1):
    if water_tank[LEFT][i][1] != -1: push_item(i, 1, water_tank[LEFT][i][1])
    if water_tank[RIGHT][i][M] != -1: push_item(i, M, water_tank[RIGHT][i][M])

BFS()

ans = 0

for h in water_height[1:N+1]:
    ans += sum(h[1:M+1])

print(ans)

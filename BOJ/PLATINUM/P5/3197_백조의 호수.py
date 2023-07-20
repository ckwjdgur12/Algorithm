import sys
from collections import deque
from copy import deepcopy
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

SWAN = -1
WATER = 0
ICE = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def swan_check():
    
    while swan_dq:
        x, y = swan_dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < R and 0 <= ny < C): continue
            if swan_visited[nx][ny]: continue
            if modified_lake[nx][ny] == SWAN: 
                return True
            
            if modified_lake[nx][ny] == ICE:
                next_swan_dq.append((nx, ny))
            else:
                swan_dq.append((nx, ny))
                
            swan_visited[nx][ny] = True

    return False


def lake_check():
    
    while water_dq:
        x, y = water_dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < R and 0 <= ny < C): continue
            if water_visited[nx][ny]: continue

            if modified_lake[nx][ny] == ICE:
                next_water_dq.append((nx, ny))
            else:
                water_dq.append((nx, ny))      

            water_visited[nx][ny] = True      

    return


def melt():
    for x, y in water_dq:
        modified_lake[x][y] = WATER
    return


R, C = map(int, input().split())

lake = []
for _ in range(R):
    lake.append(input().strip())

swans = []
water_dq = deque()
next_water_dq = deque()
modified_lake = [[-2] * C for _ in range(R)]
swan_visited = [[False] * C for _ in range(R)]
water_visited = [[False] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if lake[i][j] == 'L':
            swans.append((i, j))
            modified_lake[i][j] = SWAN
            water_dq.append((i, j))
        elif lake[i][j] == 'X':
            modified_lake[i][j] = ICE
        else:
            modified_lake[i][j] = WATER
            water_dq.append((i, j))
            water_visited[i][j] = True

swan_dq = deque()
next_swan_dq = deque()
swan_dq.append((swans[0][0], swans[0][1]))
swan_visited[swans[0][0]][swans[0][1]] = True

cnt = 0
while True:
    done = swan_check()
    swan_dq = next_swan_dq
    next_swan_dq = deque()

    if done:
        break

    lake_check()
    water_dq = next_water_dq
    next_water_dq = deque()

    melt()

    cnt += 1

print(cnt)

import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def in_range(x, y):
    if 0 <= x < h+2 and 0 <= y < w+2: 
        return True
    else: 
        return False


def bfs(x, y):

    opened_cnt = [[-1] * (w+2) for _ in range(h+2)]
    opened_cnt[x][y] = 0
    dq = deque()
    dq.append((x, y))

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < h+2 and 0 <= ny < w+2): continue
            if jail[nx][ny] == '*': continue
            if opened_cnt[nx][ny] != -1: continue

            if jail[nx][ny] == '#':
                opened_cnt[nx][ny] = opened_cnt[x][y] + 1
                dq.append((nx, ny))
                continue
            
            opened_cnt[nx][ny] = opened_cnt[x][y]
            dq.appendleft((nx, ny))
    
    return opened_cnt


T = int(input())

for _ in range(T):
    h, w = map(int, input().split())

    jail = []
    jail.append('.'*(w+2))
    for _ in range(h):
        jail.append('.' + input().strip() + '.')
    jail.append('.'*(w+2))

    prisoner = []
    for i in range(h+2):
        for j in range(w+2):
            if jail[i][j] == '$':
                prisoner.append((i, j))

    prisoner_1 = bfs(prisoner[0][0], prisoner[0][1])
    prisoner_2 = bfs(prisoner[1][0], prisoner[1][1])
    outsider = bfs(0, 0)

    # for elem in [prisoner_1, prisoner_2, outsider]:
    #     for e in elem:
    #         print(e)
    #     print()

    ans = 987654321
    for i in range(h+2):
        for j in range(w+2):
            if jail[i][j] == '*': continue
            if prisoner_1[i][j] == -1 and prisoner_2[i][j] == -1 and outsider[i][j] == -1: continue

            opened_door_cnt = prisoner_1[i][j] + prisoner_2[i][j] + outsider[i][j]

            if jail[i][j] == '#': opened_door_cnt -= 2

            ans = min(ans, opened_door_cnt)

    print(ans)

import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def spread_dust(info):
    x, y, dust = info
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < R and 0 <= ny < C): continue
        if (nx, ny) == (top, 0) or (nx, ny) == (bottom, 0): continue
        MAP[nx][ny] += dust//5
        cnt += 1
    MAP[x][y] -= dust//5 * cnt
    return


def operate_air_cleaner():

    MAP[top-1][0] = 0
    for nx in range(top-2, -1, -1):
        MAP[nx+1][0] = MAP[nx][0]
    for ny in range(1, C):
        MAP[0][ny-1] = MAP[0][ny]
    for nx in range(top):
        MAP[nx][-1] = MAP[nx+1][-1]
    for ny in range(C-2, 0, -1):
        MAP[top][ny+1] = MAP[top][ny]
    MAP[top][1] = 0

    MAP[bottom+1][0] = 0
    for nx in range(bottom+2, R):
        MAP[nx-1][0] = MAP[nx][0]
    for ny in range(1, C):
        MAP[-1][ny-1] = MAP[-1][ny]
    for nx in range(R-2, bottom-1, -1):
        MAP[nx+1][-1] = MAP[nx][-1]
    for ny in range(C-2, 0, -1):
        MAP[bottom][ny+1] = MAP[bottom][ny]
    MAP[bottom][1] = 0
    return


R, C, T = map(int, input().split())

MAP = []
for _ in range(R):
    MAP.append(list(map(int, input().split())))

dusts = []
top, bottom = None, None
for i in range(2, R-2):
    if MAP[i][0] == -1:
        top = i
        bottom = i+1
        break

for _ in range(T):
    dusts = []
    for i in range(R):
        for j in range(C):
            if MAP[i][j] != -1 and MAP[i][j] != 0:
                dusts.append((i, j, MAP[i][j]))
                
    for dust in dusts:
        spread_dust(dust)
    operate_air_cleaner()

ans = 0
for i in range(R):
    ans += sum(MAP[i])
print(ans + 2)

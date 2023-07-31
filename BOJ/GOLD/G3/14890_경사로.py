import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def row_downside_valid(x, y, h):

    if not (0 <= y+L-1 < N): return False

    for col in range(y, y+L):
        if MAP[x][col] != h: return False

    for col in range(y, y+L):
        row_v[x][col] = True

    return True


def row_upside_valid(x, y, h):

    if not (0 <= y-L+1 < N): return False
    if row_v[x][y-L+1]: return False

    for col in range(y, y-L, -1):
        if MAP[x][col] != h: return False

    for col in range(y, y-L, -1):
        row_v[x][col] = True

    return True


def col_downside_valid(x, y, h):

    if not (0 <= x+L-1 < N): return False

    for row in range(x, x+L):
        if MAP[row][y] != h: return False

    for row in range(x, x+L):
        col_v[row][y] = True

    return True


def col_upside_valid(x, y, h):

    if not (0 <= x-L+1 < N): return False
    if col_v[x-L+1][y]: return False

    for row in range(x, x-L, -1):
        if MAP[row][y] != h: return False

    for row in range(x, x-L, -1):
        row_v[row][y] = True

    return True


N, L = map(int, input().split())
MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))

row_v = [[False] * N for _ in range(N)]
col_v = [[False] * N for _ in range(N)]

cnt = 0
for row in range(N):
    for col in range(1, N):
        if MAP[row][col-1] == MAP[row][col]: 
            if col == N-1: cnt += 1
            continue

        if MAP[row][col-1] == MAP[row][col] + 1:
            if not row_downside_valid(row, col, MAP[row][col]): break
        elif MAP[row][col-1] == MAP[row][col] - 1:
            if not row_upside_valid(row, col-1, MAP[row][col-1]): break
        else: 
            break

        if col == N-1: cnt += 1

for col in range(N):
    for row in range(1, N):
        if MAP[row-1][col] == MAP[row][col]: 
            if row == N-1: cnt += 1
            continue

        if MAP[row-1][col] == MAP[row][col] + 1:
            if not col_downside_valid(row, col, MAP[row][col]): break
        elif MAP[row-1][col] == MAP[row][col] - 1:
            if not col_upside_valid(row-1, col, MAP[row-1][col]): break
        else: 
            break

        if row == N-1: cnt += 1

print(cnt)

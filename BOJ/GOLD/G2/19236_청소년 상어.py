import sys
from collections import defaultdict
from copy import deepcopy
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

POINT = 0
DIR = 1

def is_valid(x, y):
    if (0 <= x <= 3 and 0 <= y <= 3): return True
    else: return False


def get_fish_pos(f_n, fishes):
    for i in range(4):
        for j in range(4):
            if fishes[i][j][POINT] == f_n:
                return i, j
    return -1, -1


def move_fish(s_x, s_y, fishes):

    for f_n in range(1, 17):
        f_x, f_y = get_fish_pos(f_n, fishes)
        if f_x == -1: continue

        f_d = fishes[f_x][f_y][DIR]

        for i in range(8):
            nd = (f_d+i) % 8
            nx = f_x + dx[nd]
            ny = f_y + dy[nd]
            if not is_valid(nx, ny): continue
            if (s_x, s_y) == (nx, ny): continue

            fishes[f_x][f_y][DIR] = nd
            fishes[f_x][f_y], fishes[nx][ny] = fishes[nx][ny], fishes[f_x][f_y]
            break

    return


def dfs(s_x, s_y, c_point, fishes):
    global f_point

    c_point += fishes[s_x][s_y][POINT]
    f_point = max(c_point, f_point)
    fishes[s_x][s_y][POINT] = 0

    move_fish(s_x, s_y, fishes)

    d = fishes[s_x][s_y][DIR]
    for i in range(1, 4):
        nx = s_x + dx[d]*i
        ny = s_y + dy[d]*i
        if not is_valid(nx, ny): break
        if not fishes[nx][ny][POINT]: continue
        
        dfs(nx, ny, c_point, deepcopy(fishes))

    return


fishes = list([0] * 4 for _ in range(4))

for i in range(4):
    info = list(map(int, input().split()))
    for j in range(0, 7, 2):
        fishes[i][j//2] = [info[j], info[j+1]-1]

f_point = -1

dfs(0, 0, 0, fishes)
print(f_point)

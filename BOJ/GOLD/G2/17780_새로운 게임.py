import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

WHITE = 0
RED = 1
BLUE = 2

RIGHT = 1
LEFT = 2
UP = 3
DOWN = 4

X = 1
Y = 2
DIR = 3

FLAG = False

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


def in_range(x, y):
    if 1 <= x <= N and 1 <= y <= N: return True
    return False


def do_white(x, y, nx, ny):
    global FLAG

    for elem in token_pos[x][y]:
        token_pos[nx][ny].append(elem)
        tokens[elem-1][X] = nx
        tokens[elem-1][Y] = ny
    token_pos[x][y].clear()

    if len(token_pos[nx][ny]) >= 4:
        FLAG = True

    return


def do_blue(x, y, num):

    if tokens[num-1][DIR] % 2 == 0:
        tokens[num-1][DIR] -= 1
    else:
        tokens[num-1][DIR] += 1

    d = tokens[num-1][DIR]
    nx = x + dx[d]
    ny = y + dy[d]

    if not in_range(nx, ny) or board[nx][ny] == BLUE: return
    elif board[nx][ny] == RED: do_red(x, y, nx, ny)
    else: do_white(x, y, nx, ny)
            
    return


def do_red(x, y, nx, ny):

    token_pos[x][y].reverse()

    do_white(x, y, nx, ny)

    return


def move(token):
    num, x, y, d = token

    if token_pos[x][y][0] != num: return

    nx = x + dx[d]
    ny = y + dy[d]

    if not in_range(nx, ny): do_blue(x, y, num)
    elif board[nx][ny] == BLUE: do_blue(x, y, num)
    elif board[nx][ny] == RED: do_red(x, y, nx, ny)
    else: do_white(x, y, nx, ny)

    return


def do_turn():

    for token in tokens:
        move(token)

    if FLAG: return True
    else: return False


N, K = map(int, input().split())

board = list([0] * (N+1) for _ in range(N+1))
for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    for j in range(1, N+1):
        board[i][j] = tmp[j-1]

token_pos = list(list([] for _ in range(N+1)) for _ in range(N+1))

tokens = []

for i in range(1, K+1):
    x, y, d = map(int, input().split())
    tokens.append([i, x, y, d])
    token_pos[x][y].append(i)

cnt = 1
while cnt < 1001:
    if do_turn(): break
    cnt += 1

if cnt > 1000: print(-1)
else: print(cnt)


import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())

arr = [[0 for _ in range(C+1)] for _ in range(R+1)]
ans = 0
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    arr[r][c] = (s, d, z)

# arr[x][y] = (속력, 이동 방향, 크기)
# 이동방향 1 위, 2 아래, 3 오른쪽, 4 왼쪽
UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4

def catchShark(i):
    global ans

    for pos in range(1, R+1):
        if arr[pos][i] != 0:
            ans += arr[pos][i][2]
            arr[pos][i] = 0
            return
    return

# 이동방향 1 위, 2 아래, 3 오른쪽, 4 왼쪽
def get_next_pos(x, y, speed, dir):
    if dir == LEFT or dir == RIGHT:
        mod = 2 * C - 2
        if dir == RIGHT: speed += y - 1
        else: speed += mod - (y - 1)

        speed %= mod
        if speed < C: 
            return x, speed + 1, RIGHT
        else: 
            return x, mod - speed + 1, LEFT
    else:
        mod = 2 * R - 2
        if dir == DOWN: speed += x - 1
        else: speed += mod - (x - 1)

        speed %= mod
        if speed < R: 
            return speed + 1, y, DOWN
        else: 
            return mod - speed + 1, y, UP


def moveShark():
    global arr
    tArr = [[0] * (C+1) for _ in range(R+1)]

    for i in range(1, R+1):
        for j in range(1, C+1):
            if arr[i][j] != 0:
                speed, dir, size = arr[i][j]
                x, y, d = get_next_pos(i, j, speed, dir)
                if tArr[x][y] == 0 or tArr[x][y][2] < size: 
                    tArr[x][y] = (speed, d, size)

    arr = tArr

    
for i in range(1, C+1):
    catchShark(i)
    moveShark()

print(ans)

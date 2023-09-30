import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
EVEN = 4
ODD = 5

def move_fire():
    grid.clear()
    
    for x, y, m, s, d in fire_balls:
        nx = (x + dx[d]*s) % N
        ny = (y + dy[d]*s) % N

        if nx == 0: nx = N
        if ny == 0: ny = N

        n_pos = (nx, ny)
        if n_pos not in grid: grid[n_pos] = [1, m, s, d, 0, 0]
        else:
            grid[n_pos][0] += 1
            grid[n_pos][1] += m
            grid[n_pos][2] += s

        if d%2 == 0: grid[n_pos][EVEN] += 1
        else: grid[n_pos][ODD] += 1
    return


def split_fire():
    fire_balls.clear()

    for pos, (n, m, s, d, even, odd) in grid.items():
        x, y = pos
        if n == 1: fire_balls.append((x, y, m, s, d))
        else:
            if m < 5: continue

            n_m = m//5
            n_s = s//n
            if even == 0 or odd == 0: d = [0, 2, 4, 6]
            else: d = [1, 3, 5, 7]

            for i in range(4): 
                fire_balls.append((x, y, n_m, n_s, d[i]))
    return


N, M, K = map(int, input().split())

grid = {}
fire_balls = list(list(map(int, input().split())) for _ in range(M))

for _ in range(K):
    move_fire()
    split_fire()

print(sum(fire_ball[2] for fire_ball in fire_balls))

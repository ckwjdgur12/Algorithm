import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
dir = [1, 3, 5, 7, 0, 2, 4, 6]

def move_fire(fire_poses):
    split_poses = set()
    next_fire_poses = set()
    infos = []

    for x, y in fire_poses:
        for m, s, d in grid[x][y]:
            nx = x + dx[d]*s
            ny = y + dy[d]*s

            nx %= N
            ny %= N

            if nx == 0: nx = N
            if ny == 0: ny = N

            infos.append((nx, ny, m, s, d))
            next_fire_poses.add((nx, ny))

        grid[x][y].clear()

    for x, y, m, s, d in infos:
        if grid[x][y]: split_poses.add((x, y))
        grid[x][y].append([m, s, d])

    return split_poses, next_fire_poses


def split_fire(fire_poses):
    for x, y, in fire_poses:
        m_sum, s_sum, odd, even, cnt, k = 0, 0, 0, 0, 0, 0
        for m, s, d in grid[x][y]:
            m_sum += m
            s_sum += s
            cnt += 1

            if d%2 == 0: even += 1
            else: odd += 1

        grid[x][y].clear()

        if m_sum < 5: continue

        n_m = m_sum // 5
        n_s = s_sum // cnt

        if even == 0 or odd == 0: k = 4

        for i in range(4):
            grid[x][y].append([n_m, n_s, dir[i+k]])
            
    return


def print_ans(fire_poses, debug):
    if debug:
        for g in grid:
            print(g)

    ans = 0
    for pos in fire_poses:
        for m, _, _ in grid[pos[0]][pos[1]]:
            ans += m
    print(ans)
    return


N, M, K = map(int, input().split())

grid = list(list([] for _ in range(N+1)) for _ in range(N+1))
fire_poses = set()

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    grid[r][c].append([m, s, d])
    fire_poses.add((r, c))

for _ in range(K):
    split_poses, fire_poses = move_fire(fire_poses)
    split_fire(split_poses)

print_ans(fire_poses, False)

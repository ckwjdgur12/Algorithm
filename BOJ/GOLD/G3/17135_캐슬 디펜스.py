import sys
from itertools import combinations
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

dx = [0, -1, 0]
dy = [-1, 0, 1]

def get_target_pos(x, y):
    if grid[x][y] == 1: return (x, y)

    dq = deque([(x, y)])
    visited = list([False] * M for _ in range(N))
    cur_dist = 2

    while cur_dist <= D:
        next_dq = deque()

        while dq:
            x, y = dq.popleft()

            for i in range(3):
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0 <= nx < N and 0 <= ny < M): continue
                if visited[nx][ny]: continue

                if grid[nx][ny] == 1: return (nx, ny)
                visited[nx][ny] = True
                next_dq.append((nx, ny))

        dq = next_dq
        cur_dist += 1

    return False


N, M, D = map(int, input().split())

grid = list(list(map(int, input().split())) for _ in range(N))
archer_poses = list(combinations(range(M), 3))

limit = 0
for g in grid:
    for enemy in g:
        if enemy: limit += 1

max_cnt = -1
for cur_archer_poses in archer_poses:
    cur_dead_enemy = set()
    cnt = 0

    for turn in range(N-1, -1, -1):
        if cnt + (turn+1)*3 <= max_cnt: break
        if cnt == limit: 
            print(limit)
            exit(0)

        t_poses = set()
        for pos in cur_archer_poses:
            t_pos = get_target_pos(turn, pos)
            if t_pos: 
                t_poses.add(t_pos)
                cur_dead_enemy.add(t_pos)

        for t_x, t_y in t_poses:
            grid[t_x][t_y] = 0
            cnt += 1

    max_cnt = max(max_cnt, cnt)

    for d_x, d_y in cur_dead_enemy:
        grid[d_x][d_y] = 1

print(max_cnt)

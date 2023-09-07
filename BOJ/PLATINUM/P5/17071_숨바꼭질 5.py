import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def bfs(N, K):
    if N == K: return 0

    poses = set([N])
    visited = list([-1] * 500001 for _ in range(2))

    level = 1
    while True:
        next_poses = set()

        for pos in poses:
            for n_pos in (pos + 1, pos - 1, pos * 2):
                if not (0 <= n_pos <= 500000): continue
                if visited[level % 2][n_pos] != -1: continue

                visited[level % 2][n_pos] = level
                next_poses.add(n_pos)

        poses = next_poses
        K += level

        if K > 500000: return -1
        if visited[level % 2][K] != -1: return level

        level += 1


N, K = map(int, input().split())

print(bfs(N, K))

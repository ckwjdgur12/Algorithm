import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

N, L = map(int, input().split())
MAP = list(list(map(int, input().split())) for _ in range(N))

for _ in range(N):
    MAP.append([0] * N)

for i in range(N):
    for j in range(N):
        MAP[i+N][j] = MAP[j][i]

cnt = 0
for row in range(N*2):
    c = 1
    for col in range(N-1):
        if MAP[row][col] == MAP[row][col+1]: c += 1
        elif MAP[row][col]+1 == MAP[row][col+1] and c >= L: c = 1
        elif MAP[row][col]-1 == MAP[row][col+1] and c >= 0: c = -L+1
        else:
            c = -1
            break

    if col == N-2 and c >= 0: cnt += 1

print(cnt)

import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

N, M = map(int, input().split())

paper = []
for _ in range(N):
    paper.append(list(map(int, input().strip())))

ans = -1
for bit in range(1 << (N*M)):

    total = 0
    for row in range(N):
        row_sum = 0
        for col in range(M):
            idx = row*M + col

            if bit & (1 << idx) != 0:
                row_sum = row_sum * 10 + paper[row][col]
            else:
                total += row_sum
                row_sum = 0
        total += row_sum

    for col in range(M):
        col_sum = 0
        for row in range(N):
            idx = row*M + col

            if bit & (1 << idx) == 0:
                col_sum = col_sum * 10 + paper[row][col]
            else:
                total += col_sum
                col_sum = 0
        total += col_sum

    ans = max(ans, total)

print(ans)

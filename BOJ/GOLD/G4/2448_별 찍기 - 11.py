import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

N = int(input())

stars = [[' '] * (2*N-1) for _ in range(N)]

def recursion(i, j, size):
    if size == 3:
        stars[i][j] = '*'
        stars[i+1][j-1:j+2:2] = '*' * 2
        stars[i+2][j-2:j+3] = '*' * 5

    else:
        # 0, 11, 12
        next_size = size // 2
        recursion(i, j, next_size)
        recursion(i + next_size, j-next_size, next_size)
        recursion(i + next_size, j+next_size, next_size)

recursion(0, N-1, N)

for star in stars:
    print("".join(star))

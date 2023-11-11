import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

N, m = map(int, input().split())
P = 0
M = 1

seq = list([-1] * 2 for _ in range(N+1))

for _ in range(m):
    # P = 광합성
    # M = 운동성
    a, b, c = map(str, input().split())
    a = int(a)
    c = int(c)
    if c == 1:
        if b == 'P':
            seq[a][P] = True
        elif b == 'M':
            seq[a][M] = True
    else:
        if b == 'P':
            seq[a][P] = False
        elif b == 'M':
            seq[a][M] = False

max_value = 0
min_value = 0

for p, m in seq[1:]:
    if p == -1 and m == False:
        max_value += 1
    elif p == True and m == False:
        max_value += 1
        min_value += 1
    elif p == True and m == -1:
        max_value += 1
    elif p == -1 and m == -1:
        max_value += 1

print(min_value, max_value)



import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")


LEFT = 1
RIGHT = 2


T, W = map(int, input().split())
p_p = list(int(input()) for _ in range(T))
p_p.insert(0, 0)

p_c = list([0] * (W+1) for _ in range(T+1))

for t in range(1, T+1):

    if p_p[t] == LEFT: 
        p_c[t][0] += p_c[t-1][0] + 1
    else: 
        p_c[t][0] = p_c[t-1][0]

    for j_c in range(1, min(t+1, W+1)):
        if p_p[t] == LEFT and not j_c%2:
            p_c[t][j_c] = max(p_c[t-1][j_c-1], p_c[t-1][j_c]) + 1
        elif p_p[t] == RIGHT and j_c%2:
            p_c[t][j_c] = max(p_c[t-1][j_c-1], p_c[t-1][j_c]) + 1
        else:
            p_c[t][j_c] = max(p_c[t-1][j_c-1], p_c[t-1][j_c])

print(max(p_c[-1]))

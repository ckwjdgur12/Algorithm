import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

N = int(input())
order = list(map(int, input().split()))
seq = sorted(order)
maxN = max(seq) + 1
exist = [False] * (maxN)
score = [0] * (maxN)

for elem in seq:
    exist[elem] = True

for elem in seq:
    idx = elem*2
    while idx < maxN:
        if exist[idx]:
            score[elem] += 1
            score[idx] -= 1
        idx += elem

result = []
for elem in order:
    result.append(score[elem])

print(*result)

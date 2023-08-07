import sys
input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
    exit(0)

scores = []
for _ in range(n):
    scores.append(int(input()))
scores.sort()

cut = round(n * 0.15 + 0.00000001)
divider = n - cut*2

fr = cut
to = n-cut

print(round((sum(scores[fr:to]) / divider) + 0.00000001))

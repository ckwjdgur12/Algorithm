import sys
from bisect import bisect_left

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

N = int(input())
children = list(int(input()) for _ in range(N))

LIS = [children[0]]

for c in children[1:]:
    if c > LIS[-1]:
        LIS.append(c)
    else:
        LIS[bisect_left(LIS, c)] = c

print(N - len(LIS))

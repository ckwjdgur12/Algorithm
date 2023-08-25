import sys
from itertools import combinations
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

first = True

while True:
    input_string = list(map(int, input().split()))

    if input_string[0] == 0: break

    if not first: print()
    else: first = False

    k = input_string[0]
    seq = input_string[1:]

    combs = sorted(list(combinations(seq, 6)))

    for comb in combs:
        print(*comb)

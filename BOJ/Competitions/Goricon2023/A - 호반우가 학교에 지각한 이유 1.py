import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

S, D, I, L, N = map(int, input().split())

goal = N * 4
stat_sum = S + D + I + L
print(max(goal - stat_sum, 0))

import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

N, X = map(int, input().split())

dorm = list(map(int, input().split()))

n_ppl = sum(dorm)

if n_ppl % X == 0: print(1)
else: print(0)

import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

N = int(input())

cards = []
for _ in range(N):
    up, down = map(int, input().split())
    diff = up - down
    cards.append((up, down, diff))

cards.sort(key = lambda x:x[2], reverse = True)

h = 0
lowest = 0
power = 0
for up, down, diff in cards:

    h += up
    power += h
    h -= down

    lowest = min(lowest, h)

print(power + (-lowest * len(cards)))


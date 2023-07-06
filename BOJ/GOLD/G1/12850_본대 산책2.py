import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def getCnt(time, fr, to):

    if time <= 1: return dp[time][fr][to]

    dp.setdefault(time, [[0] * size for _ in range(size)])
    
    if dp[time][fr][to]: return dp[time][fr][to]

    if time % 2 == 0: left, right = time // 2, time // 2
    else: left, right = time // 2, time // 2 + 1

    for i in range(size):
        dp[time][fr][to] += getCnt(left, fr, i) * getCnt(right, i, to)
        dp[time][fr][to] %= 1000000007

    return dp[time][fr][to]

D = int(input())

size = 8
dp = {}
dp[1] = [
    [0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0],
]

print(getCnt(D, 0, 0))

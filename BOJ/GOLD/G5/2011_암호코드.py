import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

MOD = 1000000

cipher = list(map(int, input().strip()))

dp = [1] * 5002
for i in range(3, 5002):
    dp[i] = dp[i-1] + dp[i-2]

ways = 1
cnt = 2
pre = 0
for c in cipher:
    if c == 1 or c == 2: cnt += 1
    elif (pre == 0 or pre > 2) and c == 0:
        print(0)
        exit()
    else:
        if pre == 2 and c > 6: cnt -= 1
        if c == 0: cnt -= 2
        ways *= dp[cnt]
        ways %= MOD
        cnt = 2
    pre = c

if cnt != 2:
    ways *= dp[cnt-1]
    ways %= MOD

print(ways)

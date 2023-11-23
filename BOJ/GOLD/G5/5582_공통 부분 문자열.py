import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")


f_s = list(input().strip())
s_s = list(input().strip())
f_s.insert(0, 0)
s_s.insert(0, 0)
f_l = len(f_s)
s_l = len(s_s)

dp = list([0] * s_l for _ in range(f_l))

ans = 0
for f in range(1, f_l):
    for s in range(1, s_l):
        if f_s[f] == s_s[s]:
            dp[f][s] = dp[f-1][s-1] + 1
            ans = max(ans, dp[f][s])

print(ans)

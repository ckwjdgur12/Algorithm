import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")


INF = 987654321


def dfs(s1, s2, s3):

    if s1 < 0: s1 = 0
    if s2 < 0: s2 = 0
    if s3 < 0: s3 = 0
    if dp[s1][s2][s3]: return dp[s1][s2][s3]

    m1, m2, m3, m4, m5, m6 = 0, 0 ,0, 0, 0, 0
    if s1 >= s2 >= s3 or s1 >= s3 >= s2: 
        m1, m2, m3 = 9, 3, 1
        m4, m5, m6 = 9, 1, 3
    elif s2 >= s1 >= s3 or s2 >= s3 >= s1:
        m1, m2, m3 = 3, 9, 1
        m4, m5, m6 = 1, 9, 3
    elif s3 >= s1 >= s2 or s3 >= s2 >= s1:
        m1, m2, m3 = 3, 1, 9
        m4, m5, m6 = 1, 3, 9

    min_1, min_2 = INF, INF
    if s1-m1 < 1 and s2-m2 < 1 and s3-m3 < 1: min_1 = dp[s1][s2][s3]
    if s1-m4 < 1 and s2-m5 < 1 and s3-m6 < 1: min_2 = dp[s1][s2][s3]

    if min_1 == INF: min_1 = dfs(s1-m1, s2-m2, s3-m3)
    if min_2 == INF: min_2 = dfs(s1-m4, s2-m5, s3-m6)

    dp[s1][s2][s3] = min(min_1, min_2) + 1
    return dp[s1][s2][s3]


N = int(input())
SCV = [0, 0, 0]
infos = list(map(int, input().split()))
for i in range(N):
    SCV[i] = infos[i]

dp = list(list([0] * (SCV[2]+1) for _ in range(SCV[1]+1)) for _ in range(SCV[0]+1))

print(dfs(SCV[0], SCV[1], SCV[2]))

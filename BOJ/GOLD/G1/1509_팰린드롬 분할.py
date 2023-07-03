import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

string = input().strip()

dp = [2500] * 2501
dp[-1] = 0
is_p = [[False] * 2500 for _ in range(2500)]

for i in range(2500):
    is_p[i][i] = True

for i in range(1, len(string)):
    if string[i-1] == string[i]: is_p[i-1][i] = True

for end in range(2, len(string)):
    for start in range(end-1):
        if string[start] == string[end] and is_p[start+1][end-1]:
            is_p[start][end] = True

for start in range(len(string)):
    for end in range(len(string)):
        if is_p[start][end]:
            dp[end] = min(dp[end], dp[start-1]+1)
        else:
            dp[end] = min(dp[end], dp[end-1] + 1)
            
print(dp[len(string)-1])


import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

N = int(input())
train = [0] + list(map(int, input().split()))
limit = int(input())

for i in range(N):
    train[i+1] += train[i]

sum_lst = [0] * limit
for i in range(limit, N+1):
    sum_lst.append(train[i] - train[i-limit])

dp = list([0] * (N+1) for _ in range(4))
for i in range(1, 4):
    for j in range(limit*i, N+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-limit] + sum_lst[j])

print(dp[3][N])

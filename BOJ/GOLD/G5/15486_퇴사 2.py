import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")


N = int(input())
schedule = list(list(map(int, input().split())) for _ in range(N))
schedule.insert(0, 0)

dp = [0] * (N+1)

for day in range(1, N+1):
    dp[day] = max(dp[day], dp[day-1])
    t, p = schedule[day]

    fin_date = day + t - 1

    if fin_date <= N:
        dp[fin_date] = max(dp[fin_date], dp[day - 1] + p)

print(dp[-1])

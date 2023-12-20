import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")


INF = 987654321


C, N = map(int, input().split())

costs, customers = [0], [0]
for _ in range(N):
    co, cu = map(int, input().split())
    costs.append(co)
    customers.append(cu)

dp = [INF] * (C+1)

for city in range(1, N+1):
    for customer in range(1, min(customers[city]+1, C+1)):
        dp[customer] = min(dp[customer], costs[city])
            
    for customer in range(customers[city]+1, C+1):    
        dp[customer] = min(dp[customer], dp[customer-customers[city]] + costs[city])

print(dp[C])

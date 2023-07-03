import sys
input = sys.stdin.readline
INF = 9876543210

T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())

    if M == 0:
        print("Poor KCM")
        continue

    airport = [[] for _ in range(N+1)]
    for _ in range(K):
        # 출발공항, 도착공항, 비용, 소요시간
        u, v, c, d = map(int, input().split())
        airport[u].append((v, c, d))

    dp = [[INF] * (M+1) for _ in range(N+1)]
    dp[1][0] = 0

    for cost in range(M+1):
        for destination in range(1, N+1):
            if dp[destination][cost] == INF: continue
            takenTime = dp[destination][cost]
            for nextDestination, additionalCost, additionalTime in airport[destination]:
                if cost + additionalCost > M: continue
                dp[nextDestination][cost + additionalCost] = min(dp[nextDestination][cost + additionalCost], takenTime + additionalTime)

    if min(dp[N]) == INF:
        print("Poor KCM")
    else:
        print(min(dp[N]))

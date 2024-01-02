import sys

sys.stdin = open("BOJ/input.txt", "r")


INF = 9876543210


def TSP(now, visited):
    if visited == (1<<N) - 1: return dists[now][N]

    if dp[now][visited] != INF: return dp[now][visited]

    min_dist = INF
    for i in range(N):
        if not visited & (1<<i) and dists[now][i] != 0:
            min_dist = min(min_dist, dists[now][i] + TSP(i, visited | (1<<i)))

    dp[now][visited] = min_dist
    return min_dist


T = int(input())
for test_case in range(1, T+1):
    
    N = int(input())

    input_data = list(map(int, input().split()))

    company = (input_data[0], input_data[1])
    home = (input_data[2], input_data[3])
    poses = []

    poses.append(company)
    for i in range(4, 4+N*2, 2):
        poses.append((input_data[i], input_data[i+1]))
    poses.append(home)

    N += 1

    dists = list([0] * (N+1) for _ in range(N+1))
    for i in range(N+1):
        for j in range(N+1):
            if i == j: continue
            dists[i][j] = abs(poses[i][0] - poses[j][0]) + abs(poses[i][1] - poses[j][1])

    dp = list([INF] * (1 << N) for _ in range(N))

    print(f'#{test_case} {TSP(0, 1)}')
        
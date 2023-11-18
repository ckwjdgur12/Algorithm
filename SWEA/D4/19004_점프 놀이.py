INF = 987654321

T = int(input())
for test_case in range(1, T + 1):

    N, K = map(int, input().split())
    graph = list(list(map(int, input().split())) for _ in range(N))
    dist = list([INF] * N for _ in range(N))
    pos = list([] for _ in range(K+1))
    ans = INF

    for i in range(N):
        for j in range(N):
            pos[graph[i][j]].append((i, j))

    for p in pos[1:]:
        if not p: ans = -1

    if ans == -1:
        print(f'#{test_case} {ans}')
        continue

    for x, y in pos[1]:
        dist[x][y] = 0

    for i in range(1, K):
        for fx, fy in pos[i]:
            for tx, ty in pos[i+1]:
                cur_dist = abs(tx - fx) + abs(ty - fy) + dist[fx][fy]
                if dist[tx][ty] > cur_dist:
                    dist[tx][ty] = cur_dist

    for x, y in pos[K]:
        ans = min(ans, dist[x][y])

    print(f'#{test_case} {ans}')

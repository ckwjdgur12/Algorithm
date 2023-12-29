import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")


p_dx = [1, -1, 0, 0]
p_dy = [0, 0, 1, -1]
m_dx = [-1, -1, 1, 1]
m_dy = [-1, 1, 1, -1]


def check(x, y, power):
    p_flies, m_flies = grid[x][y], grid[x][y]

    for i in range(4):
        for p in range(1, power):
            p_nx, p_ny = x + p_dx[i]*p, y + p_dy[i]*p
            m_nx, m_ny = x + m_dx[i]*p, y + m_dy[i]*p

            if 0 <= p_nx < N and 0 <= p_ny < N:
                p_flies += grid[p_nx][p_ny]

            if 0 <= m_nx < N and 0 <= m_ny < N:
                m_flies += grid[m_nx][m_ny]

    return max(p_flies, m_flies)


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    grid = list(list(map(int, input().split())) for _ in range(N))

    ans = 0
    for i in range(N):
        for j in range(N):
            ans = max(ans, check(i, j, M))

    print(f'#{test_case} {ans}')
    
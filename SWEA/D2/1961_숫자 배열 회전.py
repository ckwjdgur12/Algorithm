import sys

sys.stdin = open("BOJ/input.txt", "r")


T = int(input())
for test_case in range(1, T+1):
    
    N = int(input())
    mat = list(list(map(str, input().split())) for _ in range(N))
    ans = list([''] * 3 for _ in range(N))
    
    for j in range(N):
        for i in range(N-1, -1, -1):
            ans[j][0] += mat[i][j]

    for j in range(1, N+1):
        for i in range(N-1, -1, -1):
            ans[j-1][1] += mat[-j][i]

    for j in range(1, N+1):
        for i in range(N):
            ans[j-1][2] += mat[i][-j]

    print(f'#{test_case}')
    for a in ans:
        print(" ".join(a))

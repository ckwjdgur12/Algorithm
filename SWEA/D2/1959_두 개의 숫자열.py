import sys

sys.stdin = open("BOJ/input.txt", "r")


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    i_seq = list(map(int, input().split()))
    j_seq = list(map(int, input().split()))

    ans = 0
    if N < M:
        for offset in range(M-N+1):
            t_ans = 0
            for i in range(len(i_seq)):
                t_ans += i_seq[i]*j_seq[i+offset]
            ans = max(ans, t_ans)
    else:
        for offset in range(N-M+1):
            t_ans = 0
            for i in range(len(j_seq)):
                t_ans += j_seq[i]*i_seq[i+offset]
            ans = max(ans, t_ans)

    print(f'#{test_case} {ans}')

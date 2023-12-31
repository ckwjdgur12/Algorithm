import sys

sys.stdin = open("BOJ/input.txt", "r")


T = int(input())
for test_case in range(1, T+1):

    _ = input()
    score_cnt = [0] * 101
    scores = list(map(int, input().split()))

    for score in scores:
        score_cnt[score] += 1

    ans = 0
    max_cnt = 0
    for i in range(1, 101):
        if max_cnt <= score_cnt[i]:
            max_cnt = score_cnt[i]
            ans = i
    
    print(ans)

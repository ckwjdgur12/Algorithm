import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

N = int(input())
N -= 1
*seq, goal = list(map(int, input().split()))

dp = list([0] * 21 for _ in range(N))
dp[0][seq[0]] = 1

for seq_idx in range(1, N):
    for num in range(21):
        if not dp[seq_idx-1][num]: continue

        if num + seq[seq_idx] <= 20:
            dp[seq_idx][num + seq[seq_idx]] += dp[seq_idx-1][num]
        if num - seq[seq_idx] >= 0:
            dp[seq_idx][num - seq[seq_idx]] += dp[seq_idx-1][num]

print(dp[-1][goal])

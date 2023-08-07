import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

N = int(input())

dp = [0] * 31
dp[0] = 1

for i in range(2, 31, 2):
    dp[i] = (dp[i-2] * 3)
    for j in range(i-4, -1, -2):
        dp[i] += dp[j] * 2

print(dp[N])

'''

홀수는 모두 0

N = 2
3

N = 4
(N-2) * 3 + 2 * (N-4) = 11

N = 6
(N-2) * 3 + 2 * (N-4) + 2 * (N-6) + 2 = 41
33          9           +2

N = 8
(N-2) * 3 + 2 * (N-4) + 2 * (N-6) + 2 = 153 
123         22          6           2

N = 10
(N-2) * 3 + 2 * (N-4) + 2 * (N-6) + 2 =



'''


import sys
input = sys.stdin.readline

N = int(input())
dp = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(N+1)] # dp[자리 수][시작 숫자][숫자 여부(Bit-Masking)]

for i in range(10):
    dp[1][i][1 << i] = 1

for i in range(2, N+1):
    for j in range(10):
        for k in range(1 << 10):
            if j < 9: dp[i][j][(1 << j) | k] += dp[i-1][j+1][k]
            if j > 0: dp[i][j][(1 << j) | k] += dp[i-1][j-1][k]
            dp[i][j][(1 << j) | k] %= 1000000000

ans = 0
for i in range(1, 10):
    ans += dp[N][i][(1<<10) - 1]
    ans %= 1000000000
print(ans)


# 이걸로는 시간 너무 많이 걸려 ㅠ
# N = int(input())
# cnt = 0

# def dfs(preNum, depth):
#     global cnt

#     if depth == N-1:
#         if 0 not in myNumArr: cnt += 1
#         return

#     if preNum == 0:
#         myNumArr[preNum+1] += 1
#         dfs(preNum+1, depth+1)
#         myNumArr[preNum+1] -= 1
#     elif preNum == 9: 
#         myNumArr[preNum-1] += 1
#         dfs(preNum-1, depth+1)
#         myNumArr[preNum-1] -= 1
#     else:
#         myNumArr[preNum+1] += 1
#         dfs(preNum+1, depth+1)
#         myNumArr[preNum+1] -= 1
#         myNumArr[preNum-1] += 1
#         dfs(preNum-1, depth+1)
#         myNumArr[preNum-1] -= 1

# for i in range(1, 10):
#     myNumArr = [0] * 10
#     myNumArr[i] += 1
#     dfs(i, 0)

# print(cnt)

import sys
import bisect
from itertools import combinations
input = sys.stdin.readline

N, S = map(int, input().split())
seq = list(map(int, input().split()))

cnt = 0
leftSeq = seq[:N//2]
rightSeq = seq[N//2:]
leftCombSum = []
rightCombSum = []

for i in range(1, len(leftSeq)+1):
    tmpComb = combinations(leftSeq, i)
    for com in tmpComb:
        tmp = sum(com)
        leftCombSum.append(tmp)
        if tmp == S: cnt += 1

for i in range(1, N-(N//2)+1):
    tmpComb = combinations(rightSeq, i)
    for com in tmpComb:
        tmp = sum(com)
        rightCombSum.append(tmp)
        if tmp == S: cnt += 1

rightCombSum.sort()
for LCS in leftCombSum:
    cnt += bisect.bisect_right(rightCombSum, S-LCS) - bisect.bisect_left(rightCombSum, S-LCS)

print(cnt)


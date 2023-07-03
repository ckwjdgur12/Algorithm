import sys
import math
input = sys.stdin.readline
n = int(input())

primeCheck = [True for i in range(n+1)]
primeCheck[0] = False
primeCheck[1] = False
prime = []

for i in range(2, int(math.sqrt(n)+1)): # 에라토스테네스의 체
    if primeCheck[i]:
        j = 2

        while (i*j) <= n:
            primeCheck[i*j] = False
            j += 1

for i in range(2, n+1): # 소수만 모아서 List 만들기
    if primeCheck[i]:
        prime.append(i)

l = 0
r = 0
cnt = 0
while (r < len(prime) and l <= r): # 투 포인터 사용
    now = sum(prime[l:r+1])

    if now == n: cnt+=1 # 합이 n과 같다면 cnt 1 증가

    if now < n: r += 1  # 합이 n보다 작다면 왼쪽 포인터 index 증가
    else: l += 1        # 합이 n보다 크다면 오른쪽 포인터 index 증가

print(cnt)



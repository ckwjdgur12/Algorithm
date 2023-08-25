import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

N = int(input())

arr = [0] * N
target = list(map(int, input().split()))

cnt = 0
while True:

    for i in range(N):
        if target[i] & 1:
            target[i] -= 1
            cnt += 1

    if arr == target: break

    for i in range(N):
        target[i] //= 2
    cnt += 1
        
print(cnt)

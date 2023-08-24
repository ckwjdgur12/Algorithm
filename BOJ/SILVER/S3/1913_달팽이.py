import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

N = int(input())
target = int(input())

arr = list([None] * (N+1) for _ in range(N+1))

x, y = N//2 + 1, N//2 + 1
arr[x][y] = 1
dist = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

num = 2
ans = ()

if target == 1: ans = (x, y)
    
while dist < N//2 + 1:
    for i in range(4):
        nx = x + dx[i] * dist - (dist-1) * dy[i]
        ny = y + dy[i] * dist + (dist-1) * dx[i]

        for d in range(dist*2):
            arr[nx + (d * dy[i])][ny - (d * dx[i])] = num
            if num == target:
                ans = (nx + (d * dy[i]), ny - (d * dx[i]))
            num += 1
    
    dist += 1

for a in arr[1:]:
    print(*a[1:])
print(*ans)

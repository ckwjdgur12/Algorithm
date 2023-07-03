import sys
input = sys.stdin.readline
# sys.stdin = open("BOJ/input.txt", "r")

def BackTracking(n, cnt):
    global ans

    if ans >= cnt + (lastNum + 1 - n) // 2: return

    if n >= lastNum:
        ans = max(ans, cnt)
        return
    
    for x, y in lst[n]:
        if not visited[x-y]:
            visited[x-y] = True
            BackTracking(n+2, cnt+1)
            visited[x-y] = False
    BackTracking(n+2, cnt)



size = int(input())
board = [list(map(int, input().split())) for _ in range(size)]

lst = [[] for _ in range(2*size)]

for i in range(size):
    for j in range(size):
        if board[i][j] == 1: lst[i+j].append((i, j))

visited = [False] * (2*size)
lastNum = 2*size - 1

ans = 0
BackTracking(0, 0)
black = ans
ans = 0
BackTracking(1, 0)
white = ans
print(black + white)

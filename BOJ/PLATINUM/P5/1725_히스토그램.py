import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

N = int(input())

histogram = []
for _ in range(N):
    histogram.append(int(input()))

s = []
ans = 0

for i in range(N):
    while s and histogram[s[-1]] > histogram[i]:
        height = histogram[s[-1]]
        width = i
        s.pop()
        if s: 
            width = i - s[-1] - 1
        ans = max(ans, width*height)
    s.append(i)

while s:
    height = histogram[s[-1]]
    width = N
    s.pop()
    if s: 
        width = N - s[-1] - 1
    ans = max(ans, width*height)

print(ans)

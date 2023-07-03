import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def findParent(x):
    if parent[x] != x:
        parent[x] = findParent(parent[x])
    return parent[x]

def unionParent(x, y):
    x = findParent(x)
    y = findParent(y)
    if x < y: parent[y] = x
    else: parent[x] = y

def descriminate(l1, l2):
    a = (l1[0], l1[1])
    b = (l1[2], l1[3])
    c = (l2[0], l2[1])
    d = (l2[2], l2[3])

    if a > b: a, b = b, a
    if c > d: c, d = d, c

    ab = (b[0] - a[0], b[1] - a[1])
    ac = (c[0] - a[0], c[1] - a[1])
    ad = (d[0] - a[0], d[1] - a[1])

    area1 = ab[0] * ac[1] - ab[1] * ac[0]  # 선분ab 와 점c로 만든 삼각형 넓이
    area2 = ab[0] * ad[1] - ab[1] * ad[0]  # 선분ab 와 점d로 만든 삼각형 넓이

    if area1 * area2 <= 0:
        if area1 == 0 and area2 == 0:  # 한 직선 위에 네 점 있을 때
            return a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d
        return 1
    else: 
        return 0


N = int(input())
lines = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    lines.append((x1, y1, x2, y2))

parent = [i for i in range(N)]

for i in range(N-1):
    for j in range(i+1, N):
        if descriminate(lines[i], lines[j]) and descriminate(lines[j], lines[i]):
            if findParent(i) != findParent(j):
                unionParent(i, j)

for i in range(N):
    findParent(i)

total = 0
biggest = [0] * N
for i in range(N):
    if i == parent[i]:
        total += 1
    biggest[parent[i]] += 1

print(total)
print(max(biggest))


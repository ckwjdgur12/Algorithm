import sys
input = sys.stdin.readline

def FindParent(x):
    if parent[x] != x : parent[x] = FindParent(parent[x])
    return parent[x]

def UnionParent(x, y):
    x, y = FindParent(x), FindParent(y)
    if x < y: parent[y] = x
    else: parent[x] = y


G = int(input())    # 게이트의 수
P = int(input())    # 비행기의 수

parent = list(i for i in range(G+1))
airplanes = []
for _ in range(P):
    airplanes.append(int(input()))

ans = 0
for airplane in airplanes:
    v = FindParent(airplane)

    if v == 0:
        break

    UnionParent(v, v-1)
    ans += 1

print(parent)
print(ans)

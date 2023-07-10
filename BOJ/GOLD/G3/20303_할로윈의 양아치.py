import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y: parent[y] = x
    else: parent[x] = y
    

N, M, K = map(int, input().split())
candy = list(map(int, input().split()))
parent = [i for i in range(N+1)]
for _ in range(M):
    f, t = map(int, input().split())
    union_parent(f, t)

for i in range(1, N+1):
    find_parent(i)

items = {}
for i in range(1, N+1):
    group_num = parent[i]
    if group_num not in items: items[group_num] = [1, candy[i-1]]
    else:
        items[group_num][0] += 1
        items[group_num][1] += candy[i-1]

length = len(items)
dp = [0] * K

for child_cnt, candy_cnt in items.values():
    for start in range(K-1-child_cnt, -1, -1):
        dp[start + child_cnt] = max(dp[start + child_cnt], dp[start] + candy_cnt)

print(dp[-1])

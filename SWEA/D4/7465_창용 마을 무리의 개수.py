import sys

sys.stdin = open("BOJ/input.txt", "r")


def find_parent(x):
    if parent[x] != x: parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y: parent[y] = x
    else: parent[x] = y


T = int(input())
for test_case in range(1, T+1):

    N, M = map(int, input().split())
    parent = list(i for i in range(N+1))

    for _ in range(M):
        p1, p2 = map(int, input().split())
        union_parent(p1, p2)

    for i in range(1, N+1):
        find_parent(i)

    ans = {}
    for p in parent[1:]:
        if p not in ans: ans[p] = True

    print(f'#{test_case} {len(ans)}')

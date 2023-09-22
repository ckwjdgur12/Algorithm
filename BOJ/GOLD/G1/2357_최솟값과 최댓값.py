import sys
import math
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

INF = 1000000001

def init_seg_tree(node, start, end):
    if start == end: tree[node] = (arr[start], arr[start])
    else:
        nn, mid = node*2, (start+end)//2
        init_seg_tree(nn, start, mid)
        init_seg_tree(nn+1, mid+1, end)
        tree[node] = (min(tree[nn][0], tree[nn+1][0]), max(tree[nn][1], tree[nn+1][1]))
    return


def query(node, start, end, left, right):
    if left > end or right < start: return (INF, -1)
    if left <= start and right >= end: return tree[node]

    nn, mid = node*2, (start+end)//2
    lresult = query(nn, start, mid, left, right)
    rresult = query(nn+1, mid+1, end, left, right)
    return (min(lresult[0], rresult[0]), max(lresult[1], rresult[1]))


N, M = map(int, input().split())

h = math.ceil(math.log2(N))
tree = [0] * ((1 << (h+1)) + 1)
arr = [0]
for _ in range(N):
    arr.append(int(input()))

init_seg_tree(1, 1, N)

for _ in range(M):
    a, b = map(int, input().split())
    print(*query(1, 1, N, a, b))

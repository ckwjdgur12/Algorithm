import sys
import math
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

mod = 1000000007

def init_seg_tree(node, start, end):
    if start == end: tree[node] = arr[start]
    else:
        nn, mid = node*2, (start+end)//2
        init_seg_tree(nn, start, mid)
        init_seg_tree(nn+1, mid+1, end)
        tree[node] = (tree[nn] * tree[nn+1]) % mod
    return


def update_tree(node, start, end, idx, val):
    if idx > end or idx < start: return
    if start == end:
        tree[node] = val
        return

    nn, mid = node*2, (start+end)//2
    update_tree(nn, start, mid, idx, val)
    update_tree(nn+1, mid+1, end, idx, val)
    tree[node] = (tree[nn] * tree[nn+1]) % mod
    return


def query(node, start, end, left, right):
    if left > end or right < start: return 1
    if left <= start and right >= end: return tree[node]

    nn, mid = node*2, (start+end)//2
    lsum = query(nn, start, mid, left, right)
    rsum = query(nn+1, mid+1, end, left, right)
    return (lsum * rsum) % mod


N, M, K = map(int, input().split())

h = math.ceil(math.log2(N))
tree = [0] * ((1 << (h+1)) + 1)
arr = [0]
for _ in range(N):
    arr.append(int(input()))

init_seg_tree(1, 1, N)

for _ in range(M+K):
    Q, b, c = map(int, input().split())
    if Q == 1: update_tree(1, 1, N, b, c)
    else: print(query(1, 1, N, b, c))

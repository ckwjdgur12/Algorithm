import sys
import math
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def init_seg_tree(node, start, end):
    if start == end: tree[node] = arr[start]
    else:
        nn, mid = node*2, (start+end)//2
        init_seg_tree(nn, start, mid)
        init_seg_tree(nn+1, mid+1, end)
        tree[node] = tree[nn] + tree[nn+1]
    return


def update_lazy(node, start, end):
    if lazy[node]:
        tree[node] += lazy[node] * (end-start+1)
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0
    return


def update_range(node, start, end, left, right, val):
    update_lazy(node, start, end)

    if left > end or right < start: return
    if left <= start and right >= end:
        tree[node] += (end-start+1) * val
        if start != end:
            lazy[node*2] += val
            lazy[node*2+1] += val
        return

    nn, mid = node*2, (start+end)//2
    update_range(nn, start, mid, left, right, val)
    update_range(nn+1, mid+1, end, left, right, val)
    tree[node] = tree[nn] + tree[nn+1]
    return


def query(node, start, end, idx):
    update_lazy(node, start, end)

    if idx < start or idx > end: return
    if idx == start == end: return tree[node]
    
    nn, mid = node*2, (start+end) // 2
    if start <= idx <= mid: return query(nn, start, mid, idx)
    else: return query(nn+1, mid+1, end, idx)


N = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)

h = math.ceil(math.log2(N))
tree_size = (1 << h+1) + 1
tree = [0] * tree_size
lazy = [0] * tree_size

init_seg_tree(1, 1, N)

M = int(input())
for _ in range(M):
    q = list(map(int, input().split()))

    if q[0] == 1:
        left, right, val = q[1:]
        update_range(1, 1, N, left, right, val)
    else:
        idx = q[1]
        print(query(1, 1, N, idx))

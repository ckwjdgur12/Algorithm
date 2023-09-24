import sys
import math
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def init_seg_tree(node, start, end):
    if start == end: 
        tree[node] = arr[start]
        return tree[node]
    else:
        nn, mid = node << 1, (start+end) >> 1
        tree[node] = init_seg_tree(nn, start, mid) + init_seg_tree(nn+1, mid+1, end)
        return tree[node]        


def query(node, start, end, left, right):
    if left > end or right < start: return 0
    if left <= start <= end <= right: return tree[node]

    nn, mid = node << 1, (start+end) >> 1
    return query(nn, start, mid, left, right) + query(nn+1, mid+1, end, left, right)


def update_tree(node, start, end, idx, val):
    tree[node] += val
    if start != end:
        nn, mid =node << 1, (start + end) >> 1
        if idx <= mid: update_tree(nn, start, mid, idx, val)
        else: update_tree(nn+1, mid+1, end, idx, val)


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    l = n+m

    h = math.ceil(math.log2(l))
    tree_size = (1 << h+1) + 1
    tree = [0] * tree_size

    pos = list(i+m for i in range(1, n+1))
    pos.insert(0, 0)

    arr = [0] * (l+1)
    for i in range(m+1, l+1):
        arr[i] = 1

    n_pos = m
    ans = []

    init_seg_tree(1, 1, l)

    queries = list(map(int, input().split()))
    for q in queries:
        ans.append(query(1, 1, l, 1, pos[q]-1))
        update_tree(1, 1, l, pos[q], -1)
        update_tree(1, 1, l, m, 1)
        pos[q] = m
        m -= 1

    print(*ans)

import sys
import math
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def init_seg_tree(node, start, end):
    if start == end: 
        tree[node] = arr[start]
        return tree[node]
    
    nn, mid = node*2, (start+end)//2
    tree[node] = init_seg_tree(nn, start, mid) ^ init_seg_tree(nn+1, mid+1, end)
    return tree[node]


def update_lazy(node, start, end):
    if lazy[node]:
        if (end-start+1) % 2: tree[node] ^= lazy[node]
        if start != end:
            lazy[node*2] ^= lazy[node]
            lazy[node*2+1] ^= lazy[node]
        lazy[node] = 0
    return


def update_tree(node, start, end, left, right, val):
    update_lazy(node, start, end)
    
    if left > end or right < start: return
    if left <= start <= end <= right:
        if (end-start+1) % 2: tree[node] ^= val
        if start != end:
            lazy[node*2] ^= val
            lazy[node*2+1] ^= val
        return
    
    nn, mid = node*2, (start+end)//2
    update_tree(nn, start, mid, left, right, val)
    update_tree(nn+1, mid+1, end, left, right, val)
    tree[node] = tree[nn] ^ tree[nn+1]
    return


def query(node, start, end, left, right):
    update_lazy(node, start, end)

    if left > end or right < start: return 0
    if left <= start <= end <= right: return tree[node]

    nn, mid = node*2, (start+end)//2
    lxor = query(nn, start, mid, left, right)
    rxor = query(nn+1, mid+1, end, left, right)

    return lxor ^ rxor


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
    func, *q = map(int, input().split())

    if func == 1:
        left, right, val = q
        update_tree(1, 1, N, left+1, right+1, val)
    else:
        left, right = q
        print(query(1, 1, N, left+1, right+1))

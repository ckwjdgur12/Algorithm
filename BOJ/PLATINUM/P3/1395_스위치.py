import sys
import math
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def update_lazy(node, start, end):
    if lazy[node]:
        tree[node] = (end-start+1) - tree[node]
        if start != end:
            lazy[node*2] ^= 1 
            lazy[node*2+1] ^= 1
        lazy[node] = 0
    return


def update_tree(node, start, end, left, right):
    update_lazy(node, start, end)

    if left > end or right < start: return
    if left <= start and right >= end:
        tree[node] = (end-start+1) - tree[node]
        if start != end:
            lazy[node*2] ^= 1
            lazy[node*2+1] ^= 1
        return
    
    nn, mid = node*2, (start+end)//2
    update_tree(nn, start, mid, left, right)
    update_tree(nn+1, mid+1, end, left, right)
    tree[node] = tree[nn] + tree[nn+1]
    return


def query(node, start, end, left, right):
    update_lazy(node, start, end)

    if left > end or right < start: return 0
    if left <= start and right >= end: return tree[node]

    nn, mid = node*2, (start+end)//2
    lsum = query(nn, start, mid, left, right)
    rsum = query(nn+1, mid+1, end, left, right)

    return lsum + rsum


N, M = map(int, input().split())

arr = [0] * (N+1)

h = math.ceil(math.log2(N))
tree_size = (1 << h+1) + 1
tree = [0] * tree_size
lazy = [0] * tree_size

for _ in range(M):
    q = list(map(int, input().split()))
    left, right = q[1:]

    if q[0] == 0: update_tree(1, 1, N, left, right)
    else: print(query(1, 1, N, left, right))
        

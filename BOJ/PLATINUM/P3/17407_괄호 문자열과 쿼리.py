import sys
import math
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def init_seg_tree(node, start, end):
    if start == end:
        tree[node] = asum[start]
        return tree[node]
    
    nn, mid = node*2, (start+end)//2
    tree[node] = min(init_seg_tree(nn, start, mid), init_seg_tree(nn+1, mid+1, end))
    return tree[node]


def update_lazy(node, start, end):
    if lazy[node]:
        tree[node] += lazy[node]
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0
    return


def update_range(node, start, end, left, right, val):
    update_lazy(node, start, end)

    if left > end or right < start: return tree[node]
    if left <= start <= end <= right:
        lazy[node] += val
        update_lazy(node, start, end)
        return tree[node]
    
    nn, mid = node*2, (start+end)//2
    tree[node] = min(update_range(nn, start, mid, left, right, val), update_range(nn+1, mid+1, end, left, right, val))
    return tree[node]


arr = list(input().strip())
l = len(arr)
arr.insert(0, 0)

asum = [0] * (l+1)
for i in range(1, l+1):
    if arr[i] == '(': asum[i] = 1
    else: asum[i] = -1

for i in range(1, l+1):
    asum[i] += asum[i-1]

h = math.ceil(math.log2(l))
tree_size = (1 << h+1) + 1
tree = [0] * tree_size
lazy = [0] * tree_size

init_seg_tree(1, 1, l)

N = int(input())
even, ans = 0, 0
for _ in range(N):
    idx = int(input())
    if arr[idx] == '(': val = -2
    else: val = 2
    even += val

    update_range(1, 1, l, idx, l, val)

    if arr[idx] == '(': arr[idx] = ')'
    else: arr[idx] = '('

    if (tree[1] > -1 and not even): ans += 1

print(ans)

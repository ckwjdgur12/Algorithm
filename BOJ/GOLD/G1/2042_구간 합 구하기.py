import sys
import math
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def init_segment_tree(node, start, end):
    if start == end: tree[node] = arr[start]
    else:
        n_n, n_p = node * 2, (start+end)//2
        init_segment_tree(n_n, start, n_p)
        init_segment_tree(n_n+1, n_p+1, end)
        tree[node] = tree[n_n] + tree[n_n+1]
    return


def update_tree(node, start, end, index, val):
    if index < start or index > end: return
    if start == end: 
        tree[node] = val 
        return
    
    n_n, n_p = node * 2, (start+end)//2
    update_tree(n_n, start, n_p, index, val)
    update_tree(n_n+1, n_p+1, end, index, val)
    tree[node] = tree[n_n] + tree[n_n+1]
    return


def query(node, start, end, left, right):
    if left > end or right < start: return 0
    if left <= start and right >= end: return tree[node]

    n_n, n_p = node * 2, (start+end)//2
    lsum = query(n_n, start, n_p, left, right)
    rsum = query(n_n+1, n_p+1, end, left, right)
    return lsum + rsum


N, M, K = map(int, input().split())

h = math.ceil(math.log2(N)) 
tree = [0] * 2**(h+1)
arr = [0]
for _ in range(N):
    arr.append(int(input()))

init_segment_tree(1, 1, N)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1: update_tree(1, 1, N, b, c)
    else: print(query(1, 1, N, b, c))

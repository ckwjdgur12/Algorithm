import sys
from heapq import heappop, heappush
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def push_value(n):
    if len(l_max_heap) == len(r_min_heap): heappush(l_max_heap, -n)
    else: heappush(r_min_heap, n)


def exchange_value():
    l_v = -heappop(l_max_heap)
    r_v = -heappop(r_min_heap)
    heappush(l_max_heap, r_v)
    heappush(r_min_heap, l_v)
    

def l_is_greater_than_r():
    return (r_min_heap and -l_max_heap[0] > r_min_heap[0])


def print_ans():
    for a in ans: print(a)
    return
    

N = int(input())
l_max_heap, r_min_heap = [], []
ans = []

for _ in range(N):
    num = int(input())
    push_value(num)

    if l_is_greater_than_r(): exchange_value()

    ans.append(-l_max_heap[0])

print_ans()

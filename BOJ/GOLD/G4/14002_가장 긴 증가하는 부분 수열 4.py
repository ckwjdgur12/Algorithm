import sys
from bisect import bisect_left
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

N = int(input())
seq = list(map(int, input().split()))

idx_lst = []
least_elem_lst = [0]
for i in range(N):
    if least_elem_lst[-1] < seq[i]:
        least_elem_lst.append(seq[i])
        idx_lst.append(len(least_elem_lst) - 1)
    else:
        idx = bisect_left(least_elem_lst, seq[i])
        least_elem_lst[idx] = seq[i]
        idx_lst.append(idx)

del least_elem_lst[0]
length = len(least_elem_lst)

LIS = []
for i in range(N-1, -1, -1):
    if length == 0: break
    if idx_lst[i] == length:
        LIS.append(seq[i])
        length -= 1

print(len(least_elem_lst))
print(*LIS[::-1])

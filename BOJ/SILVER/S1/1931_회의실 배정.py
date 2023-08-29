import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

N = int(input())

cnt = 0
conference = {}
exception_lst = []
for _ in range(N):
    start, end = map(int, input().split())

    if end not in conference and start != end: conference[end] = start
    elif start == end:
        cnt += 1
        if end not in exception_lst: exception_lst.append(end)
    elif start > conference[end]: conference[end] = start

conf_lst = sorted(conference)

exception_lst.append(2**31)
exception = exception_lst[0]
exception_idx = 1

cur_conf = -1
for i in range(len(conf_lst)):

    while conf_lst[i] > exception:
        cur_conf = exception
        exception = exception_lst[exception_idx]
        exception_idx += 1

    if (cur_conf <= conference[conf_lst[i]]):
        cnt += 1
        cur_conf = conf_lst[i]

print(cnt)

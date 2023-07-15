import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

for _ in range(int(input())):
    N, M = map(int, input().split())
    seq = list(map(int, input().split()))

    dq = deque()
    for i in range(N):
        dq.append((seq[i], i))

    seq.sort(reverse = True)
    seq = deque(seq)

    cnt = 0
    while True:
        value, idx = dq.popleft()

        if value < seq[0]:
            dq.append((value, idx))
        else:
            seq.popleft()
            cnt += 1
            if idx == M:
                print(cnt)
                break
            

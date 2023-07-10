import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def back_tracking(idx, depth):
    
    if depth == M:
        print(*ans)
        return
    
    for i in range(idx, N):
        ans.append(seq[i])
        back_tracking(i, depth+1)
        ans.pop()


N, M = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
ans = []
back_tracking(0, 0)

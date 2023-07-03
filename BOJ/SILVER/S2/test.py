import sys
input = sys.stdin.readline

N, M = map(int, input().split())
seq = list(map(int, input().split()))
visited = [False] * (N+1)
seq.sort()

result = []
mySeq = []


def BackTracking(depth):
    if depth == M:
        result.append(list(mySeq))
        return
    
    preNum = -1
    for i in range(N):
        if not visited[i] and preNum != seq[i]:
            visited[i] = True
            mySeq.append(seq[i])
            preNum = seq[i]
            BackTracking(depth+1)
            mySeq.pop()
            visited[i] = False

    return

BackTracking(0)

for ans in result:
    print(*ans)

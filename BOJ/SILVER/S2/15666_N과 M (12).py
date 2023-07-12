import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def back_tracking(idx, depth):

    if depth == M:
        print(*partialSeq)
        return

    for i in range(idx, length):
        partialSeq.append(seqLst[i])
        back_tracking(i, depth+1)
        partialSeq.pop()



N, M = map(int, input().split())
seq = list(map(int, input().split()))
seqSet = set(seq)
seqLst = list(seqSet)
seqLst.sort()
length = len(seqLst)

partialSeq = []
back_tracking(0, 0)
